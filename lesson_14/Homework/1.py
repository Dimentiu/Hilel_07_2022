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


class Rocket:
    """
    This class is responsible for running rockets.
    Every rocket has its own delay and countdown.
    """

    def __init__(self, name) -> None:
        self.delay = get_random_delay()
        self.countdown = get_random_countdown()
        self.name = name

    def _countdown(self):
        """Human-base countdown."""

        for i in range(self.countdown + 1, 0, -1):
            print(f"{i}...")
            sleep(1)

    def _delay(self):
        print(f"🕐 Delay for {self.delay} seconds...")
        sleep(self.delay)

    def run(self):
        # Do the countdown before start the rocket
        print(f"\nPrepare the {self.name} ✅")
        self._countdown()

        # Check the delay
        self._delay()

        # Show success message
        print("🚀 Rocket go to the moon...")


def main():
    rockets = [Rocket(name=f"Rocket {i}") for i in range(1, 3)]
    threads = [Thread(target=rocket.run) for rocket in rockets]
    for thread in threads:
        thread.start()


def T1():
    for i in range(1,10001):
        print(i)  

def T2():
    x = 0
    for i in range(1,10001):
        x += i
    print(f"T2: {x}")

def T3():
    x = 0
    for i in range(1,10001):
        x += i
        y = x/10000
    print(f"T3: {y}")
        
t1 = Thread(target=T1)
t2 = Thread(target=T2)
t3 = Thread(target=T3)

t1.start()
t1.join()

t2.start()
t2.join()

t3.start()
t3.join()


if __name__ == "__main__":
    main()