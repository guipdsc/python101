import random
import time


class CustomIterator:
    def __init__(self, max_size = 5):
        self.max_size = max_size
    def __iter__(self):
        self.grabbed = 0
        return self
    def __next__(self):
        if self.grabbed<self.max_size:
            self.grabbed += 1
            return random.randint(0,10)
        else:
            raise StopIteration


def resource_intensive_task_generator():
    for i in range(10):
        time.sleep(1)
        yield i

def resource_intensive_task_list():
    l=[]
    for i in range(10):
        l.append(i)
        time.sleep(1)
    return l


for i in resource_intensive_task_generator,resource_intensive_task_list:
    print(f"using {i}")
    for j in i():
        print(f"Working in item {j}")


