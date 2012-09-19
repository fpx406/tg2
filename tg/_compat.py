import platform, sys

if platform.system() == 'Windows': # pragma: no cover
    WIN = True
else: # pragma: no cover
    WIN = False

# True if we are running on Python 3.
PY3 = sys.version_info[0] == 3

if PY3:
    string_type = str
    unicode_text = str
else:
    string_type = basestring
    unicode_text = unicode
