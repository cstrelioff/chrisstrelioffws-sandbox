Joint, conditional and marginal probabilities
=============================================

In this post I will discuss a topic that seems very dry at first but turns out
to have many cool applications. While I will not discuss Bayesian inference in
this post, understanding the relationship between joint, conditional and
marginal probabilities is essential for the application of Bayesian thinking.
As a result, I'll will often refer back to this discussion in future posts.

.. more::

Setup
-----

To provide simple examples I will consider two scenarios:

* **scenario 1:**
  A coin is tossed, resulting in a heads: :math:`C=H`, or tails:
  :math:`C=T`, with equal probability.  Next, a six sided die is tossed,
  resulting in :math:`D=1, D=2, \ldots`  with equal probability.

* **scenario 2:**
  In scenario two, a coin is again tossed.  As in scenario 1, the probabilities
  of :math:`C=T` and :math:`C=H` are equal. However, if a
  :math:`C=T` a **four-sided die** is tossed and if :math:`C=H` a
  **six-sided die** is tossed.

In each scenario imagine that we obtain the result of a coin and die toss, say
:math:`C=T, D=3` or :math:`C=H, D=6`, *without seeing the coin or die* that
were used to obtain the results.

For each of these scenarios, we can write out a *joint probability table*,
reflecting the probability of all joint occurrences of :math:`C` and :math:`D`,
that is we will write down the joint probabilities :math:`P(C, D)` for all
combinations of :math:`C` and :math:`D` in the main (center) part of the table.

For scenario 1, the table looks like this:

.. math::
    
    \newcommand\T{\Rule{0pt}{1em}{.3em}}
    \begin{array}{c|c|c|c}
               \T & C=H     & C=T    &     \\ \hline
           D=1 \T & 1/12    & 1/12   & 1/6 \\
           D=2 \T & 1/12    & 1/12   & 1/6 \\
           D=3 \T & 1/12    & 1/12   & 1/6 \\
           D=4 \T & 1/12    & 1/12   & 1/6 \\
           D=5 \T & 1/12    & 1/12   & 1/6 \\
           D=6 \T & 1/12    & 1/12   & 1/6 \\ \hline      
               \T & 1/2     & 1/2    & 1
    \end{array}
    
For scenario 2, the table is considerably more complicated, and looks like this:

.. math::
    
    \newcommand\T{\Rule{0pt}{1em}{.3em}}
    \begin{array}{c|c|c|c}
               \T & C=H     & C=T    &     \\ \hline
           D=1 \T & 1/12    & 1/8    & 5/24 \\
           D=2 \T & 1/12    & 1/8    & 5/24 \\
           D=3 \T & 1/12    & 1/8    & 5/24 \\
           D=4 \T & 1/12    & 1/8    & 5/24 \\
           D=5 \T & 1/12    & 0      & 1/12 \\
           D=6 \T & 1/12    & 0      & 1/12 \\ \hline      
               \T & 1/2     & 1/2    & 1
    \end{array}

Before moving on consider the patterns in the above tables.  Notice how the rows
sum to give the last column: :math:`1/12+1/12=1/6` (scenario 1) and
:math:`1/12+1/8=5/24` (scenario 2) for example.  Also note how the columns
sum to give the last row. Why should these patterns be there?  If it is not
clear now, it should be by the end of the post.

Understanding the tables
------------------------

Let's first consider the table for scenario 1.  If we wanted to know the
probability that the coin landed on heads and the die rolled a 4, that is
:math:`P(C=H, D=4)`, we could look at the appropriate column and row are read
it off (blue, underlined entry):

.. math::
    
    \newcommand\T{\Rule{0pt}{1em}{.3em}}
    \begin{array}{c|c|c|c}
               \T & C=H                 & C=T    &     \\ \hline
           D=1 \T & 1/12                & 1/12   & 1/6 \\
           D=2 \T & 1/12                & 1/12   & 1/6 \\
           D=3 \T & 1/12                & 1/12   & 1/6 \\
           D=4 \T & \color{blue}{\underline{1/12}}  & 1/12   & 1/6 \\
           D=5 \T & 1/12                & 1/12   & 1/6 \\
           D=6 \T & 1/12                & 1/12   & 1/6 \\ \hline      
               \T & 1/2                 & 1/2    & 1
    \end{array}
    
So, for scenario 1, :math:`P(C=H, D=4) = 1/12`.  What if we wanted
:math:`P(C=T, D=6)` for scenario 2?  We could read off that entry from the
appropriate table (blue, underlined entry):

.. math::
    
    \newcommand\T{\Rule{0pt}{1em}{.3em}}
    \begin{array}{c|c|c|c}
               \T & C=H   & C=T    &     \\ \hline
           D=1 \T & 1/12  & 1/8   & 5/24 \\
           D=2 \T & 1/12  & 1/8   & 5/24 \\
           D=3 \T & 1/12  & 1/8   & 5/14 \\
           D=4 \T & 1/12  & 1/8   & 5/24 \\
           D=5 \T & 1/12  & 0     & 1/12 \\
           D=6 \T & 1/12  & \color{blue}{\underline{0}}   & 1/12 \\ \hline      
               \T & 1/2   & 1/2    & 1
    \end{array}

So, for scenario 2, :math:`P(C=T, D=6) = 0`.

Joint and marginal probabilities
--------------------------------

