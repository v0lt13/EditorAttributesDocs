HideField Attribute
===================

Attribute to hide fields based on a condition.

**Parameters:**
	- ``string`` conditionName: The name of the condition to evaluate
	- ``object`` enumValue: The value of the enum condition

The field will remain shown by default until its condition becomes true::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition;
	
		[SerializeField, HideField(nameof(condition))] private int field;
	}
	
.. image:: ../Images/HideField01.png

.. image:: ../Images/HideField02.png

You can also use enums as a condition like this::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		private enum States
		{
			State01,
			State02,
			State03
		}
	
		[SerializeField] private States condition;
	
		[SerializeField, HideField(nameof(condition), States.State02)] private int field;
	}
	
The field will be hidden when the ``enum`` is set to `State02`.

.. image:: ../Images/HideField03.png

.. image:: ../Images/HideField04.png

.. note::
	It cannot look for the condition inside a ``struct`` and it cannot hide arrays or lists, only the fields inside them
