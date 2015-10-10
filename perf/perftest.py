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
    _l = l[::]
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
    _l = l[::]
    while _l[-1] > 2:
        _l.pop()
    assert _l == [1, 2]


def test_pydash_drop_while():
    from pydash.arrays import drop_while
    l = [1, 2, 3, 4]
    assert drop_while(l, lambda x: x < 3) == [3, 4]


def test_python_drop_while():
    l = [1, 2, 3, 4]
    _l = l[::]
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
    assert [v if (k < start or k >= end) else filler for k, v in enumerate(l)] == [0, 0, 3, 4]


def test_pydash_find_index():
    from pydash.arrays import find_index
    l = [1, 2, 3, 4]
    assert find_index(l, lambda x: x >= 3) == 2


def test_python_find_index():
    l = [1, 2, 3, 4]
    v = -1
    for i, n in enumerate(l):
        if n >= 3:
            v = i
            break
    assert v == 2


def test_pydash_find_last_index():
    from pydash.arrays import find_last_index
    l = [1, 2, 3, 4]
    assert find_last_index(l, lambda x: x > 4) == -1


def test_python_find_last_index():
    l = [1, 2, 3, 4]
    v = -1
    l.reverse()
    for i, n in enumerate(l):
        if n > 4:
            v = i
            break
    assert v == -1


def test_pydash_first():
    from pydash.arrays import first
    l = [1, 2, 3, 4]
    assert first(l) == 1


def test_python_first():
    l = [1, 2, 3, 4]
    assert l[0] == 1


def test_pydash_flatten():
    from pydash.arrays import flatten
    l = [1, [2], [[3], [4]]]
    assert flatten(l) == [1, 2, [3], [4]]


def test_python_flatten():
    l = [1, [2], [[3], [4]]]
    _l = []
    for v in l:
        if isinstance(v, list):
            for _v in v:
                _l.append(_v)
        else:
            _l.append(v)
    assert _l == [1, 2, [3], [4]]


def test_pydash_flatten_deep():
    from pydash.arrays import flatten_deep
    l = [1, [2], [[3], [4]]]
    assert flatten_deep(l) == [1, 2, 3, 4]


def test_python_flatten_deep():
    l = [1, [2], [[3], [4]]]
    _l = []
    def flat(a):
        for v in a:
            if isinstance(v, list):
                flat(v)
            else:
                _l.append(v)
    flat(l)
    assert _l == [1, 2, 3, 4]


def test_pydash_index_of():
    from pydash.arrays import index_of
    l = [1, 2, 3, 4]
    assert index_of(l, 2) == 1


def test_python_index_of():
    l = [1, 2, 3, 4]
    assert l.index(2) == 1


def test_pydash_initial():
    from pydash.arrays import initial
    l = [1, 2, 3, 4]
    assert initial(l) == [1, 2, 3]


def test_python_initial():
    l = [1, 2, 3, 4]
    assert l[:-1] == [1, 2, 3]


def test_pydash_intercalate():
    from pydash.arrays import intercalate
    l = [1, 2, [3, 4], [[5, 6]]]
    assert intercalate(l, 'x') == [1, 'x', 2, 'x', 3, 4, 'x', [5, 6]]


def test_python_intercalate():
    l = [1, 2, [3, 4], [[5, 6]]]
    _l = []
    for i, v in enumerate(l):
        if isinstance(v, list):
            for _v in v:
                _l.append(_v)
        else:
            _l.append(v)
        if i is not (len(l) - 1):
            _l.append('x')
    assert _l == [1, 'x', 2, 'x', 3, 4, 'x', [5, 6]]


def test_pydash_interleave():
    from pydash.arrays import interleave
    l = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [1, 2])
    assert interleave(*l) == [1, 4, 7, 1, 2, 5, 8, 2, 3, 6, 9, 10]


def test_python_interleave():
    from itertools import cycle, islice
    l = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [1, 2])
    def roundrobin(*iterables):
        """Pulled from https://docs.python.org/2/library/itertools.html#recipes"""
        pending = len(iterables)
        nexts = cycle(iter(it).__next__ for it in iterables)
        while pending:
            try:
                for next in nexts:
                    yield next()
            except StopIteration:
                pending -= 1
                nexts = cycle(islice(nexts, pending))
    assert list(roundrobin(*l)) == [1, 4, 7, 1, 2, 5, 8, 2, 3, 6, 9, 10]


def test_pydash_intersection():
    from pydash.arrays import intersection
    l = ([1, 2, 3], [4, 5, 6, 2, 3], [0, 0, 1, 2, 3, 4])
    assert intersection(*l) == [2, 3]


def test_python_intersection():
    l = ([1, 2, 3], [4, 5, 6, 2, 3], [0, 0, 1, 2, 3, 4])
    _l = set(l[0])
    for s in [set(a) for a in l[1:]]:
        _l = _l.intersection(s)
    assert list(_l) == [2, 3]


def test_pydash_intersperse():
    from pydash.arrays import intersperse
    l = [1, 2, 3, [4]]
    assert intersperse(l, 'x') == [1, 'x', 2, 'x', 3, 'x', [4]]


def test_python_intersperse():
    l = [1, 2, 3, [4]]
    _l = []
    for v in l[:-1]:
        _l.append(v)
        _l.append('x')
    _l.append(l[-1])
    assert _l == [1, 'x', 2, 'x', 3, 'x', [4]]


