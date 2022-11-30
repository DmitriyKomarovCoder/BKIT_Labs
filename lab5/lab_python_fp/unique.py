from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = set(items)
        self.used_elenets = set()
        self.iter = iter(self.items)
        self.ignore_case = kwargs.get('ignore_case', False)
        if self.ignore_case == True:
            self.items={i.lower() for i in items}
        self.iter = iter(self.items)
    def __next__(self):
        for current in self.iter:
                return current 
        raise StopIteration
    def __iter__(self):
        return self

if __name__ == '__main__':
    data = [
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        gen_random(10, 1, 3),
        ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    ]
    for one in data:
        print(list(Unique(one)))
    print(list(Unique(data[-1], ignore_case=True)))