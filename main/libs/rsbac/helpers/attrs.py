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
"""	Filename:	main/libs/rsbac/helpers/attrs.py
	Project:	rsbac-python
	Last update:	2010/07/24
	Purpose:	attr helpers

"""
from rsbac.helpers.lib import *
from rsbac.types import *

def rsbac_get_attr_n(module,		# __u8
		target,			# __u8
		name,			# char *
		attr,			# __u8
		inherit = 0):		# int
	ta_number = 0

	i = c_int(42)
	value = pointer(i)
#	value = create_string_buffer('\000' * 512)

	rsys_param = (ta_number, module, target, name, attr, value, inherit)
#	print "calling rsbac_get_attr_n(%d, %d, %d, %s, %d, %s, %d)" % rsys_param
	ret = librsbac.rsbac_get_attr_n(*rsys_param)
	if ret < 0:
		raise RsbacError("rsbac_get_attr_n(): module %s, attr %s, path %s" %
			(
				get_module_name(module),
				get_attr_name(attr),
				name,
			),
			ret
		)
	return value.contents.value


def get(path):
	path_attrs = {}
	for module in modules.keys():
		if module not in module_attrs or module not in active_modules:
			continue
		path_attrs[module] = {}
		for attr in module_attrs[module]:
			value = rsbac_get_attr_n(
				modules[module],
				targets["FD"],
				path,
				attrs[attr]
			)
			path_attrs[module][attr] = value
	return path_attrs
