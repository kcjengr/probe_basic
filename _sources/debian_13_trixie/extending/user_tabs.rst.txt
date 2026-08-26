=========
User Tabs
=========

A user tab is your own page inside Probe Basic, laid out in Qt Designer. The
same pattern is used for user buttons and user DRO displays.

Each one is a folder holding two files:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - File
     - Whose
     - What it is
   * - ``<name>.ui``
     - **Yours**
     - The layout. Edit it in Qt Designer.
   * - ``<name>.py``
     - **Ours**
     - A small loader that finds and loads the ``.ui``. Do not edit it.

.. important::

   Edit the ``.ui`` in Qt Designer. Leave the ``.py`` alone. It is generic --
   it works out the ``.ui`` filename from its own name -- so the same file
   works in every folder. If you modify it you are on your own, and a future
   Probe Basic update may overwrite it.

Everything a normal tab needs is available in Designer. Widgets such as
``ActionButton``, ``MDIButton``, ``HalButton`` and ``HalLabel`` are wired up
entirely through their properties, with no Python at all.


Creating a User Tab
-------------------

Point the INI at a folder that holds your tabs:

.. code-block:: ini

   [DISPLAY]
   USER_TABS_PATH = user_tabs/

Copy one of the shipped templates and rename it. **The folder, the .py and
the .ui must all share the same name**:

.. code-block:: text

   user_tabs/
       shop_page/
           shop_page.py      <- copied from template_main.py, renamed
           shop_page.ui      <- copied from template_main.ui, renamed

Use ``template_main`` for a full page and ``template_sidebar`` for the narrow
panel beside the plot.


Naming the Tab
--------------

Open the ``.ui`` in Designer and select the **root widget** -- the top entry in
the Object Inspector, not one of its children. Two of its properties control
how the tab appears:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Property
     - Effect
   * - ``objectName``
     - The text shown on the tab. Underscores become spaces, so
       ``SHOP_PAGE`` shows as ``SHOP PAGE``. The built-in tabs are uppercase,
       so use uppercase if you want yours to match.
   * - ``sidebar``
     - ``false`` puts the tab on the main tab strip. ``true`` puts it in the
       sidebar beside the plot. Only one sidebar tab can be loaded.

``sidebar`` is a dynamic property, at the bottom of Designer's property panel.
The templates already have it set.


Upgrading From an Older Probe Basic
-----------------------------------

Your ``.ui`` files carry over untouched, including ones drawn in Qt 5 Designer
on Debian 12. The loader ``.py`` files are the part that changes between
releases.

The quickest fix by hand is to copy the current template into your folder and
rename it to match. For a tab folder called ``shop_page``:

.. code-block:: sh

   cp /usr/share/configs/probe_basic/user_tabs/template_main/template_main.py \
      ~/linuxcnc/configs/probe_basic/user_tabs/shop_page/shop_page.py

Leave the ``.ui`` alone. Repeat for each folder.


Updating Several Folders at Once
--------------------------------

If you have more than a couple of folders, there is a script that does the
same thing across a whole config directory. It is **not installed with Probe
Basic** -- download it only if you want it:

.. code-block:: sh

   wget https://raw.githubusercontent.com/kcjengr/probe_basic/pyside6/scripts/update_user_files.py

See what it would change, without changing anything:

.. code-block:: sh

   python3 update_user_files.py --dry-run ~/linuxcnc/configs/probe_basic

Then run it for real:

.. code-block:: sh

   python3 update_user_files.py ~/linuxcnc/configs/probe_basic

It refreshes the loader ``.py`` in every user tab, user button and user DRO
folder it finds, keeps each previous file alongside as ``.py.bak``, and never
touches a ``.ui``. Running it twice is harmless -- the second run reports
everything as already current.

It reads ``DISPLAY`` from your INI so a lathe config gets the lathe templates,
and takes those templates from the configs installed in ``/usr/share/configs``,
which means it updates you to whatever Probe Basic version is installed.


When a Tab Does Not Appear
--------------------------

A user tab that cannot be loaded is skipped -- the rest of Probe Basic starts
normally -- and the reason is written to the log file named by ``LOG_FILE`` in
your INI. Common causes:

- **The folder, .py and .ui names do not match.** All three must be the same.
- **No .py in the folder.** A ``.ui`` on its own does not make a tab. Qt
  Designer only writes ``.ui`` files; the ``.py`` has to be copied from a
  template.
- **The .py imports PyQt.** Probe Basic runs on PySide6. Anything importing
  PyQt directly is refused, because loading it would take down the whole
  application. Replace the loader with the current template (above), and rebuild
  any ``.qrc`` resources with ``pyside6-rcc`` rather than ``pyrcc5``.
