'''prepprocess

stopwords removed, tokenize unigrams and bigrams
training and test converted to tf-idf - BNS too?

separate headline and article features?


burfoot and baldwin
use binary features

1. binary feature detecting profanity

1. slang/informality measure

semantic validity - stanford named entity recognizer


IIIT
NRC and SENTICNet emotion lexicon for sentiments
count the number of positives and negatives
Speech acts
number of scores for each sense from sensicon

flips of sentiment, start out positive go negative or vice versa

hyperbole - three positive or negative words in a row

imagery

onomotopaeia


kings
absurdity - uses named entity recognizer and nltk
'''

#features
#remove stopwords. tokenize unigrams and bigrams
#tf-idf? BNS too?

'''
binary features:
#	profanity
#

continuous:
#	slang - number of words marked as informal / total number of words -> use wikitionary?
# of positive, negative and neutral words
# amount of polysemy -> average polysemy
#onomotopaeia
#

#SEMANTIC VALIDITY MAY BE HARD TO DO



MY OWN:
#mundanity?o



#THINGS I CAN DO WITH FULL ARTICLES
Absurdity
Humour
sentiment amplifiers like punctuation




#IDEA: Supplment with Not The Onion

'''

#for each line, read into memory, preprocess, and then write to file

#if I can get this done by 11, that's good.
import csv

from bs4 import BeautifulSoup
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import ner
import requests
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.stem import WordNetLemmatizer
import math

from nltk.tokenize import word_tokenize


#tagger = ner.HttpNER(host='localhost', port=8080)
sid = SentimentIntensityAnalyzer()

stoplist = set(stopwords.words('english'))
POS=["CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNS","NNP","NNPS","PDT","POS","PRP","PRP","RB","RBR","RBS","RP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT","WP","WP$","WRB"]



with open('swearWords.csv', 'r') as f:
    reader = csv.reader(f)
    profanity_list= list(reader)

with open('ono.csv', 'r') as f:
    reader = csv.reader(f)
    onom_list= list(reader)


#with open('REAL_CORPUS.csv', 'r') as f:
with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)[0:3000]

    sentences = []
    raw_sentences = []
    classes = []
    for el in lines:

        if len(el) <= 1:
            continue
        cl = el[-1]
        if cl is not "0":
            if cl is not "1":
                continue

        rest = el[0:len(el)-1]
        rest = " ".join(rest)

        print(rest)
        print(cl)
        print(type(rest))
        print(type(cl))

        #raw_sentences.append(el[0].lower().split())

        #sentences.append([i for i in el[0].lower().split() if i not in stoplist])
        raw_sentences.append(rest)
        #raw_sentences.append(rest.lower().split())
        sentences.append([i for i in word_tokenize(rest.lower()) if i not in stoplist])
        if(len(el)>=2):
            classes.append(cl)
        else:
            classes.append(0)

    #remove stop words

#remove stop words

def sent_counts(words):

    polarity_counts = {}
    polarity_counts['pos'] = 0
    polarity_counts['neg'] = 0
    polarity_counts['neu'] = 0

    for word in words:
        res = sid.polarity_scores(word)
        if res['neg'] > 0:
           polarity_counts['neg'] +=1

        if res['pos'] > 0:
           polarity_counts['pos'] +=1

        if res['neu'] > 0:
           polarity_counts['neu'] +=1

    return polarity_counts


def hyperbole(words):
    #3 positive words or 3 negative in a row
    streak = 0
    hyp_count = 0

    b = []
    for word in words:
        b.append(list(sid.polarity_scores(word).values()))
        #neu is 0, neg is 2, pos 3]

    b = np.asarray(b)

    for row in range(3,np.shape(b)[0]):
        #look for a sequence of 3 positive or 3 negative

        pos = np.sum(b[row-3:row][:,3])
        neg = np.sum(b[row-3:row][:,2])


        if neg < -2 or pos > 2:
            hyp_count +=1

    return hyp_count

def alliteration(words):
    allit = 0
    for word in range(0, len(words) - 1):

        if words[word][0] == words[word+1][0]:
            allit+=1

    return allit

def senses(words):
    return

def imagery(words):

    return

def pos_tags(words):

    tags = [i[1] for i in nltk.pos_tag(words)]
    tag_counts = [0]*len(POS)
    for el in tags:
        if(el in POS):
            tag_counts[POS.index(el)] +=1

    return tag_counts

