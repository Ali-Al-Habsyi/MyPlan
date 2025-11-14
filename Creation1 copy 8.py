from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen('http://pythonscraping.com/'
 'pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

# Let us bring more to 

# An AI for everyone, by everyone, the usefulness of which becomes clear 
# in everyday wonder at connections in anything. It's not about where the connections 
# lie, but the connection itself and the extensions of knowledge that can be derived 
# from it. So that all forms of enlightenment can be extracted from the things we 
# observe, and that enlightenment is stored in an external entity that will be as 
# close to objectivity as possible, at least as true as functionally necessary. 
# It will serve as an Encyclopedia for Humanity, so that people can turn to it 
# for guidance in knowledge, science, law, and, ultimately, life orientation. 
# So that someone in Japan knows how many fish live in a local river based on 
# the good or bad experience of a fellow human being in a territory flagged to 
# Canada. So that learning truly happens, not just in our heads but in an external 
# entity, most accessible through and derived from reality, whatever that may be. 
# So that major conflicts and wars can be avoided as there is a right answer, 
# so that we know what to aim for, so that we know how to navigate the universe
# in the desired event that interstellar travel becomes something grand.

# There are many ways to implement the above.
# Let us proceed by considering all-encompassing representations of reality.
# representing reality in its totality is not impossible.

# Let us start by bringing first attempts to scraping all of the web, truly all of it. Here ius one reality over which to traverse.
# And I mean all of it, if possible code through paywalls

# Let's scrape the web properly.
# Our mission is to hack the universe, we're beyond patents
#<><><><><><><><><><><>

# Stap 1.

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)

bs = BeautifulSoup(html, 'html.parser')

from urllib.request import urlopen
from urllib.error import HTTPError
try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
else:
    # program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
try:
    html = urlopen(url)
except HTTPError as e:
    return None
try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h1
except AttributeError as e:
    return None
    return title
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
{'src':'../img/gifts/img1.jpg'})
.parent.previous_sibling.get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
 {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a',

href=re.compile('^(/wiki/)((?!:).)*$'))
links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
                getLinks('')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span')
         .find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')

for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
    if 'href' in link.attrs:
        if link.attrs['href'] not in pages:
            #We have encountered a new page
            newPage = link.attrs['href']
            print('-'*20)
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)
            getLinks('')

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
    pages = set()
    random.seed(datetime.datetime.now())
    #Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl):
includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
 urlparse(includeUrl).netloc)
internalLinks = []
#Finds all links that begin with a "/"
for link in bs.find_all('a',
     href=re.compile('^(/|.*'+includeUrl+')')):
    if link.attrs['href'] is not None:
    if link.attrs['href'] not in internalLinks:
    if(link.attrs['href'].startswith('/')):
    internalLinks.append(
     includeUrl+link.attrs['href'])
else:
    internalLinks.append(link.attrs['href'])
    return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
for link in bs.find_all('a',
     href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
    if link.attrs['href'] is not None:
        if link.attrs['href'] not in externalLinks:
            externalLinks.append(link.attrs['href'])
            return externalLinks
            
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs,
     urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme,
         urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,
        len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)
    followExternalOnly('http://oreilly.com')

# Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
     urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    
for link in externalLinks:
    if link not in allExtLinks:
        allExtLinks.add(link)
        print(link)
        for link in internalLinks:
            if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)
            allIntLinks.add('http://oreilly.com')
            getAllExternalLinks('http://oreilly.com')

import requests
class Content:
def __init__(self, url, title, body):
    self.url = url
    self.title = title
    self.body = body
    
    def getPage(url):
        req = requests.get(url)
        return BeautifulSoup(req.text, 'html.parser')
    
    def scrapeNYTimes(url):
        bs = getPage(url)
        title = bs.find("h1").text
        lines = bs.find_all("p", {"class":"story-content"})
        body = '\n'.join([line.text for line in lines])
        return Content(url, title, body)
    
    def scrapeBrookings(url):
        bs = getPage(url)
        title = bs.find("h1").text
        body = bs.find("div",{"class","post-body"}).text
        return Content(url, title, body)
    
    url = 'https://www.brookings.edu/blog/future-development'
     '/2018/01/26/delivering-inclusive-urban-access-3-unc'
     'omfortable-truths/'

    content = scrapeBrookings(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)
    url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/'
     'silicon-valley-immortality.html"
    content = scrapeNYTimes(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)

