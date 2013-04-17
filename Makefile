README.rst: README.md
	pandoc -f markdown -t rst < $< > $@

test:
	nosetests -v

.PHONY: test
