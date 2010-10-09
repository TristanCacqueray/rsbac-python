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
"""	Filename:	main/tools/rsbac_menu.py
	Project:	rsbac-python
	Last update:	2010/07/05
	Purpose:	rsbac administration GUI

this is in alpha stage, mostly copy past from tbac REG module
"""
import os
import time

from Tkinter import *
import tkMessageBox
import tkSimpleDialog

from rsbac.helpers import *

def convert_hour(s):
	ts = time.strptime(s, "%H:%M")
	return ts.tm_hour * 3600 + ts.tm_min * 60 + time.altzone
def convert_date(s):
	if s == "undef":
		return 0
	elif s == "today":
		return int(time.time())
	elif s == "tomorow":
		return int(time.time()) + 3600*24
	try:
		ts = time.strptime(s, "%Y-%m-%d")
	except ValueError:
		ts = time.strptime(s, "%Y-%m-%d %H:%M:%S")
	return int(time.mktime(ts))

class Dialog(tkSimpleDialog.Dialog):
	def __init__(self, master, title, defval):
		self.defval = defval
		tkSimpleDialog.Dialog.__init__(self, master, title)

class HolidayInput(Dialog):
	def body(self, master):
		Label(master, text="Set oneshot holiday in DD/MM/YY format").grid(row=0,columnspan=2)
		Label(master, text="date:").grid(row=1)

		self.e1 = Entry(master)
		self.e1.insert(END, self.defval.strip())
		self.e1.grid(row=1, column=1)
		return self.e1

	def validate(self):
		if self.e1.get() == "0":
			self.results = 0
		else:
			self.results = convert_date(self.e1.get())
		return 1

class WorkingHourInput(Dialog):
	def body(self, master):
		Label(master, text="Set hours in HH:MM format").grid(row=0,columnspan=2)
		Label(master, text="Morning:").grid(row=1)
		Label(master, text="Evening:").grid(row=2)

		self.e1 = Entry(master)
		self.e1.insert(END, self.defval.split('->')[0].strip())
		self.e2 = Entry(master)
		self.e2.insert(END, self.defval.split('->')[1].strip())

		self.e1.grid(row=1, column=1)
		self.e2.grid(row=2, column=1)
		return self.e1

	def validate(self):
		self.results = []
		for i in (self.e1, self.e2):
			self.results.append(convert_hour(i.get()))
		if len(self.results) == 2:
			return 1
		return 0

class PathRcTypeInput(Dialog):
	def body(self, master):
		Label(master, text="Set path rc_type").grid(row=0, columnspan=2)
		Label(master, text="Rc_type:").grid(row=2)

		self.e1 = Listbox(master, selectmode=SINGLE, height=2)
		for k,v in (("General_FD", 0), ("Security_FD", 1),):
			self.e1.insert(0, k)
			if k == self.defval:
				self.e1.selection_set(0)
				self.e1.activate(0)
		self.e1.grid(row=2, column=1)
		return self.e1

	def validate(self):
		flag = self.e1.get(self.e1.curselection())
		self.results = 0
		return 1



