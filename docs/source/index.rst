MVL documentation pages
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Lukasiewicz
===========

Lukasiewicz is a many valued logic system. Originally defined by Jan Lukasiewicz
(Polish: [ˈjan wukaˈɕɛvitʂ]) in the 20th century for 3 valued logic, Lukasiewicz
later expanded his system to support arbitrary n valued logic and infinite
valued logic.

Lukasiewicz logics consists of values in the range [0, 1]. If the logic system is
finite, then the set of values in the range [0, 1] is finite and are equal
distances apart at n / (m - 1), where m is the total number of logic values, and
n is the index.

Lukasiewicz defines the following operators, given below alongside their MVL
equivalents:

- implication (implies, →)
- negation (not\_, !)
- equivalence (equivalent, ↔)
- weak conjunction (w_and, &)
- strong conjunction (s_and, &&)
- weak disjunction (w_or, \|)
- strong disjunction (s_or, \|\|)

as well as propositional constants 0 and 1.

Lukasiewicz logic defines the only value which is «true» to be 1, and so
evaluating any other lukasiewicz value as a python `bool` will evaluate to
`False`.


.. automodule:: mvl.lukasiewicz
   :members:

Goedel
======

Goedel defined many valued logics in 1932 very similarly to Lukasiewicz, using
truth values in the range [0, 1] at positions n / (m - 1) for finite logic
systems (where m is the total number of logic values, and n is the index), and
across the continuous interval [0, 1] for infinite logic systems.

Goedel logics provide only 4 logical operators:

- conjunction (and\_, &)
- disjunction (or\_, \|)
- implication (implies, →)
- negation (not\_, !)

Goedel logics are completely axiomatisable, meaning that one can define a logical
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

Post logics only work on finite valued systems. Like lukasiewicz logics, they
use logic values n / (m - 1) (where m is the total number of logic values, and n
is the index) over the interval [0, 1].

In contrast to the above logic systems, post logic values need knowledge of
how many logic values are in use inside the system that they are a part of. This
is due to the implementation of the negation (not\_, !) operator (see below).

This means that the way that Post logic values are initialized is slightly more
specific, and requires an index (: int) and a max_index (: int) to be passed in
when creating LogicValues.

Hence

``
PostLukasiewiczLogicValue(1, 3)  # Will work.

PostLukasiewiczLogicValue(1 / 3)  # Wont work (due to insufficient arguments).
``


.. automodule:: mvl.post
   :members:


Kleene
======

Kleene logic is a 3 valued logic system. It uses 3 logic values: «false»;
«unknown»; and «true», abbreviated as «f», «u», and «t» respectively.

Kleene logic uses lukasiewicz's definition of truth: the only truth value is 1
(the logic value «true» (t)). This distinguishes it from priest logic (see
below).


.. automodule:: mvl.kleene
   :members:


Bochvar
=======

Bochvar logic (also known as «kleene's weak 3 valued logic») is a 3 valued logic
system. It uses 3 logic values: «false»; «unknown»; and «true», abbreviated as
«f», «u», and «t» respectively.

Like kleene logic, the only truth value in bochvar logic is 1.

Bochvar logic uses different definitions of and\_; or\_; and implies, compared
to normal kleene logic. These tables can be found below.

In general, bochvar logic treats the unknwown value (u) as «contagious». The
presence of u in any operator will cause the result to be u, regardless of any
other variables in the expression.


.. automodule:: mvl.bochvar
   :members:


Priest
======

Priest logic is a 3 valued logic system. It uses 3 logic values: «false»;
«unknown»; and «true», abbreviated as «f», «u», and «t» respectively.

Priest logic does not lukasiewicz's definition of truth. Instead, it uses
PriestLogicValues, where all non-zero truth values are said to be truth values.
This distinguishes it from kleene logic (see above).


.. automodule:: mvl.priest
   :members:


3 valued logic operators
========================

This module describes the various operators used by different 3 valued logic
systems. There is lots of overlap between different systems of logic
(particularly kleene and priest logic, and lukasiewicz logic). Logic systems
often define the same operators, sometimes under different names. In order to
support reuse throughout the code base, this module was created as a common
repository for logic operators used in various different 3 valued logic systems.

.. automodule:: mvl.tvl_operators
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

