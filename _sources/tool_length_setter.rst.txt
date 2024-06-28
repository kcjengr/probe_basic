==================
Tool Length Setter
==================

TODO/WIP

Tool touch off position (G30), X and Y should be centre of the fixed tool setter.
Z should always be set to 0

Spindle Zero is the length of from the spindle nose to the top of the tool setter (at the trip point)

the value for ``Spindle Zero`` is measure by probing the top of the setter using the spindle nose (empty spindle no holders)

.. important::
   Currently G59.3 Must remain as 0,0,0 as this is used during the ``tool_touch_off.ngc`` routine


Tool Setter Setup
-----------------
.. image:: images/mill/tool_setter_setup.png
   :align: center

Measuring Tools
---------------
.. image:: images/mill/tool_length_measure.png
   :align: center
