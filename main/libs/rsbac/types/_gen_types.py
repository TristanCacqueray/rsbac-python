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
"""
	Filename:	_gen_types.py
	Last update:	04/06/2010
	Purpose:	Parse rsbac header, write python dictionary

give it rsbac headers directory as unique parameter
"""
import sys,os
import time
import re
# INDEV: developpement mode (exception throwing, debug output, ...)
INDEV=True

# files_content: rsbac header files readlines() dictionary
files_content = {}

def gen_init(base_dir):
	"""Prepare generation: read rsbac headers in global files_contents dictionary"""
	files_content["types.h"] = open("%s/types.h" % base_dir).readlines()
	files_content["header"] = open("_template_header.txt").read()

def gen_initfile(filename):
	"""Prepare singel generation: check if files does not exist, then add header"""
	if os.path.isfile(filename):
		if os.path.isfile("%s.ori" % filename):
			raise RuntimeError("please backup *.ori files, (%s.ori)" % filename)
		os.rename(filename, "%s.ori" % filename)
	output = open(filename, "w+")
	output.write(files_content["header"] % (filename, time.strftime("%Y/%m/%d")))
	return output

def gen_jail_types(filename):
	output = gen_initfile(filename)
	jail_flags_re = re.compile("^#define[ \t]+JAIL_([a-z_]+)[ \t]+([0-9]+)$")
	output.write("jail_flags = {\n")
	for line in files_content["types.h"]:
		m = jail_flags_re.match(line)
		if not m:
			continue
		output.write("\t'%s': %s,\n" % m.groups())
	output.write("}\n\n")
	output.write("# %s EOF\n" % filename)
	output.close()

		

def gen_types(base_dir):
	"""_gen_types.py main function"""
	gen_init(base_dir)
	gen_jail_types("jail.py")

def main():
	"""usage"""
	try:
		rsbac_header_dir = str(sys.argv[1])
		if not os.path.isdir(rsbac_header_dir) or len(sys.argv) != 2:
			raise RuntimeError("Unknown params: %s" % " ".join(sys.argv[1:]))

		gen_types(rsbac_header_dir)

	except IndexError:
		print "usage: %s rsbac_header_dir" % sys.argv[0]
	except Exception, e:
		if INDEV:
			raise
		print e


if __name__ == "__main__":
	main()
