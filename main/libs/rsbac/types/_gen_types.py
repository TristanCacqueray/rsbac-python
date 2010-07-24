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
	gen_simple	: match against regexp
	gen_multi	: first group lines of intereset, then match agains regexp
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
	files_content["capability.h"] = open(LINUX_CAP_FILE).readlines()
	files_content["header"] = open("_template_header.txt").read()

def gen_initfile(filename):
	"""Prepare singel generation: check if files does not exist, then add header"""
	if os.path.isfile(filename):
		if os.path.isfile("%s.ori" % filename):
			raise RuntimeError("please backup *.ori files, (%s.ori)" % filename)
		os.rename(filename, "%s.ori" % filename)
	print "[+] -> %s" % format(filename, "15s"),
	output = open(filename, "w+")
	output.write(files_content["header"] % (filename, time.strftime("%Y/%m/%d")))
	return output
def gen_endfile(output):
	output.write("# %s EOF\n" % output.name)
	print "\t%s%d bytes written%s" % (bcolors.OKBLUE, output.tell(), bcolors.ENDC)
	output.close()

def gen_simple(filename, regexp, dic_name, headername = "types.h"):
	output = gen_initfile(filename)
	pat_re = re.compile(regexp)
	output.write("%s = {\n" % dic_name)
	for line in files_content[headername]:
		m = pat_re.match(line)
		if not m:
			continue
		output.write("\t'%s':\t%s,\n" % m.groups())
	output.write("}\n\n")
	gen_endfile(output)

def gen_multi(filename, enum, enum_prefix, dic_name, headername = "types.h"):
	output = gen_initfile(filename)
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
	output.write("}\n\n")
	gen_endfile(output)

def gen_types(base_dir):
	"""_gen_types.py main function"""
	print "[+] Generating rsbac python types"
	gen_init(base_dir)
	gen_simple("jail.py", "^#define[ \t]+JAIL_([a-z_]+)[ \t]+([0-9]+)$", "jail_flags")
	gen_simple("cap.py", "^#define[ \t]+CAP_([a-zA-Z_]+)[ \t]+([0-9]+)$", "caps",
		headername = "capability.h")
	gen_multi("scd.py", "rsbac_scd_type_t", "ST_", "scd")
	gen_multi("modules.py", "rsbac_switch_target_t", "SW_", "modules")
	gen_multi("targets.py", "rsbac_target_t", "T_", "targets")
	gen_multi("attrs.py", "rsbac_attribute_t", "A_", "attrs")
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
