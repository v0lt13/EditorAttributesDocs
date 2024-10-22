PropertyDrawerBase
==================

The base class all property drawers from the package derive from. It contains some extra utility functions.

**Inheritance:**
	- *object* -> *GUIDrawer* -> *PropertyDrawer* -> *PropertyDrawerBase*

**Namespace:** 
	*EditorAttributes.Editor*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	public class PropertyDrawerBase : PropertyDrawer

Properties:
-----------

CanApplyGlobalColor
-------------------

Checks if the global color can be applied on an element.

**Type:** ``bool``

Declaration::

	protected bool CanApplyGlobalColor => EditorExtension.GLOBAL_COLOR != EditorExtension.DEFAULT_GLOBAL_COLOR;

Methods:
--------

CreatePropertyGUI(SerializedProperty)
-------------------------------------

Override this method to make your own UI Toolkit based GUI for the property.

Declaration::

	public override VisualElement CreatePropertyGUI(SerializedProperty property)
	
**Parameters:**
	- ``SerializedProperty`` property: The SerializedProperty to make the custom GUI for
	
**Returns:** ``VisualElement``: The element containing the custom GUI
	
Overrides::

	PropertyDrawer.CreatePropertyGUI(SerializedProperty)

DrawProperty(SerializedProperty, Label)
---------------------------------------

Draws a property field also accounting for Unity Events.

Declaration::

	protected virtual VisualElement DrawProperty(SerializedProperty property, Label label = null)
	
**Parameters:**
	- ``SerializedProperty`` property: The serialized property to draw
	- `optional`, ``Label`` label: Add a custom label to the property
	
**Returns:** ``VisualElement``: The property visual element

SetProperyValueFromString(string, ref SerializedProperty, HelpBox)
------------------------------------------------------------------

Sets the value of a property from a string.

Declaration::

	protected static void SetProperyValueFromString(string value, ref SerializedProperty property, HelpBox errorBox)
	
**Parameters:**
	- ``string`` value: The string value to convert
	- `reference`, ``SerializedProperty`` property: The serialized property reference to assign the value to
	- ``HelpBox`` errorBox: The error box to display any errors to

GetPropertyValueAsString(SerializedProperty)
--------------------------------------------

Gets the value of a serialzied property and returns it as a string.

Declaration::

	protected static string GetPropertyValueAsString(SerializedProperty property)
	
**Parameters:**
	- ``SerializedProperty`` property: The serialized property to get the value from
	
**Returns:** ``string``: The serialized property value as a string

ConvertCollectionValuesToStrings(string, SerializedProperty, MemberInfo, HelpBox)
---------------------------------------------------------------------------------

Converts the values of a collection into strings.

Declaration::

	protected static List<string> ConvertCollectionValuesToStrings(string collectionName, SerializedProperty serializedProperty, MemberInfo memberInfo, HelpBox errorBox)
	
**Parameters:**
	- ``string`` collectionName: The name of the collection to convert
	- ``SerializedProperty`` serializedProperty: The serialized property
	- ``MemberInfo`` memberInfo: The member info of the collection
	- ``HelpBox`` errorBox: The error box to display any errors to
	
**Returns:** ``List<string>``: The values of the collection in a list of strings

FindNestedProperty(SerializedProperty, string)
----------------------------------------------

Finds a nested serialized property.

Declaration::

	protected static SerializedProperty FindNestedProperty(SerializedProperty property, string propertyName)
	
**Parameters:**
	- ``SerializedProperty`` property: The serialized property
	- ``string`` propertyName: The name of the property to find
	
**Returns:** ``SerializedProperty``: The nested serialized property

GetSerializedPropertyName(string, SerializedProperty)
-----------------------------------------------------

Gets the name of a serialized property accounting for C# properties.

Declaration::

	public static string GetSerializedPropertyName(string propertyName, SerializedProperty property)
	
**Parameters:**
	- ``string`` propertyName: The name of the property to look for
	- ``SerializedProperty`` property: The serialized property
	
**Returns:** ``string``: The name of the serialized property

DisplayErrorBox(VisualElement, HelpBox)
---------------------------------------

Displays an error box in the inspector.

Declaration::

	public static void DisplayErrorBox(VisualElement root, HelpBox errorBox)
	
