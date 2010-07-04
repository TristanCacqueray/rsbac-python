from release import Release

__author__ = "\n".join([ "%s <%s>" % x for x in Release.authors.values()])
__version_info__ = Release.version_info
__version__ = Release.version
__version_number__ = Release.version_number
__version_description__  = Release.version_description
__doc__ = Release.long_description