Now that we can read off the **joint probabilities**  for the coin :math:`C`
and die :math:`D`, how do we get probabilities for specific outcomes for
*just the coin* or *just the die*?  This is exactly what **marginal
probabilities**  give us.  Let's start with an example for each of the
scenarios by calculating the probability that the die rolls a **6** (imagine
that we can't see what die is rolled and are just given the result).

* **scenario 1:** To get the probability for :math:`D=6` we have to sum the
  probability of all joint events that have the desired roll:

.. math::

    \begin{array}{rl}
        P(D=6) & = & P(C=H, D=6)  + P(C=T, D=6) \\
               & = & 1/12 + 1/12 \\
               & = & 1/6
    \end{array}

Of course, :math:`P(D=6) = 1/6` should make sense for scenario 1 because a
six-sides die is always thrown.  This means the probability that :math:`D=6` is
*independent* of the coin toss.

* **scenario 2:** Next we do the same calculation for the second scenario. Note
  that while the equation on the first line is the same, the probabilities that 
  we substitute are different:

.. math::

    \begin{array}{rl}
        P(D=6) & = & P(C=H, D=6)  + P(C=T, D=6) \\
               & = & 1/12 + 0 \\
               & = & 1/12
    \end{array}

So in this scenario, the probability is reduced due to the fact that a
four-sided die is thrown when :math:`C=T`.  This reduces the probability of
getting :math:`D=6` to :math:`1/12` -- the probability of :math:`D=6` is
*not independent* of the coin toss.

So, in general we can go from joint to marginal distribution by doing a sum
over the variable that we want to get rid of.  For our examples above we wanted
:math:`P(D=d)` where :math:`d=6` and summed over all possible values of
:math:`C`.  A general expression for this would be (for any :math:`d`):

.. math::

    \begin{array}{rl}
        P(D=d) & = & \sum_{c=H,T} P(C=c, D=d) \\
               & = & P(C=H, D=d) + P(C=T, D=d)
    \end{array}

where the symbol :math:`\Sigma` means to sum, resulting in the expanded
expression on the second line.

The same thing can be done if we are interested in just the probability of the
coin toss, resulting in the general expression:

.. math::

    \begin{array}{rl}
        P(C=c) & = & \sum_{d=1-6} P(C=c, D=d) \\
               & = & P(C=c, D=1) + P(C=c, D=2) \\
               & + & P(C=c, D=3) + P(C=c, D=4) \\
               & + & P(C=c, D=5) + P(C=c, D=6)
    \end{array}

In this case there are many more terms in the sum because there are up to six
values for :math:`D`.

Given this discussion of going from joint probabilities to marginal
probabilities you should be able to go back to tables for scenario 1 and 2
(above) and figure out why the rows and columns sum they way that they do.

Conditional probabilities
---------------------------------------------

Finally we discuss finding conditional probabilities from the joint and
marginal probabilities that we calculated above. Let's calculate a conditional 
probability of getting :math:`D=6` **given that** :math:`C=T`, denoted
:math:`P(D=6 \vert C=T)`. To calculate this probability we have to relate all
of the types of probabilities discussed in this post:

.. math::

    \begin{array}{rl}
        P(C=c, D=d) & = & P(D=d \vert C=c) P(C=c) \\
                    & \mathrm{or} & \\
        P(C=c, D=d) & = & P(C=c \vert D=d) P(D=d)
    \end{array}

So we can write the same joint probability two different ways. However, in both
cases the joint probability is equal to a conditional probability multiplied by
a marginal probability. Let's take the first form and rearrange to provide an
equation for the conditional probability that we want:

.. math::

    P(D=6 \vert C=T) = \frac{P(C=T, D=6)}{P(C=T)}

Using the relationship between joint and marginal probabilities, we can
substitute

.. math::

    P(C=T) = \sum_{d=1-6} P(C=T, D=d)

into the equation for our conditional probability to get

.. math::

    P(D=6 \vert C=T) = \frac{P(C=T, D=6)}{\sum_{d=1-6} P(C=T, D=d)}

This equation has a form that you will see over and over, including in Bayes'
Theorem, so take some time to make sure that it makes sense.

Finally, let's apply the equation to scenarios 1 and 2. First, scenario 1:

.. math::

    \begin{array}{rl} 
        P(D=6 \vert C=T) & = & \frac{1/12}{1/2} \\
                         & = & 1/6
    \end{array}

Next, scenario 2:

.. math::

    \begin{array}{rl} 
        P(D=6 \vert C=T) & = & \frac{0}{1/2} \\
                         & = & 0
    \end{array}

Do these results make sense to you? For scenario 1 a six-sided die is always
thrown so

.. math::

    P(D=6 \vert C=T) = P(D=6) 

However, for scenario 2 a four-sided is thrown if :math:`C=T` and

.. math::

    P(D=6 \vert C=T) \neq P(D=6)

This means that the die and coin variables are *independent* in scenario 1 an
*dependent* in scenario 2.

Summing up
----------

That's it, I hope some people will find this post helpful. As I mentioned at
the start of the post I hope to use this information as reference for
discussions of Bayesian methods and related topics.  As always, please
comment, ask questions and point out mistakes if you find them.

.. author:: default
.. categories:: none
.. tags:: joint probability, conditional probability, marginal probability, Bayesian
.. comments::
