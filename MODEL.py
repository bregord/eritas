import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import linear_model, datasets
from sklearn.metrics import precision_recall_fscore_support


tot = ALL.npy
print(np.shape(tot))
tot = tot.astype(np.float)
print(np.shape(tot))

X = tot[:,1:][0:1500]
Y = tot[:,0][0:1500]

X1 = tot[:,1:][1500:]
Y1 = tot[:,0][1500:]


print(np.shape(tot))

logreg = linear_model.LogisticRegression(C=1e5)

logreg.fit(X, Y)


pred_log = logreg.predict(X1)

print(np.count_nonzero(Y))
print(Y[Y==1])
print(accuracy_score(Y1,pred_log))

clf = svm.SVC()
clf.fit(X,Y)
pred = clf.predict(X1)



print(pred_log)

print("SVM")
print(accuracy_score(Y1, pred))
print(precision_recall_fscore_support(Y1, pred,pos_label=1,average='binary'))

#print(precision_recall_fscore_support(Y1, pred,))


print("LOG_REG")
print(accuracy_score(Y1,pred_log))
print(precision_recall_fscore_support(Y1, pred_log,pos_label=1,average='binary'))
