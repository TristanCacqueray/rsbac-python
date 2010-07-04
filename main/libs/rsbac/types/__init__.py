try:
	from jail import *
	from rc import *
except ImportError:
	print "Rsbac types must be generate manualy..."
	print "Goto rsbac/types python modules and run _gen_types.py"
