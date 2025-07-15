import os 
from pathlib import Path
path = Path(r"C:\Users\harsh\OneDrive\Desktop\dummy")
for file in os.listdir(path):
    file_path = Path(path / file)
    suffix = file_path.suffix
    # print(suffix)
    if suffix == ".txt":
        new_path = file_path.with_suffix(".pdf")
        file_path.rename(new_path)
for file in os.listdir(path):
    file_path = Path(path)/ file
    if file_path.is_file():
        new_name = "renamed " + file_path.name
        new_path = file_path.with_name(new_name)
        file_path.rename(new_path)
pdf = path.glob("*.pdf")
# print(list(pdf))

for index , file in enumerate(pdf , start=1):
    new = f"file{index}.pdf"
    new_path = file.with_name(new)
    file.rename(new_path)
