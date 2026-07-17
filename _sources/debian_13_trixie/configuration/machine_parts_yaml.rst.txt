====================
Machine Sim Graphics
====================

Start Here: VTK Settings
------------------------

Set your INI ``[VTK]`` section first so users know where the YAML filename is
declared and how axis ownership is called.

.. code-block:: ini

  [VTK]
  MACHINE_PARTS = machine.yml
  X = table
  Y = table
  Z = head
  A = table
  C = table

At minimum, ``MACHINE_PARTS`` must point to your YAML file. Axis ownership
(``head`` or ``table``) should match your real machine kinematics.

After VTK is configured, build the ``MACHINE_PARTS`` YAML.

This guide shows how to build a ``MACHINE_PARTS`` YAML file for common machine
kinematic combinations used by the VTK backplot machine simulation.

The YAML describes a machine as a parent-child assembly tree. Each moving node is
configured as either:

- ``linear`` (translates)
- ``angular`` (rotates)

Road Map: Complete Example First
--------------------------------

Start with this full working example, then use the rest of the guide to break it
down section by section.

This roadmap example is an ``XYZAC`` table-rotary style machine.

Start with the full ``[VTK]`` mapping first so axis ownership is clear before
reading the YAML tree:

.. code-block:: ini

  [VTK]
  MACHINE_PARTS = machine.yml
  X = table
  Y = table
  Z = head
  A = table
  C = table

Then read the ``MACHINE_PARTS`` YAML that this mapping points to:

.. code-block:: yaml

  root:
     id: "frame"
     model: "machine/frame.stl"
     type: "table"
     position: [0, 0, 0, 0, 0, 0]
     origin: [0, 0, 0]
     axis: null
     joint: null
     child_saddle:
        id: "saddle"
        model: "machine/saddle.stl"
        type: "linear"
        position: [0, 0, 0, 0, 0, 0]
        origin: [0, 0, 0]
        axis: "y"
        joint: 0
        child_table:
          id: "table"
          model: "machine/table.stl"
          type: "linear"
          position: [0, 0, 0, 0, 0, 0]
          origin: [0, 0, 0]
          axis: "x"
          joint: 1
          child_a_axis:
             id: "a_axis"
             model: "machine/a_axis.stl"
             type: "angular"
             position: [0, 0, -18, 0, 0, 0]
             origin: [0, 0, -18]
             axis: "a"
             joint: 3
             child_c_axis:
                id: "c_axis"
                model: "machine/c_axis.stl"
                type: "angular"
                position: [0, 0, -18, 0, 0, 0]
                origin: [0, 0, -18]
                axis: "c"
                joint: 4
     child_headstock:
        id: "headstock"
        model: "machine/headstock.stl"
        type: "linear"
        position: [0, 0, 0, 0, 0, 0]
        origin: [0, 0, 0]
        axis: "z"
        joint: 2

Section map for this document:

1. ``Quick Rules``: high-level checks before editing.
2. ``Node Schema``: meaning of each field in the roadmap example.
3. ``Supported Axis Tokens``: valid ``axis`` values used in the roadmap.
4. ``How To Build Any Combination``: method to adapt the roadmap to your machine.
5. ``Combination Templates``: focused variants derived from the roadmap pattern.
6. ``INI [VTK] Axis Ownership`` and ``Troubleshooting Checklist``: final validation.

Quick Rules
-----------

1. Keep one top-level key (normally ``root``).
2. Every part node is a mapping (dictionary).
3. Child nodes can use any key name, but ``child_*`` naming is recommended for readability.
4. Use ``type: linear`` or ``type: angular`` for moving parts.
5. Keep ``axis`` aligned to supported axis tokens.
6. For rotary parts, set ``origin`` to the true pivot point.

Node Schema
-----------

Typical part node (one piece of the roadmap example):

.. code-block:: yaml

  some_node:
     id: "table"
     model: "machine/table.stl"
     type: "linear"
     position: [0, 0, 0, 0, 0, 0]
     origin: [0, 0, 0]
     axis: "x"
     joint: 1
     color: [0.9, 0.9, 0.9]   # optional
     power: 5.0               # optional

Field meanings:

- ``id``: Human-readable part identifier.
- ``model``: STL path for this part.
- ``type``: Motion behavior.
  - ``linear`` for X/Y/Z translation
  - ``angular`` for A/B/C rotation
  - other values are treated as static by motion updates
- ``position``: Base transform as ``[x, y, z, rx, ry, rz]``.
  - translation uses machine units
  - rotation uses degrees
- ``origin``: Rotation pivot point ``[x, y, z]``.
  - for ``angular`` parts this is critical
  - if omitted or ``null``, transform falls back to ``position`` for pivot
- ``axis``: Motion token (see next section).
- ``joint``: LinuxCNC joint index metadata.
- ``color``: Optional diffuse color ``[r, g, b]``.
- ``power``: Optional specular power.

Supported Axis Tokens
---------------------

For ``type: linear``:

- ``x``, ``y``, ``z``
- ``-x``, ``-y``, ``-z``

For ``type: angular``:

- ``a``, ``b``, ``c``
- ``-a``, ``-b``, ``-c``

Notes:

- Use lowercase axis tokens in YAML.
- If ``axis`` does not match a supported token for the selected ``type``, that
  part will not move as expected.

How To Build Any Combination
----------------------------

Use the roadmap example above as a baseline, then adapt it with the sequence below.

1. Start with a static base/root.
2. Add linear axis chain(s) in physical order.
3. Add rotary axis nodes where the real machine rotates.
4. Set each rotary ``origin`` to the mechanical center of rotation.
5. Add matching ``[VTK]`` axis ownership in the INI (``head`` or ``table``).
6. Run and verify each axis independently.

Combination Templates
---------------------

