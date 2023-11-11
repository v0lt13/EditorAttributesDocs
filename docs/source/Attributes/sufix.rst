Sufix Attribute
===============

Attribute to add a sufix on a field

**Parameters:**
	- ``string`` sufix: The sufix to add
	- `optional`, ``float`` offset: Offset to add between the sufix and field

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, Sufix("sufix")] private int field01;
		[SerializeField, Sufix("sufix with offset", 20f)] private int field02;
	}

.. image:: ../Images/Sufix01.png
