def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+list[branches]

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts=[count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

count_leaves([3,[1],[2,[1],[1]]])

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)])

def increment_leaves(t):
    """retrun a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)

def increment(t):
    """return a tree like t but with all labels incremented"""
    return tree(label(t)+1,[increment(b) for b in branches(t)])

def print_tree(t,indent):
    print('  '*indent+str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)

numbers = tree(3,[tree(4),tree(5,[tree(6)])])

haste = tree('h',[tree('a',[tree('s'),
                            tree('t')]),
                  tree('e')])

def print_sums(t,so_far):
    so_far=so_far+label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b,so_far)

def count_paths(t,total):
    """Return the number of paths from the root to any node in 
    tree t for which the labels along the path sum to total
    >>>t = tree(3,[tree(-1),
                   tree(1,[tree(2,[tree(1)]),tree(3)]),
                   tree(1,[tree(-1)])])
    >>>count_paths(t,3)
    2
    >>>count_paths(t,4)
    2
    >>>count_paths(t,5)
    0
    >>>count_paths(t,6)
    1
    >>>count_paths(t,7)
    2

    """
    if is_leaf(t):
        found = 1 if label(t)==total else 0
    else :
        found = 1 if label(t)==total else 0
        sub_paths=sum([count_paths(b,total-label(t)) for b in branches(t)])
    return found + sub_paths

def countdown(k):
    if k>0:
        yield k
        yield countdown(k-1)
t = countdown(3)