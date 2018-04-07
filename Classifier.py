from Dataset import *
import numpy as np
from sklearn import svm


def createClasses(path):
    """Create a list that contain all the Mail Class choose like positive.
    And then create another list with the other Mail Classes in the folder, choose like negative.
    Return those two lists."""

    positiveClass = [Class(path)]
    negativeClass = []

    # from the path where is the positive class, return the list of the negative classes
    path = path.split('\\')
    folder = path[len(path)-1]
    path.remove(folder)
    path = '\\'.join(path)
    files = os.listdir(path)
    files.remove(folder)

    for filename in files:
        negativeClass.append(Class(path+'\\'+filename))

    return positiveClass, negativeClass


def createVocabulary(c, typeClass):
    """Create a dictionary (count) that contain:
      - all the words in the emails of the list of Classes c
      - how many emails contain that word
     Then return a vocabulary that contain only words that appair in over
     a number of emails if the Class c is negative, otherwise return all the words in the emails.
     And return the number of emails in the Class c."""

    count = {}
    voc = {}
    n = 0

    for cl in c:
        n = n + len(cl.mail)
        for i in range(len(cl.mail)):
            found = []
            for w in cl.mail[i].text:
                if w not in found:
                    found.append(w)
                    if w in count:
                        count[w] = count[w] + 1
                    else:
                        count[w] = 1

        print cl.name, " loaded..."

    if typeClass == 0:
        for w in count:
            if count[w] > n/150:
                voc[w] = count[w]
    else:
        for w in count:
            voc[w] = count[w]

    return voc, n


def training(pos, neg):
    """Return:
        - a vocabulary with all the words in emails of positive and negative classes
        - the dictionary 'distribution' that contain for all the words of the vocabulary, the
            probability of this word in class 0 and in class 1
        - the number of emails in the positive class
        - the number of emails in the negative classes"""

    vocabulary = []
    distribution = {}

    pos, nMailPos = createVocabulary(pos, 1)
    neg, nMailNeg = createVocabulary(neg, 0)

    pDocPos = float(nMailPos) / float(nMailPos + nMailNeg)

    for w in pos:
        vocabulary.append(w)

    for w in neg:
        if w not in vocabulary:
            vocabulary.append(w)

    for w in vocabulary:
        if w in pos:
            distribution[(w, 1)] = float(1 + pos[w] * pDocPos) / float(2 + (nMailPos + nMailNeg) * pDocPos)
        else:
            distribution[(w, 1)] = float(1) / float(2 + (nMailPos + nMailNeg) * pDocPos)
        if w in neg:
            distribution[(w, 0)] = float(1 + neg[w] * (1 - pDocPos)) / float(2 + (nMailPos + nMailNeg) * (1 - pDocPos))
        else:
            distribution[(w, 0)] = float(1) / float(2 + (nMailPos + nMailNeg) * (1 - pDocPos))

    return vocabulary, distribution, nMailPos, nMailNeg


def bernoulliDocument(doc, voc):
    """Return Bernoulli Vector of a document. It consists in a list which have the dimension
     of vocabulary and 0 in the i-th element if the i-th word of the vocabulary is in the document
     and 0 if this word isn't in the document."""

    vector = []
    for w in voc:
        if w in doc:
            vector.append(1)
        else:
            vector.append(0)
    return vector


def createBernoulliMatrix(path, vocabulary):
    """Return a matrix which have in the j-th row the Bernoulli Vector of the j-th document."""

    bernoulliMatrix = []
    print "\nBernoulli Matrix creating..."
    for folder in os.listdir(path):
        directory = path + '\\' + folder + '\\'
        for file in os.listdir(directory):
            words = Mail(directory, file).text
            bernoulliMatrix.append(bernoulliDocument(words, vocabulary))

    print "Bernoulli Matrix done.\n\n"
    return bernoulliMatrix


def trainToTest(firstFolder):
    """Receive the path of the positive class in the train and return the path of the test folder."""

    firstFolder = firstFolder.split('\\')
    firstFolder.remove(firstFolder[len(firstFolder) - 1])
    folder = firstFolder.pop(len(firstFolder) - 1)
    path = '\\'.join(firstFolder)
    directory = os.listdir(path)
    directory.remove(folder)
    return path + '\\' + directory[0]


