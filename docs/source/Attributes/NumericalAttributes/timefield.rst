TimeField Attribute
===================

Attribute to display a numerical field as a specified time format and convert it to a single value

**Parameters:**
	- ``TimeFormat`` timeFormat: The format in which to display the time
	- ``ConvertTo`` convertTo: What to convert the time value into

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField, TimeField(TimeFormat.YearMonthWeek, ConvertTo.Days)] private int intField;
		[SerializeField, TimeField(TimeFormat.DayHourMinute, ConvertTo.Seconds)] private float floatField;
	}

.. image:: ../../Images/TimeField01.png

We can see the converted value in the debug view.

.. image:: ../../Images/TimeField02.png

.. note::
	The `TimeField Attribute` can only be attached to ``float`` and ``int`` fields
