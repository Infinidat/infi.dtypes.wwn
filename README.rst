Overview
========
*infi.dtypes.wwn* provides a datatype for representing WWNs from strings in various formats.

Usage
=====
WWN:
::
  >>> from infi.dtypes.wwn import WWN
  >>> wwn = WWN("01:02:03:04:ab:cd:ef:08)
  >>> wwn == 0x01020304ABCDEF08
  True

Checking out the code
=====================

This project uses buildout and infi-projector, and git to generate setup.py and __version__.py.
In order to generate these, first get infi-projector:

    easy_install infi.projector

and then run in the project directory:

    projector devenv build

