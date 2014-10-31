.. _bayes medical tests:

Medical tests, a first example of Bayesian calculations
=======================================================

In this post I will discuss a first example of a Bayesian calculation using a
well-known example of testing for breast cancer. I choose this example for a
few reasons:

* The answer often surprises people and supposedly many doctors get this
  wrong.
* The problem provides a nice example of updating a **prior** (information
  before) to a **posterior** (information after).  This is really essential to
  understanding Bayesian thinking and I will emphasize this idea, making a
  point of connecting the concept to mathematical notation.
* The calculations are relatively simple (at least compared with other
  examples). If you understood my post on
  :ref:`joint, conditional and marginal probabilities`, you should have no
  problems.

.. more::

Before we get started, I will point out `cancer test example 1`_ and `cancer
test example 2`_, which both provide discussions of this exact same example.
You should also check those posts out for another view of the problem.  Also,
there is a `wikipedia drug test example`_ that covers a different but very
similar problem.

Now, on to the problem of what a positive medical test means.  I'll use a
direct quote from `cancer test example 1`_::

    1% of women at age forty who participate in routine
    screening have breast cancer.  80% of women with
    breast cancer will get positive mammographies. 9.6%
    of women without breast cancer will also get positive
    mammographies. A woman in this age group had a positive
    mammography in a routine screening.  What is the
    probability that she actually has breast cancer?

Parsing the problem
-------------------

The first, and maybe most confusing, part of answering the above question is
parsing the provided information.  First, what is being asked? I would reword
the last sentence(s) and say::

    What is the probability that a woman (age 40) has breast
    cancer given that she had a postive mammogram?
    
Notice that I'm not adding any new information, just restating what is given
above.  Let's start by connecting the given information to mathematical
notation.  First, let's define the two items (variables) that we are
interested in:

* :math:`C` -- cancer: This variable represents the presence or absence of
  cancer and can be equal to *yes*: :math:`C=\textrm{yes}`, or *no*:
  :math:`C=\textrm{no}`

* :math:`M` -- mammogram: This variable represents the outcome of the mammogram
  and be *positive*: :math:`M=\textrm{pos}`, or *negative*:
  :math:`M=\textrm{neg}`

So, in mathematical notation, the problem is asking for us to calculate the
following *conditional probability*:

.. math::

    P(C=\textrm{yes} \vert M=\textrm{pos}) = \, ?

In English, this is the probability that *cancer is yes* given that a
*mammogram is pos (positive)*. Notice the phrase **given that**, this is a key
indicator that we are considering a conditional probability.

Givens in the problem statement
-------------------------------

* Prior probability of cancer

There is a lot of information in the problem statement, let's properly assign
probabilities to their given values.  First, we have the statement::

    1% of women at age forty who participate in routine
    screening have breast cancer.

Mathematically, this is giving us the value for the **prior probability** that
a woman (age 40) has breast cancer:

.. math::

    P(C=\textrm{yes}) = 0.01

Also note that the probability of no breast cancer in the same group of women
must be 99% because the sum of probabilities for all outcomes must be one:

.. math::

    \begin{array}{ll}
    P(C=\textrm{no}) & = & 1 - P(C=\textrm{yes}) \\
                     & = & 0.99
    \end{array}

This is our information about the probability of breast cancer (or no breast
cancer) *before the mammogram*.

* Effectiveness of tests

Our next information gives probabilities relevant to the accuracy of the
mammograms.  First, we have::

    80% of women with breast cancer will get positive
    mammographies.

Mathematically, this turns into:

.. math::

    P(M=\textrm{pos} \vert C=\textrm{yes}) = 0.80

Again, in simple English, this is the probability that a *mammogram is pos*
given that *cancer is yes*-- you should agree that this is the same as the
statement above.  We also get another probability for free:

.. math::

    P(M=\textrm{neg} \vert C=\textrm{yes}) = 0.20

