# Apriori-and-FPGrowth-on-adult-census-dataset
Implement Apriori and FPGrowth algorithms on UCI adult census dataset to find frequent patterns in [' workclass', ' marital-status', ' occupation', ' relationship', ' race', ' sex', ' native-country', ' education'] attributes.

Apriori method will output all frequent pattens from 1-itemset to 8-itemsets (if there exists). Especially, I used hash table when programming in order to improve the efficiency. However, it still takes a while and your patience to wait for all the results being printed.

FPgrowth method will output all frequent itemsets it finds. Sorry for not organizing the results into a sorted form due to the time limit, but the code works well. It turns out that FPGrowth method is much faster than Apriori when working on a large scale of dataset.


Cd to the current firectory and run main.py in this format: python main.py ALGORITHM_NAME

For example,

`python main.py Apriori`  
`python main.py FPGrowth`  

The minimum support value is a global value fixed at 2000. You can change it in code if you want, but make sure make this change in all main.py, Apriori.py, and FPGrowth.py files.


