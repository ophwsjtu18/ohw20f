#!D:\Python3.8.2\python.exe
# coding=utf-8
import cgi, cgitb

# 创建FieldStorage实例化
form = cgi.FieldStorage()

# 获取数据
site_dir = form.getvalue('mc_dir')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>MOOC</title>")
print("</head>")
print("<body>")
print("<style> button{width:100px;height:100px;background:#ffff;position:relative;left:100px;top:100px;} </style>")
print('<form action="/cgi-bin/get.py" method="get">')
print('<button name="mc_dir" type="submit" value="q">Q</button>')
print('<button name="mc_dir" type="submit" value="w">W</button>')
print('<button name="mc_dir" type="submit" value="e">E</button><br/>')
print('<button name="mc_dir" type="submit" value="a">A</button>')
print('<button name="mc_dir" type="submit" value="s">S</button>')
print('<button name="mc_dir" type="submit" value="d">D</button>')
print("</form>")
print("</body>")
print("</html>")

with open("mc_move" + '.txt', 'w') as f:
    f.write(f'{site_dir}')
