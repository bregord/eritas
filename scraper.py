from bs4 import BeautifulSoup
import urllib





broken = False

content_id = '01'

while broken is not True:


    r = urllib.urlopen('http://www.theonion.com/r/'+content_id).read()
    soup = BeautifulSoup(r)

    print str(soup.title)

    if '404' in str(soup.title):
        #broken = False

        content_id = (str(int(content_id) + 1)).zfill(2)
        continue


    if int(content_id) > 60000:
        broken = True

    #if  <meta property="og:url" content="http://www.theonion.com/video/how-talk-your-child-about-death-54572" />
    #contains article, continue. else. skip

    for meta in soup.findAll("meta"):
        metaprop = meta.get('property', '').lower()


        if str(metaprop) == 'og:url':

            print "article" in str(meta.get('content','').lower())

            if "article" not in str(meta.get('content','').lower()):

                content_id = (str(int(content_id) + 1)).zfill(2)
                print content_id

                continue

            break


    #get article and headline

    #append to fileo

    content_id = (str(int(content_id) + 1)).zfill(2)

    print content_id

''' may also work
cur_vol =  '28'
cur_issue = '13'

last_vol = '40'

new_vol = False

new_issue = False

while cur_vol is not last_vol:


    r = urllib.urlopen('http://www.theonion.com/issue/'+cur_vol+cur_issue).read()
    soup = BeautifulSoup(r)

    if '404' in str(soup.title):

        print "ERROR AT VOL: " + cur_vol + " ISS: " + cur_issue

        cur_vol = (str(int(cur_vol) + 1)).zfill(2)

        cur_issue = '01'
        r = urllib.urlopen('http://www.theonion.com/issue/'+cur_vol+cur_issue).read()
        soup = BeautifulSoup(r)

        if '404' in str(soup.title):

            print("DONE")
            break



    print soup.title
    cur_issue = (str(int(cur_issue) + 1)).zfill(2)
    print "VOL:" + cur_vol
    print "ISSUE:" + cur_issue

    #get current article

    #title data-share-title
    #data-share-description

    #<div class="content-text">

    #get all article links on the page

    #

    for link in soup.find_all('article'):
        print link

'''
