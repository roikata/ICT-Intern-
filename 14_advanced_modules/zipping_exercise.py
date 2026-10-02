import shutil
import os
import re


shutil.unpack_archive("unzip_me_for_instructions.zip", "","zip")

with open("extracted_content/Instructions.txt") as f:
    content = f.read()





def search(file,pattern = r"\d{3}-\d{3}-\d{4}"):
    with open(file, "r") as f:
        text = f.read()

    if re.search(pattern,text):
        return re.search(pattern,text)

    else:
        return ""


result = []

for folder,subfolders,files in os.walk(os.path.join(os.getcwd(), "extracted_content")):
    for file in files:
        full_path = folder+"\\"+file
        result.append(search(full_path))

for r in result:
    if r != "":
        print(r.group())



