#!/usr/bin/python -OO
# -*- coding = utf8 -*-
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
"""	Filename:	main/libs/rsbac/types/daz.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	rsbac types

This file have been generated with _gen_types.py. DO NOT EDIT
"""

daz_scanned_values = {
	'unscanned':	0,
	'infected':	1,
	'clean':	2,
	'max':	2,
}
daz_scanned_values_names = dict((v,k) for k, v in daz_scanned_values.iteritems())

daz_do_scan_values = {
	'never':	0,
	'registered':	1,
	'always':	2,
	'inherit':	3,
	'max_do_scan':	3,
}
daz_do_scan_values_names = dict((v,k) for k, v in daz_do_scan_values.iteritems())


# daz.py EOF
