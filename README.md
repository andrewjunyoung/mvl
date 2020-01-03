# MVL (many valued logic)

MVL (many valued logic) is a python package which implements different logic
systems that use more than 2 values.

## What logic systems are implemented?
The following 3 valued logic systems are supported by MVL:
  - Bochvar
  - Kleene
  - Priest

The following n valued logic systems are supported by MVL:
  - Łukasiewicz

The following systems are planned for future support:
  - Gödel MVL
  - Belnap
  - Product logic
  - Post logic

## Usage

Using MVL is designed to integrate with existing python infrastructure as much
as possible. Example usages of kleene and lukasiewicz logic are given below.

```
>>> from mvl import kleene as k
>>> k.t
LukasiewiczLogicValue.True
>>> k.and_(k.t, k.u)
0.5
>>> k.or_(k.u, k.u)
0.5
>>> k.implies(k.u, k.t)
1.0
>>> k.implies(k.u, k.u)
0.5
>>> k.implies(k.f, k.u)
1.0

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
