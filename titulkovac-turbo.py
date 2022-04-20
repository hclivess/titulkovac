#kompilace: python -m nuitka --follow-imports titulkovac.py --standalone --show-progress -j 8 --recurse-all


import glob
import os
import time

"""
subfolder = "opraveno"

if not os.path.exists(subfolder):
    os.mkdir(subfolder)
"""

types = ('**/*.sub', '**/*.srt', '*.srt') # the tuple of file types
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))

print(files_grabbed)

encodings = ["Windows-1250"]

for file in files_grabbed:
    for encoding_var in encodings:
        try:
            with open(file, "r+", encoding=encoding_var) as file_open:
                file_contents = file_open.read()

                file_contents_new = file_contents.replace("ø","ř")
                file_contents_new = file_contents.replace("Ø", "ř")
                file_contents_new = file_contents.replace("", "š")
                file_contents_new = file_contents.replace("è", "č")
                file_contents_new = file_contents.replace("È", "Č")
                file_contents_new = file_contents.replace("ï", "ď")
                file_contents_new = file_contents.replace("Ï", "Ď")
                file_contents_new = file_contents.replace("", "ž")
                file_contents_new = file_contents.replace("", "Ž")
                file_contents_new = file_contents.replace("ì", "ě")
                file_contents_new = file_contents.replace("Ì", "Ě")
                file_contents_new = file_contents.replace("ù", "ů")
                file_contents_new = file_contents.replace("Ù", "Ů")
                file_contents_new = file_contents.replace("", "'")
                file_contents_new = file_contents.replace("", "'")
                file_contents_new = file_contents.replace("", "ť")
                file_contents_new = file_contents.replace("ò", "ň")
                file_contents_new = file_contents.replace("Ò", "Ň")

                #print(file_contents)

                with open(file, "w", encoding="utf-8") as fo:
                    fo.write(file_contents_new)

                    if file_contents != file_contents_new:
                        print(f"Finished {file}, difference of {abs(len(file_contents_new)-len(file_contents))}")

        except Exception as e:
            if not type(e) is UnicodeDecodeError:
                print(f"Exception with {file}: {e}")