**Parameters:**
	- ``VisualElement`` root: The root visual element
	- ``HelpBox`` errorBox: The help box to displaying the errors

UpdateVisualElement(VisualElement, Action)
------------------------------------------

Update logic for a visual element.

Declaration::

	protected void UpdateVisualElement(VisualElement visualElement, Action logicToUpdate)
	
**Parameters:**
	- ``VisualElement`` visualElement: The element to update
	- ``Action`` logicToUpdate: The logic to update

UpdateVisualElementAtInterval(VisualElement, Action, long)
----------------------------------------------------------

Updates a visual element at a set interval.

Declaration::

	public static void UpdateVisualElementAtInterval(VisualElement visualElement, Action logicToUpdate, long intervalMs = 60)
	
**Parameters:**
	- ``VisualElement`` visualElement: The visual element to update
	- ``Action`` logicToUpdate: The logic to execute on the specified element
	- `optional`, ``long`` intervalMs: The update interval in milliseconds
	
AddElement(VisualElement, VisualElement)
----------------------------------------

Add an element to another visual element if it doesn't exist.

Declaration::

	public static void AddElement(VisualElement root, VisualElement element)
	
**Parameters:**
	- ``VisualElement`` root: The root to add the element on
	- ``VisualElement`` element: The element to add

RemoveElement(VisualElement, VisualElement)
-------------------------------------------

Removes an element from another visual element if it exists.

Declaration::

	public static void RemoveElement(VisualElement owner, VisualElement element)
	
**Parameters:**
	- ``VisualElement`` owner: The owner containing the element
	- ``VisualElement`` element: The element to remove

GetConditionValue(MemberInfo, IConditionalAttribute, SerializedProperty, HelpBox)
---------------------------------------------------------------------------------

Gets the value of a condition for a conditional attribute.

Declaration::

	public static bool GetConditionValue(MemberInfo memberInfo, IConditionalAttribute conditionalAttribute, SerializedProperty serializedProperty, HelpBox errorBox)
	
**Parameters:**
	- ``MemberInfo`` memberInfo: The member info of the condition
	- ``IConditionalAttribute`` conditionalAttribute: The conditional attribute
	- ``SerializedProperty`` serializedProperty: The serialized property
	- ``HelpBox`` errorBox: The error box to display any errors to
	
**Returns:** ``bool``: True if the condition is satisfied

GetDynamicString(string, SerializedProperty, IDynamicStringAttribute, HelpBox)
------------------------------------------------------------------------------

Gets the string value from a member if the input mode is set to Dynamic.

Declaration::

	public static string GetDynamicString(string inputText, SerializedProperty property, IDynamicStringAttribute dynamicStringAttribute, HelpBox errorBox)
	
**Parameters:**
	- ``string`` inputText: The string input that may contain the member name
	- ``SerializedProperty`` property: The serialized property
	- ``IDynamicStringAttribute`` dynamicStringAttribute: The dynamic string attribute
	- ``HelpBox`` errorBox: The error box to display any errors to
	
**Returns:** ``string``: If the input mode is Constant will return the base input string, if is Dynamic will return the string value of the member

ApplyBoxStyle(VisualElement)
----------------------------

Applies the help box style to a visual element.

Declaration::

	public static void ApplyBoxStyle(VisualElement visualElement)
	
**Parameters:**
	- ``VisualElement`` visualElement: The element to apply the style to

Print(object)
-------------

A short handy version of ``Debug.Log``.

Declaration::

	protected void Print(object message)
	
**Parameters:**
	- ``object`` message: The message to print

IsCollectionValid(ICollection)
------------------------------

Checks if a collection is null or has no members.

Declaration::

	public static bool IsCollectionValid(ICollection collection)
	
**Parameters:**
	- ``ICollection`` collection: The collection to check
	
**Returns:** ``bool``: False is the collection is null or has no members, true otherwise

GetTextureSize(Texture2D)
-------------------------

Gets the size of a 2D texture.

Declaration::

	public static Vector2 GetTextureSize(Texture2D texture)
	
**Parameters:**
	- ``Texture2D`` texture: The texture to get the size from
	
**Returns:** ``Vector2``: The width and height of the texture as a Vector2
