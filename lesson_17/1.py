import asyncio
from random import randint, random
from threading import Thread
from time import sleep


def get_random_delay():
    """
    Just return radom value from 0 to 2.
    Represents seconds of delay.
    """
    return random() * randint(1, 2)


def get_random_countdown():
    """Just return integer in range 1 <= N <= 5."""
    return randint(3, 5)


class BaseRocket:
    """Base rocket class. use only for inheritance."""

    def __init__(self, name) -> None:
        self.delay = get_random_delay()
        self.countdown = get_random_countdown()
        self.name = name


class AsyncRocket(BaseRocket):
    """
    This class is responsible for running async rockets.
    Every rocket has its own delay and countdown.
    """

    async def _countdown(self):
        """Human-base countdown."""

        for i in range(self.countdown + 1, 0, -1):
            # print(f"{i}...")
            await asyncio.sleep(1)

    async def _delay(self):
        # print(f"🕐 Delay for {self.delay} seconds...")
        await asyncio.sleep(self.delay)

    async def run(self):
        # Do the countdown before start the rocket
        # print(f"\nPrepare the {self.name} ✅")
        await self._countdown()

        # Check the delay
        await self._delay()

        # Show success message
        # print(f"🚀 Rocket {self.name} go to the moon...")


class Rocket(BaseRocket):
    """
    This class is responsible for running rockets.
    Every rocket has its own delay and countdown.
    """

    def _countdown(self):
        """Human-base countdown."""

        for i in range(self.countdown + 1, 0, -1):
            # print(f"{i}...")
            sleep(1)

    def _delay(self):
        # print(f"🕐 Delay for {self.delay} seconds...")
        sleep(self.delay)

    def run(self):
        # Do the countdown before start the rocket
        # print(f"\nPrepare the {self.name} ✅")
        self._countdown()

        # Check the delay
        self._delay()

        # Show success message
        # print("🚀 Rocket go to the moon...")


def run_sync_one_thread(rockets):
    for rocket in rockets:
        rocket.run()


def run_in_threads(rockets):
    threads = [Thread(target=rocket.run) for rocket in rockets]

    for thread in threads:
        thread.start()


async def run_async(rockets):
    # NOTE: Will run sync
    # for rocket in rockets:
    #     await rocket.async_run()

    # Gather realization
    tasks = [rocket.run() for rocket in rockets]
    await asyncio.gather(*tasks)


# NOTE: Get 100_000 rockets.
#       Run in 1000 threads
#       Each thread runs rockets asynchronously
def run_super(rockets):
    pass


def main():
    # rockets = [Rocket(name=f"Rocket {i}") for i in range(1, 100_000)]
    # async_rockets = (AsyncRocket(name=f"Rocket {i}") for i in range(1, 100_000))

    # run_sync_one_thread(rockets)
    # run_in_threads(rockets)
    # asyncio.run(run_async(async_rockets))


if __name__ == "__main__":
    main()