def calcolatePDC(v, bM, d, path):
    """Return the probability of a document if is in positive class and if is in negative class."""

    PDC = {}
    j = 0
    for folder in os.listdir(path):
        directory = path + '\\' + folder + '\\'
        for file in os.listdir(directory):
            pPos = 1
            pNeg = 1
            i = 0
            for w in v:
                pPos *= (bM[j][i] * d[(w, 1)]) + (1 - bM[j][i]) * (1 - d[(w, 1)])
                pNeg *= (bM[j][i] * d[(w, 0)]) + (1 - bM[j][i]) * (1 - d[(w, 0)])
                i = i + 1

                # if probability go under a certain number it can be become zero
                # for the program and we don't want this case
                if pPos < 1e-200 or pNeg < 1e-200:
                    pPos *= 1e100
                    pNeg *= 1e100

            PDC[(j, 1)] = pPos
            PDC[(j, 0)] = pNeg
            j = j + 1

    return PDC


def likelihoodClass(nMP, nMN):
    """Return the likelihood of a class."""

    pDocPos = float(nMP) / float(nMP + nMN)
    pDocNeg = float(nMN) / float(nMP + nMN)

    return pDocPos, pDocNeg


def likelihoodDocument(path, lCP, lCN, PDC):
    """Return the likelihood of a document."""

    lD = []
    i = 0
    for folder in os.listdir(path):
        directory = path + '\\' + folder + '\\'
        for file in os.listdir(directory):
            l = lCP * PDC[(i, 1)] + lCN * PDC[(i, 0)]
            lD.append(l)
            i = i + 1

    return lD


def createData(path, voc):
    """Return the data needed for the scikit learn function to
    calculate che separation hyperplane."""

    x = []
    y = []

    path = path.split('\\')
    posFolder = path.pop(len(path) - 1)
    path = '\\'.join(path)

    print "\nCalculating hyperplane..."

    for folder in os.listdir(path):
        if folder == posFolder:
            c = 1
        else:
            c = 0
        directory = path + '\\' + folder
        for file in os.listdir(directory):
            bD = bernoulliDocument(Mail(directory, file).text, voc)
            x.append(bD)
            y.append(c)

    return x, y


def hyperplane(X, Y):
    """Return the parameters of the hyperplan, calculate by scikit learn functions."""

    clf = svm.SVC(kernel='linear')
    clf.fit(X, Y)

    w = clf.coef_[0]
    b = clf.intercept_[0]

    print "Hyperplane done!!!"

    return w, b


def classifier(firstFolder):
    """Print for each folder the number of emails detected like positive and negative.
    Return a list that contain the values wanted by ROC Curve function."""

    positiveClass, negativeClass = createClasses(firstFolder)

    print "\nTraining...\n"
    vocabulary, distribution, nMailPos, nMailNeg = training(positiveClass, negativeClass)
    print "\nTRAINING DONE!!!\n"

    x, y = createData(firstFolder, vocabulary)
    w, b = hyperplane(x, y)

    normW = np.linalg.norm(w)

    path = trainToTest(firstFolder)

    lCPos, lCNeg = likelihoodClass(nMailPos, nMailNeg)
    bernoulliMatrix = createBernoulliMatrix(path, vocabulary)

    print "\nCalculating probability...\n"
    PDC = calcolatePDC(vocabulary, bernoulliMatrix, distribution, path)
    print "\nCOMPLETE!!!\n"

    lD = likelihoodDocument(path, lCPos, lCNeg, PDC)

    value = []
    i = 0
    for folder in os.listdir(path):
        pos = 0
        neg = 0
        directory = path + '\\' + folder + '\\'
        for file in os.listdir(directory):
            pDocPos = float(lCPos * PDC[(i, 1)]) / float(lD[i])
            pDocNeg = float(lCNeg * PDC[(i, 0)]) / float(lD[i])

            if pDocPos > pDocNeg:
                pos = pos + 1
                #print file, "--> Pos"
            elif pDocPos < pDocNeg:
                neg = neg + 1
                #print file, "--> Neg"
            d = float(np.dot(w, bernoulliMatrix[i]) + b) / float(normW)
            value.append(d)
            i = i + 1
        print folder + "--> Pos:", pos, " Neg:", neg

    return value
