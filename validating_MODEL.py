import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import linear_model, datasets
from sklearn.metrics import precision_recall_fscore_support

print("VALIDATING ALL TESTS")
print("========")

'''
p = np.load("BASELINE.npy")
p2 = np.load("BASELINE2.npy")
p3 = np.load("BASELINE3.npy")

total = np.vstack((p,p2))
total = np.vstack((total,p3))
'''

print("TESTING ALL")

total = np.load("BASELINE_TOTAL.npy")
total = total.astype('float')



print(np.shape(total))

test_cutoff = int(0.2*np.shape(total)[0])
valid_cutoff = test_cutoff*2

test = total[0:test_cutoff]
valid = total[test_cutoff:valid_cutoff]
train = total[valid_cutoff:]



Y = train[:,0]
Y1 = valid[:,0]
Y = Y.astype('int')
Y1 = Y1.astype('int')


print("Alliteration")
print("======")
X1 = valid[:,2]
X = train[:,2]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Hyperbole")
print("======")
X1 = valid[:,3]
X = train[:,3]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Inversion")
print("======")
X1 = valid[:,4]
X = train[:,4]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Onom")
print("======")
X1 = valid[:,5]
X = train[:,5]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Flip")
print("======")
X1 = valid[:,6]
X = train[:,6]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Repeated")
print("======")
X1 = valid[:,7]
X = train[:,7]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Polysemy")
print("======")
X1 = valid[:,8]
X = train[:8]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("POS tags")
print("======")
X1 = valid[:,9:44]
X = train[:,9:44]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))


print("Profanity")
print("======")
X1 = valid[:,45]
X = train[:,45]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("Sem_valid")
print("======")
X1 = valid[:,46]
X = train[:,46]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))

print("sent_counts")
print("======")
line.append(sem_valid(rs)) #- use rs

print("======")
X1 = valid[:,47:]
X = train[:,47:]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))


print("ALL")
print("=======")

X1 = valid[:,1:]
X = train[:,1:]

clf = svm.SVC()
clf.fit(X,Y)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))
