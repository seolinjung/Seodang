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

    kkma = Kkma()

    broken_sentence = kkma.pos(sentence)
    print("broken sentence is", broken_sentence)
    new_sentence = []

    for word in broken_sentence:
        word_to_append = word[0]
        if (word[1][0] == 'N'):
            word_to_append = convert_word(word[0])
        new_sentence.append(word_to_append)
    return " ".join(new_sentence)

