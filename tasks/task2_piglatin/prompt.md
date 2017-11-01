# Task 2: Piglatin

## Prompt

Write a script that will listen for a user's input. The user will give some word. The program would then print the 'pig latin' form of that input. The program doesn't need to provide any kind of prompt

Pig latin is an operation on a string, whereby the last letter is moved to the front, and the end is appended with '-ay'. More formally, it is given as:

*x<sub>1</sub>x<sub>2</sub>...x<sub>n-1</sub>x<sub>n</sub>* =>  *x<sub>n</sub>x<sub>1</sub>x<sub>2</sub>...x<sub>n-1</sub>* ay

eg:

hello => ellohay

The user's input might consist of several words. The transformation should be applied to each word in the input *separately*.

Once the output is given, the program should ask again. This behaviour loops endlessly

(Use `CTRL + C` or `Command + C` to interrupt a program runnning in your terminal. This will kill it)

Here's an example of a correct interaction

```
>>> hello there
ellohay etheray
>>> my you're a tall one
ymay eyou'ray aay ltalay eonay
``

## Intention

Here you will learn about loops, as well as splitting strings and performing some basic opertions on them.
