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
"""	Filename:	main/libs/rsbac/types/_gen_types.py
	Project:	rsbac-python
	Last update:	2010/07/24
	Purpose:	Parse rsbac header, write python dictionary

This is a standalone programe, give it rsbac headers directory as unique parameter.
Main methods:
	gen_init	: read headers files once
	gen_initfile	: prepare new file and return file object
	gen_define	: match against regexp
	gen_enum	: first group lines of intereset, then match agains regexp
	gen_types	: main function
	main		: usage function
"""
import sys,os
import time
import re
from rsbac.tools import *

# files_content: rsbac header files readlines() dictionary
files_content = {}

LINUX_CAP_FILE="/usr/include/linux/capability.h"

def gen_init(base_dir):
	"""Prepare generation: read rsbac headers in global files_contents dictionary"""
	files_content["types.h"] = open("%s/types.h" % base_dir).readlines()
	files_content["error.h"] = open("%s/error.h" % base_dir).readlines()
	files_content["capability.h"] = open(LINUX_CAP_FILE).readlines()
	files_content["header"] = open("_template_header.txt").read()

def gen_initfile(filename):
	"""Prepare single generation: check if files does not exist, then add header"""
	if os.path.isfile(filename):
		if os.path.isfile("%s.ori" % filename):
			raise RuntimeError("please backup *.ori files, (%s.ori)" % filename)
		os.rename(filename, "%s.ori" % filename)
	print "[+] -> %s" % format(filename, "15s"),
	output = open(filename, "w+")
	output.write(files_content["header"] % (filename, time.strftime("%Y/%m/%d")))
	return output
def gen_endfile(output):
	output.write("\n# %s EOF\n" % output.name)
	print "\t%s%d bytes written%s" % (bcolors.OKBLUE, output.tell(), bcolors.ENDC)
	output.close()

def get_output(fileobj):
	if isinstance(fileobj, str):
		# fileobj can be a path str if it contains a single dictionary
		output = gen_initfile(fileobj)
	else:
		# or an already opened file if it contains multiple dictionary
		output = fileobj
	return output

def gen_define(fileobj, regexp, dic_name, headername = "types.h", start_pattern = None):
	output = get_output(fileobj)
	pat_re = re.compile(regexp)
	output.write("%s = {\n" % dic_name)
	start_pattern_finded = False
	for line in files_content[headername]:
		if start_pattern and not start_pattern_finded:
			if not line.startswith(start_pattern):
				continue
			start_pattern_finded = True
			continue
		m = pat_re.match(line)
		if start_pattern and not m:
			break
		if not m:
			continue
		output.write("\t'%s':\t%s,\n" % m.groups())
	output.write("}\n")
	output.write("%s_names = dict((v,k) for k, v in %s.iteritems())\n\n" %
			(dic_name, dic_name)
	)
	if isinstance(fileobj, str):
		gen_endfile(output)

def gen_enum(fileobj, enum, enum_prefix, dic_name, headername = "types.h"):
	output = get_output(fileobj)
	# first make one string for all enum
	enum_string = ""
	for line in files_content[headername]:
		if line.startswith("enum") and line.find("%s" % enum) != -1:
			s_idx = files_content[headername].index(line)
			e_idx = s_idx + 500
			enum_string = " ".join(files_content[headername][s_idx:e_idx])
			break
	# then extract enum names
	pat_re = re.compile("enum[ \t]+%s[ \t\n]+{([^}]+)}" % enum, re.MULTILINE)
	m = pat_re.match(enum_string)
	if not m:
		raise RuntimeError("Could not parse %s" % enum)
	# for each enum, write name and position
	output.write("%s = {\n" % dic_name)
	i = 0
	for enum in m.groups()[0].replace('\n', '').split(','):
		if enum.strip().startswith('#ifdef __KERNEL__'):
			break
		output.write("\t'%s':\t%s,\n" % (enum.replace(enum_prefix, "").strip(), i))
		i += 1
	output.write("}\n")
	output.write("%s_names = dict((v,k) for k, v in %s.iteritems())\n\n" %
			(dic_name, dic_name)
	)
	if isinstance(fileobj, str):
		gen_endfile(output)

def gen_types(base_dir):
	"""_gen_types.py main function"""
	print "[+] Generating rsbac python types"
	gen_init(base_dir)
	gen_define("errors.py", "^#define[ \t]+RSBAC_([a-zA-Z_]+)[ \t]+([0-9]+)$", "errors",
		headername = "error.h")
	gen_define("jail.py", "^#define[ \t]+JAIL_([a-z_]+)[ \t]+([0-9]+)$", "jail_flags")
	gen_define("cap.py", "^#define[ \t]+CAP_([a-zA-Z_]+)[ \t]+([0-9]+)$", "caps",
		headername = "capability.h")
	gen_enum("scd.py", "rsbac_scd_type_t", "ST_", "scd")
	gen_enum("modules.py", "rsbac_switch_target_t", "SW_", "modules")
	gen_enum("targets.py", "rsbac_target_t", "T_", "targets")
	gen_enum("attrs.py", "rsbac_attribute_t", "A_", "attrs")
	gen_enum("auth.py", "rsbac_auth_may_setuid_t", "AMS_", "auth_may_setuid_values")

	gen_define("ff.py", "^#define[ \t]+FF_([a-zA-Z_]+)[ \t]+([0-9]+)$",
		dic_name = "ff_flags_values")

	daz_fileobj = gen_initfile("daz.py")
	gen_define(daz_fileobj, "^#define[ \t]+DAZ_([a-zA-Z_]+)[ \t]+([0-9]+)$",
		dic_name = "daz_scanned_values",
		start_pattern = "typedef __u8 rsbac_daz_scanned_t;")
	gen_define(daz_fileobj, "^#define[ \t]+DAZ_([a-zA-Z_]+)[ \t]+([0-9]+)$",
		dic_name = "daz_do_scan_values",
		start_pattern = "typedef __u8 rsbac_daz_do_scan_t;")
	gen_endfile(daz_fileobj)
	print "[+] %sdone%s" % (bcolors.OKGREEN, bcolors.ENDC)

def main():
	"""usage"""
	try:
		rsbac_header_dir = str(sys.argv[1])
		if not os.path.isdir(rsbac_header_dir) or len(sys.argv) != 2:
			raise RuntimeError("Unknown params: %s" % " ".join(sys.argv[1:]))
		if not os.path.isfile(LINUX_CAP_FILE):
			raise RuntimeError("%s does not exist, please fixe" %
						LINUX_CAP_FILE)
		gen_types(rsbac_header_dir)

	except IndexError:
		print "usage: %s rsbac_header_dir" % sys.argv[0]
	except Exception, e:
		if INDEV:
			raise
		print e


if __name__ == "__main__":
	main()
