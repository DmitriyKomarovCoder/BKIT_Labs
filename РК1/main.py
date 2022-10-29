# используется для сортировки
from operator import itemgetter
 

 
class Microprocessor:
    """Микропроцессор"""
    def __init__(self, id, name, threads, comp_id):
        self.id = id
        self.name = name
        self.threads = threads
        self.comp_id = comp_id
 
class Computer:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MicropComp:
    """
    'Сотрудники отдела' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, comp_id, proc_id):
        self.comp_id = comp_id
        self.proc_id = proc_id
 
# Компьютеры
computers = [
    Computer(1, 'MacBook'),
    Computer(2, 'ThinkPad'),
    Computer(3, 'MateBookX'),
    
    Computer(11, 'Latitude'),
    Computer(22, 'ThinkPad'),
    Computer(33, 'Inspiron'),
]
 
# Микропроцессоры
microprocessor = [
    Microprocessor(1, 'Intel Core i5-12500k', 4, 1),
    Microprocessor(2, 'Intel Core i9-9000', 16, 2),
    Microprocessor(3, 'AMD Ryzen 5', 4, 3),
    Microprocessor(4, 'AMD Ryzen 3', 32, 3),
    Microprocessor(5, 'AMD Ryzen 8', 12, 1),
]
 
microp_comp = [
    MicropComp(1,1),
    MicropComp(2,2),
    MicropComp(3,3),
    MicropComp(3,4),
    MicropComp(3,5),
    MicropComp(11,1),
    MicropComp(22,2),
    MicropComp(33,3),
    MicropComp(33,4),
    MicropComp(33,5),
]

def task1(one_to_many):

    for proc in microprocessor:
        res = list(filter(lambda i: i[0][0] == 'I', one_to_many))
    print(res)

def task2(one_to_many):
    res_min = []
    for c in computers:
        c_proc_threads = [(c_name, proc_threads) for proc_name, proc_threads, c_name in one_to_many if c_name == c.name]
    #Если в компьютере есть процессор
        if len(c_proc_threads) > 0:
            res_min.append(min(c_proc_threads, key = itemgetter(1)))
    res_2 = sorted(res_min, key = itemgetter(1))
    for r in res_2:
        print(r)

def task3(many_to_many):
    res3 = sorted(many_to_many, key = itemgetter(2))
    for r in res3:
        print(r)

def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(proc.name, proc.threads, c.name) 
        for c in computers 
        for proc in microprocessor 
        if proc.comp_id==c.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, procc.comp_id, procc.proc_id) 
        for c in computers 
        for procc in microp_comp
        if c.id == procc.comp_id]
    
    many_to_many = [(proc.name, proc.threads, procc_name) 
        for procc_name, c_id, proc_id in many_to_many_temp
        for proc in microprocessor if proc.id==proc_id]
 
    print('Заданик 1')
    task1(one_to_many)
    print('\nЗадание 2')
    task2(one_to_many)
    print("\nЗадание 3")
    task3(many_to_many)
 
if __name__ == '__main__':
    main()
