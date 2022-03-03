import pandas as pd
import configuration as config
import itemset as it
    

def main():
    data =  pd.read_csv(config.FILE, sep=",")
    
    '''
    one_item=ap.find_1_item(data)
    count=ap.find_2_item(data, one_item)
    '''
    itemsets1=it.Itemsets(1, data)
    print(itemsets1.freq_items)
    print(itemsets1.l)
    itemsets2=it.Itemsets(2, l_prev=itemsets1.l)
    print(itemsets2.l)
   
   
    


if __name__ == '__main__':
    main()