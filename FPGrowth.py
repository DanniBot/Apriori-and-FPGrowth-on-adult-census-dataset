import collections as col


features=[' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education']
MIN_SUP=2000


class FPnode(object):

    def __init__(self, name, count, parent):
        self.name = name
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
#header is a dict of which the key is 'item name' and the value is [their occurance times, link].


def createTree(header,data):
    root=FPnode('Null', 0, None)
    for _, sample in data.iterrows():
        path=[]
        for item in sample:
            if item in header:
                path.append((item, header[item][0]))
        if path:
            sortedPath=[x[0] for x in sorted(path, key=lambda x:x[1], reverse=True)]
            updateTree(sortedPath, root, header)
    return root


def updateTree(sortedPath, cur_node, header):
    cur_item=sortedPath.pop(0)
    # if current item is one of the current node's children
    if cur_item in cur_node.children:
        cur_node.children[cur_item].count+=1
    else:  # is not
        cur_node.children[cur_item]=FPnode(cur_item,1, cur_node)
        if header[cur_item][1]==None:
            header[cur_item][1]=cur_node.children[cur_item]
        else:
            updateHeader(header, cur_item, cur_node.children[cur_item])
    if sortedPath:
        updateTree(sortedPath, cur_node.children[cur_item], header)
        


def updateHeader(header, item, node):
    flag=header[item][1]
    while flag.next!=None:
        flag=flag.next
    flag.next=node


def findPath(header, root):
    dic={}
    for key, val in header.items():
        node=val[1]
        all_path=[]
        while node.next!=None:
            if not node.children:
                flag=node
                path=[]
                while flag.parent!=root:
                    path.append(flag.parent.name)
                    flag=flag.parent
                if path:
                    all_path.append((list(reversed(path)), node.count))
            node=node.next
        dic[key]=all_path
    return dic


    

            





        
    

