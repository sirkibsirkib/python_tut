# Task 1: Converter

## Prompt

Write a script that, when run, will wait for the user's input. The program will support conversion from kilometers to miles, and kilograms to pounds. The program interprets the user's input and determines what to print depending on the input unit. For example:

```
Input your value:
>>> 1.0
Input your unit:
>>> kg
2.20462 lb
```

Your script should use `lb`, `kg`, `km`, `mi` as the unit denominator. Once the output is given, the program ends. If the user gives something unexpected, the program should complain that it doesn't recognize the unit.

```
Input your value:
>>> 48
Input your unit:
>>> zoop
Unknown unit!
```

## Intention

This second assignment forces you to use conditionals and handle some variables.
