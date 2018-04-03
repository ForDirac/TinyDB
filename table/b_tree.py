from typing import List, Tuple

class Pair(object):
    def __init__(self, key: Tuple = None, value: List = None):
        self.key = key or ()
        self.value = value or []

    def __str__(self):
        return "{}{}".format(str(self.key), str(self.value))

    def is_empty(self) -> bool:
        return len(self.value) == 0

    # A.is_less_than(B) -> A<B:1, A=B:0, A>B:-1
    def is_less_than(self, target) -> int:
        if self.is_empty():
            return 0
        if self.key < target.key:
            return 1
        if self.key == target.key:
            return 0
        if self.key > target.key:
            return -1

    def insert(self, pair) -> None:
        self.value.extend(pair.value)

class Node(object):
    def __init__(self, parent = None, is_root = None):
        self.is_root = is_root or False
        self.order = 3  # constant
        self.parent = parent
        self.length = 0
        self.pairs = [None for _ in range(self.order-1)]
        self.children = [None for _ in range(self.order)]

    def show(self, depth):
        print('| '*depth+"Node: " + ", ".join(filter(lambda x: x!="None", [str(p) for p in self.pairs])))
        for child in self.children:
            if not child:
                break
            child.show(depth+1)

    def is_root(self):
        return self.is_root

    def is_empty(self):
        return self.length == 0

    def _keep_length(self):
        # assert(self.order-1 >= len(self.pairs))
        # assert(self.order >= len(self.children))
        self.pairs.extend([None for _ in range(self.order-1-len(self.pairs))])
        self.children.extend([None for _ in range(self.order-len(self.children))])

    def insert(self, pair):
        root = self
        node, idx = self._find_seat(pair)
        if node.length > node.order - 1:
            root = node._divide()
        return root

    def _insert_pair(self, index, pair):
        self.length += 1
        self.pairs = self.pairs[:index] + [pair] + self.pairs[index:]

    def _find_node(self, target):
        return self.children.index(target)

    def _find_seat(self, new):
        for i, pair in enumerate(self.pairs):
            if not pair:
                if not self.children[i]:
                    self._insert_pair(i, new)
                    return self, i
                return self.children[i]._find_seat(new)
            r = new.is_less_than(pair)
            if r == 1:
                if not self.children[i]:
                    self._insert_pair(i, new)
                    return self, i
                return self.children[i]._find_seat(new)
            if r == 0:
                pair.insert(new)
                return self, i
            if r == -1:
                continue
        if not self.children[i+1]:
            self._insert_pair(i+1, new)
            return self, i+1
        return self.children[i+1]._find_seat(new)

    def _divide(self):
        assert(self.length <= self.order)
        if not self.length > (self.order - 1):
            if self.parent is None:
                return self
            return self.parent._divide()
        if self.parent is None:
            self.parent = Node(is_root=True)
            self.parent.children[0] = self
            self.is_root = False
        pivot = int((self.order-1) / 2)
        left_node = Node(self.parent)
        left_node.pairs = self.pairs[:pivot]
        left_node.length = len(list(filter(lambda x: x != None, left_node.pairs)))
        left_node.children = self.children[:pivot+1]
        for child in left_node.children:
            if not child:
                continue
            child.parent = left_node
        left_node._keep_length()

        right_node = Node(self.parent)
        right_node.pairs = self.pairs[pivot+1:]
        right_node.length = len(list(filter(lambda x: x != None, right_node.pairs)))
        right_node.children = self.children[pivot+1:]
        for child in right_node.children:
            if not child:
                continue
            child.parent = right_node
        right_node._keep_length()

        idx = self.parent._find_node(self)
        parent_pair = self.pairs[pivot]
        self.parent._insert_pair(idx, parent_pair)
        leftside_children = self.parent.children[:idx]
        rightside_children = self.parent.children[idx+1:]
        # for child in leftside_children:
        #     if not child:
        #         continue
        #     child.parent = self.parent
        # for child in rightside_children:
        #     if not child:
        #         continue
        #     child.parent = self.parent
        self.parent.children = leftside_children + [left_node, right_node] + rightside_children
        return self.parent._divide()

    def search(self, key):
        for i, pair in enumerate(self.pairs):
            if not pair:
                if not self.children[i]:
                    return []
                return self.children[i].search(key)
            target = Pair(key, [0])
            r = target.is_less_than(pair)
            if r == 1:
                if not self.children[i]:
                    return []
                return self.children[i].search(key)
            if r == 0:
                return pair.value
            if r == -1:
                continue
        if not self.children[i+1]:
            return []
        return self.children[i].search(key)

    def delete(self, pair):
        pass

    def update(self, old_p: Pair, new_p: Pair):
        assert(old_p.value == new_p.value)
        self.delete(old_p)
        root = self.insert(new_p)
        return root


