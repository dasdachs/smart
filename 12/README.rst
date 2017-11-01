###################################################
Scraping Datai, SmartNinja Coding School Exercise 1
###################################################

:author: Jani Šumak
:date: 2017-11-1

Both scripts are console apps. Please consult the `help` flag for further instructions, e.g. `python got.py --help`.

Installing dependencies
=======================

Both apps use well supported 3rd party libraries:

* `Requests <http://docs.python-requests.org/en/master/>`_ 
  Requests is the **de facto** standard library for http requests. It is well maintained, stable and probably the most popular package on `PyPi <https://pypi.python.org/pypi>`_.

* `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ 
  BeautifulSoup is a ``library for pulling data out of HTML and XML``. It is a powerful library for traversing the HTML and XML documents, manipulating data and extracting text and attributes.

* `html5lib <https://github.com/html5lib/html5lib-python>`_
  BeautifulSoup uses on of three parsers: the standard parser, `html.parser <https://docs.python.org/2/library/htmlparser.html>`_, html5lib or `lxml <http://lxml.de/>`_. While the later is considered the best, it is not well supported for Windows, so we use `html5lib`. The parser from the standard library is a good parser, but the authors of BeautifulSoup recommend that we use `lxml or html5lib`_.

If you are using Windows OS chances are you do not have the requirements to run either script. Normally I would recommend using a virtual environment, but since these dependencies should not cause any problems, install them via `pip`:

Global install
--------------

From your console type:

::
  pip install -r requirements.txt

Note: you can the dependencies from Pycharm.  

Virtual environment
-------------------

From you terminal run:

#. Globally install `virtualenv`
::
    pip install virtualenv
    
#. Create a virtual environment `virtualenv venv`

#. Activate the virtual environment

   *Windows*
   `venv\scripts\activate`
   
   *POSIX*
   `source venv/bin/activate

   The name of your virtual environment should appear in the terminal: `(venv)`.

#. Install the dependencies within the virtual environment `pip install -r requirements.txt`.

Run the apps
============

Run the apps with python

::
        python got.py

After you finish, deactivate you virtual environment `deactivate`.

.. _lxml or html5lib:  https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
