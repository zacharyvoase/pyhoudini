README.rst: README.md
	pandoc -f markdown -t rst < $< > $@
