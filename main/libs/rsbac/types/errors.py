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
"""	Filename:	main/libs/rsbac/types/errors.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	rsbac types

This file have been generated with _gen_types.py. DO NOT EDIT
"""

errors = {
	'EPERM':	1001,
	'EACCESS':	1002,
	'EREADFAILED':	1003,
	'EWRITEFAILED':	1004,
	'EINVALIDPOINTER':	1005,
	'ENOROOTDIR':	1006,
	'EPATHTOOLONG':	1007,
	'ENOROOTDEV':	1008,
	'ENOTFOUND':	1009,
	'ENOTINITIALIZED':	1010,
	'EREINIT':	1011,
	'ECOULDNOTADDDEVICE':	1012,
	'ECOULDNOTADDITEM':	1013,
	'ECOULDNOTCREATEPATH':	1014,
	'EINVALIDATTR':	1015,
	'EINVALIDDEV':	1016,
	'EINVALIDTARGET':	1017,
	'EINVALIDVALUE':	1018,
	'EEXISTS':	1019,
	'EINTERNONLY':	1020,
	'EINVALIDREQUEST':	1021,
	'ENOTWRITABLE':	1022,
	'EMALWAREDETECTED':	1023,
	'ENOMEM':	1024,
	'EDECISIONMISMATCH':	1025,
	'EINVALIDVERSION':	1026,
	'EINVALIDMODULE':	1027,
	'EEXPIRED':	1028,
	'EMUSTCHANGE':	1029,
	'EBUSY':	1030,
	'EINVALIDTRANSACTION':	1031,
	'EWEAKPASSWORD':	1032,
	'EINVALIDLIST':	1033,
	'EMAX':	1033,
}
errors_names = dict((v,k) for k, v in errors.iteritems())


# errors.py EOF
