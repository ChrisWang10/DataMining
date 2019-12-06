transactions = [
    [1, 2, 5],
    [2, 4],
    [2, 3],
    [1, 2, 4],
    [1, 3],
    [2, 3],
    [1, 3],
    [1, 2, 3, 5],
    [1, 2, 3]
]


def check_frequency(candidate_set, min_sup):
    count = 0
    for transaction in transactions:
        if candidate_set.issubset(frozenset(transaction)):
            count += 1
        if count >= min_sup:
            return True
    return False


def get_frequent_item_sets(frequent_item_sets):
    # get candidates from previous FIS(frequent item sets)
    candidates = []
    record = []
    for i in range(len(frequent_item_sets)):
        for j in range(i, len(frequent_item_sets)):
            union_sets = frequent_item_sets[i].union(frequent_item_sets[j])
            if union_sets not in record:
                record.append(union_sets)
            else:
                continue
            if len(union_sets) == len(frequent_item_sets) + 1:
                candidates.append(union_sets)


def main():
    min_support = 3
    candidate = list(set(item for transaction in transactions for item in transaction))
    frequent_itemsets = []
    counter = {}
    for v in candidate:
        for transaction in transactions:
            if v in transaction:
                counter[v] = 1 if v not in counter.keys() else counter[v] + 1
        if counter[v] > min_support:
            frequent_itemsets.append(frozenset([v]))


if __name__ == '__main__':
    main()
