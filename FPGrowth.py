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

def findCondFP(CondPB):
    header_dic={}
    for key, val in CondPB.items():
        dic={}
        for path in val:
            if path[0]:
                one_condfp=dic.get(path[0][0],{})
                for item in path[0]:
                    one_condfp[item]=one_condfp.get(item,0)+path[1]
                dic[path[0][0]]=one_condfp
        header_dic[key]=dic
    

    for i, dic in header_dic.items():
        for key in dic:
            single_item=dic[key]
            single_item={item:val for item, val in single_item.items() if val>= MIN_SUP}
            dic[key]=single_item

        one_condfp=dic
        one_condfp={item:val for item, val in one_condfp.items() if len(val)!=0}
        header_dic[i]=one_condfp

    header_dic={item:val for item, val in header_dic.items() if len(val)!=0}


    return header_dic


def allSubsets(s):
    if len(s) == 0 :
        return [[]]
    return allSubsets(s[1:]) + [[s[0]] + r for r in allSubsets(s[1:])]


def find_freq(condFP,header):
    result={}
    for item, itemsets in condFP.items():
        dic={}
        for i in itemsets.values():
            for key, val in i.items():
                dic[key]=dic.get(key,0)+val
        sets=tuple(x for x in dic)
        subsets=allSubsets(sets)
        #subsets=[s.append(item) for s in subsets if len(s)>0]
        for freq_sets in subsets:
            if freq_sets:
                count=header[item][0]
                for single_item in freq_sets:
                    if dic[single_item]<count:
                        count=dic[single_item]
                freq_sets.append(item)
                result[frozenset(freq_sets)]=count
    return result



    


    

            





        
    

