from Tree import *
from linked_list import *
#1
#Recursion

def count_partitions_recursion(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions_recursion(n-m, m)
        without_m = count_partitions_recursion(n, m-1)
        return with_m + without_m

#2
#Tree materialize

def partition_tree(n, m):
        """Return a partition tree of n using parts of up to m."""
        if n == 0:
            return tree(True)
        elif n < 0 or m == 0:
            return tree(False)
        else:
            left = partition_tree(n-m, m)
            right = partition_tree(n, m-1)
            return tree(m, [left, right])
        
def print_parts(tree, partition=[]):
        if is_leaf(tree):
            if label(tree):
                print(' + '.join(partition))
        else:
            left, right = branches(tree)
            m = str(label(tree))
            print_parts(left, partition + [m])
            print_parts(right, partition)
        
#3
#linked list
def partitions(n, m):
        """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
        """
        if n == 0:
            return link(empty, empty) # A list containing the empty partition
        elif n < 0 or m == 0:
            return empty
        else:
            using_m = partitions(n-m, m)
            with_m = apply_to_all_link(lambda s: link(m, s), using_m)
            without_m = partitions(n, m-1)
            return extend_link(with_m, without_m)
        
def print_partitions(n, m):
        lists = partitions(n, m)
        strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
        print(join_link(strings, "\n"))

#4
#the final
def count_partition(n,m):
    """Count partitions.
    >>> count_partitions(6,4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partition(n-m,m)
        without_m = count_partition(n,m-1)
        return exact_match + with_m + without_m

def list_partition(n,m):
    """list partitions.
>>> for p in list_partitions(6,4) : print(p)
[2, 4]
[1, 1, 4]
[3, 3]
[1, 2, 3]
[1, 1, 1, 3]
[2, 2, 2]
[1, 1, 2, 2]
[1, 1, 1, 1, 2]
[1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partition(n-m,m)]
        without_m = list_partition(n,m-1)
        return exact_match + with_m + without_m

def strings_partition(n,m):
    """strings partitions.
>>> for p in list_partitions(6,4) : print(p)
2+4
1+1+4
3+3
1+2+3
1+1+1+3
2+2+2
1+1+2+2
1+1+1+1+2
1+1+1+1+1+1
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in strings_partition(n-m,m)]
        without_m = strings_partition(n,m-1)
        return exact_match + with_m + without_m
    
def yield_partition(n,m):
    """yield partitions.
>>> for p in list_partitions(6,4) : print(p)
2 + 4
1 + 1 + 4
3 + 3
1 + 2 + 3
1 + 1 + 1 + 3
2 + 2 + 2
1 + 1 + 2 + 2
1 + 1 + 1 + 1 + 2
1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partition(n-m,m):
            yield p + ' + ' + str(m)
        yield from yield_partition(n,m-1)