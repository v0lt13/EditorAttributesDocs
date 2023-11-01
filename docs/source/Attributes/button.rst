Button Attribute
================

Attribute to add a button in the inspector.

**Parameters:**
	- ``string`` functionName: The name of the function to call when the button is pressed
	- `optional`, ``string`` buttonLabel: The label displayed on the button
	
.. note::
	The function must be public for it to be found.

Because a function is not a property that can be displayed in the editor we need to have a holder variable to attach the attribute to::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		// Button will default to the function name as a label
		[SerializeField, Button(nameof(Button))] private Void buttonHolder01;
	
		// Button with a custom label
		[SerializeField, Button(nameof(Button), "Press Me")] private Void buttonHolder02;
	
		public void Button() => print("Hello World!");
	}

.. image:: ../Images/Button01.png

If your function has parameters they will be displayed under the button as a foldout::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, Button(nameof(Button))] private Void buttonHolder;
	
		public void Button(int param01, float param02, string param03, bool param04) => print("Hello World!");
	}

.. image:: ../Images/Button02.png

.. note::
	The attribute cannot look for functions inside a ``struct`` and it doesn't work well if the holder is an array or list