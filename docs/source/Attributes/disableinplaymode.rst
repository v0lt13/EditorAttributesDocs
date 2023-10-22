DisableInPlaymode Attribute
===========================

Attribute to disable a field when entering play mode::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[DisableInPlaymode] public int field = "51";
	}

Outside of playmode:

.. image:: ../Images/DisableInPlaymode01.png

During playmode:

.. image:: ../Images/DisableInPlaymode02.png

Useful when you want to make sure no values can be modified in the inspector while you're playing the game but you can still see them.
