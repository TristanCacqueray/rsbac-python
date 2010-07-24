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
"""	Filename:	main/libs/rsbac/helpers/lib.py
	Project:	rsbac-python
	Last update:	2010/07/05
	Purpose:	librsbac.so ctype loader

Documentation
"""
from ctypes import *

try:
	librsbac = cdll.LoadLibrary("librsbac.so.1")
except OSError:
	import sys
	print >>sys.stderr, "Could not find librsbac.so.1"
