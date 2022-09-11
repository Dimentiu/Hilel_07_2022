import asyncio
from time import sleep

async def get_primes_amount(num):
    result = 0
    for i in range (2, num +1):
        counter = 0
        for j in range(2, i):
            if i % j == 0:
                counter += 1
        if counter == 1:
            result += 1

            await asyncio.sleep(0)
    
    print(result)
    return result

async def main():
    numbers = [40000, 400, 1000000, 700]
    for i in numbers:
        print(i)
        await asyncio.gather(get_primes_amount(i))
  

asyncio.run(main())