def sem_valid(words):
    #get named entities

    tags = [i[1] for i in nltk.pos_tag(words)]

    indices = [i for i, x in enumerate(tags) if "NN" in x]
    entities = [words[i] for i in indices]

    #entities = tagger.get_entities(" ".join(words))
    #entities = list(entities.values())


    search = "https://www.google.dz/search?q="+"+".join(entities)

    page = requests.get(search)
    soup = BeautifulSoup(page.content)

    elements = soup.findAll("h3")

    if len(elements) == 0:
        return 0
    valid = 0


    num_el = len(elements)
    for el in elements:

        if(el.find("a") is None):
            return 0

        sent =  "".join(str( el.find("a").contents)).lower()
        ent_cnt = 0
        for ent in entities:
            if ent in sent:
                ent_cnt +=1

        if ent_cnt == len(entities):
            valid +=1


    return float(valid)/num_el


def inversion(words):

    '''Adjective after Noun- e.g: soldier strong
    Verb before subject- e.g: Shouts the policeman
    Noun before Proposition- e.g: worlds between
    '''
    tags = [i[1] for i in nltk.pos_tag(words)]

    inv_count = 0

    if("NN" in tags and "JJ" in tags):
        if tags.index("NN") < tags.index("JJ") :
            inv_count += 1

    if "VB" in tags and "NN" in tags:
        if tags.index("VB") < tags.index("NN"):
            inv_count +=1

    return inv_count

def profanity(words):
    for word in words:
        if word in profanity_list:
            return 1

    return 0

def onom(words):
    for word in words:
        if word in onom_list:
            return 1

    return 0


#polysemy

def polysemy(words):
    # number of polysemous words
    avg_ambig= 0
    for word in words:
        avg_ambig += len(wn.synsets(word))

    return float(avg_ambig)/len(words)


def slang(words):
    #<div id="catlinks" class="catlinks" data-mw="interfac

    slang_cnt = 0
    for word in words:
        search = "https://en.wiktionary.org/wiki/"+word
        page = requests.get(search)
        soup = BeautifulSoup(page.content)

    return

def punc(words):

    punct = 0

    punct+= words.count("!")
    punct+= words.count("?")
    punct+= words.count("...")

    return punct

def parse_ambig(raw_sentence):

    return


def repeated(words):

    arr = np.asarray(words)
    num = len(np.unique(arr))

    return len(words) - num

#see if there is a marked difference in polarity
def flip(words):

    flip = 0
    b = []
    for word in words:
        print(word)
        pole_score = sid.polarity_scores(word)
        b.append(list(pole_score.values()))

        print(pole_score.values())
        print(pole_score)
        #neu is 0, neg is 2, pos 3]

    b = np.asarray(b)
    if len(b) <= 2:
        return 0
    b = b[:,1:]
    length = np.shape(b)[0]
    mid = math.ceil(length/2)

    neg_to_pos = -np.sum(b[:,0][0:mid]) + np.sum(b[:,1][mid-1:length])
    pos_to_neg = np.sum(b[:,1][0:mid]) - np.sum(b[:,0][mid-1:length])

    print(neg_to_pos)
    print(pos_to_neg)

    if pos_to_neg < 0.1 and pos_to_neg > -0.1:
        return 1
    if neg_to_pos < 0.1 and neg_to_pos > -0.1:
        return -1
    else:
        return flip


if __name__=='__main__':

    '''
    print (np.asarray(raw_sentences))
    np.save("raw_sentences",np.asarray(raw_sentences))

    feat_vector = TfidfVectorizer( stop_words='english', strip_accents='unicode', ngram_range=(1, 2), analyzer='word', max_features=100, min_df=1)

    x = feat_vector.fit_transform(np.load("raw_sentences.npy"))

    print(x.toarray())
    '''
    feature_array = []
    for el in range(0, len(sentences)):
        s = sentences[el]
        rs = raw_sentences[el]

        line = []

        line.append(alliteration(s))
        line.append(hyperbole(s))
        #imagery'
        line.append(inversion(s))
        line.append(onom(s))
        line.append(flip(s))
        line.append(repeated(s))
        line.append(polysemy(s))
        line+=pos_tags(s)
        line.append(profanity(s))
        line.append(sem_valid(rs)) #- use rs
        #senses',
        line+=list(sent_counts(s).values())
        #slang',

        #print(sentences[el])
        #print(line)
        print(str(el) + " out of " + str(len(sentences)))
        feature_array.append(line)

    #write raw_sentences
    #read in as count vectorizer


    feats = np.asarray(feature_array)
    classes = np.asarray(classes)

   # print(np.shape(x))
   # print(classes)
   # print(feats)
   # print(np.shape(feats))
   # print(np.shape(classes))
    final = np.column_stack((classes,feats))
    #final = np.concatenate((final,x))

    #final = np.column_stack((classes,x.toarray()))
    #np.save("raw_sentences",np.asarray(raw_sentences))
    np.save("All_features", final)
    #print(final)

