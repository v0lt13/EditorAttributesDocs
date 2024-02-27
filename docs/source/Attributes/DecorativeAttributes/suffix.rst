Suffix Attribute
================

Attribute to add a suffix on a field

**Parameters:**
	- ``string`` suffix: The suffix to add
	- `optional`, ``float`` offset: Offset to add between the suffix and field
	- `optional`, ``StringInputMode`` stringInputMode: Set if the string input is set trough a constant or dynamically trough another member

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, Suffix("suffix")] private int field01;
		[SerializeField, Suffix("suffix with offset", 20f)] private int field02;
	}

.. image:: ../../Images/Suffix01.png

You can dynamically change the label by setting the `stringInputMode` parameter to dynamic and specify a member name in the string parameter to get the string value from::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[Suffix(nameof(stringField), stringInputMode: StringInputMode.Dynamic)]
		[SerializeField] private string stringField;
	}
	
.. image:: ../../Images/Suffix02.gif
