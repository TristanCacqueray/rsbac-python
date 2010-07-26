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

res_fields = {
	"cpu": 0,
	"fsize": 1,
	"data": 2,
	"stack": 3,
	"core": 4,
	"rss": 5,
	"nproc": 6,
	"nofile": 7,
	"memlock": 8,
	"as": 9,
	"locks": 10
}
res_fields_names = dict((v,k) for k, v in res_fields.iteritems())

named_attr_values = {}
for d in dir():
	if d.endswith("_values_names"):
		named_attr_values[d[:-13]] = eval(d)

named_attr_fields = {}
for d in dir():
	if d.endswith("_fields_names"):
		named_attr_fields[d[:-13]] = eval(d)

on_off_attr = set()
for module in modules:
	on_off_attr.add("%s_learn" % module.lower())
for attr in ("auth_may_set_cap", ):
	on_off_attr.add(attr)

module_attrs = {
	"AUTH": ("auth_may_setuid", "auth_may_set_cap", "auth_learn"),
	"RES": ("res_min", "res_max"),
	"RC": ("rc_type_fd", ),
	"FF": ("ff_flags", ),
}
