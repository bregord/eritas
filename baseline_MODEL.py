import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import linear_model, datasets
from sklearn.metrics import precision_recall_fscore_support

print("BASELINE")
print("========")

'''
p = np.load("BASELINE.npy")
p2 = np.load("BASELINE2.npy")
p3 = np.load("BASELINE3.npy")

total = np.vstack((p,p2))
total = np.vstack((total,p3))
'''

total = np.load("BASELINE_TOTAL.npy")
total = total.astype('float')

print(np.shape(total))

test_cutoff = int(0.2*np.shape(total)[0])
valid_cutoff = test_cutoff*2

test = total[0:test_cutoff]
valid = total[test_cutoff:valid_cutoff]
train = total[valid_cutoff:]

Y = train[:,0]
X = train[:,1:]

Y = Y.astype('int')

X1 = test[:,1:]
Y1 = test[:,0]


Y1 = Y1.astype('int')

clf = svm.SVC()
clf.fit(X1,Y1)

pred = clf.predict(X1)
logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

pred_log = logreg.predict(X1)



print(pred_log)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

#print(precision_recall_fscore_support(Y1, pred,))


print("LOG_REG")
print(accuracy_score(Y1,pred_log))

print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))
