#Step 0: Install all the requirements
#pip install requests
#pip install bs4 

import requests
from bs4 import BeautifulSoup


#Step 1: Get the HTML
url = "https://www.gcet.ac.in/"
r = requests.get(url) # r variable has all the HTML code
htmlcontent = r.content # r returns response so if we want the code we write r.content
#print(htmlcontent)

#Step 2: Parse the HTML
soup = BeautifulSoup(htmlcontent, "html.parser") #. All the data we want is present in soup, we just have to target it and get it.
# print(soup.prettify) # to print html in tree structure

#Step 3: HTML Tree Traversal
title = soup.title #scrap title of the page
print(title)