import requests
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    
    def getPage(url):
        req = requests.get(url)
        return BeautifulSoup(req.text, 'html.parser')
    
    def scrapeNYTimes(url):
        bs = getPage(url)
        title = bs.find("h1").text
        lines = bs.find_all("p", {"class":"story-content"})
        body = '\n'.join([line.text for line in lines])
        return Content(url, title, body)
    
    def scrapeBrookings(url):
        bs = getPage(url)
        title = bs.find("h1").text
        body = bs.find("div",{"class","post-body"}).text
        return Content(url, title, body)
        
    url = 'https://www.brookings.edu/blog/future-development'
     '/2018/01/26/delivering-inclusive-urban-access-3-unc'
     'omfortable-truths/'
    content = scrapeBrookings(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)
    url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/'
     'silicon-valley-immortality.html"
    content = scrapeNYTimes(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)

import requests
from bs4 import BeautifulSoup
    class Crawler:
        def getPage(self, url):
            try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
            return BeautifulSoup(req.text, 'html.parser')
    
    def safeGet(self, pageObj, selector):
    """
     Utility function used to get a content string from a
     Beautiful Soup object and a selector. Returns an empty
     string if no object is found for the given selector
     """
    selectedElems = pageObj.select(selector)
    if selectedElems is not None and len(selectedElems) > 0:
        return '\n'.join(
         [elem.get_text() for elem in selectedElems])
        return ''
    def parse(self, site, url):
    """
     Extract content from a given page URL
     """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
        if title != '' and body != '':
            content = Content(url, title, body)
            content.print()

import requests
from bs4 import BeautifulSoup
Structuring Crawlers | 59
class Crawler:
    def getPage(self, url):
    try:
        req = requests.get(url)
    except requests.exceptions.RequestException:
        return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
    childObj = pageObj.select(selector)
    if childObj is not None and len(childObj) > 0:
        return childObj[0].get_text()
        return ""

    def search(self, topic, site):
    """
     Searches a given website for a given topic and records all pages found
     """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs["href"]
    # Check to see whether it's a relative or an absolute URL
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("Something was wrong with that page or URL. Skipping!")
            return
                title = self.safeGet(bs, site.titleTag)
                body = self.safeGet(bs, site.bodyTag)
        if title != '' and body != '':
    content = Content(topic, title, body, url)
    content.print()
    crawler = Crawler()
    siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
     'https://ssearch.oreilly.com/?q=','article.product-result',
     'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com',
     'http://www.reuters.com/search/news?blob=',
     'div.search-result-content','h3.search-result-title a',
     False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
    'div.list-content article', 'h4.title a', True, 'h1',
    60 | Chapter 4: Web Crawling Models
     'div.post-body']
    ]
    sites = []
    for row in siteData:
        sites.append(Website(row[0], row[1], row[2],
        row[3], row[4], row[5], row[6], row[7]))
        topics = ['python', 'data science']
        for topic in topics:
            print("GETTING INFO ABOUT: " + topic)
            for targetSite in sites:
                crawler.search(topic, targetSite)

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup
wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'xml')
textStrings = wordObj.find_all('w:t')
for textElem in textStrings:
    print(textElem.text)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
 for word in sentence]
    sentence = [word for word in sentence if len(word) > 1
 for (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

def cleanInput(content):
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    sentences = content.split('. ')
return [cleanSentence(sentence) for sentence in sentences]

def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
        return output
    def getNgrams(content, n):
        content = cleanInput(content)
        ngrams = []
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n))
    return(ngrams)

from urllib.request import urlopen
from random import randint
def wordListSum(wordList):
 sum = 0
 for word, value in wordList.items():
     sum += value
     return sum

def retrieveRandomWord(wordList):
 randIndex = randint(1, wordListSum(wordList))
 for word, value in wordList.items():
     randIndex -= value
     if randIndex <= 0:
         return word

