#!C:\Program Files (x86)\Python37-32\python.exe
print("content-type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>home</title>
  </head>
  <body>
    <header>
      <h1><a href="index.py?id=home">Web</a></h1>
    </header>
    <ul>
        <li><a href="index.py?id=html">HTML</a></li>
        <li><a href="index.py?id=client">client</a></li>
        <li><a href="index.py?id=server">server</a></li>
        <li><a href="index.py?id=python">python</a></li>
    </ul>
    <h2>{title}</h2>
    <p>
        "HTML"은 웹을 배우는데 있어서 가장 기초적이고 중심적인 내용이다.
    </p>
  </body>
</html>
'''.format(title=pageId))
