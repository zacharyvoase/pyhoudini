README.rst: README.md
	pandoc -f markdown -t rst < $< > $@

test:
	nosetests -v
	pep8 houdini.py test_houdini.py

.PHONY: test
