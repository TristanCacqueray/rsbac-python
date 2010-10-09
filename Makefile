#
# Nice make. Use make VERBOSE=1 to verbose compilation.
#
ifneq ($(VERBOSE), 1)
.SILENT:
E = @echo
else
E = @:
endif

all:
	@echo "Welcome to rsbac-python package!"
	@echo "To compile all packages, type:"
	@echo "\`\`make build'"
	@echo 
	@echo "Be sure to read the \`\`INSTALL' and \`\`README' files for"
	@echo "more information."
	@echo 
	@echo "The rsbac-python team - http://github.com/gcm/rsbac-python"

clean:
	$(call E, "Cleaning rsbac type dictionnaries...")
	@$(MAKE) clean -C main/libs/rsbac/types/
