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
"""	Filename:	main/libs/rsbac/types/targets.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	rsbac types

This file have been generated with _gen_types.py. DO NOT EDIT
"""

targets = {
	'FILE':	0,
	'DIR':	1,
	'FIFO':	2,
	'SYMLINK':	3,
	'DEV':	4,
	'IPC':	5,
	'SCD':	6,
	'USER':	7,
	'PROCESS':	8,
	'NETDEV':	9,
	'NETTEMP':	10,
	'NETOBJ':	11,
	'NETTEMP_NT':	12,
	'GROUP':	13,
	'FD':	14,
	'UNIXSOCK':	15,
	'NONE':	16,
}
targets_names = dict((v,k) for k, v in targets.iteritems())


# targets.py EOF
