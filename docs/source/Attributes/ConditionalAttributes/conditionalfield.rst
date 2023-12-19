ConditionalField Attribute
==========================

Attribute to show/hide or disable/enable a field based on a bunch of conditions.

**Parameters:**
	- ``ConditionType`` conditionType: How to evaluate the the specified booleans
	- `optional`, ``ConditionResult`` conditionResult: What happens to the property when the condition evaluates to true
	- `optional`, ``bool array`` negatedValues: Specify which booleans to negate
	- `params`, ``string`` booleanNames: The names of the booleans to evaluate

The field will be shown when the result of the specified conditions return true::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition01;
		[SerializeField] private bool condition02;
	
		[SerializeField, ConditionalField(ConditionType.AND, nameof(condition01), nameof(condition02))] 
		private int field;
	}
	
In this case we set the ``ConditionType`` to ``AND`` so the evaluation will be something like this:
``condition01 && condition02``

.. image:: ../Images/ConditionalField01.png

.. image:: ../Images/ConditionalField02.png

We can also set it to ``OR`` and it will evaluate like this:
``condition01 || condition02``

.. image:: ../Images/ConditionalField03.png

.. image:: ../Images/ConditionalField04.png

``NAND`` which will evaluate like this:
``!condition01 && !condition02``

.. image:: ../Images/ConditionalField05.png

.. image:: ../Images/ConditionalField06.png

And ``NOR`` which evaluates like this:
``!condition01 || !condition02``

.. image:: ../Images/ConditionalField07.png

.. image:: ../Images/ConditionalField08.png

On top of the ``ConditionType`` we can also specify a certain condition we want to negate by creating a ``bool`` array that must contain the 
the conditions we want to negate in the order we added them.
We set true for conditions we want to negate and set false for conditions we don’t::
	
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition01;
		[SerializeField] private bool condition02;
	
		[SerializeField, ConditionalField(ConditionType.AND, new bool[] { false, true }, nameof(condition01), nameof(condition02))] 
		private int field;
	}
	
So in this case we only negate `condition02` and the evaluation will be something like this:
``condition01 && !condition02``

.. image:: ../Images/ConditionalField09.png

.. image:: ../Images/ConditionalField10.png

.. image:: ../Images/ConditionalField03.png

.. image:: ../Images/ConditionalField05.png

By default the ConditionalField attribute will only show/hide fields, but you can also set it to only enable/disable fields, 
by setting the ``ConditionResult`` parameter to the value `EnableDisable`, like so::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition01;
		[SerializeField] private bool condition02;
	
		[SerializeField, ConditionalField(ConditionType.AND, ConditionResult.EnableDisable, nameof(condition01), nameof(condition02))] 
		private int field;
	}
	
.. image:: ../Images/ConditionalField11.png

.. image:: ../Images/ConditionalField12.png

.. note::
	It cannot hide arrays or lists, only the fields inside them
