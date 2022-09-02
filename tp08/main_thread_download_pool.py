import httpx
import threading
from bs4 import BeautifulSoup
from  multiprocessing.pool import ThreadPool


def download(url):
    print(threading.current_thread().name)
    log_file = url.split("/")[-1]
    print(url,log_file)
    resp = httpx.get(url)
    open(log_file,'w').write(resp.text)


def main():
    url = "http://logs.eolem.com"
    resp = httpx.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = [link['href'] for link in soup.find_all('a') if link['href'][0]!="?"]
    print(links)

    with ThreadPool(10) as p:
        p.map(download, [f"{url}/{link}" for link in links])


if __name__ == '__main__':
    main()
