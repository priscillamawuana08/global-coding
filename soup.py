from bs4 import BeautifulSoup

html_doc ="""
<html>
  <head>
   <title>hello world</title>
  </head>
  <body>
    <p>Flexzy is a smart girl</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc,'html.pasrser')

soup.title
soup.title.text

