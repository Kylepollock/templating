# Splitting into utils.py and manage.py
#------------------------------------------------
print('This is the manage')

def main():
	template = open("templates/base.html").read()

	#read files in the content directory

	import glob
	all_html_files = glob.glob("content/*.html")

	i=0
	pages = []
	template = open("templates/base.html").read()
	navbar = ""
	navbar_output = ""
	add_navbar = []
	combined_base = ""
	filename = {}
	output = {}
	title = {}
	html_result = {}


	# create the auto-generated list:
	for html_file in all_html_files:
		import os

		file_path = all_html_files[i]
		file_name = os.path.basename(file_path)
		i = i+1

		name_only, extension = os.path.splitext(file_name)

		path = "content/index.html"

		pages.append({
			"filename": "content/" + file_name,
			"title":"" + name_only + "",
			"output": "docs/" + file_name,
			"filename_only": file_name,
		})

	from jinja2 import Template

	for page in pages:

		index_html = open(page["filename"]).read()

		template_html = open("templates/base.html").read()
		template = Template(template_html)
		html_result = template.render(
			title=page['title'],
			content=index_html,
			pages=pages,
		)


		
		open(page['output'], 'w+').write(html_result)


import utils

import sys
print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
	utils.main()
	print("Build was specified")
elif command == "new":
	open('content/new_page.html', 'w+').write("New Page")
	print("New page was specified")
else:
	print("Please specify ’build’ or ’new’")

