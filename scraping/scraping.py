import datetime
import random
import sys
import bs4
import requests
import logging

proxies = ['174.138.16.96:8888', '186.5.94.209:999', '143.198.40.24:8888']

raw_urls = []


def logg(**kwargs):
    mode = 'a'
    file_p = 'logg_scraping.log'
    level_debug = logging.DEBUG
    logging.basicConfig(filename=file_p, filemode=mode, level=level_debug)
    log_ = logging.getLogger('scraping-logger')
    for key, value in kwargs.items():
        match key:
            case 'info':
                log_.info(f'{value} date: {datetime.datetime.now()}')
            case 'error':
                log_.error(f'{value} date: {datetime.datetime.now()}')
            case 'warning':
                log_.warning(f'{value} date: {datetime.datetime.now()}')
            case 'debug':
                log_.debug(f'{value} date: {datetime.datetime.now()}')


def random_choice(lst) -> dict:
    logg(info=f'started work function: {random_choice.__name__}')
    elem = random.choice(lst)
    print(f'ip address-proxy: {elem}')
    proxy_ = {'https': elem}
    return proxy_


def svg():
    pass


def file(file_, format_: str = None):
    try:
        # with open('file.html' + f'*.{format_}', 'w', encoding='utf-8') as f:
        with open('file.html', 'w', encoding='utf-8') as f:
            f.write(file_)
        return True
    except Exception as ex:
        logg(error=ex)
        return False


def beauty_s():
    pass


def req():
    while True:
        try:
            response = requests.get(
                url='https://google.com',
                timeout=5,
                proxies=random_choice(proxies),
                verify=False
            )
            html = response.text
            file(html)
        except Exception as ex:
            logg(error=ex)


req()
