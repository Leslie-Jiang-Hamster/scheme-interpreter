from pair import nil

def pair_to_list(pair):
    if pair == nil:
        return []
    return [pair.first] + pair_to_list(pair.rest)