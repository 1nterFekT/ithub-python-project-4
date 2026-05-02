"""
For the full list of core and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from split_settings.tools import include

include("common.py")
include("auth.py")
include("files.py")
include("database.py")
include("security.py")
