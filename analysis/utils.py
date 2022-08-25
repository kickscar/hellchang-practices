import ssl
import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(url='', encoding='utf-8', err=lambda e: print(f'{e} : {datetime.now()}', file=sys.stderr)):
    try:
        req = Request(url)
        ssl._create_default_https_context = ssl._create_unverified_context

        resp = urlopen(req)
        recv = resp.read().decode(encoding, errors='replace')

        print(f'{datetime.now()}: success for request [{url}]')
        return recv
    except Exception as e:
        err(e)


def strsclean(strs, *funcs):
    res = []
    for s in strs:
        for func in funcs:
            s = func(s)
        res.append(s)
    return res


def filters(data, *procs):
    res = data
    for proc in procs:
        res = proc(res)
    return res



