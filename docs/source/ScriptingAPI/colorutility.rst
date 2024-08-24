Class ColorUtility
==================

An utiliy class containing usefull functions related to editor coloring.

**Inheritance:**
	- *object* -> *ColorUtility*

**Namespace:** 
	EditorAttributes.Editor.Utility
	
**Assembly:**
	EditorAttributes.Editor.asmdef
	
Syntax::
	public static class ColorUtility

***Methods:***

ApplyColor(VisualElement, IColorAttribute, HelpBox)
---------------------------------------------------

Applies a color to a visual element via the color attribute.

Declaration::
	public static void ApplyColor(VisualElement visualElement, IColorAttribute color, HelpBox errorBox)
	
**Parameters:**
	- ``VisualElement`` visualElement: The visual element to color
	- ``IColorAttribute`` color: The color attribute
	- ``HelpBox`` errorBox: The error box to display any errors to

ApplyColor(VisualElement, Color, int)
-------------------------------------

Applies a color to a visual element.

Declaration::
	public static void ApplyColor(VisualElement visualElement, Color color, int delay = 50)
	
**Parameters:**
	- ``VisualElement`` visualElement: The visual element to color
	- ``Color`` color: The color to apply
	- `optional`, ``int`` delay: How many milliseconds to delay before applying the color

GetColorFromProperty(SerializedProperty)
----------------------------------------

Gets the color from a serialzied property with a color attribute.

Declaration::
	public static Color? GetColorFromProperty(SerializedProperty property)
	
**Parameters:**
	- ``SerializedProperty`` property: The property to get the color from
	
**Returns:** ``Color?``: The color from the attribute, null if the attribute is not found

GetColorFromAttribute(IColorAttribute, HelpBox)
-----------------------------------------------

Gets the color value from a color attribute

Declaration::
	public static Color GetColorFromAttribute(IColorAttribute attribute, HelpBox errorBox)
	
**Parameters:**
	- ``SerializedProperty`` attribute: The color attribute
	- ``HelpBox`` errorBox: The error box to display any errors to
	
**Returns:** ``Color``: The color from the attribute

ColorAttributeToColor(IColorAttribute)
--------------------------------------

Converts the color attribute values from the color attribute to a color

Declaration::
	public static Color ColorAttributeToColor(IColorAttribute colorAttribute)
	
**Parameters:**
	- ``IColorAttribute`` colorAttribute: The color attribute
	
**Returns:** ``Color``: The color value

ColorAttributeToColor(IColorAttribute, float)
---------------------------------------------

Converts the color attribute values from the color attribute to a color

Declaration::
	public static Color ColorAttributeToColor(IColorAttribute colorAttribute, float alpha)
	
**Parameters:**
	- ``IColorAttribute`` colorAttribute: The color attribute
	- ``float`` alpha: Custom transparency value
	
**Returns:** ``Color``: The color value

GUIColorToColor(GUIColor)
-------------------------

Converts the GUIColor value to a color

Declaration::
	public static Color GUIColorToColor(GUIColor color)
	
**Parameters:**
	- ``GUIColor`` color: The color value
	
**Returns:** ``Color``: The color value

GUIColorToColor(GUIColor, float)
--------------------------------

Converts the GUIColor value to a color

Declaration::
	public static Color GUIColorToColor(GUIColor color, float alpha)
	
**Parameters:**
	- ``GUIColor`` color: The color value
	- ``float`` alpha: Custom transparency value
	
**Returns:** ``Color``: The color value
