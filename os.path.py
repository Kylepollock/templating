import os
file_path = "content/give.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)


pages = [] pages.append({
    "filename": "content/index.html",
    "title": "Index",
    "output": "docs/index.html",
}) print(pages)
