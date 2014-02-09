import inspect
import sys
if sys.version_info[0] == 2:
    from .python2 import httplib2
else:
    from .python3 import httplib2
globals().update(inspect.getmembers(httplib2))
