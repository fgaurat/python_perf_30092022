import httpx
from bs4 import BeautifulSoup
from glob import glob
from pprint import pprint
import re

def main():
    logs = glob('*.log')
    for log in logs:
        with open(log) as f:

            for line in f:                
                line = line.strip()
                # result = re.findall(r"^((\d{1,3}\.){3}\d{1,3})", line)
                # result = re.findall(r"^(?:\d{1,3}\.?){4}", line)
                result = re.findall(r"^(.+?)\s", line)

                print(result)


def main01():
    url = "http://logs.eolem.com/"
    resp = httpx.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = [link['href'] for link in soup.find_all('a') if link['href'][0]!="?"]
    print(links)

    for link in links:
        log_url = f"{url}{link}"
        print(log_url)
        resp = httpx.get(log_url)
        open(link,'w').write(resp.text)



if __name__ == '__main__':
    main()



