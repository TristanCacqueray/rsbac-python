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
"""	Filename:	jail.py
	Last update:	2010/07/05
	Purpose:	rsbac_jail helpers


"""
from rsbac.helpers.lib import *
from rsbac.types import *

RSBAC_JAIL_VERSION = 1

def rsbac_jail(rootdir = None,	# char *
	ip = "0.0.0.0",		# __u32
	jail_flags = 0,		# __u32
	max_caps = [0, 0],	# struct {__u32 cap[2]; }
	scd_get = 0,		# __u32
	scd_modify = 0):	# __u32

	#ip conversion
	try:
		if ip:
			ip_number = map(int, ip.split('.'))
		else:
			ip_number = [0]*4
	except ValueError, e:
		raise RuntimeError("Ip format error: '%s', must be in forme 'A.B.C.D'" % ip)
	ip_nr = 0
	for i in xrange(4):
		ip_nr |= ((ip_number[i] & 0xff) << ((3-i)*8))

	# max_caps  conversion
	class MaxCaps(Structure):
		_fields_ = [("0", c_int), ("1", c_int)]
	maxcaps = MaxCaps(*max_caps)

	#print "calling rsbac_jail(%d, %s, %d, %d, %s, %d, %d)" % (RSBAC_JAIL_VERSION,
	#		rootdir, ip_nr, jail_flags, max_caps, scd_get, scd_modify)
	ret = librsbac.rsbac_jail(RSBAC_JAIL_VERSION, rootdir, ip_nr, jail_flags, maxcaps,
				scd_get, scd_modify)
	if ret < 0:
		raise RuntimeError("rsbac_jail() failled with %d" % ret)
