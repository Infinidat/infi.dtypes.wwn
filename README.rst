Overview
========
*infi.dtypes.wwn* provides a datatype for representing WWNs from strings in
various formats.

Usage
=====
``WWN`` accepts an optional ``0x`` prefix and either ``:`` or ``-`` as the group
separator. Whatever the input form, the address is normalized to sixteen
lowercase hex digits, so values parsed from different formats compare equal:

::

  >>> from infi.dtypes.wwn import WWN
  >>> wwn = WWN("01:02:03:04:ab:cd:ef:08")
  >>> wwn
  01020304abcdef08
  >>> wwn == "01-02-03-04-AB-CD-EF-08"
  True
  >>> wwn == "0x01020304abcdef08"
  True

Short addresses are left-padded to the full width:

::

  >>> WWN("1")
  0000000000000001

Instances are hashable and orderable, so they can be used as dictionary keys
and sorted. Comparing against a string that cannot be parsed yields ``False``
rather than raising:

::

  >>> wwn == "not-a-wwn"
  False

Equality is supported against strings and other ``WWN`` instances only.
Comparing a ``WWN`` against an integer returns ``False``.

Installing
==========

::

  pip install infi.dtypes.wwn

Requires Python 3.3 or later. ``infi`` and ``infi.dtypes`` are PEP 420 implicit
namespace packages, so they contain no ``__init__.py``.

Checking out the code
=====================

::

  git clone https://github.com/Infinidat/infi.dtypes.wwn.git
  cd infi.dtypes.wwn
  pip install --editable .

Running the tests
=================

::

  python -m unittest discover -s tests -v
