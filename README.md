# file_organizer
A Python script to batch rename files, convert `.txt` to `.pdf`, and apply custom filename formats using `pathlib` and `os`.
📂 File Organizer using Python (`pathlib` & `os`)

This Python script automates basic file management tasks such as:
 Converting `.txt` files to `.pdf`
 Prefixing all filenames with `renamed `
 Renaming `.pdf` files to a numbered format (`file1.pdf`, `file2.pdf`, ...)



 ✅ Features

 🔁 Batch rename files with a custom prefix (`renamed `)
 🔄 Convert `.txt` files to `.pdf` (extension change only)
 🔢 Rename `.pdf` files sequentially (`file1.pdf`, `file2.pdf`, ...)
 🧩 Uses both `os` and `pathlib` modules
 💻 Works on Windows and crossplatform with Python 3.6+



 🧾 Requirements

 Python 3.6 or above
 No external libraries required



 📂 Folder Example (Before and After)

 🔸 Before:
dummy/
├── notes.txt
├── image.jpg
├── script.py

 🔹 After Running Script:
dummy/
├── file1.pdf
├── renamed_image.jpg
├── renamed_script.py



 🚀 How to Use

1. Set your folder path:
   ```python
   path = Path(r"C:\Users\harsh\OneDrive\Desktop\dummy")
2.	Run the script:
3.	python Rename_files.py

