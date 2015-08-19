# -*- coding: utf-8 -*-
"""
Performance testing
How to run:
 cd pydash/
 python -m perf.perftest
"""
import timeit


class TimedTest(object):
    def __init__(self, name, _python_func, _pydash_func, note='', number=1000):
        self.name = name
        self.python = _python_func
        self.pydash = _pydash_func
        self.number = number
        self.note = note

    def run(self):
        return '{0: <30} | {1: >8.3f} | {2: >8.3f} | {3}'.format(
            self.name,
            min(timeit.repeat(self.pydash + '()', setup='from __main__ import ' + self.pydash, number=self.number))*1000,
            min(timeit.repeat(self.python + '()', setup='from __main__ import ' + self.python, number=self.number))*1000,
            self.note
        )


########################################################################################################################


def test_pydash_append():
    from pydash.arrays import append
    l = [1, 2, 3, 4]
    append(l, 5, 6, [4])
    assert l == [1, 2, 3, 4, 5, 6, [4]]


def test_python_append():
    l = [1, 2, 3, 4]
    list(map(l.append, [5, 6, [4]]))
    assert l == [1, 2, 3, 4, 5, 6, [4]]


def test_pydash_cat():
    from pydash.arrays import cat
    l = [[1, 2], [3, 4], [[5], [6]]]
    assert cat(*l) == [1, 2, 3, 4, [5], [6]]


def test_python_cat():
    l = [[1, 2], [3, 4], [[5], [6]]]
    _l = []
    for v in l:
        _l += v
    assert _l == [1, 2, 3, 4, [5], [6]]


def test_pydash_chunk():
    from pydash.arrays import chunk
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert chunk(l, 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]


def test_python_chunk():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    _l = []
    for i in range(0, len(l), 2):
        _l.append(l[i:i+2])
    assert _l == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]


def test_pydash_compact():
    from pydash.arrays import compact
    l = ['', 1, 0, True, False, None]
    assert compact(l) == [1, True]


def test_python_compact():
    l = ['', 1, 0, True, False, None]
    _l = []
    for v in l:
        if bool(v):
            _l.append(v)
    assert _l == [1, True]


def test_pydash_difference():
    from pydash.arrays import difference
    l = [1, 2, 3]
    assert difference(l, [1], [2]) == [3]


def test_python_difference():
    l = [1, 2, 3]
    _l = l.copy()
    for v in ([1], [2]):
        _l = list(set(_l) - set(v))
    assert _l == [3]


def test_pydash_drop():
    from pydash.arrays import drop
    l = [1, 2, 3, 4]
    assert drop(l, 2) == [3, 4]


def test_python_drop():
    l = [1, 2, 3, 4]
    assert l[2:] == [3, 4]


def test_pydash_drop_right():
    from pydash.arrays import drop_right
    l = [1, 2, 3, 4]
    assert drop_right(l, 2) == [1, 2]


def test_python_drop_right():
    l = [1, 2, 3, 4]
    assert l[:2] == [1, 2]


def test_pydash_drop_right_while():
    from pydash.arrays import drop_right_while
    l = [1, 2, 3, 4]
    assert drop_right_while(l, lambda x: x > 2) == [1, 2]


def test_python_drop_right_while():
    l = [1, 2, 3, 4]
    _l = l.copy()
    while _l[-1] > 2:
        _l.pop()
    assert _l == [1, 2]


def test_pydash_drop_while():
    from pydash.arrays import drop_while
    l = [1, 2, 3, 4]
    assert drop_while(l, lambda x: x < 3) == [3, 4]


def test_python_drop_while():
    l = [1, 2, 3, 4]
    _l = l.copy()
    while _l[0] < 3:
        _l.pop(0)
    assert _l == [3, 4]


def test_pydash_duplicates():
    from pydash.arrays import duplicates
    l = [1, 2, 3, 4, 1, 2, 3, 4]
    assert duplicates(l) == [1, 2, 3, 4]


def test_python_duplicates():
    l = [1, 2, 3, 4, 1, 2, 3, 4]
    assert list(set([x for x in l if l.count(x) > 1])) == [1, 2, 3, 4]


def test_pydash_fill():
    from pydash.arrays import fill
    l = [1, 2, 3, 4]
    assert fill(l, 0, 0, 2) == [0, 0, 3, 4]


def test_python_fill():
    l = [1, 2, 3, 4]
    filler, start, end = 0, 0, 2
    assert [v if (k <= start or k >= end) else filler for k, v in enumerate(l)] == [0, 0, 3, 4]


def main():
    perftests = [
        TimedTest('pydash.array.append', 'test_python_append', 'test_pydash_append'),
        TimedTest('pydash.array.cat', 'test_python_cat', 'test_pydash_cat'),
        TimedTest('pydash.array.chunk', 'test_python_chunk', 'test_pydash_chunk'),
        TimedTest('pydash.array.compact', 'test_python_compact', 'test_pydash_compact'),
        TimedTest('pydash.array.difference', 'test_python_difference', 'test_pydash_difference'),
        TimedTest('pydash.array.drop', 'test_python_drop', 'test_pydash_drop'),
        TimedTest('pydash.array.drop_right', 'test_python_drop_right', 'test_pydash_drop_right'),
        TimedTest('pydash.array.drop_right_while', 'test_python_drop_right_while', 'test_pydash_drop_right_while'),
        TimedTest('pydash.array.drop_while', 'test_python_drop_while', 'test_pydash_drop_while'),
        TimedTest('pydash.array.duplicates', 'test_python_duplicates', 'test_pydash_duplicates', note='This is an unfair comparison, since pydash.duplicate does so much more.'),
        TimedTest('pydash.array.fill', 'test_python_fill', 'test_pydash_fill'),
    ]
    print('{0: <30} | {1: ^8} | {2: ^8} |'.format('Test Name', 'pydash', 'python'))
    print('{0: <30} | {1: <8} | {2: <8} |'.format('---------', 'time(ms)', 'time(ms)'))
    for perftest in perftests:
        print(perftest.run())


if __name__ == '__main__':
    main()
