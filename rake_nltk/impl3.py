from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
twitter = Twitter()

s = "공군통역장교가 통역을 맡는 사람엔 누가 있어"
pprint(twitter.phrases(s))



