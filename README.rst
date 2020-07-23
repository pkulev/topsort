|PyPI| |Build Status| |codecov.io|

=======
topsort
=======

Python implementation of topological sort.

Requirements
============

This package has no dependencies.

Installation
============

Unsurprisingly, name **topsort** have been in use on PyPI for ages.

.. code-block:: console

	$ pip install pytopsort


Examples
========

.. code-block:: python

    from pytopsort import topsort

    # This simple recipe is a complete mess, until we apply topological sort to it!
    recipe = [{
        # This action depends on another
        "action": "spread peanut butter on bread",
        "after": ["slice bread"],
    }, {
        # This action has no dependencies
        "action": "slice bread",
        "after": [],
    }, {
        "action": "eat the delicious breakfast!",
        "after": ["spread jam on top", "make a cup of coffee"],
    }, {
        "action": "make a cup of coffee",
        "after": [],
    }, {
        "action": "spread jam on top",
        "after": ["spread peanut butter on bread"],
    }]

    recipe = topsort(
        recipe,
        deptest=lambda self, other: self["action"] in other["after"],
    )

    # If we then print list(recipe), it will be like:
    [{
        'action': 'make a cup of coffee',
        'after': []
    }, {
        'action': 'slice bread',
        'after': []
    }, {
        'action': 'spread peanut butter on bread',
        'after': ['slice bread']
    }, {
        'action': 'spread jam on top',
        'after': ['spread peanut butter on bread']
    }, {
        'action': 'eat the delicious breakfast!',
        'after': ['spread jam on top', 'make a cup of coffee']
    }]


Now we can put this recipe into the breakfast machine!


Development
===========

Installation
------------

.. code-block:: console

   $ poetry install

Testing
-------

.. code-block:: console

   $ poetry run pytest -s -v tests/  # run all tests
   $ poetry run pytest --cov=pytopsort -s -v tests/  # run all tests with coverage
   $ poetry run black pytopsort/ tests/  # autoformat code
   $ # run type checking
   $ poetry run pytest --mypy --mypy-ignore-missing-imports -s -v pytopsort/ tests/
   $ # run code linting
   $ poetry run pylint pytopsort/

Documentation
-------------

* **To be added**

.. |PyPI| image:: https://badge.fury.io/py/pytopsort.svg
   :target: https://badge.fury.io/py/pytopsort
.. |Build Status| image:: https://github.com/pkulev/topsort/workflows/CI/badge.svg
.. |codecov.io| image:: http://codecov.io/github/pkulev/topsort/coverage.svg?branch=master
   :target: http://codecov.io/github/pkulev/topsort?branch=master
