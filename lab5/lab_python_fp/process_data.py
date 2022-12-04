from gen_random import gen_random
from  unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
import json
from field import field

@print_result
def f1(arg):
    return sorted(Unique(list(field(arg, 'job-name')), ignore_case=True))

@print_result
def f2(arg):
    return list(filter(lambda x: x[:11] == 'программист', arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + str(' с опытом Python'), arg))

@print_result
def f4(arg):
    return list(zip(arg, map(lambda x: 'зарплата ' +str(x) + str(' руб.') ,gen_random(len(arg), 100000, 200000))))

def main():
    with open('data_light.json') as f:
        data = json.load(f)
    with cm_timer_1():
       f4(f3(f2(f1(data))))

if __name__ == '__main__':
    main()