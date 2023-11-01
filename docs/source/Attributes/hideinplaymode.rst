HideInPlayMode Attribute
=======================

Attribute to hide a field when entering play mode::
	
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[HideInPlayMode] public int field = 51;
	}

Outside of play mode:

.. image:: ../Images/DisableInPlaymode01.png

During play mode:

.. image:: ../Images/HideInPlaymode01.png

.. note:: 
	It cannot hide arrays or lists, only the fields inside them
