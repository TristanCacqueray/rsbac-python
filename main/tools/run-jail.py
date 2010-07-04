#!/usr/bin/python -OO
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
"""
	Filename:	run-jail.py
	Last update:	04/06/2010
	Purpose:	replace rsbac_jail legacy tool

It feature: jail configuration files and auto-jailling with symlinks
"""

import rsbac.tools
from rsbac.types.jail import *

print dir(rsbac.types.jail)
print rsbac.tools.hello()
