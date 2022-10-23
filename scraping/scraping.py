import sys
from time import sleep

import bs4
from functools import lru_cache
import secrets
import threading
from threading import Timer
import datetime
import random
import requests
import logging
import urllib3

proxies = ['174.138.16.96:8888', '186.5.94.209:999', '143.198.40.24:8888']
useless_proxies = ['174.138.16.96:8888', '186.5.94.209:999']


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


def random_choice(lst):
    logg(info=f'started work function: {random_choice.__name__}')
    if not lst:
        logg(warning='list is empty')
    else:
        elem = random.choice(lst)
        try:
            index = lst.index(elem)
            print(f'ip address-proxy: {elem} and index him: {index}')
            proxy_ = {'https': elem}
            return proxy_, index
        except ValueError as valErr:
            logg(error=valErr)


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
        rand_proxy, index = random_choice(proxies)
        if not bool(rand_proxy):
            logg(warning=f'list is empty, from function: {req.__name__}')
            break
        try:
            response = requests.get(
                url='https://google.com',
                timeout=5,
                proxies=rand_proxy,
                verify=False
            )
            html = response.text
            file(html)
        except requests.exceptions.ConnectionError as ex:
            logg(error=ex)
            useless_proxies.append(rand_proxy['https'])
            continue
        except urllib3.exceptions.ProxyError or urllib3.exceptions.TimeoutError as ex:
            if requests.exceptions.ProxyError:
                logg(error=ex)
                useless_proxies.append(rand_proxy['https'])
                continue


def cleaning_useless_proxies(list_proxy, n):
    list_proxy.clear()
    print(f'list: was clear {n}')


def funcc():
    while True:
        list_ = [1, 2, 3, 4, 5]
        useless_list = [1, 2, 3, 4]
        try:
            elem = random.choice([x for x in list_ if x not in useless_list])
            print(elem)
            sleep(0.5)
            continue
        except IndexError as err:
            print('error with index')
            break


# while True:
#     function_cleaning = Timer(5.0, cleaning_useless_proxies, (useless_proxies, 1))
#     threads = []
#     if function_cleaning.:
#         sleep(5)
#         print('thread is running.')
#     else:
#         print('start thread.')
#         function_cleaning.start()


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


def foo():
    print ("hello")


setInterval(foo,5)

while True:
    sleep(2)
    print('hi')
