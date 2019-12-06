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

def get_frequent_item_sets(frequent_item_sets):
    # get candidates from previous FIS(frequent item sets)






def main():
    min_support = 3
    candidate = list(set(item for transaction in transactions for item in transaction))
    frequent_itemsets = []
    counter = {}
    for v in candidate:
        for transaction in transactions:
            if v in transaction:
                counter[v] = 1 if v not in counter.keys() else counter[v]+1
        if counter[v] > min_support:
            frequent_itemsets.append(v)




if __name__ == '__main__':
    main()
