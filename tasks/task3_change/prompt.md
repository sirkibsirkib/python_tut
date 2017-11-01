# Task 3: Change

The task is to write a program a check-out cachier might use, to transform any given currency amount into a quantity of coins of various denominations.

Write a script that listens for the user to input a number, representing some currency. The script will then decompose that quantity into that smallest number of coins possible out of a set pool of coins. The available values of coins are:
`2.00`, `1.00`, `0.50`, `0.20`, `0.05`, `0.01`.

You can safely assume that the input values will be rounded to the nearest cent (0.01). The output should be a sequence of lines, where each line lists the demonination and the corresponding count, separated by a tab (written as `\t` in a string). Leave out any coins for which the number is zero.

Here is a correct interaction with the finished script:

```
>>> 20.58
2.00	10
0.50	1
0.05	1
0.01	3
```

TODO

## Intention

This task is intended to get you to understanding some more complex control flows, with multiple loops and branches. You will also have to make a slightly more involved output, formatting the lines and correctly leaving out some outputs depending on a condition. Hopefully you will also encounter more than one way to solve the problem and consider the advantages of one over the other(s).