These are targeted variations of the roadmap pattern, not replacements for the
schema/rules above.

3-axis mill (XYZ)
^^^^^^^^^^^^^^^^^

.. code-block:: yaml

  root:
     id: "frame"
     model: "machine/frame.stl"
     type: "table"
     position: [0, 0, 0, 0, 0, 0]
     origin: [0, 0, 0]
     axis: null
     joint: null
     child_saddle:
        id: "saddle"
        model: "machine/saddle.stl"
        type: "linear"
        position: [0, 0, 0, 0, 0, 0]
        origin: [0, 0, 0]
        axis: "y"
        joint: 0
        child_table:
          id: "table"
          model: "machine/table.stl"
          type: "linear"
          position: [0, 0, 0, 0, 0, 0]
          origin: [0, 0, 0]
          axis: "x"
          joint: 1
     child_headstock:
        id: "headstock"
        model: "machine/headstock.stl"
        type: "linear"
        position: [0, 0, 0, 0, 0, 0]
        origin: [0, 0, 0]
        axis: "z"
        joint: 2

4-axis table rotary (XYZA or XYZB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a rotary node under the table branch.

.. code-block:: yaml

  child_a_axis:
     id: "a_axis"
     model: "machine/a_axis.stl"
     type: "angular"
     position: [0, 0, -18, 0, 0, 0]
     origin: [0, 0, -18]
     axis: "a"   # use "b" for B-axis machine
     joint: 3

4-axis head rotary (XYZ + head A/B/C)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the rotary node under the head branch instead of table branch.

.. code-block:: yaml

  child_headstock:
     id: "headstock"
     model: "machine/headstock.stl"
     type: "linear"
     position: [0, 0, 0, 0, 0, 0]
     origin: [0, 0, 0]
     axis: "z"
     joint: 2
     child_a_head:
        id: "a_head"
        model: "machine/a_head.stl"
        type: "angular"
        position: [0, 0, 0, 0, 0, 0]
        origin: [0, 0, 0]
        axis: "a"
        joint: 3

5-axis trunnion style XYZAC
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add A then C on the table branch (nested rotary stages).

.. code-block:: yaml

  child_a_axis:
     id: "a_axis"
     model: "machine/a_axis.stl"
     type: "angular"
     position: [0, 0, -18, 0, 0, 0]
     origin: [0, 0, -18]
     axis: "a"
     joint: 3
     child_c_axis:
        id: "c_axis"
        model: "machine/c_axis.stl"
        type: "angular"
        position: [0, 0, -18, 0, 0, 0]
        origin: [0, 0, -18]
        axis: "c"
        joint: 4

5-axis trunnion style XYZBC
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as above, but use B then C.

.. code-block:: yaml

  child_b_axis:
     id: "b_axis"
     model: "machine/b_axis.stl"
     type: "angular"
     position: [0, 0, -18, 0, 0, 0]
     origin: [0, 0, -18]
     axis: "b"
     joint: 3
     child_c_axis:
        id: "c_axis"
        model: "machine/c_axis.stl"
        type: "angular"
        position: [0, 0, -18, 0, 0, 0]
        origin: [0, 0, -18]
        axis: "c"
        joint: 4

Lathe-style XZC (example pattern)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use X and Z as linear, with C as angular on the spindle/table side.

.. code-block:: yaml

  child_x:
     id: "x_slide"
     model: "machine/x_slide.stl"
     type: "linear"
     position: [0, 0, 0, 0, 0, 0]
     origin: [0, 0, 0]
     axis: "x"
     joint: 0
     child_z:
        id: "z_slide"
        model: "machine/z_slide.stl"
        type: "linear"
        position: [0, 0, 0, 0, 0, 0]
        origin: [0, 0, 0]
        axis: "z"
        joint: 1
        child_c:
          id: "c_spindle"
          model: "machine/c_spindle.stl"
          type: "angular"
          position: [0, 0, 0, 0, 0, 0]
          origin: [0, 0, 0]
          axis: "c"
          joint: 2

INI [VTK] Axis Ownership
------------------------

Set ownership for active machine axes in the INI.

- ``head``: axis motion belongs to spindle/head side
- ``table``: axis motion belongs to table/workholding side

Example for XYZAC trunnion:

.. code-block:: ini

  [VTK]
  MACHINE_PARTS = machine.yml
  X = table
  Y = table
  Z = head
  A = table
  C = table

Example for head rotary A:

.. code-block:: ini

  [VTK]
  MACHINE_PARTS = machine_head_a.yml
  X = table
  Y = table
  Z = head
  A = head

Use only ``head`` or ``table`` values.

Troubleshooting Checklist
-------------------------

1. Part does not move: check ``type`` and ``axis`` token pair, then verify the
   axis is active in machine coordinates.
2. Rotary appears to orbit incorrectly: correct the part ``origin`` pivot point.
3. Warning about missing machine axes in ``MACHINE_PARTS``: add YAML nodes for
   all active axes (X/Y/Z/A/B/C as applicable).
4. Warning about table rotary missing origin: define ``origin`` for each
   table-owned rotary axis.
5. VTK ownership mismatch warnings: align INI ``[VTK]`` axis ownership with the
   actual machine design.

Reference Examples In This Repository
-------------------------------------

- ``configs/probe_basic_asm/machine3.yml`` (3-axis)
- ``configs/probe_basic_asm/machine.yml`` (XYZAC)
- ``configs/probe_basic_asm/machine_b.yml`` (XYZBC)
- ``configs/probe_basic_asm/probe_basic.ini`` (INI mapping example)
- ``configs/probe_basic_asm/probe_basic_xyzac.ini`` (INI mapping example)
- ``configs/probe_basic_asm/probe_basic_xyzbc.ini`` (INI mapping example)
