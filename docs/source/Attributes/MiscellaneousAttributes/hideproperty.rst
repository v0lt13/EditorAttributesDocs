HideProperty Attribute
======================

Attribute to hide a field in the inspector but still show it in debug view::
	
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[HideProperty] public int field;
	}

Normal inspector mode:
.. image:: ../../Images/HideProperty01.png

Debug inspector mode:
.. image:: ../../Images/HideProperty02.png

.. note::
	The attribute wont work inside serialized structs or classes.
