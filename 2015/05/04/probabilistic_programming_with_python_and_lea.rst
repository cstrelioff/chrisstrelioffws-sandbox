Probabilistic programming with Python and Lea
=============================================

In this post I will cover installation of a probabilistic programming package
for Python called `Lea`_ and provide some simple examples of using the package
to do calculations with joint, conditional and marginal distributions.  These
examples follow the by-hand calculations done in my previous
:ref:`joint, conditional and marginal probabilities` post.  `Lea`_ is
really interesting to me because it makes probabilistic programming very easy--
think reasoning with distributions and Bayesian networks instead of MCMC
calculations.  In this post I'll start with basic calculations to demonstrate
usage, but I'll move onto classic Bayesian and Bayesian network examples in
future posts. Also, be sure to check out the `Lea Python tutorials`_ for other
great examples.

.. more::

Installing Lea
--------------

Okay, let's get started with the installation.  To do this we'll use **pip**,
and optionally **virtualenv**, for the install. If you do not have these tools
setup, I have posts that cover this in detail for Ubuntu 14.04:

* :ref:`initial python setup`
* :ref:`virtualenvs on ubuntu 14.04`

Assuming these tools are available you can install in *one of the following
ways*:

**1. as a user**

.. code-block:: bash

    $ pip install --user lea

**2. global install**

.. code-block:: bash

    $ sudo pip install lea

**3. in a virtual environment**

.. code-block:: bash

    $ mkvirtualenv lea_env
    (lea_env)$ pip install lea

To check the install, whichever way you chose to do it, you should be able to
do:

.. code-block:: bash

    $ pip show lea
    ---
    Name: lea
    Version: 2.1.1
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: 

and get something like the above.  From the output we can see the Version
**2.1.1** is installed, the current version at this time. From the *Location*
output, we can also see that I've installed Lea as a user.  You should
also able to start Python and import the package without errors:

.. code-block:: python

    >>> import lea

Okay, that's it, Lea is installed and we're ready to do the examples. As I
mentioned above, the `Lea Python tutorials`_ are also very nicely done, so you
should check those out for many more examples.

Examples
--------

All the examples to follow are available as a **gist**: `my lea gist`_, or you
can follow along at your terminal.  To start we do imports:


.. code-block:: python

    from __future__ import division, print_function
    from lea import Lea
    



These statements import `Lea`_ as well as some utility functions that let
Python 2.7 behave more like Python 3.x with respect to division and print.

Next, let's review the two scenarios from the
:ref:`joint, conditional and marginal probabilities` post. The goal will be
to use `Lea`_ to replicate the calculations done there. So, to the scenarios:

* **scenario 1:**
  A coin is tossed, resulting in a heads: :math:`C=H`, or tails:
  :math:`C=T`, with equal probability.  Next, a six sided die is tossed,
  resulting in :math:`D=1, D=2, \ldots`  with equal probability.

* **scenario 2:**
  In scenario two, a coin is again tossed.  As in scenario 1, the probabilities
  of :math:`C=T` and :math:`C=H` are equal. However, if a
  :math:`C=T` a **four-sided die** is tossed and if :math:`C=H` a
  **six-sided die** is tossed.

To review, **scenario 1** is designed to have the coin toss and die roll be
*independent*: a six-sided die is always thrown, whether the coin resulted in
an `H` or `T`.  **Scenario 2** is designed to have the coin toss and die roll
be *dependent*: whether a six-sided or four-sided die is tossed *depends* on the
outcome of the coin-toss.

To implement these scenarios, we'll start by defining distributions for the
coin, four-sided die and six-sided die.  First, the coin:


.. code-block:: python

    # define coin
    coin = Lea.fromValFreqs(('H', 1),
                            ('T', 1))
    
    print('Coin Distribution',
          coin,
          sep='\n')
    

::

    Coin Distribution
    H : 1/2
    T : 1/2
    
    



next, the six-sided die:


.. code-block:: python

    # define six-sided die
    die6 = Lea.fromValFreqs(('1', 1),
                            ('2', 1),
                            ('3', 1),
                            ('4', 1),
                            ('5', 1),
                            ('6', 1))
    
    print('Six-sided Die Distribution',
          die6,
          sep='\n')
    

::

    Six-sided Die Distribution
    1 : 1/6
    2 : 1/6
    3 : 1/6
    4 : 1/6
    5 : 1/6
    6 : 1/6
    
    



and, finally, the four-sided die:


.. code-block:: python

    # define four-side die
    die4 = Lea.fromValFreqs(('1', 1),
                            ('2', 1),
                            ('3', 1),
                            ('4', 1))
    
    print('Four-sided Die Distribution',
          die4,
          sep='\n')
    

::

    Four-sided Die Distribution
    1 : 1/4
    2 : 1/4
    3 : 1/4
    4 : 1/4
    
    



Next we define the scenarios in Lea using *conditional probability tables* and
the building blocks defined above. For the first scenario we have:


