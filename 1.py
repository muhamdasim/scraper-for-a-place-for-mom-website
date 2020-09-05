import urllib2
import html2text
url=''
page = urllib2.urlopen(url)
html_content = page.read()
rendered_content = html2text.html2text(html_content)
file = open('file_text.txt', 'w')
file.write(rendered_content)
file.close()