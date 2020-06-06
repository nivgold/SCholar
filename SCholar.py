from scholarly import scholarly as sc
from PIL import Image
import requests
from io import BytesIO
import sys

if (len(sys.argv) != 2):
	print(f'Invalid number of arguments: {len(sys.argv)-1}. the program expect to get 1 variable')
	exit()

author_name = sys.argv[1]

author = next(sc.search_author(author_name))

response = requests.get(author.url_picture)
img = Image.open(BytesIO(response.content))


author = author.fill(sections=['publications'])

publications = len(author.publications)
citations = author.citedby

img.show()
print(f'Found: {author.name}')
print(f'Number of publications: {publications}')
print(f'Number of citations: {citations}')
print(f'CP ratio (citations/publications): {citations/publications}')