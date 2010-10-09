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

from rsbac.types import *

try:
	librsbac = cdll.LoadLibrary("librsbac.so.1")
except OSError:
	import sys
	raise RuntimeError("Could not find librsbac.so.1")

def rsbac_check():
	import os.path
	if not os.path.exists("/proc/rsbac-info/active"):
		raise RuntimeError("CONFIG_RSBAC_PROC must be enable.")
	return True

if not rsbac_check():
	raise RuntimeError("Rsbac must be active to use this package.")

active_modules = set()

def load_active_module():
	for line in open("/proc/rsbac-info/active").readlines():
		if line.startswith("Module: "):
			active_modules.add(line.split()[1])
	print "Debug: %s active module detected" % active_modules
load_active_module()


def get_name(dic, key):
	if key not in dic.keys():
		return "UNKNOWN"
	return dic[key]

import errno
def get_error_name(syserrno):
	syserrno = abs(syserrno)
	if syserrno < 35:
		# Try linux errno
		try:
			return errno.errorcode[syserrno]
		except:
			pass
	return get_name(errors_names, syserrno)

def get_attr_name(attr):
	return get_name(attrs_names, attr)

def get_module_name(module):
	return get_name(modules_names, module)

def get_attr_value_name(attr, value):
	# Try direct attribute value name, ie auth_may_setuid
	if attr in named_attr_values.keys():
		return named_attr_values[attr][value]

	# Try bitfield attribute value names, ie res_*
	fields = []
	for attr_name in named_attr_fields.keys():
		if not attr.startswith(attr_name):
			continue
		try:
			for idx,field_name in named_attr_fields[attr_name].items():
				fields.append("%s %d" %
					(
						field_name,
						value[idx],
					)
				)
		except IndexError, e:
			print "get_attr_value_name could not depack %s (%s)" % (
				attr, repr(value)
			)
			return repr(value)
	if len(fields) > 0:
		return fields

	# Try on of attribute value name, ie auth_learn
	if attr in on_off_attr:
		if value == 1:
			return "on"
		return "off"

	# Custom attrs
#	if attr == "rc_type_fd":
#		return get_rc_type_name(attr, value)
	return repr(value)

class RsbacError(Exception):
	def __init__(self, msg, syserrno):
		self.msg = msg
		self.syserrno = syserrno
	def __str__(self):
		return "%s FAILLED. return value = %d (%s)" % (
			self.msg,
			self.syserrno,
			get_error_name(self.syserrno),
		)

