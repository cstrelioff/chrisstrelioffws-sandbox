Install oauth2 Python package on Ubuntu 14.04
================================================

The first assignment for `Coursera's Introduction to Data Science`_ focuses on
sentiment analysis of twitter data.  To do this the oauth2_ package needs to be
installed. Following the style outlined in my :ref:`initial python setup` post,
I will use pip to install the package as a user:

.. code-block:: bash

    $ pip install --user oauth2

.. more::

If we use ``pip show``, we can set that the package is installed locally:

.. code-block:: bash

    $ pip show oauth2
    ---
    Name: oauth2
    Version: 1.5.211
    Location: /home/cstrelioff/.local/lib/python2.7/site-packages
    Requires: httplib2

The required ``httplib2`` package is not installed because this is already
present in the default Python setup for Ubuntu 14.04:

.. code-block:: bash

    $ pip show httplib2
    ---
    Name: httplib2
    Version: 0.8
    Location: /usr/lib/python2.7/dist-packages
    Requires: 

Note the install location at **/usr/lib/python2.7/dist-packages** instead of
**/home/cstrelioff/.local/lib/python2.7/site-packages**.

.. _Coursera's Introduction to Data Science: https://www.coursera.org/course/datasci
.. _oauth2: https://pypi.python.org/pypi/oauth2/1.5.211


.. author:: default
.. categories:: none
.. tags:: my ubuntu setup, my python setup, python 2.7, coursera intro to data science
.. comments::
