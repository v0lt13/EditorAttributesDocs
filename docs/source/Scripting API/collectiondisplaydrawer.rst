CollectionDisplayDrawer
=======================

The base class all property drawers that display collection values.

**Inheritance:**
	- *object* -> *GUIDrawer* -> *PropertyDrawer* -> *PropertyDrawerBase* -> *CollectionDisplayDrawer*

**Namespace:** 
	*EditorAttributes.Editor*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	public abstract class CollectionDisplayDrawer : PropertyDrawerBase

Fields:
-------

nullList
^^^^^^^^

A predefined list representing a null collection.

**Type:** ``List<string>``

Declaration::

	protected readonly List<string> nullList = new() { "NULL" };

Methods:
--------

CreateDropdownField(List<string>, SerializedProperty)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a dropdown field with all the basic setup for displaying collections.

Declaration::

	protected virtual DropdownField CreateDropdownField(List<string> choices, SerializedProperty property)
	
**Parameters:**
	- ``List<string>`` choices: The choices for the dropdown
	- ``SerializedProperty`` property: The serialized property this dropdown attaches to

**Returns:** ``DropdownField``: The dropdown field created

SetDropdownDefaultValue(List<string>, SerializedProperty)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the initial value for when the dropdown is created in the inspector.

Declaration::

	protected virtual string SetDropdownDefaultValue(List<string> collectionValues, SerializedProperty property)
	
**Parameters:**
	- ``List<string>`` collectionValues: The collection linked to the dropdown
	- ``SerializedProperty`` property: The serialized property attached to the dropdown
  
**Returns:** ``string``: The string value set to the dropdown

SetPropertyValueFromDropdown(SerializedProperty, DropdownField)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the value of the property from the dropdown selection.

Declaration::

	protected virtual void SetPropertyValueFromDropdown(SerializedProperty property, DropdownField dropdownField)
	
**Parameters:**
	- ``SerializedProperty`` property: The property attached to the dropdown
	- ``DropdownField`` dropdownField: The dropdown field

SetDropdownValueFromProperty(SerializedProperty, DropdownField)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the value of the dropdown from the property value.

Declaration::

	protected virtual void SetDropdownValueFromProperty(SerializedProperty trackedProperty, DropdownField dropdownField)
	
**Parameters:**
	- ``SerializedProperty`` trackedProperty: The property attached to the dropdown
	- ``DropdownField`` dropdownField: The dropdown field
  
GetDisplayValues(MemberInfo, IDisplayNamesAttribute, SerializedProperty, List<string>)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the display names from the list or dictionary.

Declaration::

	protected List<string> GetDisplayValues(MemberInfo collectionInfo, IDisplayNamesAttribute displayNamesAttribute, SerializedProperty serializedProperty, List<string> propertyValues)
	
**Parameters:**
	- ``MemberInfo`` collectionInfo: The member info of the collection
	- ``IDisplayNamesAttribute`` displayNamesAttribute: The attribute containing the display names
	- ``SerializedProperty`` serializedProperty: The target property
	- ``List<string>`` propertyValues: A collection of all property values as a string

**Returns:** ``List<string>``: A list with the display names

IsCollectionDictionary(MemberInfo, SerializedProperty, out IDictionary)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if a collection is a dictionary.

Declaration::

	protected bool IsCollectionDictionary(MemberInfo collectionInfo, SerializedProperty serializedProperty, out IDictionary dictionary)
	
**Parameters:**
	- ``MemberInfo`` collectionInfo: The member info of the collection
	- ``SerializedProperty`` serializedProperty: The target property
	- `output`, ``IDictionary`` dictionary: The collection as a dictionary

**Returns:** ``bool``: True if the collection is an IDictionary, false otherwise

ConvertCollectionValuesToStrings(string, SerializedProperty, MemberInfo, HelpBox)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts the values of a collection into strings.

Declaration::

	protected static List<string> ConvertCollectionValuesToStrings(string collectionName, SerializedProperty serializedProperty, MemberInfo memberInfo, HelpBox errorBox)
	
**Parameters:**
	- ``string`` collectionName: The name of the collection to convert
	- ``SerializedProperty`` serializedProperty: The serialized property
	- ``MemberInfo`` memberInfo: The member info of the collection
	- ``HelpBox`` errorBox: The error box to display any errors to
	
**Returns:** ``List<string>``: The values of the collection in a list of strings
