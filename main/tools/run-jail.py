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
"""	Filename:	main/tools/run-jail.py
	Project:	rsbac-python
	Last update:	04/06/2010
	Purpose:	replace rsbac_jail legacy tool

It feature: jail configuration files and auto-jailling with symlinks
"""

import os

from rsbac.types import *

## Possible import technique
#from rsbac.helpers import *
#try:
#	rsbac_jail("import test 1")
#except RuntimeError:
#	pass


## Recommenced import
import rsbac.helpers.jail


def main(argv):
	try:
		if len(argv[1:]) == 0:
			print "usage: %s prog args"
			return
		rsbac.helpers.jail.rsbac_jail()
		os.execvp(argv[1], argv[1:])
	except RuntimeError:
		pass

if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv))
