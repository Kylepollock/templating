def listdic():

	i = 0
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


	import glob
	all_html_files = glob.glob("content/*.html")
	# print(all_html_files)


	for html_file_name in all_html_files:
		# print(html_file_name)
		# print("templates/base.html")


		import os
		file_path = all_html_files[i]
		file_name = os.path.basename(file_path)
		i = i + 1


		print(file_name)
		
		# print(file_name)
		name_only, extension = os.path.splitext(file_name)
		# print(name_only)

		path = "content/index.html"


		pages.append({
		    "filename": "content/" + file_name,
		    "title": name_only,
		    "output": "docs/" + file_name
		    # "filename_only": filename,
		}) 
		# print(pages)


		#create navbar
		add_navbar = '''<nav class="navbar navbar-expand-lg bg-secondary text-uppercase fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="#page-top">Moblize Love Playbook</a>
      <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#portfolio">Why We Exist</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#about">What We Do</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#contact">How We Behave</a>
          </li>
            <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded" href="contact.html">Contact</a>
          </li>
           <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded" href="give.html">Give</a>'''



		for page in pages:
			template = open(page['filename']).read()
			combined_file = template.replace("{{content}}",template)
			combined_file = template.replace("{{add_navbar}}",template)
			open(page['output'],'w+').write(combined_file)

pages = [] 			

from jinja2 import Template

for page in pages:
	index_html = open(page["filename"]).read()
	template_html = open("templates/base.html").read()
	template = Template(template_html)
	html_result = template.render(
	    title=page['title'],
	    content=index_html,

	    page = pages,
)



	


	template.render(pages=pages, content=content_html)

	open(page['output'], 'w+').write(html_result)
print(pages)




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

