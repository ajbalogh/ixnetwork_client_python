.. image:: https://travis-ci.org/ajbalogh/ixnetwork_client_python.svg?branch=master
    :target: https://travis-ci.org/ajbalogh/ixnetwork_client_python

.. image:: https://img.shields.io/pypi/v/ixnetwork-rest.svg
    :target: https://pypi.org/project/ixnetwork-rest
 
.. image:: https://img.shields.io/pypi/pyversions/ixnetwork-rest.svg
    :target: https://pypi.org/project/ixnetwork-rest

.. image:: https://img.shields.io/badge/license-MIT-green.svg
    :target: https://en.wikipedia.org/wiki/MIT_License

IxNetwork REST API python client
================================
A python client that interacts with an Ixia Solutions Group IxNetwork test tool.
In order to use the REST feature the IxNetwork test tool must be version 8.x or higher.

BREAKING CHANGES!!!
-------------------
+ New Package Name on PyPi

  + pip install ixnetwork-rest

+ As of version 0.55a32 IxnObject auto generated .create_<child_name> methods are no longer supported.

  + Existing code that uses those methods will need to be refactored to IxnObject.create_child(<child_name>).
  + As a result a significant increase in performance will be realized.

Features
--------
+ JSON import/export/configure
+ Low level access to the entire IxNetwork hierarchy
+ Query the ixnetwork hierarchy
+ Sample Code
+ High level management classes

  + Session Management
  + File Management
  + Configuration Management
  + Port Management
  + Statistics Management

In Development
--------------
+ Protocol emulation management class
  
  + Find protocol emulation instances and sessions
  + Execute operations on those specific sessions
