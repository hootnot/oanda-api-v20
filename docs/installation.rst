Introduction
============

The `oandapyV20` package offers an API to the OANDA V20 REST service.
To use the REST-API-service you will need a *token* and an *account*. This
applies for both *live*  and *practice* accounts. For details check oanda.com_.

.. _oanda.com: https://oanda.com


Install
-------

Install the pypi package with pip::

    $ pip install oandapyV20

Or alternatively install the latest development version from github::

    $ pip install git+https://github.com/hootnot/oanda-api-v20.git


You may consider using *virtualenv* to create isolated Python environments. Python 3.4 has *pyvenv* providing
the same kind of functionality.


Download from Github
--------------------

If you want to run the tests, download the source from github::


    $ git clone https://github.com/hootnot/oanda-api-v20.git
    $ cd oanda-api-v20
    $ python setup.py test
    $ python setup.py install