This is because the probabilities of a mammogram being positive or negative
must sum to one, even with the conditioning on :math:`C=\textrm{yes}`:

.. math::

    P(M=\textrm{pos} \vert C=\textrm{yes}) + P(M=\textrm{neg} \vert C=\textrm{yes}) = 1

Finally (at least for the givens), we have the specificity of the test.  This
provides the probability of getting a positive mammogram even when there is
*no breast cancer*.  The relevant part of the problem is::

    9.6% of women without breast cancer will also get
    positive mammographies.

Mathematically, this translates to the following probability:

.. math::

    P(M=\textrm{pos} \vert C=\textrm{no}) = 0.096

Again, in simple English, this is the probability that a *mammogram is pos
(positive)* given that *cancer is no*.

Joint probabilities
-------------------

Before moving onto the final calculation, it is worth putting together the
joint probabilities for all possible outcomes.  We can do this using the
following relationships:

.. math::

    P(C=c, M=m) =  P(M=m \vert C=c) P(C=c)

where I use :math:`c` and :math:`m` to represent any valid values for the
presence of cancer and the mammogram result.  This allows us to substitute the
desired values for :math:`c` and :math:`m` and use the above equation over and
over again. For example, let's start with :math:`c=\textrm{yes}` and 
:math:`m=\textrm{pos}`:

.. math::

    \begin{array}{ll}
    P(C=\textrm{yes}, M=\textrm{pos}) & = & P(M=\textrm{pos} \vert C=\textrm{yes}) P(C=\textrm{yes}) \\
                                      & = & 0.80 \times 0.01 \\
                                      & = & 0.008
    \end{array}

This says the probability that *cancer is yes* **and** a *mammogram is pos* is
only 0.8% -- I'm sure that will surprise many people.  Why is it so small?
Well, this is driven by the fact that only 1% of women at this age have breast
cancer at all-- see the 0.01 in the calculation.  Only 80% of those women get a
positive mammogram, resulting in the very low 0.8%.

**Wait a second, isn't that the answer we want???** Actually, no.  We want to
know the probability *cancer is yes* **given that** a *mammagram is pos*, not
the probability *cancer is yes* **and** a *mammogram is pos*.  That is, we want
a probability conditioned on the fact that we know for certain that we have a
positive mammogram. We'll get to the answer in a bit.

Let's try another joint probability:

.. math::

    \begin{array}{ll}
    P(C=\textrm{no}, M=\textrm{pos})  & = & P(M=\textrm{pos} \vert C=\textrm{no}) P(C=\textrm{no}) \\
                                      & = & 0.096 \times 0.99 \\
                                      & = & 0.09504 
    \end{array}

This says the probability that *cancer is no* **and** a *mammogram is pos* is 9.5%,
fairly high.  Again, this is driven by the fact that most women at this age do
not have breast cancer-- the 0.99 in the calculation-- and the probability of
false positives is fairly high at 9.6%.

Let's calculate the probability of the other two joint outcomes:

.. math::

    \begin{array}{ll}
    P(C=\textrm{no}, M=\textrm{neg})  & = & P(M=\textrm{neg} \vert C=\textrm{no}) P(C=\textrm{no}) \\
                                      & = & 0.904 \times 0.99 \\
                                      & = & 0.89496
    \end{array}

and

.. math::

    \begin{array}{ll}
    P(C=\textrm{yes}, M=\textrm{neg}) & = & P(M=\textrm{neg} \vert C=\textrm{yes}) P(C=\textrm{yes}) \\
                                      & = & 0.20 \times 0.01 \\
                                      & = & 0.002
    \end{array}

From the above, we can see that it is most common to have no cancer and a
negative mammogram, at 89.5%.

Joint probability table
-----------------------

Let's put together a joint probability table to see everything at
once:

