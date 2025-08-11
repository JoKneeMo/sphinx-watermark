# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAPIDOC  = sphinx-apidoc
BUILDDIR      = build

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
ALLSPHINXOPTS   = --keep-going -d $(BUILDDIR)/doctrees $(SPHINXOPTS) content
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(SPHINXOPTS) content

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone full HTML files"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pdf        to make a singlehtml file and run it through WeasyPrint"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  xelatexpdf to make LaTeX files and run them through xelatex"


.PHONY: clean
clean:
	rm -rf $(BUILDDIR)/*

.PHONY: html
html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

.PHONY: singlehtml
singlehtml:
	$(SPHINXAPIDOC) -o . ../
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

.PHONY: pdf
pdf:
	make singlehtml
	sed -i -e "s/href\=\"index\.html\#/href\=\"\#/g" "$(BUILDDIR)/singlehtml/index.html"
	@PDFFILENAME=$$(jq -r '"\(.pdf)_v\(.version).pdf"' content/docvars.json); \
	weasyprint $(BUILDDIR)/singlehtml/index.html "content/_static/$$PDFFILENAME"
	rm -rf $(BUILDDIR) content/docvars.json
	@echo
	@echo "Build finished. The PDF file is in $(BUILDDIR)/."

.PHONY: latexpdf
latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

.PHONY: xelatexpdf
xelatexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through xelatex..."
	$(MAKE) PDFLATEX=xelatex -C $(BUILDDIR)/latex all-pdf
	@echo "xelatex finished; the PDF files are in $(BUILDDIR)/latex."
