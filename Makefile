#
# Nice make. Use make VERBOSE=1 to verbose compilation.
#
ifneq ($(VERBOSE), 1)
.SILENT:
endif
E = @echo -e "[+] "

all:
	@echo "Welcome to rsbac-python package!"
	@echo "To compile all packages, type:"
	@echo "\`\`make build'"
	@echo 
	@echo "Be sure to read the \`\`INSTALL' and \`\`README' files for"
	@echo "more information."
	@echo 
	@echo "The rsbac-python team - http://github.com/gcm/rsbac-python"

build:
	$(E) "Building rsbac type dictionaries in main/libs/rsbac/types"
	@$(MAKE) build -C main/libs/rsbac/types/

clean:
	$(E) "Cleaning rsbac type dictionaries..."
	@$(MAKE) clean -C main/libs/rsbac/types/
	$(E) "Cleaning python objects..."
	find . -name "*.py[oc]" -exec rm {} \;
