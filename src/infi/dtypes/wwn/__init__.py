__import__("pkg_resources").declare_namespace(__name__)

import sys
import string

PY2 = sys.version_info[0] == 2
string_type = basestring if PY2 else str

class InvalidWWN(ValueError):
    def __init__(self, value):
        super(InvalidWWN, self).__init__("Invalid FC address form: {0!r}".format(value))

class WWN(object):
    def __init__(self, address):
        super(WWN, self).__init__()
        if isinstance(address, WWN):
            self._address = address._address
        else:
            self._address = self._normalize(address)
    @classmethod
    def _normalize(cls, address):
        if address.startswith("0x"):
            address = address[2:]
        sep = '-' if '-' in address else ':'
        components = address.split(sep)
        if not all(components):
            raise InvalidWWN(address)
        address = "".join(components)
        address = address.rjust(16, '0')
        if not set(address).issubset(set(string.hexdigits)) or len(address) != 16:
            raise InvalidWWN(address)
        return address.lower()
    def __eq__(self, other):
        if isinstance(other, string_type):
            try:
                other = WWN(other)
            except InvalidWWN:
                return False
        elif not isinstance(other, WWN):
            return False
        return self._address == other._address
    def __ne__(self, other):
        return not (self == other)
    def __repr__(self):
        return self._address
    def __hash__(self):
        return hash(self._address)
    def __lt__(self, other):
        if isinstance(other, string_type):
            other = WWN(other)
        if not isinstance(other, WWN):
            raise TypeError("Comparing WWN object to {0!r}".format(other))
        return self._address < other._address
    def __gt__(self, other):
        return not self <= other
    def __le__(self, other):
        return self < other or self == other
    def __ge__(self, other):
        return not self < other
