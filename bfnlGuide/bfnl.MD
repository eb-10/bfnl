# Language Design

bfnl is designed to be a lightweight and easy to learn language. Similar to brainfuck, it uses a cell system in which you cycle through different cells and change their numeral values. Unlike brainfuck, you can set these cells to any value, whether that be a string, number, list or whatever it may be. bfnl also comes loaded with other abilities brainfuck doesn't offer, including functions.

# Syntax

The only whitespace that matters in bfnl is linebreaks. bfnl is run line by line and therefore runs each line as its own statement.

## Operation Syntax

To cycle through cells in bfnl you use '<' and '>' side by side with an integer. If no integer is by its side, it will default to 1. For example,

```
12>
```

will go forward 12 cells, while

```
12<
```

will go back 12 cells.

A similar system is used to change cell values.

```
15+
```

will add 15 to the currently selected cell, while

```
15-
```

will subtract 15 from the currently selected cell. The same syntax is used for multiplication('n*'), division('n/') and exponents('n^')

You also may set a cell by simply running

```
15=
```

Of course this is also how you can set cells to lists and strings.


When using operators with lists and strings, only + and - are supported. To do so, simply run either

```
'your_string_here' +/-
```

or

```
['your', 'list', 'here'] +/-
```

Attempting to subtract a list or string from a cell that doesn't contain the list or string will throw a syntax error. For example, you may not run

```
['your', 'list', 'here']-
```

to a cell with

```
['your', 1, 2]
```

because list 2 does not contain the entirety of list 1. However, you may run

```
[0, 1]-
```

to a cell containing

```
[0, 1, 2]
```

and the remaining list will simply be

```
[2]
```

The same logic applies to strings.

## Function Syntax

Functions are another data type that can be entered into a cell. No operator other than '=' can be used on a function and functions are the single data type that can be accessed no matter what cell you are selected on.

To create a function, simply select your cell and run

```
my_function(params):function_code_here =
```

Functions can of course be accessed from anywhere, by simply calling

```
my_function(params)
```

# Basic Tools

## Printing

In order to print, select the cell you wish to print and simply run

```
print
```