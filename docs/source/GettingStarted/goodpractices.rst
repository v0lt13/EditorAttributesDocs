Good Practices
==============

Here are a few good practices to follow when using this package.

.. note::
	These are just some general recommendations to follow when using this package, you don't have to abide by them like laws, if you already have a workflow that fits better for you,
	feel free to use it.
	
Using the void struct
---------------------

The :doc:`voidstruct` is made to act as a holder for attributes that redraw the property is attached to.
While it’s not necessary to use the struct for those attributes (any serialized data type can be used), using the struct as a holder makes the code more readable for you and others.

When you use the :doc:`voidstruct` as a variable it makes it obvious that is a holder and it will be redrawn, it also keeps some consistency in your code rather than using 
``int`` or ``float`` randomly in your code as holders.

Is also a good idea to add a `holder` suffix or other naming convention to the void fields so when it comes up in something like `IntelliSense` you know what it is.

Managing multiple attributes
----------------------------

When an attribute has a lot of parameters or you use multiple attributes on one field, that line of code can become pretty long which is generally a bad thing.
Here is an example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition01;
		[SerializeField] private bool condition02;
		[SerializeField] private bool condition03;
	
		[SerializeField, ReadOnly, ConditionalField(ConditionType.AND, new bool[] { false, true, false }, nameof(condition01), nameof(condition02), nameof(condition03))] private int field;
	}

Our ``int`` field got pretty long, let's see what can we do to organize this better.

- We can put the variable on a separate line with all attributes above it::

	[SerializeField, ReadOnly, ConditionalField(ConditionType.AND, new bool[] { false, true, false }, nameof(condition01), nameof(condition02), nameof(condition03))] 
	private int field;
	
- Keep the attributes from the package and the built-in Unity ones separate::

	[ReadOnly, ConditionalField(ConditionType.AND, new bool[] { false, true, false }, nameof(condition01), nameof(condition02), nameof(condition03))]
	[SerializeField] private int field;

- Put the attribute with a lot of parameters on a separate line::

	[ConditionalField(ConditionType.AND, new bool[] { false, true, false }, nameof(condition01), nameof(condition02), nameof(condition03))]
	[SerializeField, ReadOnly] private int field;

Any of these methods are valid ways of shortening the line of code, is up to you which one you prefer.

Using the nameof expression
---------------------------

Some attributes need to look for a member in your script and it will ask you to give the name of that member as a ``string`` parameter, but strings are error prone and you might encounter issues saying,
`that field cannot be found` and spend hours scratching you head when you realize you just made a typo or had a character in the wrong case. Thats why you should use the 
`nameof <https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/nameof>`_ expression, that allows you to add your variable like a parameter and converts its name to a 
``string`` for the attribute::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private bool condition01;
	
		// Passing the variable as a string (error prone)
		[SerializeField, EnableField("condition01")] private int field01;
	
		// Using the nameof condition
		[SerializeField, EnableField(nameof(condition01))] private int field02;
	}