def test_pydash_last():
    from pydash.arrays import last
    l = [1, 2, 3, 4]
    assert last(l) == 4


def test_python_last():
    l = [1, 2, 3, 4]
    assert l[-1] == 4


def test_pydash_last_index_of():
    from pydash.arrays import last_index_of
    l = [1, 2, 3, 4, 3]
    assert last_index_of(l, 3) == 4


def test_python_last_index_of():
    l = [1, 2, 3, 4, 3]
    assert len(l) - l[::-1].index(3) - 1 == 4


def test_pydash_mapcat():
    from pydash.arrays import mapcat
    l = [1, 2, 3, 4]
    assert mapcat(l, lambda x: list(range(x))) == [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]


def test_python_mapcat():
    l = [1, 2, 3, 4]
    _l = []
    for v in l:
        _l += list(range(v))
    assert _l == [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]


def test_pydash_object_():
    from pydash.arrays import object_
    keys = [1, 2, 3]
    values = [4, 5, 6]
    assert object_(keys, values) == {1: 4, 2: 5, 3: 6}


def test_python_object_():
    keys = [1, 2, 3]
    values = [4, 5, 6]
    assert dict(zip(keys, values)) == {1: 4, 2: 5, 3: 6}


def test_pydash_pull():
    from pydash.arrays import pull
    l = [1, 2, 3, 4]
    pull(l, 2, 4)
    assert l == [1, 3]


def test_python_pull():
    l = [1, 2, 3, 4]
    l = [v for v in l if v not in [2, 4]]
    assert l == [1, 3]


def test_pydash_pull_at():
    from pydash.arrays import pull_at
    l = [1, 2, 3, 4]
    pull_at(l, 0, 2)
    assert l == [2, 4]


def test_python_pull_at():
    l = [1, 2, 3, 4]
    l = [v for k, v in enumerate(l) if k not in [0, 2]]
    assert l == [2, 4]


def test_pydash_remove():
    from pydash.arrays import remove
    l = [1, 2, 3, 4]
    remove(l, lambda x: x < 3)
    assert l == [3, 4]


def test_python_remove():
    l = [1, 2, 3, 4]
    for v in l[::]:
        if v < 3:
            l.remove(v)
    assert l == [3, 4]


def test_pydash_rest():
    from pydash.arrays import rest
    l = [1, 2, 3, 4]
    assert rest(l) == [2, 3, 4]


def test_python_rest():
    l = [1, 2, 3, 4]
    assert l[1:] == [2, 3, 4]


def test_pydash_reverse():
    from pydash.arrays import reverse
    l = [1, 2, 3, 4]
    assert reverse(l) == [4, 3, 2, 1]


def test_python_reverse():
    l = [1, 2, 3, 4]
    assert list(reversed(l)) == [4, 3, 2, 1]


def test_pydash_shift():
    from pydash.arrays import shift
    l = [1, 2, 3, 4]
    assert shift(l) == 1 and l == [2, 3, 4]


def test_python_shift():
    l = [1, 2, 3, 4]
    assert l.pop(0) == 1 and l == [2, 3, 4]


def test_pydash_slice_():
    from pydash.arrays import slice_
    l = [1, 2, 3, 4]
    assert slice_(l, 0, 2) == [1, 2]


def test_python_slice_():
    l = [1, 2, 3, 4]
    assert l[0:2] == [1, 2]


def test_pydash_sort():
    from pydash.arrays import sort
    l = [2, 1, 4, 3]
    sort(l)
    assert l == [1, 2, 3, 4]


def test_python_sort():
    l = [2, 1, 4, 3]
    l.sort()
    assert l == [1, 2, 3, 4]


def test_pydash_splice():
    from pydash.arrays import splice
    l = [2, 1, 4, 3]
    assert splice(l, 1, 2, 0, 0) == [1, 4]
    assert l == [2, 0, 0, 3]


def test_python_splice():
    l = [2, 1, 4, 3]
    assert l[1:3] == [1, 4]
    l = [v for k, v in enumerate(l) if k not in range(1, 3)]
    l.insert(1, 0)
    l.insert(1, 0)
    assert l == [2, 0, 0, 3]






def main():
    array_funcs = ['append', 'cat', 'chunk', 'compact', 'difference', 'drop', 'drop_right', 'drop_right_while',
                   'drop_while', 'duplicates', 'fill', 'find_index', 'find_last_index', 'first', 'flatten',
                   'flatten_deep', 'index_of', 'initial', 'intercalate', 'interleave', 'intersection', 'intersperse',
                   'last', 'last_index_of', 'mapcat', 'object_', 'pull', 'pull_at', 'remove', 'rest', 'reverse',
                   'shift', 'slice_', 'sort', 'splice']
    perftests = list()

    # Add all array function tests to the list of performance tests
    perftests += [TimedTest('pydash.array.{}'.format(f), 'test_python_{}'.format(f), 'test_pydash_{}'.format(f))
                 for f in array_funcs]
    print('{0: <30} | {1: ^8} | {2: ^8} |'.format('Test Name', 'pydash', 'python'))
    print('{0: <30} | {1: <8} | {2: <8} |'.format('---------', 'time(ms)', 'time(ms)'))
    for perftest in perftests:
        print(perftest.run())


if __name__ == '__main__':
    main()
