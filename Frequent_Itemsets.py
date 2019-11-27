import numpy as np

transactions = [
    ['bread', 'milk', 'vegetable', 'fruit', 'eggs'],
    ['noodle', 'beef', 'pork', 'water', 'socks', 'gloves', 'shoes', 'rice'],
    ['socks', 'gloves'],
    ['bread', 'milk', 'shoes', 'socks', 'eggs'],
    ['socks', 'shoes', 'sweater', 'cap', 'milk', 'vegetable', 'gloves'],
    ['eggs', 'bread', 'milk', 'fish', 'crab', 'shrimp', 'rice']
]


class TreeNode:
    def __init__(self, node_name, frequency, node_parent):
        self.node_name = node_name
        self.frequency = frequency
        self.node_parent = node_parent
        self.next_similar = None
        self.children = {}


def construct_fp_tree(frozen_data, min_support):
    """
    :param data:            all transactions
    :param min_support:     minimum support for each item
    :return:                tree, header table
    """
    print(frozen_data)
    # 1 generate head table
    head_point_table = {}
    for contents in frozen_data:
        for item in contents:
            head_point_table[item] = head_point_table.get(item, 0) + frozen_data[contents]
    head_point_table = {k: v for k, v in head_point_table.items() if v >= min_support}
    frequent_items = set(head_point_table)

    for k in head_point_table:
        head_point_table[k] = [head_point_table[k], None]

    fp_tree = TreeNode('NUll', 1, None)
    for transaction, frequency in frozen_data.items():
        for item in transaction:
            if item in frequent_items:
                






def main():
    frozen_data = {frozenset(item): 1 for item in transactions}
    construct_fp_tree(frozen_data=frozen_data, min_support=3)


if __name__ == '__main__':
    main()
