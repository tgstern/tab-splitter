# Bill Splitter

A bill splitter web application built in Flask

This application creates a web form to enter the bill total, number
of splits, and the tip amount. When the form is submitted, it posts the data
and runs code in Python to calculate the amounts each person owes.

The code checks for valid inputs, first with JavaScript to ensure that values are
entered, and again in Python to make sure the right types of values are present.

When the form is submitted, the tip is added to the total and split amongs the number
of people on the bill. The remainder is added 1 cent at a time to each split, to
be sure the correct total is reached.

The calculated screen also shows the tip and final amounts to write on the
receipt.