.. math::
    
    \newcommand\T{\Rule{0pt}{1em}{.3em}}
    \begin{array}{c|c|c|c}
                     \T & C=\textrm{yes}    & C=\textrm{no}       &     \\ \hline
      M=\textrm{pos} \T & \color{blue}{0.008} & \color{blue}{0.09504} & 0.10304 \\
      M=\textrm{neg} \T & \color{blue}{0.002} & \color{blue}{0.89496} & 0.89696 \\ \hline      
                     \T & 0.01              & 0.99                & 1
    \end{array}

The central part of the table (blue values) provides the joint
probabilities calculated above. Notice that the sum of these values is equal to
one because they cover all possible combinations of :math:`C` and :math:`M`.
The bottom row provides the sum of probabilities in the column-- these sums are
also known as marginal probabilities. For example, we have

.. math::

    \begin{array}{ll}
    P(C=\textrm{yes}) & = & P(M=\textrm{neg}, C=\textrm{yes})  \\
                      & + & P(M=\textrm{pos}, C=\textrm{yes}) \\
                      & = & 0.008 + 0.0002 \\
                      & = & 0.01
    \end{array}

This result just reconstructs a probability that we already knew and were
given in the problem statement.

Also note that the last column provides the sum of the probabilities in each
row. Here, we can find something new:

.. math::

    \begin{array}{ll}
    P(M=\textrm{pos}) & = & P(M=\textrm{pos}, C=\textrm{yes})  \\
                      & + & P(M=\textrm{pos}, C=\textrm{no}) \\
                      & = & 0.008 + 0.09504  \\
                      & = & 0.10304
    \end{array}

This says :math:`P(M=\textrm{pos})` is 10.3% and gives the probability of a
positive mammogram in all testing, including women that both have, and do not
have, breast cancer.

Prior to posterior
------------------

Finally, let's calculate the posterior to get the desired quantity.  Again, the
idea is that we are updating the prior to the posterior:

* **prior**: :math:`P(C=\textrm{yes}) = 0.01` -- information before mammogram

to

* **posterior**: :math:`P(C=\textrm{yes} \vert M=\textrm{pos})` -- information
  after the mammogram (conditioned on a positive result)

We've already calculated every relevant probability, so let's construct Bayes'
rule for this problem.  We can relate the joint, conditional and marginal
probabilities of interest in two ways (both correct):

.. math::

    P(C=\textrm{yes}, M=\textrm{pos}) = P(M=\textrm{pos} \vert C=\textrm{yes})
    P(C=\textrm{yes})

*and*

.. math::

    P(C=\textrm{yes}, M=\textrm{pos}) = P(C=\textrm{yes} \vert M=\textrm{pos})
    P(M=\textrm{pos})

Note that :math:`P(C=\textrm{yes}, M=\textrm{pos})` is on the left side of both
equations. So, we can set the right side of each equation equal and re-arrange
to get:

.. math::

    P(C=\textrm{yes} \vert M=\textrm{pos}) =
    \frac{P(M=\textrm{pos} \vert C=\textrm{yes})P(C=\textrm{yes})}{P(M=\textrm{pos})}

Notice that the left side of the equation has the (unknown) quantity that we
want and the right side of the equation has only known quantities that we were
given or calculated above.  So, we can find our answer:

.. math::

    P(C=\textrm{yes} \vert M=\textrm{pos}) =
    \frac{0.8 \times 0.01}{0.01034} = 0.077

So, the probability of breast cancer given a positive mammogram is just 7.7%.
Most people are shocked at how low this value is.  However, remember that
before the mammogram the probability of cancer was just 1%.  The positive test
increased the probability of cancer by a factor of roughly *eight times*:
:math:`0.01 \rightarrow 0.077`.

* **Why isn't it 100%, or at least really high probability?**

Well, the mammogram is not perfect (no medical test is)-- it will be negative
20% of the time when a woman *does have* breast cancer and it will also be
positive 9.6% of the time when the woman *does not have* breast cancer. Another
factor is that only 1% of women in this age group actually have breast cancer
at all.  These factor combine to result in a fairly low value of 7.7%.

