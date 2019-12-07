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


def check_frequency(candidate_set):
    count = 0
    for transaction in transactions:
        if candidate_set.issubset(frozenset(transaction)):
            count += 1
    return count


def get_frequent_item_sets(frequent_item_sets, min_sup, F):
    # get candidates from previous FIS(frequent item sets)
    new_frequent_item_sets = []
    record = []
    for i in range(len(frequent_item_sets) - 1):
        for j in range(i + 1, len(frequent_item_sets)):
            union_sets = frequent_item_sets[i].union(frequent_item_sets[j])
            # print(union_sets)
            if union_sets not in record:
                record.append(union_sets)
            else:
                continue
            if len(union_sets) == len(frequent_item_sets[0]) + 1:
                # print(union_sets)
                if check_frequency(union_sets) > min_sup:
                    new_frequent_item_sets.append(union_sets)
                    F.append(union_sets)
    if len(new_frequent_item_sets):
        get_frequent_item_sets(new_frequent_item_sets, min_sup, F)


def generate_association(frequent_item_sets):
    for fis in frequent_item_sets:
        if len(fis) >= 2:
            for i in range(1, len(fis)):
                confidence = check_frequency(fis) / check_frequency(frozenset(list(fis)[i:]))
                # if confidence > 0.4:
                print('{}->{}, confidence {}'.format(list(fis)[:i], list(fis)[i:], confidence))


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
    get_frequent_item_sets(frequent_itemsets, min_support, frequent_itemsets)

    generate_association(frequent_itemsets)


if __name__ == '__main__':
    main()
