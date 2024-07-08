.. _installation:

============
Installation
============

Before Installation
===================

.. WARNING::
  **geodefi** Python SDK (as of v2.0.0) only supports the Python versions from ``3.8`` to ``3.12``.  

.. NOTE::
  We recommend that you read protocol's `documentation <https://docs.geode.fi>`_ to become familiar with the terms.

.. NOTE:: 
  Following examples that start with a ``$`` is meant to run on your terminal.

----

1. Check your python version
=============================
.. code-block:: shell
   
  $ python3 --version 
  # Python 3.7.0 <> 3.10.13

2. Create a virtual environment
=========================================

Using a virtual environment is advised

On Linux and MacOS:

.. code-block:: shell
   
  $ python3 -m venv {environment_name} # creates virtual environment
  $ source {environment_name}/bin/activate # activates the virtual environment

On Windows:

.. code-block:: shell
   
  $ python3 -m venv {environment_name} # creates virtual environment
  $ {environment_name}\Scripts\activate # activates the virtual environment

3. Install the package
================================
  
.. code-block:: shell

  $ python3 -m pip install geodefi 

| Successfully installed.
| **Next step: configuration of the enviroment variables.**