# Task 4: Calculator

For this task, you will make an interactive calculator. The calculator is initialized with a stored value of 0. The user can enter *operations* one at a time, which will change the stored value, depending on the operation. After being changed, the new value is printed to output. The user can continue to enter values in this way endlessly.

The last feature is that the calculator should support a concept of "memory slots". The user is allowed to give a command which will save or load the current STORED calculator value into a slot. The calculator has 10 such slots which can be used independently. These slots are identified simply using numbers 0-9.

(Tip: This loading functionality can be implemented using either a python `list` or a python `dict`)

The script offers seven operation in total. Below is a list of operations and how the user needs to format them. 'X' here is a stand-in for some number.
1. `+ X` adds X to the stored value.
1. `- X` subtracts X from the stored value.
1. `* X` multiplies the stored value by X.
1. `/ X` divides the stored value by X.
1. `save X` saves the current stored value into slot '4'. The stored value stays unchanged.
1. `load X` replaces the current stored value with the stored value in slot '4'. The value in slot '4' remains unchanged.
1. `exit` ends the script.

You can safely assume the user will give good input. You can *optionally* extend your calculator to support additional operations, such as `sqr` to square the stored number, `sqrt` to square-root the stored number, etc.

## Intention

This task requires you to manipulate a loop again, but now inside the loop there is some changing of some global state. This combination is a very common design pattern and is analagous to an 'event loop' which is common for games and other interactive applications.
