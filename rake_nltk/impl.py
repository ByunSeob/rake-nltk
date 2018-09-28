# -*- coding: utf-8 -*-
from rake_nltk import Rake
from konlpy.tag import Okt
twitter = Okt()

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

# If you want to provide your own set of stop words and punctuations to
# r = Rake(<list of stopwords>, <string of puntuations to ignore>)


test = 'If you want to provide your own set of stop words and punctuations to'
test = '피겨선수 김보름의 개인최고기록은 어떤 대회지'

tt = twitter.phrases(test)
print(tt)


r.extract_keywords_from_text(tt)
dd = r.get_ranked_phrases()

print(dd)

