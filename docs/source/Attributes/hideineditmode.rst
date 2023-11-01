HideInEditMode Attribute
========================

Attribute to hide a field when outside of play mode::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[HideInEditMode] public int field = "51";
	}

Outside of play mode:

.. image:: ../Images/HideInPlaymode01.png

During play mode:

.. image:: ../Images/DisableInPlaymode01.png

Useful when you want to show certain fields only when playing.
