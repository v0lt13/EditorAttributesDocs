PropertyWidth Attribute
=======================

Attribute to adjust the width of a property

**Parameters:**
	- ``float`` widthOffset: By how much to offset the width of the property in pixels

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, PropertyWidth(200f)] private int intField;
		[SerializeField, PropertyWidth(100f)] private float floatField;
		[SerializeField, PropertyWidth(-100f)] private string stringField;
	}
	
.. image:: ../../Images/PropertyWidth01.png
