import pandas as pd
import configuration as config
import Apriori as ap
    

def main():
    data =  pd.read_csv(config.FILE, sep=",")
    '''
    #age
    sim.numeric(data, 4, 5, 'age')
    
    #fnlwgt
    sim.numeric(data, 4, 5, ' fnlwgt')

    #education-num
    sim.numeric(data, 4, 5, ' education-num')
   
    #capital-gain
    sim.numeric(data, 4, 5, ' capital-gain')

    #capital-loss
    sim.numeric(data, 4, 5, ' capital-loss')

    #hours-per-week
    sim.numeric(data, 4, 5, ' hours-per-week')
    
    
    
    #workclass
    sim.nominal(data, 4, 5, ' workclass')
    
    #marital-status
    sim.nominal(data, 4, 5, ' marital-status')

    #occupation
    sim.nominal(data, 4, 5, ' occupation')
    
    #relationship
    sim.nominal(data, 4, 5, ' relationship')
    
    #race
    sim.nominal(data, 4, 5, ' relationship')

    #sex
    sim.nominal(data, 4, 5, ' sex')
    
    #native-country
    sim.nominal(data, 4, 5, ' native-country')
    

    
    
    #education
    sim.ordinal(data, 4, 5, ' education')
    
    '''
    '''
    one_item=ap.find_1_item(data)
    count=ap.find_2_item(data, one_item)
    '''
    l=[{1,2}, {1,3}, {1,5}, {2, 3}, {2, 4}, {2, 5}]
    C_k=ap.apriori_gen(l, 3)
    print(C_k)
   
   
    


if __name__ == '__main__':
    main()