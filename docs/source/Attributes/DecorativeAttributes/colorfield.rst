ColorField Attribute
====================

Attribute to color a field in the inspector

**Parameters:**
	- ``float`` red: Red amount
	- ``float`` green: Green amount
	- ``float`` blue: Blue amount
	- ``string`` hexColor: The color in hexadecimal
	- ``GUIColor`` color: The color of the field

Unlike the :doc:`guicolor` the `ColorField Attribute` only colors the field is attached to and overrides the :doc:`guicolor`::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, ColorField(GUIColor.Green)] private int field01;
		[SerializeField, ColorField(255f, 0f, 123f)] private int field02;
		[SerializeField, ColorField("#00f2ff")] private int field03;
	}
	
.. image:: ../Images/ColorField01.png
