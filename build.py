print('this is the build')



from jinja2 import Template
index_html = open("content/index.html").read()
template_html = open("templates/base.html").read()
give_html = open("content/give.html").read()
contact_html = open("content/contact.html").read()
template = Template(template_html)
template.render(
    title="Homepage",
    content=index_html,
)




def main():
	top = ('templates/top.html')
	bottom = ('templates/bottom.html')
	give = ('content/give.html')
	contact = ('content/contact.html')
	index = ('content/index.html')


#combine top.html with bottom.htm ito base.html with {{content}}





	
	top_template = open(top).read()
	bottom_template = open(bottom).read()
	base_template = top_template + "{{content}}" + bottom_template
	base_template = open('templates/base.html').read()
	open('templates/base.html', 'w+').write(base_template)


	



if __name__ == "__main__":
  main()

#template = open('templates/base.html').read() 





def listdic():

	pages = [ {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Mobilize Love Playbook",
		}, 
		{
		"filename": "content/contact.html",
		"output": "docs/contact.html",
		"title": "Contact",
		}, 
		{
		"filename": "content/give.html",
		"output": "docs/give.html",
		"title": "Give",
		}
		]



	for page in pages:
		template = open('templates/base.html').read()
		filename = open(page['filename']).read()
		combined_file = template.replace("{{content}}",filename)
		open(page['output'],'w+').write(combined_file)
		# title1 = open(page['title']).read()
		# title = template.replace("{{title}}",title1)
		# open(page['output'],'w+').write(filename)
		

listdic()



def apply_template():


#TODO: Read in template, do string replacing, and return the result


	# #create and combine index html 
	# template = open("templates/base.html").read()
	# index_content = open("content/index.html").read()
	# finished_index_page = template.replace("{{content}}", index_content)
	# open("docs/index.html", 'w+').write(finished_index_page)

#create and combine index html 
	template = open("templates/base.html").read()
	index_content = open("content/index.html").read()
	finished_index_page = template.replace("{{content}}", index_content)
	open("docs/index.html", 'w+').write(finished_index_page)



	return

apply_template()









# #index
# top_template = open('templates/top.html').read()
# body = open('content/index.html').read()
# bottom_template = open('templates/bottom.html').read()
# index_html = top_template + body + bottom_template 
# open('docs/index.html', 'w+').write(index_html)

# #testimonial 
# content = open('content/contact.html').read()
# contact = top_template + content + bottom_template
# open('docs/contact.html', 'w+').write(contact) 



# #give 
# page = open('content/give.html').read()
# give = top_template + page + bottom_template
# open('docs/give.html', 'w+').write(give) 




