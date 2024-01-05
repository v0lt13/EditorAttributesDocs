HideInEditMode Attribute
========================

Attribute to hide a field when outside of play mode::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, HideInEditMode] private int field;
	}

.. image:: ../../Images/HideInEditmode01.gif

Useful when you want to show certain fields only when playing.
