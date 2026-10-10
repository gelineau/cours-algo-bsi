MD      := cours2.md
HTML    := cours2.html
PDF     := cours2.pdf
CHROME  := google-chrome

.PHONY: build_pdf clean

build_pdf: $(PDF)
	rm -f $(HTML)

$(HTML): $(MD)
	pandoc $(MD) -s -o $(HTML) --metadata title="Cours 2 - Exercices"

$(PDF): $(HTML)
	$(CHROME) --headless --disable-gpu --no-pdf-header-footer \
		--print-to-pdf=$(PDF) "file://$(CURDIR)/$(HTML)"

clean:
	rm -f $(HTML) $(PDF)

