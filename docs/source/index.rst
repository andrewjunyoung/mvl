MVL documentation pages
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Lukasiewicz
===========

Łukasiewicz is a many valued logic system. Originally defined by Jan Łukasiewicz
(Polish: [ˈjan wukaˈɕɛvitʂ]) in the 20th century for 3 valued logic, Łukasiewicz
later expanded his system to support arbitrary n valued logic and infinite
valued logic.

Łukasiewicz logics consist of values in the range [0, 1]. If the logic system is
finite, then the set of values in the range [0, 1] is finite and are equal
distances apart at n / (m - 1), where m is the total number of logic values, and
n is the index.

Łukasiewicz defines the following operators, given below alongside their MVL
equivalents:

- implication (implies, →)
- negation (not\_, !)
- equivalence (equivalent, ↔)
- weak conjunction (w_and, &)
- strong conjunction (s_and, &&)
- weak disjunction (w_or, \|)
- strong disjunction (s_or, \|\|)

as well as propositional constants 0 and 1.

Łukasiewicz logics defines the only value which is «true» to be 1, and so
evaluating any other Łukasiewicz value as a python `bool` will evaluate to
`False`.


.. automodule:: mvl.lukasiewicz
   :members:

Goedel
======

Gödel defined many valued logics in 1932 very similarly to Łukasiewicz, using
truth values in the range [0, 1] at positions n / (m - 1) for finite logic
systems (where m is the total number of logic values, and n is the index), and
across the continuous interval [0, 1] for infinite logic systems.

Gödel logics provide only 4 logical operators:

- conjunction (and\_, &)
- disjunction (or\_, \|)
- implication (implies, →)
- negation (not\_, !)

Gödel logics are completely axiomatisable, meaning that one can define a logical
calculus in which all tautologies are provable.


.. automodule:: mvl.goedel
   :members:


Product logic
=============

Product logic applies over the range [0, 1], for finite or infinite logic
systems. It also defines 4 logical operators:

- 2 conjunction operators (mult\_, \*) (and\_, &)
- implication (implies, →)
- negation (not\_, !)


.. automodule:: mvl.product
   :members:

Post logic
==========

Post logics only work on finite valued systems. Like Łukasiewicz logics, they
use logic values n / (m - 1) (where m is the total number of logic values, and n
is the index) over the interval [0, 1].

In contrast to the above logic systems, post logic values need knowledge of
how many logic values are in use inside the system that they are a part of. This
is due to the implementation of the negation (not\_, !) operator (see below).

This means that the way that Post logic values are initialized is slightly more
specific, and requires an index (: int) and a max_index (: int) to be passed in
when creating LogicValues.

Hence

```
PostLukasiewiczLogicValue(1, 3)  # Will work.
PostLukasiewiczLogicValue(1 / 3)  # Wont work (due to insufficient arguments).
```


.. automodule:: mvl.post
   :members:

Bochvar
=======
.. automodule:: mvl.bochvar
   :members:

Kleene
======
.. automodule:: mvl.kleene
   :members:

Priest
======
.. automodule:: mvl.priest
   :members:

3 valued logic operators
========================
.. automodule:: mvl.tvl_operators
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

