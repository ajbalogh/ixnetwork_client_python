https://travis-ci.org/ajbalogh/ixnetwork_client_python.svg?branch=master

IxNetwork REST API python client
================================
A python client that interacts with an Ixia Solutions Group IxNetwork test tool.
In order to use the REST feature the IxNetwork test tool must be version 8.x or higher.

BREAKING CHANGES
--------
As of version 0.55a32 IxnObject auto generated .create_<child_name> methods are no longer supported.
Existing code that uses those methods will need to be refactored to IxnObject.create_child(<child_name>).
As a result a significant increase in performance will be realized.

Features
--------
* JSON import/export/configure
* Low level access to entire ixNet hierarchy
* Query ixNet hierarchy
* High level management classes
+ Session Management
+ File Management
+ Configuration Management
+ Port Management
+ Statistics Management
+ NGPF Emulation Host wrapper classes
* sample code






