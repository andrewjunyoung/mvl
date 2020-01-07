# MVL (many valued logic)

MVL (many valued logic) is a flexible, expressive, and extensible python package
which makes it easy to work with many valued logic systems: logic systems which
use more than 2, or infinite truth values, beyond «True» and «False».

|                |       | 
|----------------|-------|
| Latest release | 0.2.0 |

## Table of contents

<!-- vim-markdown-toc GFM -->

* [Problem statement](#problem-statement)
  * [Example](#example)
* [What does MVL do?](#what-does-mvl-do)
  * [Example usage](#example-usage)
* [Where to get it](#where-to-get-it)
  * [PyPI (pip)](#pypi-pip)
* [Features](#features)
  * [Summary](#summary)
  * [Supported logic systems](#supported-logic-systems)
* [Usage examples](#usage-examples)
  * [Importing and using 3 valued systems](#importing-and-using-3-valued-systems)
  * [Creating n valued logical systems](#creating-n-valued-logical-systems)
  * [Creating arbitrary logical values](#creating-arbitrary-logical-values)
* [License](#license)
* [Documentation](#documentation)
* [Links](#links)

<!-- vim-markdown-toc -->


## Problem statement
By default, python doesn't provide any boolean infrastructure for values other
than «True» and «False». This makes it verbose, difficult, or impossible to deal
with situations involving many valued logic.

### Example
To demonstrate this limitation, we'll use an example in logic. Consider the
sentence:

```
The apple is red.
```

We have an apple that's kinda redish yellow, or somewhere in the middle. So the
answer to this question is a very half-hearted «maybe?».

Now consider the sentence:

```
The apple is red, and the apple is not red.
```

In 2 valued logic, this would always be false. But our apple is maybe red, but
also maybe not red.

3 valued logic has a solution to problems like this, where we have ranges of
truth values between true and false. Say our answer to the first question is `maybe` then our answer to the second question can be `maybe and maybe`. So our
final answer to the second question is `maybe`.

In real life, SQL uses 3 valued logic to implement its logic. MVL provides an
easy way to implement these sort of checks in python.


## What does MVL do?

MVL provides classes and functions which implement 3, n, or ∞ valued logic which
can be imported and used in code bases. It provides conversion between floats
and logical values to allow different degrees of truthfulness, provides a
library of default operators, and allows for the implementation of custom
operators which can be used to analyze logical statements of arbitrary values.

### Example usage
Going back to our apple example, to do logic on keys that may be pressed, we
need more than just «true» and «false» values to deal with this -- we need 3
valued logic.

Writing a logical condition for the second sentence will look like this:

```
if (priest.bool_(
    priest.or_(is_red(apple), priest.not_(is_red(apple)))
)):
    do something
```

Let's break this down.

First, imagine that `is_red(apple)` is some function defined somewhere else
that returns one of 3 logic values telling us if `apple` is red.

We're going to use priest logic, which just means that we use 3 boolean
values, and that anything that's not «false» will evaluate to «true» when we
convert it into python's 2 valued boolean system. The 3 values we use are
(«priest.f» for «false»; «priest.u» for «unknown»; and «priest.t» for «true»).

`if(...)` is a normal python `if` statement. This needs a normal, 2 valued
python boolean in order to work. We'll come back to this.

`priest.bool_(...)` will convert whatever our 3 valued logic value is into a 2
valued python boolean. Exactly how this is defined depends a on the logic system
we choose to use. We've used priest logic, so «priest.u» and «priest.t» will
evaluate to python's built-in «True», and «priest.f» will evaluate to python's
built-in «False».

There's more to this function going on behind the scenes. You won't need it for
this example, but you can read about it in the documentation if you're
interested.

The rest of the example is logical statements made up of comparisons between the
key state (pressed or not pressed) and the priest logic value we want them to
be. This will give us a result as a float between 0 and 1.

The result is passed into `priest.bool_` to give a python boolean, which is
passed into the `if` statement to decide whether or not to output a capital
letter.


## Where to get it

The source code is hosted on github at https://github.com/andrewjunyoung/mvl.

### PyPI (pip)


To install mvl through pip, open a command line interface and run

```
$ pip install mvl
```


## Features

### Summary
- Logical systems which can use 3, n, or infinite logic values.
- A rich library of logical operators for 3, n, and ∞ valued logic.
- Conversion between floats and logical values.

### Supported logic systems
The following 3 valued logic systems are supported by MVL:
  - Bochvar
  - Kleene
  - Priest

The following n valued logic systems are supported by MVL:
  - Łukasiewicz
  - Gödel (under the name «goedel»)
  - Product logic
  - Post logic

The following systems are planned for future support:
  - Belnap's 4 valued logic


## Usage examples

Using MVL is designed to integrate with existing python infrastructure as much
as possible. Example usages of kleene and lukasiewicz logic are given below.

### Importing and using 3 valued systems

```
>>> from mvl import kleene
>>> kleene.t
LukasiewiczLogicValue.True
>>> kleene.and_(k.t, k.u)
0.5
>>> kleene.or_(k.u, k.u)
0.5
>>> kleene.implies(k.u, k.u)
0.5
>>> kleene.implies(k.f, k.u)
1.0
```

### Creating n valued logical systems

```
>>> from mvl.lukasiewicz import *
>>> ls = LogicSystem(5, LukasiewiczLogicValue)
>>> ls.values
[LukasiewiczLogicValue(0.0), LukasiewiczLogicValue(0.25), LukasiewiczLogicValue(0.5), LukasiewiczLogicValue(0.75), LukasiewiczLogicValue(1.0)]
>>> t = ls.values[4]
>>> bool(t)
True
>>> bool(ls.values[3])
False
```

### Creating arbitrary logical values

```
>>> from mvl.lukasiewicz import *
>>> x = LukasiewiczLogicValue(0.123)
>>> x
LukasiewiczLogicValue(0.123)
>>> bool(x)
False
>>> s_and(x, 1)
0.123
```


## License

Unlicense. 


## Documentation

The sphinx documentation can be generated and opened as follows:

1. Open a command line.
1. Navigate to the «docs» directory.
1. Run the command `make html`

It can be read by opening the file `<project_path>/docs/build/html/index.html`.


## Links

| Resource                                |           |
|-----------------------------------------|-----------|
| How do I know what logic system to use? | Todo      |
| Documentation                           | Todo      |

