GroupDrawer
===========

The base class for all group property drawers.

**Inheritance:**
	- *object* -> *GUIDrawer* -> *PropertyDrawer* -> *PropertyDrawerBase* -> *GroupDrawer*

**Namespace:** 
	*EditorAttributes.Editor*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	public abstract class GroupDrawer : PropertyDrawerBase

Methods:
--------

CreateGroupProperty(string, SerializedProperty)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a property setup to display in a group.

Declaration::

	protected virtual VisualElement CreateGroupProperty(string memberName, SerializedProperty property)
	
**Parameters:**
	- ``string`` memberName: The name of the member to create the property for
	- ``SerializedProperty`` property: The target serialized property
	
**Returns:** ``VisualElement``: A visual element contaning the property field
