#!/usr/bin/python -OO
# -*- coding: utf8 -*-
############################################################################
# (c) 2005-2010 freenode#rsbac
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
############################################################################
"""	Filename:	main/tools/attr_get.py
	Project:	rsbac-python
	Last update:	2010/07/24
	Purpose:	Rsbac attribute get wrapper

This tool mostly illustrate how to use rsbac-python.
It's recommended to only use load_policy or rsbac_menu
"""

import os
import pprint

from rsbac.types import *
import rsbac.helpers.attrs

from rsbac.helpers.lib import get_attr_value_name

def main(argv):
	for path in argv[1:]:
		if not os.path.exists(path):
			raise RuntimeError("usage: %s object_path ..." % argv[0])
		print "=== %s's attributes ===" % path
		path_attrs = rsbac.helpers.attrs.get(path)
		for module,attrs in path_attrs.items():
			for attr,value in attrs.items():
				print "%s.%s = %s (%s)" % (
					module,
					attr,
					repr(value),
					get_attr_value_name(attr, value),
				)
#		pprint.pprint(attrs, width=20)

if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv))
