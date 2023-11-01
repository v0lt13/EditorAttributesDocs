DisableInEditMode Attribute
===========================

Attribute to disable a field when outside of play mode::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[DisableInEditMode] public int field = "51";
	}

Outside of play mode:

.. image:: ../Images/DisableInPlaymode02.png

During play mode:

.. image:: ../Images/DisableInPlaymode01.png

Useful when you want to enable certain fields only when playing.
