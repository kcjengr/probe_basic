=========
User Tabs
=========

A user tab is your own page inside Probe Basic, laid out in Qt Designer.

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

``USER_TABS_PATH`` is commented out in the shipped INI files. Uncomment it, or
add it, pointing at a folder that holds your tabs:

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

Both shipped templates name their root widget ``USER``, so rename yours as
soon as you copy it -- otherwise every tab you add is labelled ``USER``.


When a Tab Does Not Appear
--------------------------

Check that the folder, the ``.py`` and the ``.ui`` are all named the same, and
that ``USER_TABS_PATH`` is uncommented in the INI file you are running.

A ``.ui`` on its own does not make a tab. Qt Designer only writes ``.ui``
files; the ``.py`` has to be copied from a template.

.. warning::

   A user tab that cannot be loaded will stop Probe Basic from starting, not
   just hide that one tab. If Probe Basic will not open after you add a tab,
   comment out ``USER_TABS_PATH`` to get back in, then check the folder and
   file names.
