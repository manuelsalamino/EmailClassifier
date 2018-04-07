from Classifier import *
from ROCCurve import *
import time


# first test
trainPath = 'dataset\\20news-bydate-train\\alt.atheism'
testPath = 'dataset\\20news-bydate-test\\alt.atheism'

tInit = time.time()
predictions = classifier(trainPath)
rocCurve(testPath, predictions, "First")
tFinal = time.time()
print "\nFirst test -->\ttime:", tFinal - tInit
print "########################################################################"


# second test
trainPath = 'dataset\\20news-bydate-train\\rec.motorcycles'
testPath = 'dataset\\20news-bydate-test\\rec.motorcycles'

tInit = time.time()
predictions = classifier(trainPath)
rocCurve(testPath, predictions, "Second")
tFinal = time.time()
print "\nSecond test -->\ttime:", tFinal - tInit
print "########################################################################"


# third test
trainPath = 'dataset\\20news-bydate-train\\sci.electronics'
testPath = 'dataset\\20news-bydate-test\\sci.electronics'

tInit = time.time()
predictions = classifier(trainPath)
rocCurve(testPath, predictions, "Third")
tFinal = time.time()
print "\nThird test -->\ttime:", tFinal - tInit
print "########################################################################"
