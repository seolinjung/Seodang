import os
import requests
import krdict
import urllib.request
import json

# from bs4 import BeautifulSoup

from django.conf import settings

from konlpy.tag import Kkma
from konlpy.utils import pprint

def convert_word(word):
    
    krdict.set_key(settings.API_KEY)
    response = krdict.search(
        query=word,
        raise_api_errors=False
    )

    try:
        return response.asdict()["data"]["results"][0]["origin"]
    except Exception as e:
        return word
    
def convert_sentence(sentence):
    
    


if __name__=="__main__":
    
    '''
    krdict.set_key('A9BEAD2EC65F7830E89AFB1DC81D7E21')
    response = krdict.search(
        query='행복',
        raise_api_errors=True
        # search_target='original_language',
        # target_language='chinese'
        # origin_type='hanja'
    )
    '''

    kkma = Kkma()

    # pprint(response.asdict()["data"]["results"][0]["origin"])
    pprint(kkma.pos('오늘 날씨가 굉장히 좋다는 생각이 드네요.'))

    # print(json.dumps(response.asdict(), indent=2, ensure_ascii=False))