# kompilace: python -m nuitka --follow-imports titulkovac.py --standalone --show-progress -j 8 --recurse-all


import glob
import os
import time
import re

"""
subfolder = "opraveno"

if not os.path.exists(subfolder):
    os.mkdir(subfolder)
"""


def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict, key=len, reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)


types = ('**/*.sub', '**/*.srt', '*.srt')  # the tuple of file types
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))

print(files_grabbed)

encodings = ["Windows-1250"]

for file in files_grabbed:
    for encoding_var in encodings:
        try:
            with open(file, "r+", encoding=encoding_var) as file_open:
                file_contents_orig = file_open.read()
                file_contents = file_contents_orig

                file_contents = multiple_replace(file_contents,
                                                 {"ø": "ř", "": "š", "è": "č", "È": "Č", "ï": "ď", "Ï": "Ď", "": "ž",
                                                  "": "Ž", "ì": "ě", "Ì": "Ě", "ù": "ů", "Ù": "Ů", "": "'", "": "'",
                                                  "": "ť", "ò": "ň", "Ò": "Ň", "Ø": "ř"})

                # print(file_contents)

                with open(file, "w", encoding="utf-8") as fo:
                    print(f"Opened {file} because it is {encoding_var}")
                    fo.write(file_contents)

                    if b'file_contents_orig' != b'file_contents':
                        print(
                            f"Finished {file}, difference of {abs(len(b'file_contents_orig') - len(b'file_contents'))}")

        except Exception as e:
            if not type(e) is UnicodeDecodeError:
                print(f"Exception with {file}: {e}")
