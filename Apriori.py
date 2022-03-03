import collections as col

features=[' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education']

def find_1_item(data, min_sup=3000):
    count=[]
    for f in features:
        c=col.Counter(data[f])
        dic=dict(c)
        dic={frozenset([key]):val for key, val in dic.items() if val>= min_sup and key!=' ?'}
        count.append(dic)
    return count


def apriori_gen(l, k):
    # l is L_K-1 
    l_copy=l
    for i in range(len(l)):
        item1=l[i]
        for j in range(i+1, len(l)):
            item2=l[j]
            if list(item1)[:k-1] == list(item2)[:k-1] and 

            


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

    






