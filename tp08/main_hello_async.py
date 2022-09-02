import asyncio
import time

async def add(a,b):
    await asyncio.sleep(0.5)
    return a+b

async def main():
    print('Hello ...')
    # await asyncio.sleep(1)
    print('... World!')
    c = await add(2,5)
    # print(c)
    # c = await add(2,5)
    # print(c)
    r = await asyncio.gather(add(1,2),add(4,2),add(1,5),add(1,20))
    print(r)


if __name__ == '__main__':
    asyncio.run(main())