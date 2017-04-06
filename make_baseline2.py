import csv
import gc
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


#tagger = ner.HttpNER(host='localhost', port=8080)
stoplist = set(stopwords.words('english'))


#with open('REAL_CORPUS.csv', 'r') as f:
with open('../../CORPUS.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    lines = list(reader)

    sentences = []
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

        #raw_sentences.append(el[0].lower().split())
        #sentences.append([i for i in el[0].lower().split() if i not in stoplist])
        #raw_sentences.append(rest.lower().split())
        #sentences.append([i for i in word_tokenize(rest.lower()) if i not in stoplist])

        sentences.append(rest)
        #sentences.append([i for i in word_tokenize(rest) if i not in stoplist])
        if(len(el)>=2):
            classes.append(cl)
        else:
            classes.append(0)



feat_vector = TfidfVectorizer( stop_words='english', strip_accents='unicode', ngram_range=(1, 2), analyzer='word', tokenizer=word_tokenize, max_features=100, min_df=2)

feature_array =[]
cla = []
notch = 1000
for el in range(0, len(sentences)):

    if el % notch == 0 and el is not 0:

        x = feat_vector.fit_transform(feature_array)

        np.save("baseline_part_" + str(el), np.column_stack((np.asarray(cla),x.toarray())))

        feature_array = []
        cla = []
        gc.collect()


    s = sentences[el]
    if(len(s) == 0):
        print("skipped")
        continue
    cla.append(classes[el])
    feature_array.append(s)

   # np.save("SENTENCES",np.asarray(sentences))


   # x = feat_vector.fit_transform(np.load("SENTENCES.npy"))

x = feat_vector.fit_transform(feature_array)

np.save("baseline" + str(el + 1), np.column_stack((np.asarray(cla),x.toarray())))

