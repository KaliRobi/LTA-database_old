# this file attempted to serialize the data to be the best fit for the postgres when I convert the excel to its final format

import re
from csv import reader
import psycopg2
from psycopg2 import pool


with open('lta.csv') as f:
    cases = reader(f)
    
    nums = []
    for case in cases:      
        #cleaning up the variaty of the not available formats
        case = ['Null' if atr == ''  else atr for atr in case ]
        case = ['Null' if atr == 'na' else atr for atr in case]
        case = ['Null' if atr == 'NA' else atr for atr in case]
        case = ['Null' if atr == 'N.A' else atr for atr in case]
        case = ['Null' if atr == 'n.a' else atr for atr in case]
        #print(case)
        new_c = []
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
                                new_c.append(new_date)
                                
                            else:
                                new_c.append(new_date)
                        
                
                        
                                
                else:
                    new_c.append(case[i]) 
                # if case[8] == 'Null':
                #     case[8] = None
                #     print(case[8])

        
        print(new_c)
        for i in range(len(new_c)):
            if new_c[4] == 'Null':
                    new_c[4] = None
            elif new_c[8] == 'Null':
                    new_c[8] = None
            elif new_c[15] == 'Null':
                    new_c[15] = None
            elif new_c[24] == 'Null':
                    new_c[24] = None
            elif new_c[25] == 'Null':
                    new_c[25] = None
            elif new_c[27] == 'Null':
                    new_c[27] = None
         # float values in the ransom filed...
        # if re.match(r'.\..', new_c[27]):
        #     new_c.split('.')
        
                    
                 
                            
               

        #print(new_c) 
        data_pool = psycopg2.pool.SimpleConnectionPool(1,20,
                                    dbname='lta_data',
                                    host='localhost',
                                    user = 'teszt_user',
                                    password = '123456')
        conn = data_pool.getconn()        
        with conn.cursor() as cursor:
            dbquery = "INSERT INTO teszt_lta (volume, id, name, sex, height, build, dentition, special_peculiarities, date_of_birth, place_of_birth, place_of_residence, residence, religion, childhood_status, marital_status, number_of_children, occupation, occupation_2, occupation_3, military_service, literacy, education, criminal_history, crime, sentence_begins, sentence_expires, prison_term_day, ransome, associates, degree_of_crime, degree_of_punishment, notes, arrest_site)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(dbquery, tuple(new_c))
        conn.commit()
        print('inserted row')
                        
