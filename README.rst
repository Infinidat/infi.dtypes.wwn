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

This project uses buildout, and git to generate setup.py and __version__.py.
In order to generate these, run:
::
  python -S bootstrap.py -d -t
  bin/buildout -c buildout-version.cfg

If you don't have nose in your environment, you can have an isolated environment in this project by executing:
::
  bin/buildout install scripts
