'''
.. module: settings
   :synopsis: Settings used throughout the MVL package.

.. moduleauthor: Andrew J. Young
'''


CLASS_CREATION_THRESHOLD: int = 100
"""
If a user tries to generate a logic system (`LogicSystem.gen_classes()`) with
<n_values> > <CLASS_CREATION_THRESHOLD>, then they will receive a warning.
This warning can be suppressed by passing in `i_have_read_the_ts_and_cs = True`
to that function.
"""
