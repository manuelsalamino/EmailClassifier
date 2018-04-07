from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import os


def calcolateActual(path):
    """Return a list with 0 in position i in i-th email is the class choose like positive and
    0 if it's in a negative class.
    'path' contain the path of the positive class."""

    value = []

    path = path.split('\\')
    folder = path.pop(len(path) - 1)
    path = '\\'.join(path)

    for f in os.listdir(path):
        if f == folder:
            for i in os.listdir(path + '//' + f):
                value.append(1)
        else:
            for i in os.listdir(path + '//' + f):
                value.append(0)

    return value


def rocCurve(path, predictions, nTest):
    """Receive:
        - the path of the positive class to calculate the actual values of the emails (0 or 1)
        - the predictions of this value
        - the number of the test, it need only to write on the plot which number of test is it"""

    actual = calcolateActual(path)

    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)

    plt.title('ROC Curve: ' + nTest + 'Test')
    plt.plot(false_positive_rate, true_positive_rate, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.2])
    plt.ylim([-0.1, 1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
