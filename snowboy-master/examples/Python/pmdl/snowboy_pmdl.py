import os
import sys
import platform
import distro  # Use distro for Linux distribution checking

# Determine if the system is macOS (Darwin)
if platform.system() == "Darwin":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib/osx/pmdl"))
    from snowboy import *

# Check for Ubuntu Linux (or other versions of Ubuntu)
elif distro.id() == "ubuntu":
    # Adjust this to match any version of Ubuntu, not just 16.04
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib/ubuntu64/pmdl"))
    from snowboy import *

# Check for Windows platform
elif platform.system() == "Windows":
    # Add the necessary path or logic for Windows (if the support exists)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib/windows/pmdl"))
    from snowboy import *

# If none of the conditions are met, raise an error
else:
    raise ImportError("pmdl generator only runs on OSX, Ubuntu, or Windows.")