def buildWordDict(text):
 # Remove newlines and quotes
 text = text.replace('\n', ' ');
 text = text.replace('"', '');
 # Make sure punctuation marks are treated as their own "words,"
 # so that they will be included in the Markov chain
 punctuation = [',','.',';',':']
 for symbol in punctuation:
     text = text.replace(symbol, ' {} '.format(symbol));
     words = text.split(' ')
     # Filter out empty words
     words = [word for word in words if word != '']
     wordDict = {}
     for i in range(1, len(words)):
         if words[i-1] not in wordDict:
         # Create a new dictionary for this word
     wordDict[words[i-1]] = {}
     if words[i] not in wordDict[words[i-1]]:
         wordDict[words[i-1]][words[i]] = 0
         wordDict[words[i-1]][words[i]] += 1
     return wordDict
    text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt')
     .read(), 'utf-8')
    wordDict = buildWordDict(text)

#Generate a Markov chain of length 100
length = 100
chain = ['I']
for i in range(0, length):
     newWord = retrieveRandomWord(wordDict[chain[-1]])
     chain.append(newWord)
 
import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
 user='', passwd='', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')
def getUrl(pageId):
     cur.execute('SELECT url FROM pages WHERE id = %s', (int(pageId)))
     return cur.fetchone()[0]
def getLinks(fromPageId):
     cur.execute('SELECT toPageId FROM links WHERE fromPageId = %s',
     (int(fromPageId)))
     if cur.rowcount == 0:
         return []
             return [x[0] for x in cur.fetchall()]
def searchBreadth(targetPageId, paths=[[1]]):
 newPaths = []
 for path in paths:
     links = getLinks(path[-1])
     for link in links:
         if link == targetPageId:
             return path + [link]
         else:
             newPaths.append(path+[link])
             return searchBreadth(targetPageId, newPaths)

nodes = getLinks(1)
targetPageId = 28624
pageIds = searchBreadth(targetPageId)
for pageId in pageIds:
 print(getUrl(pageId))
 
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
def waitForLoad(driver):
elem = driver.find_element_by_tag_name("html")
count = 0
while True:
count += 1
if count > 20:
print('Timing out after 10 seconds and returning')
return
time.sleep(.5)
try:
elem == driver.find_element_by_tag_name('html')
except StaleElementReferenceException:
return
driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
print(driver.page_source)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.PhantomJS(executable_path=
 'drivers/phantomjs/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
try:
    bodyElement = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
     (By.XPATH, '//body[contains(text(),
     "This is the page you are looking for!)]")))
    print(bodyElement.text)
