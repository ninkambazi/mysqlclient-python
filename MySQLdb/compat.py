import sys

if sys.version_info[0] == 2:
    PY2 = True
    unicode = unicode
    unichr = unichr
    long = long
else:
    PY2 = False
    unicode = str
    unichr = chr
    long = int
