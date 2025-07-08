EditorAttributes Settings
=========================

The settings for EditorAttributes package are located in `Edit/ProjectSettings/EditorAttributes`.

Disable Build Validation
-----------------------

Disables automatic validation when building the project.

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
