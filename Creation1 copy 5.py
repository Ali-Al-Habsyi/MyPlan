# The following downloads all files from all links that connect externally to some source link.
# One task to follow lies in the integration of BFS in link-dicovery.

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from pathlib import Path

# website_downloader.py
# Safe, respectful, and LEGAL web mirror tool
# Use ONLY on sites you own or have written permission for

import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time
import hashlib

SPREAD_COUNT = 1000
OUTPUT_FOLDER = "/Users/ali/Downloads"

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

# CONFIGURE THESE BEFORE RUNNING
TARGET_URL = "https://files.example.com/public/"   # CHANGE THIS
OUTPUT_FOLDER = "downloaded_site"                  # Local save folder
DELAY_BETWEEN_REQUESTS = 1.0                       # Be nice to servers
USER_AGENT = "WebsiteMirrorBot/1.0 (+your-email@example.com)"  # REQUIRED

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Session for connection reuse
session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_files(base_url):
    to_download = set()
    visited = set()
    queue = [base_url]

    print(f"Starting crawl of {base_url}")

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue

        try:
            response = session.get(url, timeout=10)
            visited.add(url)

            if response.status_code != 200:
                print(f"Failed {response.status_code}: {url}")
                continue

            # Detect content type
            content_type = response.headers.get('Content-Type', '')
            
            # If it's a file (not HTML), download immediately
            if not content_type.startswith('text/html'):
                to_download.add(url)
                print(f"Found file: {url}")
                continue

            # Parse HTML for links
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all(['a', 'img', 'link', 'script']):
                href = link.get('href') or link.get('src')
                if href:
                    absolute = urljoin(url, href)
                    if is_valid(absolute) and absolute.startswith(base_url):
                        if absolute not in visited:
                            queue.append(absolute)

            print(f"Crawled: {url} ({len(queue)} in queue)")

        except Exception as e:
            print(f"Error crawling {url}: {e}")

        time.sleep(DELAY_BETWEEN_REQUESTS)

    return to_download

def download_file(url, folder):
    try:
        local_path = os.path.join(folder, urlparse(url).path.lstrip('/'))
        local_dir = os.path.dirname(local_path)
        os.makedirs(local_dir, exist_ok=True)

        if os.path.exists(local_path):
            print(f"Already exists: {local_path}")
            return

        print(f"Downloading: {url}")
        r = session.get(url, stream=True, timeout=30)
        r.raise_for_status()

        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Saved: {local_path}")

    except Exception as e:
        print(f"Failed to download {url}: {e}")

# MAIN
if __name__ == "__main__":
    print("Website File Downloader (Ethical Use Only)")
    print("Make sure you have permission!\n")

    batch_of_links = followExternalOnly('https://en.wikipedia.org/wiki/Ronin_(Marvel_Comics)')
    OUTPUT_FOLDER = OUTPUT_FOLDER # SET EQUAL TO DOWNLOAD FOLDER
    
    while spread_count < SPREAD_COUNT:
        
        new_batch_of_links = followExternalOnly(batch_of_links[-1])
        for link in new_batch_of_links:
            if is_valid(link):
                to_download = get_all_files(link)
                for downloadable in to_download:
                    download_file(downloadable, OUTPUT_FOLDER)
            else:
                continue
            
        batch_of_links = new_batch_of_links
            