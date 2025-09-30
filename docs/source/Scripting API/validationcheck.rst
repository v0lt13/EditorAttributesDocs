ValidationCheck
===============

A class to use for more advanced validation checks.

**Inheritance:**
	- *object* -> *ValidationCheck*

**Namespace:** 
	*EditorAttributes*
	
**Assembly:**
	*EditorAttributes.asmdef*
	
Syntax::

	public class ValidationCheck

Properties:
-----------

ValidationMessage
^^^^^^^^^^^^^^^^^

The message displayed in the console.

Declaration::

	public string ValidationMessage { get; private set; }
	

PassedCheck
^^^^^^^^^^^

Has passed the validation check.

Declaration::

	public bool PassedCheck { get; private set; }
	

KillBuild
^^^^^^^^^

Will the validation an error during build time and cancel it.

Declaration::

	public bool KillBuild { get; private set; }
	
	
Severety
^^^^^^^^

The severety of the validation.

Declaration::

	public MessageMode Severety { get; private set; }

Methods:
--------

Fail(string, MessageMode, bool)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Marks the validation as failed.

Declaration::

	public static ValidationCheck Fail(string validationMessage, MessageMode severety = MessageMode.Error, bool killBuild = false)
	
**Parameters:**
	- ``string`` validationMessage: The message to display in the console
	- `optional`, ``MessageMode`` severety: The severety of the validation
	- `optional`, ``bool`` killBuild: Throw an error during build time and cancel it

**Returns:** ``ValidationCheck``: The validation check object

Pass()
^^^^^^

Marks the validation as passed.

Declaration::

	public static ValidationCheck Pass()
	
**Returns:** ``ValidationCheck``: The validation check object
