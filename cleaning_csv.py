# this file attempts to serialize the data to be the best fit for the postgres when I convert the excel/csv to its final format

import re
from csv import reader


with open('lta.csv') as f:
    cases = reader(f)
    new_c = []
    for case in cases:      
        #cleaning up the variaty of the not available formats
        case = ['Null' if atr == ''  else atr for atr in case ]
        case = ['Null' if atr == 'na' else atr for atr in case]
        case = ['Null' if atr == 'NA' else atr for atr in case]
        case = ['Null' if atr == 'N.A' else atr for atr in case]
        case = ['Null' if atr == 'n.a' else atr for atr in case]
        
        for i in range(len(case)):
                        
                #cleaning up the various kind of date formats
                if re.match(r'\d\d\d\d[.|/]\d{1,2}[.|/]\d{1,2}', case[i]):
                    if case[i].count('.'):
                        t= case[i].split('.')  
                        t = f"{t[0]}-{t[1]}-{t[2]}"
                        new_c.append(t)



                    elif case[i].count('/'):
                        t= case[i].split('/')
                        t = f"{t[0]}-{t[1]}-{t[2]}"
                        new_c.append(t)

                
                elif re.match(r'\d{1,2}[.|/|-]\d{1,2}[.|/|-]\d\d\d\d', case[i]):
                    if case[i].count('.'):
                        t= case[i].split('.')
                        t = f"{t[-1]}-{t[1]}-{t[0]}"
                        new_c.append(t)


                    elif case[i].count('/'):
                        t= case[i].split('/')
                        t = f"{t[-1]}-{t[1]}-{t[0]}"
                        new_c.append(t)

                        
                    elif case[i].count('-'):
                        t= case[i].split('-')        
                        t = f"{t[-1]}-{t[1]}-{t[0]}"
                        new_c.append(t)
                    
                    print(new_c)
                elif re.match(r'\d\d\d\d[/|.|-]\w{1,2}[/|-|.]\w{1,2}', case[i]):
                    print(case[i])
                

                else:
                    t= case[i]
                    new_c.append(t)
                                
                    ind = i
                print(new_c)
                    #replace the word characters with the 01-01 and append the 'note' = 'date is nut sure' 

                
                # else:
                    # print(c[i])



        #data colums also need to receive '' instead of Null so they need to be replaced again to get the null value of the DATE fieled
