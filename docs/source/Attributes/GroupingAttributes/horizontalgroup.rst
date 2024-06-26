HorizontalGroup Attribute
=========================

Attribute to display specified fields horizontally.

**Parameters:**
	- `optional`, ``float`` widthOffset: By how much to offset the width of the properties in pixels
	- `optional`, ``bool`` drawInBox: Draw the group in a nice box
	- `params`, ``string`` fieldsToGroup: The name of the fields to group

Example::
	
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, HorizontalGroup(nameof(field01), nameof(field02), nameof(field03), nameof(field04))]
		private Void groupHolder01;
	
		[SerializeField, HorizontalGroup(50f, true, nameof(field05), nameof(field06))]
		private Void groupHolder02;
	
		// The fields needs to be serialized, but we don't want them to show twice in the inspector
		[SerializeField, HideInInspector] private int field01;
		[SerializeField, HideInInspector] private float field02;
		[SerializeField, HideInInspector] private string field03;
		[SerializeField, HideInInspector] private bool field04;
	
		[SerializeField, HideInInspector] private Vector3 field05;
		[SerializeField, HideInInspector] private Vector4 field06;
	}

.. image:: ../../Images/HorizontalGroup01.png
