def listdic():

	pages = [] 



	import glob
	all_html_files = glob.glob("content/*.html")
	print(all_html_files)


	for html_file_name in all_html_files:
		print(html_file_name)
		print("templates/base.html")


	pages.append({
	    "filename": "content/index.html",
	    "title": "Index",
	    "output": "docs/index.html",
	}) 
	print(pages)

	pages.append({
 		"filename": "content/contact.html",
	    "title": "Contact",
	    "output": "docs/contact.html",
	}) 
	print(pages)

	pages.append({
 		"filename": "content/give.html",
	    "title": "Give",
	    "output": "docs/give.html",
	}) 
	print(pages)

	for page in pages:
		template = open('templates/base.html').read()
		filename = open(page['filename']).read()
		combined_file = template.replace("{{content}}",filename)
		open(page['output'],'w+').write(combined_file)
		# title1 = open(page['title']).read()
		# title = template.replace("{{title}}",title1)
		# open(page['output'],'w+').write(filename)
		

listdic()

