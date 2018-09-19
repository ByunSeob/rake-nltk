# -*- coding: utf-8 -*-
from rake_nltk import Rake
from konlpy.tag import Okt
twitter = Okt()

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

# If you want to provide your own set of stop words and punctuations to
# r = Rake(<list of stopwords>, <string of puntuations to ignore>)


test = '교황좌가 비어있다는 주장을 하는 전통 가톨릭 신자를 부르는 말은'

tt = twitter.phrases(test)
print(tt)
bb = list(set().union(tt))
print(bb)

r.extract_keywords_from_text(bb)
dd = r.get_ranked_phrases()

print(dd)

