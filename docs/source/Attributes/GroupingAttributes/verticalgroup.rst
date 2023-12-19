VerticalGroup Attribute
=======================

Attribute to display specified fields vertically.

**Parameters:**
	- `optional`, ``float`` labelWidth: The width of the field labels
	- `optional`, ``float`` fieldWidth: The width of the input fields
	- `optional`, ``bool`` drawInBox: Draw the group in a nice box
	- `params`, ``string`` fieldsToGroup: The name of the fields to group

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, VerticalGroup(nameof(field01), nameof(field02), nameof(field03), nameof(field04))]
		private Void groupHolder;
	
		// The fields needs to be serialized, but we don't want them to show in the inspector
		[SerializeField, HideInInspector] private int field01;
		[SerializeField, HideInInspector] private float field02;
		[SerializeField, HideInInspector] private string field03;
		[SerializeField, HideInInspector] private bool field04;
	}

.. image:: ../../Images/VerticalGroup01.png

This attribute is best used with the :doc:`horizontalgroup` to display a bunch of field groups horizontally::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[HorizontalGroup(nameof(verticalGroupHolder01), nameof(verticalGroupHolder02))]
		[SerializeField] private Void horizontalGroupHolder;
	
		[VerticalGroup(drawInBox: true, nameof(intField01), nameof(stringField01), nameof(boolField01))]
		[SerializeField, HideInInspector] private Void verticalGroupHolder01;
	
		[VerticalGroup(drawInBox: true, nameof(intField02), nameof(stringField02), nameof(boolField02))]
		[SerializeField, HideInInspector] private Void verticalGroupHolder02;
	
		[SerializeField, HideInInspector] private int intField01;
		[SerializeField, HideInInspector] private string stringField01;
		[SerializeField, HideInInspector] private bool boolField01;
	
		[SerializeField, HideInInspector] private int intField02;
		[SerializeField, HideInInspector] private string stringField02;
		[SerializeField, HideInInspector] private bool boolField02;
	}

.. image:: ../../Images/VerticalGroup02.png
