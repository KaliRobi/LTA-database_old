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
                    
                    # looking for the not complete dates in the databses. they are marked with year.hh.nn (Hónap=month, Nap=day )
                elif re.match(r'\d{4}\.(\d{2}|[a-zA-Z]{2})\.([a-zA-Z]{2})', case[i]):
                    date_mod = case[i].split('.')                    
                    for u in range(len(date_mod)):
                        #looking for the ones where the month is there
                        if re.match(r'.\d{2}.',  date_mod[u]):
                            new_date = f'{date_mod[0]}-{date_mod[1]}-01'                            
                            case[-2] = f"{case[-2]}, Date modified from {case[i]} to {new_date} 0001." #0001 = dtae modified by us, code for easier auto filtering
                            #looking for the month if it is still not valid
                            if re.match(r'[a-z]',  date_mod[1]):
                                date_mod = new_date.split('-')                                                                    
                                new_date = f'{date_mod[0]}-01-{date_mod[2]}'
                                case[-2] = f"{case[-2]}, Date modified from {case[i]} to {new_date} 0001." #0001 = dtae modified by us, code for easier auto filtering
                                nums.append(new_date) 
                            else:
                                nums.append(new_date) 
                

                else:
                    t= case[i]
                    new_c.append(t)
                                
                    ind = i
                print(new_c)
                    #replace the word characters with the 01-01 and append the 'note' = 'date is nut sure' 

                
                # else:
                    # print(c[i])



        #data colums also need to receive '' instead of Null so they need to be replaced again to get the null value of the DATE fieled
