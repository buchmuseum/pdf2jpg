import os

# Vorher mit poetry add wand installieren. Damit wand läuft, muss zunächst ImageMagick installiert werden: `sudo apt-get install libmagickwand-dev`
# Ggf. dann noch Lese- und Schreibrechte erteilen mit <policy domain="coder" rights="read | write" pattern="PDF" /> in /etc/ImageMagick-7/policy.xml.

from wand.image import Image

def convert_pdfs_to_jpgs(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:            
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file) # Merkt sich den kompletten Dateinamen inkl. Pfad.
                jpg_path = os.path.splitext(pdf_path)[0] + '.jpg' # Nimmt den Dateinamen und ergänzt ".jpg".

                with Image(filename=pdf_path, resolution=300) as img: # Speichert PDF als Jpg.
                    img.format = 'jpg'
                    img.save(filename=jpg_path)

                print(f"Converted '{pdf_path}' to '{jpg_path}'")

# Ersetze 'directory_path' mit dem Verzeichnis, in dem sich die PDFs befinden.
directory_path = '/mnt/b/Projekte/_Wasserzeichen/WZIS_Bilder/WZ_II_Sachsen'
convert_pdfs_to_jpgs(directory_path)
