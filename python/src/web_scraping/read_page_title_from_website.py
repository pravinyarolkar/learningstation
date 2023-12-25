#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

result = requests.get('https://www.google.com')

print(result.status_code)
# print(result.text)

import bs4

bs4var = bs4.BeautifulSoup(result.text,"lxml")
# print(f"---------------------------------->--------------------------------> {bs4var}")
title = bs4var.select("title")[0].getText()
print(f"title we found is \"{title}\"")


# In[2]:


res = requests.get("https://en.wikipedia.org/wiki/Sachin_Tendulkar", verify=False)
soup = bs4.BeautifulSoup(res.text, "lxml")
soup.select('.infobox-label')[0].getText()
for data in soup.select('.infobox-data'):
    print(data.text)
# soup.select('.reference')


# In[3]:


res = requests.get('https://samples.ffmpeg.org/4khdr/', verify=False)
# print(res.text)
soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)
soup.select('img a')


# In[61]:


res = requests.get("https://unsplash.com/s/photos/laptop-wallpaper", verify=False)
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.mItv1')
img = soup.select('img')
img


# In[105]:


# quotestoscrape
number_of_pages = 15

for page in range(1, number_of_pages+1):
    res = requests.get(f'https://quotes.toscrape.com/page/{page}/',verify=False)
#     res = requests.get(f'https://quotes.toscrape.com/tag/inspirational/page/{page}/',verify=False)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    text = soup.select('.author')
    count = len(text)
    if count == 0:
        print("All quote pages are visited...!\n")
        break
    else:
        print(f"----------- for Page {page} -----------\n")
    author_list=[]
    for num in range(count):
        author_list.append(text[num].getText())

    # print(author_list)

    # quotes

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    text = soup.select('.text')
    cnt = len(text)
    quotes = []
    for cnt in range(cnt):
        quotes.append(text[cnt].getText())

    quotes_authors = {}

    for cnt in range(cnt):
        quotes_authors[author_list[cnt]] = quotes[cnt]

    print(quotes_authors)

