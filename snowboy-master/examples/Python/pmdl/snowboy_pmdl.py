import os
import sys
import platform
import distro  # Import distro to replace platform.linux_distribution()

if platform.system() == "Darwin":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib/osx/pmdl"))
    from snowboy import *
elif distro.id() == "ubuntu" and distro.version() == "16.04":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib/ubuntu64/pmdl"))
    from snowboy import *
else:
    raise ImportError("pmdl generator only runs on OSX or Ubuntu 16.04.")
