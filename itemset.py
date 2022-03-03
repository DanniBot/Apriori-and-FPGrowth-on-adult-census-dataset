import collections as col

features=[' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education']
MIN_SUP=3000

class Itemsets:
    def __init__(self, k, data=None, l_prev=None):
        self.k=k
        if k==1:
            self.l=[{x} for x in range(8)]
            self.freq_items=self.find_1_item(data)
        else:
            self.freq_items=[]
            self.l=self.apriori_gen(l_prev)
        
    

    def find_1_item(self, data):
        count=[]
        for f in features:
            c=col.Counter(data[f])
            dic=dict(c)
            dic={frozenset([key]):val for key, val in dic.items() if val>= MIN_SUP and key!=' ?'}
            count.append(dic)
        return count



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


    def apriori_gen(self, l_prev):
        # l is L_K-1 
        C_k=[]
        for i in range(len(l_prev)):
            item1=l_prev[i]
            for j in range(i+1, len(l_prev)):
                item1_lst=list(item1)
                item2=l_prev[j]
                item2_lst=list(item2)
                if item1_lst[:self.k-2] == item2_lst[:self.k-2] and item1_lst[-1]<item2_lst[-1]:
                    item1_lst.append(item2_lst[-1])
                    c=set(item1_lst)
                    if not self.has_infrequent_subset(l_prev, c):
                        C_k.append(c)
        return C_k
                

    

            


def find_2_item(data, one_item, min_sup=3000):
    feature_2=[]
    for i in  range(8):
        temp=set()
        temp.add(i)
        for j in range(i+1,8):  
            temp.add(j)
            feature_2.append(temp)
            temp={i}
    print(feature_2)
    count=[]
    for f in feature_2:
        temp=[]
        a, b = list(f)[0], list(f)[1]
        item1, item2 = one_item[a], one_item[b]
        dic={}
        for x in item1.keys():
            for y in item2.keys():
                key=x.union(y)
                dic[key]=0
        for _, point in data.iterrows():
            for key in dic.keys():
                label=list(key)
                if point[features[a]]==label[1] and point[features[b]]==label[0]:
                    dic[key]+=1
        dic={key: val for key, val in dic.items() if val>=min_sup}
        if dic:
            temp.append(dic)
            count.append((f, temp))
    print(len(count))
    print(count)

    






