TagDropdown Attribute
=====================

Attribute to make a dropdown of tags

.. note::
	The `TagDropdown Attribute` can only be attached to a ``string``

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, TagDropdown] private string objectTag;
	}

.. image:: ../../Media/TagDropdown01.gif
