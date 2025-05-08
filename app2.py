# using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created : {cls.count}")

c1 = Counter()
c1 = Counter()
Counter.display_count()