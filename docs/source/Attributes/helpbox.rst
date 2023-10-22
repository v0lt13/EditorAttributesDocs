HelpBox Attribute
=================

Attribute to display a help box.

**Parameters:**
	- ``string`` message: The message to display
	- `optional`, ``bool`` drawProperty: Draw the property this attribute is attached to
	- ``MessageMode`` messageType: The type of the message
	
Example::
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, HelpBox("This is a normal help box", MessageMode.None)] 
		private string helpBox;
	
		[SerializeField, HelpBox("This is a log help box", MessageMode.Log)]
		private string helpBoxLog;
	
		[SerializeField, HelpBox("This is a warning help box", MessageMode.Warning)]
		private string helpBoxWarning;
	
		[SerializeField, HelpBox("This is a error help box", MessageMode.Error)]
		private string helpBoxError;
	
		[SerializeField, HelpBox("This is a help box with the attached field hidden", false)]
		private Void helpBoxHolder;
	}
	
.. image:: ../Images/HelpBox01.png

.. note::
	Doesn’t work well with arrays or lists
