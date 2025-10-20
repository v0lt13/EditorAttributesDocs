PropertyDropdown Attribute
==========================

Attribute to make a dropdown containing all properties of a ``Component`` or ``ScriptableObject``.

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, PropertyDropdown] private BoxCollider boxCollider;
		[SerializeField, PropertyDropdown] private ExampleScriptableObject scriptableObject;
	}

.. image:: ../../Media/PropertyDropdown01.png
