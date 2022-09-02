import asyncio

import requests
import threading
from bs4 import BeautifulSoup



async def download(input_q, output_q, worker_id):
    while True:
        data = await input_q.get()
        url = data['url']
        log_file =url.split("/")[-1]
        print(url, log_file)
        resp = requests.get(url)
        output_q.put_nowait({"text" :resp.text,"url":url})
        input_q.task_done()


async def write_log(input_q, worker_id):
    while True:
        data = await input_q.get()
        text = data['text']
        url = data['url']
        log_file = url.split('/')[-1]
        open(log_file, 'w').write(text)
        input_q.task_done()

async def main():
    url = "http://logs.eolem.com"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = [link['href'] for link in soup.find_all('a') if link['href'][0] != "?"]

    input_q = asyncio.Queue()
    output_q = asyncio.Queue()

    downloaders = [asyncio.create_task(download(input_q, output_q, worker_id)) for worker_id in range(5)]
    writers = [asyncio.create_task(write_log(output_q, worker_id)) for worker_id in range(2)]

    for link in links:
        m = {"url" : f"{url}/{link}"}
        print("put_nowait", m)
        input_q.put_nowait(m)

    print("before input_q.join()")
    await input_q.join()
    print("input_q.join()")

    await output_q.join()
    print("output_q.join()")

    for w in downloaders:
        w.cancel()

    for w in writers:
        w.cancel()

if __name__ == '__main__':
    asyncio.run(main())        