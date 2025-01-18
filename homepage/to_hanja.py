import os
import requests
import krdict
import urllib.request
import json
import hanja

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

    kkma = Kkma()

    broken_sentence = kkma.pos(sentence)
    list_sentence = list(sentence)

    for hangul_word in broken_sentence:
        if (hangul_word[1][0] == 'N'):
            converted_word = convert_word(hangul_word[0])
            if hanja.is_hanja(converted_word[0]) == True:
                start_id = sentence.index(hangul_word[0])
                end_id = start_id - 1 + len(hangul_word[0])
                list_sentence[start_id:end_id+1] = converted_word

    return "".join(list_sentence)

