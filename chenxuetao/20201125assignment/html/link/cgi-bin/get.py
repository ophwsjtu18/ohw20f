#!/usr/bin/python
import cgi,cgitb
#创建Fieldstorage实例化
form =cgi.FieldStorage()
site_name = form.getvalue('mc_move')
site_dir=form.getvalue('mc_dir')
#map=[[O.5,0.5]for x in range (10) ]print (map)
print "Content-type:text/html")
print()
print ("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>MOOC</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s</h2>"%(site_name,site_dir))
print("</body>")
print("</html>")
with open(site_name+'.txt','w') as f:
f.write(f'{site_dir}')