.. code-block:: python

    # construct Scenario 1
    scenario1 = Lea.buildCPT((coin == 'H', die6),
                             (coin == 'T', die6))
    
    print('Scenario 1',
          scenario1,
          sep='\n')
    

::

    Scenario 1
    1 : 1/6
    2 : 1/6
    3 : 1/6
    4 : 1/6
    5 : 1/6
    6 : 1/6
    
    



and for the second scenario we change to :code:`die4` if a T is thrown:


.. code-block:: python

    # construct Scenario 2
    scenario2 = Lea.buildCPT((coin == 'H', die6),
                             (coin == 'T', die4))
    
    print('Scenario 2',
          scenario2,
          sep='\n')
    

::

    Scenario 2
    1 : 5/24
    2 : 5/24
    3 : 5/24
    4 : 5/24
    5 : 2/24
    6 : 2/24
    
    



In each case Lea provides the marginal probabilities for the value obtained
from the die roll. To get a better sense of the two scenarios we can also
have Lea provide the joint probabilities for all outcomes, both coin toss and
die roll, using the *Cartesian product*:


.. code-block:: python

    # get joint probs for all events
    # -- scenario 1
    joint_prob1 = Lea.cprod(coin, scenario1)
    
    print('Scenario 1',
          '* Joint Probabilities',
          joint_prob1,
          sep='\n')
    

::

    Scenario 1
    * Joint Probabilities
    ('H', '1') : 1/12
    ('H', '2') : 1/12
    ('H', '3') : 1/12
    ('H', '4') : 1/12
    ('H', '5') : 1/12
    ('H', '6') : 1/12
    ('T', '1') : 1/12
    ('T', '2') : 1/12
    ('T', '3') : 1/12
    ('T', '4') : 1/12
    ('T', '5') : 1/12
    ('T', '6') : 1/12
    
    



and, for scenario 2:


.. code-block:: python

    # get joint probs for all events
    # -- scenario 2
    joint_prob2 = Lea.cprod(coin, scenario2)
    
    print('Scenario 2',
          '* Joint Probabilities',
          joint_prob2,
          sep='\n')
    

::

    Scenario 2
    * Joint Probabilities
    ('H', '1') : 2/24
    ('H', '2') : 2/24
    ('H', '3') : 2/24
    ('H', '4') : 2/24
    ('H', '5') : 2/24
    ('H', '6') : 2/24
    ('T', '1') : 3/24
    ('T', '2') : 3/24
    ('T', '3') : 3/24
    ('T', '4') : 3/24
    
    



These should be compared with the Joint Probability Tables that I constructed
in my :ref:`joint, conditional and marginal probabilities` post-- exactly the
same output and super simple to obtain with Lea.

Let's finish up by calculating the some *conditional probabilities*. In this
case, what are the probabilities of an 'H' or 'T' given that we have a '6' from
the die?  Using Lea, this is simple:


.. code-block:: python

    # prob coin given D=6, scenario 1
    print("Scenario 1 -> P(C|D=6)",
          coin.given(scenario1 == '6'),
          sep='\n')
    

::

    Scenario 1 -> P(C|D=6)
    H : 1/2
    T : 1/2
    
    



whereas for scenario 2 we get:


.. code-block:: python

    # prob coin given D=6, scenario 2
    print("Scenario 2 -> P(C|D=6)",
          coin.given(scenario2 == '6'),
          sep='\n')
    

::

    Scenario 2 -> P(C|D=6)
    H : 1
    
    



The results are very different for the two scenarios by construction. Does
the difference make sense? Calculate things out by-hand if they don't and then
reflect on how easy `Lea`_ makes things!

What if we'd seen a '4' instead? For scenario 1


.. code-block:: python

    # prob coin given D=4, scenario 1
    print("Scenario 1 -> P(C|D=4)",
          coin.given(scenario1 == '4'),
          sep='\n')
    

::

    Scenario 1 -> P(C|D=4)
    H : 1/2
    T : 1/2
    
    



and for scenario 2:


.. code-block:: python

    # prob coin given D=4, scenario 2
    print("Scenario 2 -> P(C|D=4)",
          coin.given(scenario2 == '4'),
          sep='\n')
    

::

    Scenario 2 -> P(C|D=4)
    H : 2/5
    T : 3/5
    
    



In this example the difference between scenarios 1 and 2 is more subtle, but
it's still there.  Again, make sure the difference makes sense.

Summing Up
----------

`Lea`_ is a great tool for probabilistic programming and thinking in Python.
I'll definitely be posting more examples with a goal of looking at Bayesian
(aka Belief) networks using `Lea`_.  As always corrections, comments and
questions are welcome below.

.. _Lea: https://code.google.com/p/lea/
.. _Lea Python tutorials: https://code.google.com/p/lea/wiki/LeaPyTutorial

.. _my lea gist: https://gist.github.com/cstrelioff/468414dd8cc3c3b60b26

.. author:: default
.. categories:: none
.. tags:: python, Lea, joint probability, conditional probability, marginal probability, Bayesian
.. comments::