class RsbacMenu:
	def refresh(self):
		# --------- Refresh ACI ---------
		try:
			stat = os.stat(self.path)
		except OSError, e:
			tkMessageBox.showerror(
				"Access file/dir",
				str(e)
			)
			self.master.destroy()
			raise

		try:
			working_hours = ("08:30", "19:00") #tbac.get_working_hours()
			oneshot_holiday = "0" #tbac.get_oneshot_holiday()
		except OSError, e:
			tkMessageBox.showerror(
				"TBAC REG Module",
				"Failed to access time configuration, is tbac loaded ?"
			)
			self.master.destroy()
			raise

		try:
			path_flags = "NC" #tbac.get_flags(self.path)
		except OSError, e:
			if str(e) == "RSBAC_EACCESS":
				tkMessageBox.showerror(
					"TBAC Attributes",
					"Failed to read '%s' attributes,"
					"does tbac enforce this device (%02x:%02x) ?" %
					(self.path, stat.st_dev >> 8 & 0xff, stat.st_dev & 0xff)
				)
			raise

		# --------- Update Tkinter variable ---------
		self.time.set("%d" % int(time.time()))
		self.hours.set("%s -> %s" % working_hours)
		self.oneshot.set("%s" % oneshot_holiday.split()[0])

		self.inode.set(stat.st_ino)
		self.rc_type.set(path_flags)

	def edit_time(self, e):
		tkMessageBox.showinfo("RSBAC info", "Can not update time...")

	def edit_path_rc_type(self, e):
		d = PathRcTypeInput(self.master, self.path, self.rc_type.get())
		if "results" not in dir(d):
			return
		try:
			tbac.set_flags(self.path, d.results)
		except:
			if str(e) == "RSBAC_EINVALIDVALUE":
				tkMessageBox.showerror("TBAC Attributes",
					"Wrong range definition.")
			else:
				raise

	def edit_oneshot_holiday(self, e):
		d = HolidayInput(self.master, "oneshot holiday", self.oneshot.get())
		if "results" not in dir(d):
			return
		try:
			tbac.set_oneshot_holiday(d.results)
		except OSError, e:
			if str(e) == "RSBAC_EINVALIDVALUE":
				tkMessageBox.showerror("TBAC Attributes",
					"Wrong working hours definition.")
			else:
				raise

	def edit_working_hours(self, e):
		d = WorkingHourInput(self.master, "working hours", self.hours.get())
		if "results" not in dir(d) or len(d.results) != 2:
			return
		try:
			print "setting working_hours(%d,%d)" % (d.results[0], d.results[1])
			tbac.set_working_hours(d.results[0], d.results[1])
		except OSError, e:
			if str(e) == "RSBAC_EINVALIDVALUE":
				tkMessageBox.showerror("TBAC Attributes",
					"Wrong working hours definition.")
			else:
				raise


	def editLabelFactory(self, group, var, act):
		l = Label(group, textvariable = var)
		l.bind("<Button-1>", act)
		return l


	def __init__(self, master, path):
		self.master, self.path = master, path

		# updatable content
		self.time = StringVar()
		self.hours = StringVar()
		self.oneshot = StringVar()

		self.inode = StringVar()
		self.rc_type = StringVar()
		self.refresh()

		group = LabelFrame(master, text="TBAC", padx=5, pady=5)
		group.grid(row=1)
		Label(group, text = 'Local Timezone: ').grid(row=1, sticky=E)
		Label(group, text = 'Current time (UTC): ').grid(row=2, sticky=E)
		Label(group, text = 'Working hour: ').grid(row=3, sticky=E)
		Label(group, text = 'Oneshot Holyday: ').grid(row=4, sticky=E)

		Label(group, text = 'UTC%d' % (time.altzone/3600.0)).grid(row=1, column=1)
		self.editLabelFactory(group, self.time,
				self.edit_time).grid(row=2, column=1)
		self.editLabelFactory(group, self.hours,
				self.edit_working_hours).grid(row=3, column=1)
		self.editLabelFactory(group, self.oneshot,
				self.edit_oneshot_holiday).grid(row=4, column=1)

		group = LabelFrame(master, text=path, padx=5, pady=5)
		group.grid(row=1, column=1)
		Label(group, text="inode: ").grid(row=1, sticky=E)
		Label(group, text="rc_type: ").grid(row=2, sticky=E)
		Label(group, textvariable=self.inode).grid(row=1, column=1)
		self.editLabelFactory(group, self.rc_type, self.edit_path_rc_type).grid(
			row=2, column=1)
#		self.editLabelFactory(group, self.range, self.edit_path_range).grid(row=3, column=1)

		self.refresh()



def main():
	import sys

	if len(sys.argv) != 2:
		print "usage: %s path" % sys.argv[0]
		return -1

	root = Tk()
	rsbac_python_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
	for path in ("%s/contrib" % rsbac_python_root, "/usr/share", "/usr/local/share"):
		try:
			print "%s/pixmaps/rsbac-logo.gif" % path
			photo = PhotoImage(file="%s/pixmaps/rsbac-logo.gif" % path)
			Label(image=photo).grid(row=0, columnspan=2)
			break
		except:
			pass

	app = RsbacMenu(root, path = sys.argv[1])
	root.mainloop()

if __name__ == "__main__":
	main()

