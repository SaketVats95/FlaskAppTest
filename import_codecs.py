import codecs
from collections import Counter
wordDict = Counter()

with codecs.open('./data/file1.txt','r',encoding='cp720') as f:
    for line in f:
        #wordDict.update(line.strip().split())
        print(line)
        

for word, count in wordDict.most_common(): 
    print(word)