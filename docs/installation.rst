Installation
============

Introduction
------------

The OANDA REST-V20 package offers an API to the OANDA V20 REST service.
To use the API-service you will need a *token* and an *account*. This
applies for both *live*  and *practice* accounts. For details check oanda.com_.

.. _oanda.com: https://oanda.com


Download & Install
------------------


Install the package with pip::

    $ pip install git+https://github.com/hootnot/oanda-api-v20.git


You may consider using *virtualenv* to create isolated Python environments. Python 3.4 has *pyvenv* providing
the same kind of functionality.


From Github
```````````

.. code-block:: shell

    $ git clone https://github.com/hootnot/oanda-api-v20.git
    $ cd oanda-api-v20

    Run the tests:
    $ python setup.py test
    $ python setup.py install

