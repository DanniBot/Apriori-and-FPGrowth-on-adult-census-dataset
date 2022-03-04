import collections as col


features=[' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education']
MIN_SUP=2000


class FPnode(object):

    def __init__(self, item, count, parent):
        self.item = item
        self.count = count              # support
        self.parent = parent
        self.next = None                # the same elements
        self.children = {}





def createHeader(data):
    header={}
    for f in features:
        c=col.Counter(data[f])
        dic=dict(c)
        dic={key:[val,None] for key, val in dic.items() if val>= MIN_SUP and key!=' ?'}
        if dic:
            header.update(dic)
    return header


def createTree(header):
    if not header:
        return None
    freqItemSet = set(header.keys())
    fptree=FPnode('Null Set', 1, None)
    
