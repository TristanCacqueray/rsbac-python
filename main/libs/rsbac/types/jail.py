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
"""	Filename:	main/libs/rsbac/types/jail.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	rsbac types

This file have been generated with _gen_types.py. DO NOT EDIT
"""

jail_flags = {
	'allow_external_ipc':	1,
	'allow_all_net_family':	2,
	'allow_inet_raw':	8,
	'auto_adjust_inet_any':	16,
	'allow_inet_localhost':	32,
	'allow_dev_get_status':	128,
	'allow_dev_mod_system':	256,
	'allow_dev_read':	512,
	'allow_dev_write':	1024,
	'allow_tty_open':	2048,
	'allow_parent_ipc':	4096,
	'allow_suid_files':	8192,
	'allow_mount':	16384,
	'this_is_syslog':	32768,
	'allow_ipc_to_syslog':	65536,
	'allow_netlink':	131072,
}
jail_flags_names = dict((v,k) for k, v in jail_flags.iteritems())


# jail.py EOF
