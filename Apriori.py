import collections as col

features=[' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education']
MIN_SUP=2000

class Itemsets(object):


    def __init__(self, k, freq_items=[], l_k=[]):
        self.k=k
        self.freq_items=freq_items.copy()
        self.l_k=l_k.copy()

    def __str__(self):
        if not self.freq_items and not self.l_k:
            return f'frequent {self.k}-itemsets\nfrequent {self.k}-itemsets is null'
        return f'''{self.k}-itemsets\ncandidate {self.k}-itemsets is {self.l_k}\nfrequent {self.k}-itemset is {self.freq_items}\n'''
    
    __repr__ = __str__


    def find_1_item(self, data):
        for i, f in enumerate(features):
            c=col.Counter(data[f])
            dic=dict(c)
            dic={frozenset([key]):val for key, val in dic.items() if val>= MIN_SUP and key!=' ?'}
            if dic:
                self.freq_items.append(dic)
                self.l_k.append({i})



    @staticmethod
    def has_infrequent_subset(l_prev, c):
        c_lst=list(c)
        for i in range(len(c_lst)):
            c_copy=c_lst.copy()
            c_copy.pop(i)
            temp=set(c_copy)
            if temp not in l_prev:
                return True
        return False



    def apriori(self, data, prev=None):
        if self.k==1:
            self.find_1_item(data)
        else:
            for i in range(len(prev.l_k)):
                item1=prev.l_k[i]
                for j in range(i+1, len(prev.l_k)):
                    item1_lst=list(item1)
                    item2=prev.l_k[j]
                    item2_lst=list(item2)
                    if item1_lst[:self.k-2] == item2_lst[:self.k-2] and item1_lst[-1]<item2_lst[-1]:
                        item1_lst.append(item2_lst[-1])
                        c=set(item1_lst)
                        if not self.has_infrequent_subset(prev.l_k, c):
                            dic=self.find_freq(data, prev, i, j)
                            if dic:
                                self.l_k.append(c)
                                self.freq_items.append(dic)
        

    def find_freq(self, data, prev, i, j):
        freq_set1=prev.freq_items[i]    #{:}
        freq_set2=prev.freq_items[j]    #{:}
        dic={}
        for key1 in freq_set1.keys():
            for key2 in freq_set2.keys():
                freq=key1.union(key2)
                if len(freq)==self.k:
                    dic[freq]=0
        for _, point in data.iterrows():
            point=frozenset(point)
            for key in dic.keys():
                if key.issubset(point):
                    dic[key]+=1
        dic={key: val for key, val in dic.items() if val>=MIN_SUP}
        return dic




    






