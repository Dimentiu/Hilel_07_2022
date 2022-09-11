# Client == function -- corutine
# Manager == event_loop


import asyncio
from time import sleep


async def client1():
    print("Client 1 making his order...")
    print("Cooking for client 1...")
    await asyncio.sleep(1)

    print("Client 1 taking his order!")


async def client2():
    print("Client 2 making his order...")

    print("Cooking for client 2...")
    await asyncio.sleep(0)

    print("Client 2 taking his order!")


async def client3():
    print("Client 3 making his order...")

    print("Cooking for client 3...")
    await asyncio.sleep(0)

    print("Client 3 taking his order!")


async def manager():
    # NOTE: Will run sync
    # await client1()
    # await client2()

    # NOTE: Run async
    await asyncio.gather(client1(), client2(), client3())


if __name__ == "__main__":
    asyncio.run(manager())

# def manager():
#     tasks = [client1(), client2()]

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.gather(*tasks))
#     loop.close()