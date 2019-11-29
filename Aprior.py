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


def generate_candidate_set(transactions):
    c = []
    for trade in transactions:
        for item in trade:
            if [item] not in c:
                c.append([item])
    return list(map(frozenset, c))


def get_frequent_item_sets(frozen_data, candidates, min_support):
    frequent_item_sets = []
    for item in candidates:
        print(item)
    return 1


def generate_candidates_general(k, frequent_itemsets_previous_layer):
    candidates = {}
    for sets in frequent_itemsets_previous_layer.keys():
        pass


def main():
    min_support = 3
    frozen_data = list(map(set, transactions))
    c1 = generate_candidate_set(transactions)
    l1 = get_frequent_item_sets(frozen_data, c1, min_support)


if __name__ == '__main__':
    main()
