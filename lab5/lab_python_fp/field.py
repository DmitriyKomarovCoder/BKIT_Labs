def field(items, *args):
    stri = ''
    assert len(args) > 0
    if len(args) == 1:
        for dic in items:
            value = dic.get(args[0])
            if value is not None:
                 yield value
    else:
        for item in items:
            res = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    res[key] = value
            yield res

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(list(field(goods, 'title'))) # 'Ковер', 'Диван для отдыха'
    for el in field(goods, 'title', 'price'):
        print(el) # {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
