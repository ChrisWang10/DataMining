import numpy as np
import os

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
    # generate head table
    head_point_table = {}
    for contents in frozen_data:
        for item in contents:
            head_point_table[item] = head_point_table.get(item, 0) + frozen_data[contents]
    head_point_table = {k: v for k, v in head_point_table.items() if v >= min_support}
    frequent_items = set(head_point_table)

    # element of head table consists of frequency and a pointer map to the node in FP tree
    for k in head_point_table:
        head_point_table[k] = [head_point_table[k], None]

    fp_tree = TreeNode('NUll', 1, None)
    for transaction, count in frozen_data.items():
        # we need to rearrange the order of each transaction based on its element frequency in the head table
        frequent_items_in_record = {}
        for item in transaction:
            if item in frequent_items:
                frequent_items_in_record[item] = head_point_table[item][0]
        if len(frequent_items_in_record) > 0:
            ordered_frequent_items = [v[0] for v in sorted(frequent_items_in_record.items(),
                                                           key=lambda v: v[1], reverse=True)]
            # insert to FP tree
            update_fp_tree(fp_tree, ordered_frequent_items, head_point_table, count)
    return fp_tree, head_point_table


def update_fp_tree(fp_tree, ordered_frequent_items, head_point_table, count):
    if ordered_frequent_items[0] in fp_tree.children:
        fp_tree.children[ordered_frequent_items[0]].frequency += 1

    # start a new branch
    else:
        fp_tree.children[ordered_frequent_items[0]] = TreeNode(ordered_frequent_items[0], count, fp_tree)

        # head_point_table point to the node in FP tree
        if not head_point_table[ordered_frequent_items[0]][1]:
            head_point_table[ordered_frequent_items[0]][1] = fp_tree.children[ordered_frequent_items[0]]

        # If already point to the node, then link old node to new node
        else:
            update_head_point_table(head_point_table[ordered_frequent_items[0]][1],
                                    fp_tree.children[ordered_frequent_items[0]])
    if len(ordered_frequent_items) > 1:
        update_fp_tree(fp_tree.children[ordered_frequent_items[0]], ordered_frequent_items[1::], head_point_table,
                       count)


def fp_tree_mining(head_point_table, prefix, frequent_patterns, min_support):
    # for each item in head table, find conditional prefix path and create conditional fp-tree
    head_point_items = [v[0] for v in sorted(head_point_table.items(), key=lambda v: v[1][0])]

    for item in head_point_items:
        new_prefix = prefix.copy()
        new_prefix.add(item)
        support = head_point_table[item][0]
        frequent_patterns[frozenset(new_prefix)] = support

        prefix_path = get_prefix_path(head_point_table, item)
        if prefix_path != {}:
            conditional_fp_tree, conditional_head_point_table = construct_fp_tree(prefix_path, min_support)
            if conditional_head_point_table:
                fp_tree_mining(conditional_head_point_table, new_prefix, frequent_patterns, min_support)


def get_prefix_path(head_point_table, item):
    prefix_path = {}
    begin_node = head_point_table[item][1]
    prefixs = ascend_tree(begin_node)
    if len(prefixs):
        prefix_path[frozenset(prefixs)] = begin_node.frequency

    while begin_node.next_similar:
        begin_node = begin_node.next_similar
        prefixs = ascend_tree(begin_node)
        if len(prefixs):
            prefix_path[frozenset(prefixs)] = begin_node.frequency
    return prefix_path


def ascend_tree(node):
    prefixs = []
    while node.node_parent and node.node_parent.node_name != 'NUll':
        node = node.node_parent
        prefixs.append(node.node_name)
    return prefixs


def update_head_point_table(begin_node, target_node):
    while begin_node.next_similar:
        begin_node = begin_node.next_similar
    begin_node.next_similar = target_node


def main():
    frozen_data = {frozenset(item): 1 for item in transactions}
    min_support = 3
    # 1 construct FP tree
    fp_tree, head_point_table = construct_fp_tree(frozen_data=frozen_data, min_support=3)

    frequent_patterns = {}
    prefix = set([])
    # 2 Mining FP tree
    fp_tree_mining(head_point_table, prefix, frequent_patterns, min_support)
    print(frequent_patterns)


if __name__ == '__main__':
    main()
