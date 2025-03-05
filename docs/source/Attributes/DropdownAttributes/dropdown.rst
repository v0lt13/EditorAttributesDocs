Dropdown Attribute
==================

Attribute to make a dropdown menu out of a collection of elements.

**Parameters:**
	- ``string`` valueCollectionName: The name of the collection for the values set by the dropdown
	- ``string[]`` displayNames: Change the display name for each item inside the dropdown

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, Dropdown(nameof(dropdownValues))] private string stringDropdown;
	
		private string[] dropdownValues = new string[]
		{
			"Value01", "Value02", "Value03"
		};
	}

Now you can specify the value of the ``string`` from a dropdown.

.. image:: ../../Images/Dropdown01.gif

You can also customize how to display dropdown values like this::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[Dropdown(nameof(dropdownValues), new string[] { "Directions/Forward", "Directions/Up", "Directions/Down", "One", "Zero" })] 
		[SerializeField] private Vector3 vectorDropdown;
	
		private Vector3[] dropdownValues = new Vector3[]
		{
			Vector3.forward, Vector3.up, Vector3.right, Vector3.one, Vector3.zero
		};
	}

.. image:: ../../Images/Dropdown02.gif
