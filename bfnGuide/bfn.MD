# Language Design

Bfn is designed to purposely use as few characters as possible. Similar to brainfuck, it uses a cell system in which you cycle through different cells and change their numeral values. Unlike brainfuck, you can set these cells to any value, whether that be a string, number, list or whatever it may be. Bfn also comes loaded with other abilities brainfuck doesn't offer.

# Syntax

The only whitespace that matters in bfn is linebreaks. Bfn is run line by line and therefore runs each line as its own statement.

## Operation Syntax

To cycle through cells in bfn you use '<' and '>' side by side with an integer. If no integer is by its side, it will default to 1. For example,

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

# Basic Tools

## Printing

In order to print, select the cell you wish to print and simply run

```
print
```

## Loops

The only loop available as of now in bfn is a while loop. The syntax is as follows

```
while =0:1+;print
```

This simply says while the current cell is equal to 0, it will add one to the cell and print. Semicolons replace linebreaks and all comparators(=, !=, <, >, >=, <=) are available. Comparators go before the first number and the code to run is placed after the colon.

## If

If statements use the exact same logic and syntax as while loops but only activate once.

```
if =0:1+;print
```