Many people find it helpful to think of this problem using 1,000 imaginary
women and think in terms of number of people instead of probabilities.  We can
do that by multiplying all of the probabilities in our joint probability table
by 1000 to get the number of women in each status:

.. math::
    
    \newcommand\T{\Rule{0pt}{1em}{.3em}}
    \begin{array}{c|c|c|c}
                     \T & C=\textrm{yes}  & C=\textrm{no}     &     \\ \hline
      M=\textrm{pos} \T & \color{blue}{8} & \color{blue}{95}  & 103 \\
      M=\textrm{neg} \T & \color{blue}{2} & \color{blue}{895} & 897 \\ \hline      
                     \T & 10              & 990               & 1,000
    \end{array}

Looking at this table, the problem should be very apparent: of 103 positive
mammograms, only 8 really have breast cancer.  The other 95 women have *false
positives*.  Also, 2 women with breast cancer get negative mammograms.  As a
result, a positive mammogram increases the probability of cancer, from 1% to
7.7%, but does not make it certain.

Bayes' theorem
--------------

While digging into the details of the above calculations it would be easy to
loose site of where Bayes' theorem appeared and what it looks like.  A more
typical presentation would look something like:

.. math::

    \color{blue}{P(C=c \vert M=m)} = \frac{P(M=m \vert C=c) \color{red}{P(C=c)}
    }{
    P(M=m)}

In the above we colored the **posterior blue** and the **prior red**.  As
always, we think of updating a prior to a posterior given some
information or data. Another form of Bayes' theorem that is often used, if
the term in the denominator is expanded, is:

.. math::

    P(C=c \vert M=m) = \frac{P(M=m \vert C=c)P(C=c)
    }{
    \sum_{\hat{c}=\textrm{yes},\textrm{no}} P(M=m \vert C=\hat{c})P(C=\hat{c})
    }

where we use the relation between joint and marginal probabilities (see my post
on :ref:`joint, conditional and marginal probabilities` if this doesn't make 
sense to you):

.. math::

    \begin{array}{ll}
    P(M=m) & = & \sum_{\hat{c}=\textrm{yes},\textrm{no}} P(M=m \vert C=\hat{c})P(C=\hat{c}) \\
           & = & P(M=m \vert C=\textrm{yes})P(C=\textrm{yes}) \\
           & + & P(M=m \vert C=\textrm{no})P(C=\textrm{no})
    \end{array}

Let's apply this last form of Bayes' theorem to do the calculation (again) for
:math:`c=\textrm{yes}` and :math:`m=\textrm{pos}`:

.. math::

    \begin{array}{ll}
    P(C=\textrm{yes} \vert M=\textrm{pos}) & = & \frac{
    P(M=\textrm{pos} \vert C=\textrm{yes})P(C=\textrm{yes})
    }{
    \sum_{\hat{c}=\textrm{yes},\textrm{no}} P(M=\textrm{pos} \vert C=\hat{c})P(C=\hat{c})
    } \\
    & = & \frac{ 0.80 \times 0.01}{0.80 \times 0.01 + 0.096 \times 0.99} \\
    & = & 0.077
    \end{array}

The same answer, whew! Seriously, make sure that all of the substitutions make
sense and that you can relate this calculation back to the more incremental
calculation done above.

Summing up
----------

So, that's it, a first example of a Bayesian calculation done a couple of ways.
I hope the level of detail will encourage you replicate the calculations and
understand how all of the probabilities are related.  As always leave
comments, questions, and corrections below.

.. _cancer test example 1: http://www.yudkowsky.net/rational/bayes
.. _cancer test example 2: http://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/
.. _wikipedia drug test example: http://en.wikipedia.org/wiki/Bayes%27_theorem#Drug_testing

.. author:: default
.. categories:: none
.. tags:: joint probability, conditional probability, marginal probability, Bayesian
.. comments::
