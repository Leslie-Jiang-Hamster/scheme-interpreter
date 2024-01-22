from pair import nil, Pair

def pair_to_list(pair):
    if pair == nil:
        return []
    return [pair.first] + pair_to_list(pair.rest)

def last(pair):
    return pair_to_list(pair)[-1]

def except_last(pair):
    return pair_to_list(pair)[:-1]

def map_(seq, fn):
    new_seq = []
    for i in range(len(seq)):
        new_seq.append(fn(seq[i]))
    return new_seq

def second(pair):
    return pair.rest.first

def iota(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

def list_to_pair(seq):
    pair = nil
    for item in reversed(seq):
        pair = Pair(item, pair)
    return pair

def unique(seq):
    return list(set(seq))

def all_distinct(seq):
    return len(seq) == len(unique(seq))