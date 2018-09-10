#!C:\Program Files (x86)\Python37-32\python.exe
print("content-type: text/html")
print()#위의 것들은 파이썬cgi를 위해 필요한 것이다.
import cgi, sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())#한글처리
form = cgi.FieldStorage()#page id 값 받음
files=os.listdir('data')#파일 목록을 리스트 형태로 받음
listStr=''
for value in files:
    listStr=listStr+'<li><a href="index.py?id={name}">{name}</a></li>'.format(name=value)
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding='utf8').read()#'open()'함수는 3번째 인자로 인코딩을 명시해 준다.
else :
    pageId='home'
    description = '환영합니다.'

print('''<!DOCTYPE html>
<html>
  <head>
    <title>의미없지만 의미있는 사이트</title>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <h1><a href="index.py">WEB</a></h1>
    </header>
    <ul>
        {listStr}
    </ul>
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
