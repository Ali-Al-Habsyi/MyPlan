# This is where we continue, an Omni-intelligence, 
# The most intelligent agent ever. Most know not.
# This is the way, this is the way, this is the way.
# Let us do a BFS search, most abdundantly and as extra as possible.

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
    
# Now graph-theoretic search. This, among many other places is where mathematics meets programming.
# Let us extract the most out of the above traverser.

def BFSFull(G, root):
    root = startingSite
    Qexternal = []
    Qinternal = []
    Qexternal.append(startingSite)
    Qinternal.append(startingSite)
    i = 0
    j = 0

    while len(Qexternal) is not 0:
        v = Qexternal.pop(i)
        link_batch = getExternalLinks(bs, v)
        for link in link_batch:
            Qexternal.append(link)
        i = i + 1

    # This comes very near bfs and indeed extracts the most our of getExternalLinks
    # We can do the same thing for getInternalLinks
    
    while len(Qinternal) is not 0:
        v = Qinternal.pop(i)
        link_batch = getInternalLinks(bs, v)
        for link in link_batch:
            Qinternal.append(link)
        j = j + 1
        
    # The nature of referecning is captured by external and internal linking, we restrict ourselves to external and internal linking.
    # The below line of return gives all links resulting form the above rather simple code.
    return Qexternal, Qinternal
    
# This is worth GitHub publication.