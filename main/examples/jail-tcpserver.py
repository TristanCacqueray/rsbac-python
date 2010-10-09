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
"""	Filename:	main/examples/jail-tcpserver.py
	Project:	rsbac-python
	Last update:	2010/10/09
	Purpose:	Jail helper usecase

This is a simple echo back tcpserver using rsbac_jail python helper

--no-jail parameter disable rsbac jailing
"""

import socket,os,resource

import SocketServer

from rsbac.types import *
import rsbac.helpers.jail

def allowed(msg):
	print "[+] \033[91m%32s -> Allowed\033[0m" % msg
def denied(msg):
	print "[+] \033[92m%32s -> Denied\033[0m" % msg

def test(test_name, func):
	try:
		func()
		allowed(test_name)
		return True
	except:
		denied(test_name)
		return False

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		# User data inputs
		self.data = self.request.recv(1024).strip()
		# Security check
		test("listen on other ip", lambda : SocketServer.TCPServer(("0.0.0.0", 9998), MyTCPHandler))
		test("/dev/ access", lambda : open("/dev/zero", "r").read(4096))
		test("other process status", lambda : open("/proc/1/cmdline", "r").read())
		test("non unix socket creation", lambda : socket.socket(socket.AF_NETLINK, socket.SOCK_DGRAM))
		test("set ressource", lambda : resource.setrlimit(resource.RLIMIT_NOFILE, (500, 500)))
		if os.getuid() == 0:
			test("raw socket creation", lambda : socket.socket(socket.AF_PACKET, socket.SOCK_RAW))
			test("/etc/shadow read", lambda : open("/etc/shadow").read())
		# User data outputs
		self.request.send(self.data.upper())

def main(argv):
	HOST, PORT = "127.0.0.1", 9999

	if "--no-jail" in argv:
		print "[+] No rsbac jail created..."
	else:
		print "[+] Creating rsbac jail"
		rootdir = "/var/empty"
		if os.getuid() != 0:
			rootdir = None
		rsbac.helpers.jail.rsbac_jail(
			rootdir = rootdir,
			ip = HOST,
		)

	SocketServer.TCPServer.allow_reuse_address = True
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

	print "[+] %d Listening on %s:%d" % (os.getpid(), HOST, PORT)
	server.serve_forever()

if __name__ == "__main__":
	import sys
	main(sys.argv)

