# Task 2: Piglatin

## Prompt

### Step 1

Write a script that will listen for a user's input. The user will give some word. The program would then print the 'pig latin' form of that input. The program doesn't need to provide any kind of prompt

Pig latin is an operation on a string, whereby the last letter is moved to the front, and the end is appended with -'ay'. More formally, it is given as:

*x<sub>1</sub>x<sub>2</sub>...x<sub>n-1</sub>x<sub>n</sub>* =>  *x<sub>n</sub>x<sub>1</sub>x<sub>2</sub>...x<sub>n-1</sub>* ay

eg:

hello => ellohay

(Use `CTRL + C` or `Command + C` to interrupt a program runnning in your terminal. This will kill it)

Here's an example of a correct interaction:

```
>>> banana
ananabay
>>> sleep
psleeay
```

### Step 2

The user's input might consist of several words. The transformation should be applied to each word in the input *separately*. This requires considering each word in turn.
For this, you need can use the `split()` function for strings.

Once the output is given, the program should ask again. This behaviour loops endlessly


```
>>> hello there
ellohay etheray
>>> my you're a tall one
ymay eyou'ray aay ltalay eonay
``

## Intention
This task requires string and list operations
