#
# Nice make. Use make VERBOSE=1 to verbose compilation.
#
ifneq ($(VERBOSE), 1)
.SILENT:
endif
E = @echo -e " "

all: build

build:
	$(E) "BUILD\t\t types dictionaries (based on /usr/local/include/rsbac)"
	@./_gen_types.py /usr/local/include/rsbac

clean:
	$(E) "CLEAN\t\t types dictionaries"
	rm -v -f *.pyo		\
		cap.py		\
		jail.py		\
		scd.py		\
		modules.py	\
		targets.py	\
		attrs.py	\
		errors.py	\
		auth.py		\
		daz.py		\
		ff.py		\
		*.py.ori

