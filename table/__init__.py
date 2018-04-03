from datetime import datetime
from typing import Tuple
from table.b_tree import Pair

class Key(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Instance(object):
    _id = None

    def __init__(self, schema: Tuple, values: Tuple):
        self.schema = schema
        key = []
        for sc, v in zip(schema, values):
            if isinstance(sc, Key):
                key.append(v)
            setattr(self, str(sc), v)
        self.key = tuple(key)

    def __str__(self):
        return str(self._id)+'. |'+'|'.join([str(getattr(self, str(sc))) for sc in self.schema]) + '|'

    def to_pair(self):
        return Pair(self.key, [self._id])

class Table(object):
    def __init__(self, name: str, schema: Tuple):
        self.schema = schema
        self.current_id = 0
        self.total_instances = 0
        self.contents = []

    def show(self):
        print('-.-|'+'|'.join([str(sc) for sc in self.schema]) + '|')
        for row in self.contents:
            print(row)

    def insert(self, inst: Instance) -> Instance:
        self.current_id += 1
        inst._id = self.current_id
        self.contents.append(inst)
        self.total_instances += 1
        return inst

    def delete(self, _id: int) -> Instance:
        i, inst = self.search(_id)
        if not inst:
            return None
        self.contents.pop(i)
        self.total_instances -= 1
        return inst

    def search(self, _id: int) -> Tuple[int, Instance]:
        for i, inst in enumerate(self.contents):
            if inst._id == _id:
                return i, inst
        return None, None

    def update(self, _id: int, new: Instance) -> Instance:
        i, inst = self.search(_id)
        if not inst:
            return None
        self.contents[i] = new
        new._id = inst._id
        return inst, new
