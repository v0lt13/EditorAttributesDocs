DisableField Attribute
=====================

Attribute to disable a field based on a condition.

**Parameters:**
	- ``string`` conditionName: The name of the boolean condition to evaluate
	- ``object`` enumValue: The value of the enum condition
	
The field will remain enabled by default until its condition becomes true::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition;
	
		[SerializeField, DisableField(nameof(condition))] private int field;
	}
	
.. image:: ../Images/DisableField01.png

.. image:: ../Images/DisableField02.png

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
	
		[SerializeField, DisableField(nameof(condition), States.State02)] private int field;
	}
	
The field will be disabled when the ``enum`` is set to `State02`.

.. image:: ../Images/DisableField03.png

.. image:: ../Images/DisableField04.png

.. note::
	It cannot look for the condition inside a ``struct``

