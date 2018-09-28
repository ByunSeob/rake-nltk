from rake_nltk.utils.commonPandas import PandasHandler

from rake_nltk import Rake
from konlpy.tag import Okt
twitter = Okt()

r = Rake()




def test_acc():

    questions = []
    extracts = []
    total_cnt = 0

    pandas_handler = PandasHandler()
    data_list = pandas_handler.read_xlsx('test.xlsx', ['question'], usecols="A")

    for data in data_list:
        total_cnt += 1

        question = data['question']
        phrases = twitter.phrases(question)
        no_dup_phrases = list(set().union(phrases))
        r.extract_keywords_from_text(no_dup_phrases)
        extract = r.get_ranked_phrases()

        try:
            extracts.append(extract[0])
            questions.append(question)
        except:
            pass

        if total_cnt % 100 == 0:
            print(total_cnt)

    dic = {'질문': questions, '추출키워드': extracts}

    pandas_handler.write_xlsx('extractor_top2', dic)


test_acc()