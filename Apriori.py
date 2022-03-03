import itemset as it

def apriori(data):
    result=[]
    itemsets1=it.Itemsets(1, data)
    result.append(itemsets1)
    for i in range(2,9):
        prev=result[-1].deepcopy()
        itemsets=it.Itemsets(i, l_prev=prev.l)
        
        

