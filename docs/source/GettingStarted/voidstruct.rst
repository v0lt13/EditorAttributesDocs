Void Struct
===========

The **Void** struct is an empty serialized struct to use as a holder property for attributes like the :doc:`../Attributes/button`, :doc:`../Attributes/horizontalgroup`, etc. 
that completely redraw the property in the inspector.

The **Void** struct can also be passed as a type in generics, which commonly happens when you make an event system that you want to return void::

	[Serializable]
	public class UnityVoidEvent : UnityEvent<Void> { }
	
If you are using the `System` namespace and `EditorAttributes` namespace in your script then use the **Void** struct you will notice a naming conflict between
``System.Void`` and ``EditorAttributes.Void``, to fix that you will just have to specify which version you want to use, and there are 2 ways to do that.

1. Specify the namespace of the version you want to use on that line::
	
	private System.Void systemVoidField;
	// Or
	private EditorAttributes.Void attributesVoidField;

2. Specify which version you want to use for the whole script under your other usings::

	using Void = System.Void;
	// Or
	using Void = EditorAttributes.Void;
	
A common way this conflict can happen is when you use the editor attributes and serialize structs::

	using System;
	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[Serializable]
		private struct ExampleStruct
		{
			public int data01;
			public int data02;
		}
	
		[SerializeField] private ExampleStruct exampleStruct;
	
		[Button(nameof(Button))]
		[SerializeField] private Void buttonHolder; // This line will throw an error
	
		public void Button() => print("Hello World!");
	}

We can fix the error either by adding ``using Void = EditorAttributes.Void;`` between the usings and class declaration or by removing the ``using System;`` at the top of the file,
then to use the `Serializable Attribute <https://learn.microsoft.com/en-us/dotnet/api/system.serializableattribute?view=net-7.0>`_ we just call the namespace directly::

	[System.Serializable]
	private struct ExampleStruct
	{
		public int data01;
		public int data02;
	}

Now which version you want to use if up to personal preferece.
