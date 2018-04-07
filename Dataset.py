import re
import os

commonWords = ['thanks', 'would', 'there', 'writes', 'about', 'article', 'which', 'anyone', 'other', 'dont', 'please',
              'email', 'using', 'could', 'these', 'because', 'cant', 'should', 'where', 'their', 'another', 'since',
              'anything', 'something', 'someone', 'really', 'going', 'while', 'thing', 'wrote', 'either', 'after',
              'those', 'looking', 'still', 'anybody', 'without', 'might', 'trying', 'everything', 'recently', 'least',
              'doesnt', 'didnt']


class Mail:
    """The class which represent the email in this program.
    It contains:
        - the number/name of the email which represent
        - the subject of the email
        - the text of email
    The subject and the text are lists of the single words in the email."""

    def __init__(self, path, file):
        self.number = file
        self.subject = []
        self.text = []

        self.readMail(path, file)

    def readMail(self, path, file):
        startText = False

        for line in open(path+'\\'+file).readlines():
            parts = line.split(' ')
            if parts[0] == 'Subject:':
                words = checkWords(line)
                words.remove('subject')
                for w in words:
                    self.subject.append(w)
                    self.text.append(w)

            if startText == False:
                if parts[0] == '\n':
                    startText = True

            else:
                parts = checkWords(line)
                for w in parts:
                    self.text.append(w)

    def foundMailAddress(self, list):
        for w in list:
            if '@' in w:
                return w
        return ''


class Class:
    """The class which represent a category of emails.
    It contains:
        - the name of the class, that's the same of the folder
        - the list of emails that are in this class/folder."""

    def __init__(self, path):
        folder = path.split('\\')
        folder = folder[len(folder)-1]
        self.name = folder
        self.mail = []

        for filename in os.listdir(path):
            self.mail.append(Mail(path, filename))


def checkWords(line):
    """Receive a list of words and return a list containing only the words
    that respect certain conditions."""

    words = []
    parts = re.sub('[^a-zA-Z0-9@ ]', '', line)
    parts = parts.lower()
    parts = parts.split(' ')
    for w in parts:
        if w is not '' and len(w) > 4 and len(w) < 15 and w not in commonWords:
        # if w is not '':
            words.append(w)

    return words
