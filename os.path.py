print('---this is the os path file!---')

import os
file_path = "content/give.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

file_path = "content/contact.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

file_path = "content/index.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)


def write_pages():

	pages = [] 
	pages.append({
	    "filename": "content/index.html",
	    "title": "Index",
	    "output": "docs/index.html",

	    "filename": "content/contact.html",
	    "title": "Contact",
	    "output": "docs/contact.html",


	    "filename": "content/give.html",
	    "title": "Give",
	    "output": "docs/give.html",
	}) 
	print(pages)

write_pages()
