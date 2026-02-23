EditorAttributes Settings
=========================

The settings for EditorAttributes package are located in `Edit/ProjectSettings/EditorAttributes`.

Disable Editor Extension
------------------------

Disables the drawing of the editor by the editor extension script, usefull if you want to override the base ``UnityEngine.Object`` yourself.

.. warning::
	The following attributes will stop working when enabling this setting: :doc:`../Attributes/ButtonAttributes/button`, :doc:`../Attributes/DecorativeAttributes/guicolor`,
	:doc:`../Attributes/DecorativeAttributes/propertyorder`, :doc:`../Attributes/MiscellaneousAttributes/hideproperty`, :doc:`../Attributes/MiscellaneousAttributes/showininspector`.

Disable Build Validation
------------------------

Disables automatic validation when building the project.

Asset Preview Load Time
-----------------------

Time in milliseconds to wait for the asset preview to load, increase this value if the previews are not showing up.

Custom Unit Definitions
-----------------------

Define custom units for use with :doc:`../Attributes/NumericalAttributes/unitfield`.

**Fields:**
	- ``string`` unitName: The name of the custom unit
	- ``UnitCategory`` category: The category this unit is part of
	- ``string`` categoryName: Define a custom category for this unit. Only relevant when the `category` field is set to `Custom`
	- ``string`` unitLabel: The label used for displaying the unit in the inspector
	- ``double`` baseFactor: How many base units equal one of this unit. Must be 1 for the base unit

Delete Buttons Parameter Data
-----------------------------

Deletes all buttons parameter data stored in `ProjectSettings/EditorAttributes` folder.
