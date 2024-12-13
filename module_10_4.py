import queue
import threading
import time
from queue import Queue
import random

from threading import Thread


class Table:

    def __init__(self, numbers):
        self.numbers = numbers
        self.guest = None

class Guest(Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time1 = random.randint(3, 10)
        time.sleep(time1)

class Cafe():
    queue = Queue()

    tables = [Table(number) for number in range(1, 6)]

    def guest_arrival(self, *guests):
        for i in guests:
            for j in self.tables:
                if j.guest is None:
                    j.guest = i
                    print(f'{i.name} сел(-а) за стол номер {j.numbers}.')
                    j.guest.start()
                    break
                elif j.numbers < 5:
                    continue
                elif j.numbers == 5:
                    self.queue.put(i)
                    print(f'{i.name} в очереди.')

    def discuss_guests(self):
        check1 = False
        while self.queue.empty() is False or check1 == True:
            for i in self.tables:
                if i.guest != None:
                    check1 = True
                else:
                    check1 = False
                    continue

                for i in self.tables:
                    if i.guest != None:
                        if i.guest.is_alive() is True:
                            i.guest.join()

                        else:
                            print(f'{i.guest.name} покушал(-а) и ушёл(ушла).')
                            i.guest = None
                            print(f'Стол номер {i.numbers} свободен.')
                            if self.queue.empty() is False:
                                i.guest = self.queue.get()
                                print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.numbers}.')
                                check1 = True
                                i.guest.start()
                    else:
                        continue







guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]
cafe = Cafe()
cafe.guest_arrival(*guests)
cafe.discuss_guests()



