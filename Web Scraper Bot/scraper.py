#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import re
import os
import openai


# In[2]:


BIG_DATA_JOURNAL = "https://www.dbta.com/BigDataQuarterly/ArticleIndex.aspx"
MEDIUM = "https://medium.com/tag/big-data-analytics"


# In[3]:


url_dict = {}
def scrape_data(url):
    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content)
    results = soup.find_all("div", class_="post_content")
    url_article = soup.find_all("h3")
    reg_url = 'href="(.*\.aspx)'
    reg_title = 'span itemprop="name">(.*)\</span></a><'
    for item in url_article:
        try:
            url_match = re.findall(reg_url, str(item))[0]
            url_title = re.findall(reg_title, str(item))[0]
            url_dict[str(url_title)] = url_match
        except:
            print("*" * 100)
    return url_dict


# In[4]:


url_dict= scrape_data(BIG_DATA_JOURNAL)


# In[5]:


def article_generator():
    arr = []
    n1 = np.random.randint(20)
    for item in list(url_dict.items())[n1]:
        arr.append(item)
    try:
        art_rep[arr[0]] = arr[1]
    except:
        article_generator(n1)
        
    return art_rep


# In[6]:


art_rep = {}
curr_arr = article_generator()
curr_arr


# In[7]:


title = list(curr_arr.keys())[0]


# In[8]:


OPENAI_API_KEY = "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"


# In[18]:


openai.api_key = OPENAI_API_KEY

prompt = "Visit the URL {0}, and summarise it.".format(list(curr_arr.values())[0])
#url = 'https://www.informationweek.com/cloud/rise-of-data-and-asynchronization-hyped-up-at-aws-re-invent'
prompt = "Visit the URL {0}, and summarise it.".format(url)
response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=0.6,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)


# In[10]:


list(curr_arr.values())[0]


# In[19]:


prompt


# In[20]:


response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=0.6,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)


# In[14]:


message = "{0} {1}".format(response["choices"][0]['text'].strip(), list(curr_arr.values())[0])


# In[22]:


message


# In[ ]:


### For publishing on Slack


# In[16]:


# def message_body(mes, title):
#     url = "https://hooks.slack.com/services/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"
#     message = mes
#     title = (title)
#     slack_data = {
#         "username": "Utsav Ajay",
#         "channel" : "slackbot-v1",
#         "attachments": [
#             {
#                 "color": "#9733EE",
#                 "fields": [
#                     {
#                         "title": title,
#                         "value": message,
#                         "short": "true",
#                     }
#                 ]
#             }
#         ]
#     }
#     byte_length = str(sys.getsizeof(slack_data))
#     headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
#     response = requests.post(url, data=json.dumps(slack_data), headers=headers)
#     if response.status_code != 200:
#         raise Exception(response.status_code, response.text)


