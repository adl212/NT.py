.. NT.py documentation master file, created by
   sphinx-quickstart on Sun Dec 20 16:59:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NT.py's documentation!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

NT.py is a package to help you get stats and access the nitrotype api

**Features:**
=====
- Has a ``Racer`` class to help you get racer stats
- Has a ``Team`` class to help you get racer stats
- Can use the whole nitrotype api!

.. code-block::
    :linenos:
    import nitrotype
    racer = Racer('adl212')
    print(racer.username)