#!/usr/bin/python -OO
# -*- coding: utf8 -*-

try:
	from errors import *

	from modules import *
	from targets import *
	from attrs import *

	from scd import *

	from jail import *
	from cap import *
	from auth import *
	from daz import *
	from ff import *
except ImportError:
	from rsbac.tools import bcolors
	print "%s[E] Rsbac types must be generate manualy..." % bcolors.FAIL
	print "[E] Goto %s and run _gen_types.py%s" % (__path__, bcolors.ENDC)

module_attrs = {
	"AUTH": ("auth_may_setuid", "auth_may_set_cap", "auth_learn"),
	"RES": ("res_min", "res_max"),
	"RC": ("rc_type_fd", ),
	"FF": ("ff_flags", ),
}
