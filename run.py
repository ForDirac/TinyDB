from table.b_tree import Node, Pair
from table import Key
from DBMS import DBMS
    # root = Node(is_root=True)
    # p = Pair((3,'2004-04-06'), [1])
    # root = root.insert(p)
    # p = Pair((5,'2005-03-24'), [2])
    # root = root.insert(p)
    # p = Pair((5,'2005-03-24'), [3])
    # root = root.insert(p)
    # p = Pair((3,'2005-09-01'), [4])
    # root = root.insert(p)
    # p = Pair((2,'2005-09-01'), [5])
    # root = root.insert(p)
    # p = Pair((1,'2002-09-01'), [6])
    # root = root.insert(p)
    # p = Pair((1,'2002-09-01'), [7])
    # root = root.insert(p)
    # p = Pair((5,'2005-09-01'), [8])
    # root = root.insert(p)
    # p = Pair((5,'2006-09-01'), [9])
    # root = root.insert(p)
    # p = Pair((6,'2004-09-01'), [10])
    # root = root.insert(p)
    # p = Pair((6,'2004-10-01'), [11])
    # root = root.insert(p)
    # root.show(depth=0)
    # print("\n----DELETE result----")
    # p = Pair((5,'2005-03-24'), [3])
    # root = root.delete(p)
    # root.show(depth=0)
    # p = Pair((5,'2005-03-24'), [2])
    # root = root.delete(p)
    # root.show(depth=0)
db = DBMS((Key('rating'), Key('date'), 'mid', 'uid'))
if __name__ == '__main__':
    ###########################################################################
    ##   There are 5 APIs in this DBMS.                                      ##
    ##   db.insert(TUPLE)                # INSERT operation                  ##
    ##   db.delete(TUPLE_NUMBER)         # DELETE operation                  ##
    ##   db.search(KEY)                  # SEARCH operation                  ##
    ##   db.update(TUPLE_NUM, NEW_TUPLE) # UPDATE operation                  ##
    ##   db.show()                       # shows current table and b-tree    ##
    ###########################################################################
    ##   Schema                                                              ##
    ##   1. rating: integer type, key attribute                              ##
    ##   2. date  : date type, key attribute                                 ##
    ##   3. mid   : string type                                              ##
    ##   4. uid   : string type                                              ##
    ###########################################################################
    # Examples                                                                #
    db.insert((3, '2004-04-06', '1', '12'))                                   #
    db.insert((5, '2005-03-24', '2', '23'))                                   #
    db.insert((5, '2005-03-24', '3', '34'))                                   #
    db.insert((4, '2004-07-14', '4', '45'))                                   #
    db.insert((6, '2005-07-14', '5', '56'))                                   #
    db.insert((4, '2006-07-14', '6', '67'))                                   #
    db.insert((7, '2007-07-14', '7', '78'))                                   #
    db.insert((4, '2004-07-14', '8', '89'))                                   #
    db.insert((4, '2001-07-14', '9', '910'))                                  #
    db.insert((2, '2004-02-14', '10', '1011'))                                 #
    db.insert((4, '2004-07-14', '11', '1112'))                                 #
    db.insert((1, '2004-03-14', '12', '1213'))                                 #
    db.insert((2, '2004-11-14', '13', '1314'))                                 #
    db.insert((4, '2004-07-14', '14', '1415'))                                 #
    db.show()                                                               #
    db.search((5, '2005-03-24'))                                            #
    db.delete(2)                                                            #
    db.delete(3)                                                            #
    db.delete(4)                                                            #
    db.show()                                                               #
    db.update(1, (5, '2005-03-24', '2', '23'))                              #
    db.show()                                                               #
    ###########################################################################
                 ## Please Use Section Below to Test ##




    ###########################################################################
