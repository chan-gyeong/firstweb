#!C:\Program Files (x86)\Python37-32\python.exe
print("content-type: text/html")
print()
import cgi
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding='utf8').read()#'open()'함수 3번째 인자로 인코딩을 명시해 준다.
else :
    pageId='home'
    description = '환영합니다.'
print('''<!DOCTYPE html>
<html>
  <head>
    <title>dkscksrud</title>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <h1><a href="index.py">Web</a></h1>
    </header>
    <ul>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=client">client</a></li>
        <li><a href="index.py?id=server">server</a></li>
        <li><a href="index.py?id=python">python</a></li>
    </ul>
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
</html>
'''.format(title=pageId, desc=description))
