GUIColor Attribute
==================

Attribute to color the GUI

**Parameters:**
	- ``float`` red: Red amount
	- ``float`` green: Green amount
	- ``float`` blue: Blue amount
	- ``string`` hexColor: The color in hexadecimal
	- ``GUIColor`` color: The color of the GUI

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[GUIColor(GUIColor.Lime)]
		[SerializeField] private int field01;
		[SerializeField] private int field02;
		[SerializeField] private int field03;
	
		[GUIColor(144f, 151f, 222f)]
		[SerializeField] private int field04;
		[SerializeField] private int field05;
		[SerializeField] private int field06;
	
		[GUIColor("#8c508b")]
		[SerializeField] private int field07;
		[SerializeField] private int field08;
		[SerializeField] private int field09;
	}
	
.. image:: ../Images/GUIColor01.png
