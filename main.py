import pandas as pd
import Apriori as ap
import FPGrowth as fp
    
FILE = "./adult/adult.data"

features=[' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education']
MIN_SUP=2000

def main():
    data =  pd.read_csv(FILE, sep=",")
    
    '''
    itemsets1=ap.Itemsets(1)
    itemsets1.apriori(data)
    print(itemsets1)
    
    itemsets2=ap.Itemsets(2)
    itemsets2.apriori(data, itemsets1)
    print(itemsets2)

    itemsets3=ap.Itemsets(3)
    itemsets3.apriori(data, itemsets2)
    print(itemsets3)

    itemsets4=ap.Itemsets(4)
    itemsets4.apriori(data, itemsets3)
    print(itemsets4)

    itemsets5=ap.Itemsets(5)
    itemsets5.apriori(data, itemsets4)
    print(itemsets5)

    itemsets6=ap.Itemsets(6)
    itemsets6.apriori(data, itemsets5)
    print(itemsets6)

    itemsets7=ap.Itemsets(7)
    itemsets7.apriori(data, itemsets6)
    print(itemsets7)

    itemsets8=ap.Itemsets(8)
    itemsets8.apriori(data, itemsets7)
    print(itemsets8)
    '''
    
    dic={1:2, 2:3}
    for i in dic:
        print(i)

    

   
   
    


if __name__ == '__main__':
    main()