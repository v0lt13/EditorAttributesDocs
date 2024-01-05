HideInPlayMode Attribute
=======================

Attribute to hide a field when entering play mode::
	
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, HideInPlayMode] private int field;
	}

.. image:: ../../Images/HideInPlayMode01.gif

.. note:: 
	It cannot hide arrays or lists, only the fields inside them
