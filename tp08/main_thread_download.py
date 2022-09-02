import httpx
import threading
from bs4 import BeautifulSoup

def download(url):
    log_file = url.split("/")[-1]
    print(url,log_file)
    resp = httpx.get(url)
    open(log_file,'w').write(resp.text)


def main():
    url = "http://logs.eolem.com/"
    resp = httpx.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = [link['href'] for link in soup.find_all('a') if link['href'][0]!="?"]
    print(links)

    for link in links:
        log_url = f"{url}{link}"
        threading.Thread(target=download,args=[log_url]).start()



if __name__ == '__main__':
    main()
