{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [/Users/adriannaaddicks/.wdm/drivers/chromedriver/mac64/91.0.4472.101/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "url=\"https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest\"\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "nasa=soup(html,'html.parser')\n",
    "result=nasa.find_all('div',class_='content_title')\n",
    "result[1].text\n",
    "           \n",
    "mars[\"news_title\"]=result[1].text\n",
    "\n",
    "             \n",
    "             \n",
    "             \n",
    "             \n",
    "             \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "paragraph=nasa.find('div', class_='article_teaser_body')  \n",
    "\n",
    "mars[\"paragraph\"]=paragraph.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<div class=\"article_teaser_body\">The six-wheeled scientist is heading south to explore Jezero Crater’s lakebed in search of signs of ancient microbial life.</div>\n"
     ]
    }
   ],
   "source": [
    "print(paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'news_title': \"NASA's Perseverance Rover Begins Its First Science Campaign on Mars\",\n",
       " 'paragraph': 'The six-wheeled scientist is heading south to explore Jezero Crater’s lakebed in search of signs of ancient microbial life.'}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