except TimeoutException:
    print('Did not find the element')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).findAll('a',
    href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    #Format of revision history pages is:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title={}&action=history'
    .format(pageUrl)
    print('history url is: {}'.format(historyUrl))
    html = urlopen(historyUrl)
    bs = BeautifulSoup(html, 'html.parser')
    #finds only the links with class "mw-anonuserlink" which has IP addresses
    #instead of usernames
    ipAddresses = bs.findAll('a', {'class':'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
        return addressList
        links = getLinks('/wiki/Python_(programming_language)')
    while(len(links) > 0):
        for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs['href'])
    for historyIP in historyIPs:
        print(historyIP)
        newLink = links[random.randint(0, len(links)-1)].attrs['href']
        links = getLinks(newLink)

def getCountry(ipAddress):
    try:
        response = urlopen(
        'http://freegeoip.net/json/{}'.format(ipAddress)).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')
    
links = getLinks('/wiki/Python_(programming_language)')
while(len(links) > 0):
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
    if country is not None:
        print('{} is from {}'.format(historyIP, country))
        newLink = links[random.randint(0, len(links)-1)].attrs['href']
        links = getLinks(newLink)

import time
from urllib.request import urlretrieve
from PIL import Image
import tesseract
from selenium import webdriver

def getImageText(imageUrl):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'],
     stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())
    #Create new Selenium driver
    driver = webdriver.Chrome(executable_path='<Path to chromedriver>')
    driver.get('https://www.amazon.com/Death-Ivan-Ilyich'\
     '-Nikolayevich-Tolstoy/dp/1427027277')
    time.sleep(2)
    #Click on the book preview button
    driver.find_element_by_id('imgBlkFront').click()
    imageList = []
    #Wait for the page to load
    time.sleep(5)
    while 'pointer' in driver.find_element_by_id(
         'sitbReaderRightPageTurner').get_attribute('style'):
        # While the right arrow is available for clicking, turn through pages
        driver.find_element_by_id('sitbReaderRightPageTurner').click()
        time.sleep(2)
        # Get any new pages that have loaded (multiple pages can load at once,
        # but duplicates will not be added to a set)
        pages = driver.find_elements_by_xpath('//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print("No pages found")
        for page in pages:
            image = page.get_attribute('src')
            print('Found image: {}'.format(image))
            if image not in imageList:
                imageList.append(image)
                getImageText(image)
                driver.quit()

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps
def cleanImage(imagePath):
image = Image.open(imagePath)
image = image.point(lambda x: 0 if x<143 else 255)
borderImage = ImageOps.expand(image,border=20,fill='white')
borderImage.save(imagePath)
html = urlopen('http://www.pythonscraping.com/humans-only')
bs = BeautifulSoup(html, 'html.parser')
#Gather prepopulated form values
imageLocation = bs.find('img', {'title': 'Image CAPTCHA'})['src']
formBuildId = bs.find('input', {'name':'form_build_id'})['value']
captchaSid = bs.find('input', {'name':'captcha_sid'})['value']
captchaToken = bs.find('input', {'name':'captcha_token'})['value']
captchaUrl = 'http://pythonscraping.com'+imageLocation
urlretrieve(captchaUrl, 'captcha.jpg')
cleanImage('captcha.jpg')
p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'], stdout=
subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt', 'r')
#Clean any whitespace characters
captchaResponse = f.read().replace(' ', '').replace('\n', '')
print('Captcha solution attempt: '+captchaResponse)
if len(captchaResponse) == 5:
    params = {'captcha_token':captchaToken, 'captcha_sid':captchaSid,
    'form_id':'comment_node_page_form', 'form_build_id': formBuildId,
    'captcha_response':captchaResponse, 'name':'Ryan Mitchell',
    'subject': 'I come to seek the Grail',
    'comment_body[und][0][value]':
    '...and I am definitely not a bot'}
    r = requests.post('http://www.pythonscraping.com/comment/reply/10',
    data=params)
    responseObj = BeautifulSoup(r.text, 'html.parser')
if responseObj.find('div', {'class':'messages'}) is not None:
    print(responseObj.find('div', {'class':'messages'}).get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
class TestWikipedia(unittest.TestCase):
bs = None
def setUpClass():
    url = 'http://en.wikipedia.org/wiki/Monty_Python'
    TestWikipedia.bs = BeautifulSoup(urlopen(url), 'html.parser')
def test_titleText(self):
    pageTitle = TestWikipedia.bs.find('h1').get_text()
    self.assertEqual('Monty Python', pageTitle);
def test_contentExists(self):
    content = TestWikipedia.bs.find('div',{'id':'mw-content-text'})
    self.assertIsNotNone(content)

if __name__ == '__main__':
 unittest.main()

##########################################

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    
    return content

pdfFile = urlopen('http://pythonscraping.com/'
 'pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

pdfFile = open('../pages/warandpeace/chapter1.pdf', 'rb')

##########################################

# First you get all internat and external links, start at any page, github.com might do.


from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
#Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
internalLinks = []
#Finds all links that begin with a "/"
for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
    if link.attrs['href'] is not None:
        if link.attrs['href'] not in internalLinks:
            if(link.attrs['href'].startswith('/')):
                internalLinks.append(includeUrl+link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
    for link in bs.find_all('a',
        href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])  
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme,
            urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,
            len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)
    followExternalOnly('http://GitHub.com')

# Start at GitHub.com
# Applied cybersecurity
# What for? We must breach through all walls

# Cryptography
https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_4.pdf
# Cybersec body of knowledge
https://www.cybok.org/media/downloads/CyBOK_v1.1.0.pdf
# Practical Cybersec
https://edu.anarcho-copy.org/Against%20Security%20-%20Self%20Security/Cybersecurity_Ops_with_bash_Attack.pdf

# Our next DL starsystem is our first piece of malware.

# One mountain for cyberDataExtraction
# One mountain for AI superintelligence data processing
# One mountain for exascale execution of data extraction, Exascale superintelligence. Data mills, etc.
# These are the fouding mountains.
