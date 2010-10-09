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
"""	Filename:	main/libs/rsbac/types/ff.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	rsbac types

This file have been generated with _gen_types.py. DO NOT EDIT
"""

ff_flags_values = {
	'read_only':	1,
	'execute_only':	2,
	'search_only':	4,
	'write_only':	8,
	'secure_delete':	16,
	'no_execute':	32,
	'no_delete_or_rename':	64,
	'append_only':	256,
	'no_mount':	512,
	'no_search':	1024,
	'add_inherited':	128,
}
ff_flags_values_names = dict((v,k) for k, v in ff_flags_values.iteritems())


# ff.py EOF
