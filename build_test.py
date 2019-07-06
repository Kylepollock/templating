def listdic():

	pages = [] 



	import glob
	all_html_files = glob.glob("content/*.html")
	# print(all_html_files)


	for html_file_name in all_html_files:
		print(html_file_name)
		print("templates/base.html")


		import os
		file_path = html_file_name
		file_name = os.path.basename(file_path)
		print(file_name)
		name_only, extension = os.path.splitext(file_name)
		print(name_only)


		pages.append({
		    "filename": html_file_name,
		    "title": name_only,
		    "output": "docs/" + name_only + ".html"
		}) 
		print(pages)


		for page in pages:
			template = open(html_file_name).read()
			combined_file = template.replace("{{content}}",html_file_name)
			open(page['output'],'w+').write(combined_file)

			

from jinja2 import Template
index_html = open("content/index.html").read()
template_html = open("templates/base.html").read()
template = Template(template_html)
template.render(
    title="Homepage",
    content=index_html,
)




		# for html_file_name in pages:
		# 	template = open('content/*.html').read()
		# 	filename = open(page['filename']).read()
		# 	combined_file = template.replace("{{content}}",filename)
		# 	open(page['output'],'w+').write(combined_file)


	# pages.append({
 # 		"filename": "content/contact.html",
	#     "title": "Contact",
	#     "output": "docs/contact.html",
	# }) 
	# print(pages)

	# pages.append({
 # 		"filename": "content/give.html",
	#     "title": "Give",
	#     "output": "docs/give.html",
	# }) 
	# print(pages)

	# for page in pages:
	# 	template = open('templates/base.html').read()
	# 	filename = open(page['filename']).read()
	# 	combined_file = template.replace("{{content}}",filename)
	# 	open(page['output'],'w+').write(combined_file)
		# title1 = open(page['title']).read()
		# title = template.replace("{{title}}",title1)
		# open(page['output'],'w+').write(filename)
		

listdic()

