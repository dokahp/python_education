import requests
from bs4 import BeautifulSoup
import sys

languages = {1: 'arabic', 2: 'german', 3: 'english', 4: 'spanish', 5: 'french', 6: 'hebrew', 7: 'japanese',
             8: 'dutch', 9: 'polish', 10: 'portuguese', 11: 'romanian', 12: 'russian', 13: 'turkish'}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8'
           }
file = open('hello.txt', 'w', encoding='utf-8')

def get_html(url, params=''):
    s = requests.Session()
    return s.get(url, headers=HEADERS, params=params)


def get_content(html, trans_lang, number_of_items):
    soup = BeautifulSoup(html, 'html.parser')
    translated_words = soup.find_all('a', {'class': 'translation'})
    translated_words = translated_words[1:]
    words = []
    for word in translated_words:
        words.append(word.get_text().strip())
    eng_sentence = soup.find_all('div', class_='src')
    fr_sentence = soup.find_all('div', class_='trg')
    eng_list = [word.get_text().strip() for word in eng_sentence if word != '']
    fr_list = [word.get_text().strip() for word in fr_sentence if word != '']
    for error in eng_list:
        if error == '':
            eng_list.remove(error)
    for error in fr_list:
        if error == '':
            fr_list.remove(error)
    if len(eng_sentence) != 0 and len(fr_sentence) != 0:
        print(f'\n{trans_lang.title()} Translations:')
    file.write('{trans_lang} Translations:\n'.format(trans_lang=trans_lang.title()))
    print(*words[0:number_of_items], sep='\n')
    file.write('{x}\n'.format(x=words[0]))

    print(f'\n{trans_lang.title()} Examples:')
    file.write(f'\n{trans_lang.title()} Examples:\n')
    for i in range(number_of_items):
        print(eng_list[i] + ':' + '\n' + fr_list[i] + '\n')
        file.write(f"{eng_list[i]}:\n{fr_list[i]}\n\n")


def all_languages(your_lang, word):
    for key, value in languages.items():
        if value != your_lang:
            URL = f'https://context.reverso.net/translation/{your_language}-{value}/{word}'
            html = get_html(URL)
            get_content(html.text, languages[key], 1)


argv = sys.argv
your_language = argv[1]
trans_lang = argv[2]
word = argv[3]
check_con = requests.get('https://context.reverso.net', headers=HEADERS)
if check_con.status_code == 200:
    if your_language in languages.values():
        if trans_lang in languages.values() or trans_lang == 'all':
            if trans_lang != 'all':
                URL = f'https://context.reverso.net/translation/{your_language}-{trans_lang}/{word}'
                html = get_html(URL)
                try:
                    get_content(html.text, trans_lang, 5)
                except IndexError:
                    print(f'Sorry, unable to find {word}')
            else:
                try:
                    all_languages(your_language, word)
                except IndexError:
                    print(f'Sorry, unable to find {word}')
        else:
            print(f"Sorry, the program doesn't support {trans_lang}")
    else:
        print(f"Sorry, the program doesn't support {your_language}")
else:
    print('Something wrong with your internet connection')
file.close()
