from table import Instance, Table
from table.b_tree import Node, Pair
from typing import List, Tuple

class DBMS(object):
    def __init__(self, schema = None):
        self.table = Table('movies', schema)
        self.b_tree = Node(is_root=True)
        self.schema = schema

    def show(self):
        print("\n-------------------database-------------------")
        print("<TABLE>")
        self.table.show()
        print("<B-TREE>")
        self.b_tree.show(0)
        print("---------------------------------------------\n")

    def insert(self, values: Tuple):
        print('>>> INSERT Tuple of {}'.format(str(values)))
        inst = Instance(self.schema, values)
        self.table.insert(inst)
        pair = Pair(inst.key, [inst._id])
        self.b_tree = self.b_tree.insert(pair)

    def delete(self, num: int):
        print('>>> DELETE Tuple#{}'.format(num))
        inst = self.table.delete(num)
        self.b_tree = self.b_tree.delete(inst.to_pair())
        self.b_tree.show(0)

    def search(self, key: Tuple):
        print('>>> SEARCH key of {}'.format(str(key)))
        v_list = self.b_tree.search(key)
        result = []
        for _id in v_list:
            i, inst = self.table.search(_id)
            result.append(str(inst))
            print(str(inst))
        if len(result) == 0:
            print("** No such key **")
        return result

    def update(self, num: int, values: Tuple):
        print(">>> UPDATE Tuple#{} to {}".format(num, str(values)))
        inst = Instance(self.schema, values)
        old, new = self.table.update(num, inst)
        self.b_tree = self.b_tree.update(old.to_pair(), new.to_pair())

