HideProperty Attribute
======================

Attribute to hide a field in the inspector but still show it in debug view.
	
Examplke::

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
	
.. note::
	If the attribute is attached to an inherited field, that field has to be marked as ``public`` or ``protected`` for it to work.
