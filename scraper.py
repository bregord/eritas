from bs4 import BeautifulSoup
import urllib.request
import csv


broken = False

content_id = '01'

import time

FILENAME = "corpus_" + str(time.time()) + ".csv"

to_write = []
count = 0


with open(FILENAME, 'wb') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=",")

    wr.writerow(["title", "subheader", "article"])

while broken is not True:

    try:

        r = urllib.request.urlopen('http://www.theonion.com/r/'+content_id).read()
        soup = BeautifulSoup(r)

        print (str(soup.title))

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

                #print "article" in str(meta.get('content','').lower())

                if "article" not in str(meta.get('content','').lower()):

                    content_id = (str(int(content_id) + 1)).zfill(2)
                    #print content_id

                    continue

                break


        for header in soup.findAll("header", class_="content-header"):
            print (header.getText())

            header = header.getText().replace("\n","")

        for content in soup.findAll("div", class_="content-text"):

            #print content.getText()
            text = content.getText().replace("\n"," ")
            sentences = text.split(".")



            subhead = sentences[0]

            article = "".join(sentences[1:])
            print (article)
            #p = content.findAll("p").getText()


        #append to csv file
        #get article and headline

        #append to fileo

        row = [header, subhead, article]

        to_write.append(row)

        if count < 10:

            count +=1


        if count >= 10:


            count = 0

            print ("adding to csv")
            with open(FILENAME, 'ab') as f:
                #wr = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar="|",dialect='excel', delimiter=",")

                #wr.writerows(to_write)
                for el in to_write:
                    f.write("|"+el[0]+"|,|"+el[1]+"|,|"+el[2]+"|\n")

            to_write = []



        content_id = (str(int(content_id) + 1)).zfill(2)

        print (content_id)

    except HTTPError:

        content_id = (str(int(content_id) + 1)).zfill(2)
        pass
