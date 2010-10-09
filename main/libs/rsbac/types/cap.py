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
"""	Filename:	main/libs/rsbac/types/cap.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	rsbac types

This file have been generated with _gen_types.py. DO NOT EDIT
"""

caps = {
	'CHOWN':	0,
	'DAC_OVERRIDE':	1,
	'DAC_READ_SEARCH':	2,
	'FOWNER':	3,
	'FSETID':	4,
	'KILL':	5,
	'SETGID':	6,
	'SETUID':	7,
	'SETPCAP':	8,
	'LINUX_IMMUTABLE':	9,
	'NET_BIND_SERVICE':	10,
	'NET_BROADCAST':	11,
	'NET_ADMIN':	12,
	'NET_RAW':	13,
	'IPC_LOCK':	14,
	'IPC_OWNER':	15,
	'SYS_MODULE':	16,
	'SYS_RAWIO':	17,
	'SYS_CHROOT':	18,
	'SYS_PTRACE':	19,
	'SYS_PACCT':	20,
	'SYS_ADMIN':	21,
	'SYS_BOOT':	22,
	'SYS_NICE':	23,
	'SYS_RESOURCE':	24,
	'SYS_TIME':	25,
	'SYS_TTY_CONFIG':	26,
	'MKNOD':	27,
	'LEASE':	28,
	'AUDIT_WRITE':	29,
	'AUDIT_CONTROL':	30,
	'SETFCAP':	31,
	'MAC_OVERRIDE':	32,
	'MAC_ADMIN':	33,
}
caps_names = dict((v,k) for k, v in caps.iteritems())


# cap.py EOF
