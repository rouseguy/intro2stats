"""
    This script will check if the environment setup is correct for the workshop.

    To run, please execute the following command from the command prompt
               >>> python check_env.py
    
    The output will indicate if any of the libraries are missing or need to be updated. 

    This script is inspired from https://github.com/fonnesbeck/scipy2015_tutorial/blob/master/check_env.py
"""

from __future__ import print_function

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

import sys
try:
    import importlib
except ImportError:
    print(FAIL, "Python version 2.7 is required, but %s is installed." % sys.version)
from distutils.version import LooseVersion as Version

def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        # workaround for Image not having __version__
        version = getattr(mod, "__version__", 0) or getattr(mod, "VERSION", 0)
        if Version(version) < min_ver:
            print(FAIL, "%s version %s or higher required, but %s installed."
                  % (lib, min_ver, version))
        else:
            print(OK, '%s version %s' % (pkg, version))
    except ImportError:
        print(FAIL, '%s not installed. %s' % (pkg, fail_msg))
    return mod


# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = Version(sys.version)
if pyversion >= "3":
    print(FAIL, "Python version 2.7 is required, but %s is installed." % sys.version)
elif pyversion >= "2":
    if pyversion < "2.7":
        print(FAIL, "Python version 2.7 is required, but %s is installed." % sys.version)
else:
    print(FAIL, "Unknown Python version: %s" % sys.version)

print()
requirements = {'numpy': "1.9.2", 'pandas': "0.16.2", 'scipy': "0.9", 'matplotlib': "1.4.3",
        'IPython': "4.0", 'sklearn': "0.16.1", 'seaborn': "0.6.0", 'statsmodels': "0.6.1"}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)
