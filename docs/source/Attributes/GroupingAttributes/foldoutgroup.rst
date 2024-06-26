FoldoutGroup Attribute
======================

Attribute to display the specified fields in a foldout

**Parameters:**
	- ``string`` groupName: The name of the group
	- `optional`, ``float`` widthOffset: By how much to offset the width of the properties in pixels
	- `optional`, ``bool`` drawInBox: Draw the group in a nice box
	- `params`, ``string`` fieldsToGroup: The name of the fields to group

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[FoldoutGroup("FoldoutGroup", nameof(intField), nameof(stringField), nameof(boolField))]
		[SerializeField] private Void groupHolder;
	
		[SerializeField, HideInInspector] private int intField;
		[SerializeField, HideInInspector] private string stringField;
		[SerializeField, HideInInspector] private bool boolField;
	}
	
.. image:: ../../Images/FoldoutGroup01.gif
