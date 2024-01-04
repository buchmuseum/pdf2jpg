# PDFs in JPGs umwandeln

Wir haben auf einem Netzlaufwerk einige hundert Scans von Wasserzeichen, die nicht als JPGs, sondern als PDFs abgespeichert wurden. Um sie in den Katalog einspielen zu können, müssen alle PDFs in JPGs umgewandelt werden.

# Lösung

1. Neues poetry-Projekt: `poetry new pdf2jpg`.
2. Dann muss ImageMagick installiert werden: `sudo apt-get install libmagickwand-dev`
3. Damit es auch PDFs lesen darf, muss in der Datei `/etc/ImageMagick-7/policy.xml` die Zeile `<policy domain="coder" rights="none" pattern="PDF" />` in `<policy domain="coder" rights="read | write" pattern="PDF" />` abgeändert, also Lese- und Schreibberechtigung erteilt werden.
4. Jetzt können wir "Wand" zu Python hinzufügen: `poetry add wand`.
5. Mithilfe von ChatGPT haben wir rasch ein passendes Skript erstellt...
6. Es lässt sich mit `poetry run python pdf2jpg/pdf2jpg.py` aufrufen.