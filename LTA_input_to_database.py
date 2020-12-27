import re


# functions for data validation with regexp

#for date
def is_date(val):
    val = "dummy123" 
    while not re.match((r"\d{4}-\d{2}-\d{2}|^Null$"), val):
        val = input("Entered wrong data format please try (yyyy-mm-ddd) or Null \n")
    else:
        print("Dataformat valid")
        pass
#\w{4}

# to check if there is only three word chars or Null
def is_three_wchar(value):
    value = "dummy123"
    while not re.match(r"\b\D{1,3}\b|^Null$", value):
        value = input("Please enter the correct format, in this field 3 word charaters or Null is allowed \n")
    else:
        print("dataformat valid")
        pass

# to check if there is only there digits or null
# def is_three_dchar(value):
#     value = "dummy123"
#     while not re.match(r"\b\d{1,3}\b|^Null$", value):
#         value = input("please try again. This field takes max three digits or null!\n")
#     else:
#         print("Valid format!")
#         pass
def is_three_dchar(val):
    while not re.match(r"\b\d{1,3}\b|^Null$", str(val)):
            val = input("please try again. This field takes max three digits or null!\n")


# ro check if there is only one word chars of null

# class for each record, each captive has 31 properties. The calss will make the the sql execution easier as the data is oragnised already.
class Record:
    def __init__(self, Volume, ID, Name_with_aliases, Sex, Height_cm, Build, Dentition, Special_Peculiarities, Date_of_Birth, Place_of_Birth, Place_of_Residence, Address, Religion, Childhood_status, Marital_Status, Number_of_Children, Occupation, Occupation_2, Occupation_3, Military_Service, Literacy,  Education, Criminal_History,  Crime_Sentence_Begins, Sentence_Expires, Prison_Term_day, Ransome, Associates, Degree_of_the_Crime, Degree_of_the_Punishment, Notes_Arrest_Site ):
        self.Volume = Volume , 
        self.ID = ID,
        self.Name_with_aliases = Name_with_aliases, 
        self.Sex = Sex, 
        self.Height_cm  =  Height_cm, 
        self.Build  = Height_cm, 
        self.Dentition = Dentition, 
        self.Special_Peculiarities = Special_Peculiarities,
        self.Date_of_Birth = Date_of_Birth, 
        self.Place_of_Birth = Place_of_Birth, 
        self.Place_of_Residence = Place_of_Residence, 
        self.Address= Address, 
        self.Religion = Religion, 
        self.Childhood_status = Childhood_status, 
        self.Marital_Status = Marital_Status, 
        self.Number_of_Children = Marital_Status, 
        self.Occupation  = Occupation, 
        self.Occupation_2 = Occupation_2, 
        self.Occupation_3 = Occupation_3, 
        self.Military_Service = Military_Service, 
        self.Literacy = Literacy,  
        self.Education = Education, 
        self.Criminal_History = Criminal_History,  
        self.Crime_Sentence_Begins = Criminal_History, 
        self.Sentence_Expires = Sentence_Expires, 
        self.Prison_Term_day = Prison_Term_day, 
        self.Ransome =  Ransome, 
        self.Associates = Associates, 
        self.Degree_of_the_Crime = Degree_of_the_Crime, 
        self.Degree_of_the_Punishment = Degree_of_the_Punishment, 
        self.Notes_Arrest_Site = Degree_of_the_Punishment 


#every each new record should have a method verify whith option to overwrite
    def show_record(self,):
        pass

    def verify_data(self):
        pass
#every each new record shuld have a new mehod called execute


# all the input should be callable at once


# create a workflow which creates gets the data.

#inputs


#when it is ok, pass it to the database





volume = input("What is the VOLUME? \n"),  # \d{3} 
is_three_dchar(volume)


id = input("what is the ID: \n"),
name_with_aliases = input("What is the NAME of the captive?\n"),
sex = input("Sex of the captive?\n")  # \w
while not re.match(r"\bf\b|\bn\b", sex): #checks if the info is .
    sex = input("Please enter n for woman or f for man\n")
else:
    pass

height_cm = input("Height?\n")  # \d{3}
is_three_dchar(height_cm)


build = input("Build? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", build) == None:
    is_three_wchar(build)
else:
    pass


dentition = input("Dentition? \n")  # \w
special_peculiarities = input("Any Special Peculiarities? \n")
date_of_birth = input("Date of Birth? \n")
if re.match((r"\d{4}-\d{2}-\d{2}"), date_of_birth) == None:
    is_date(date_of_birth)
else:
    pass
place_of_birth = input("Place of Birth? \n")  
place_of_residence = input("Place of Residence? \n")
address = input("Address? \n"),
religion = input("Religion? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", religion) == None:
    is_three_wchar(religion)
else:
    pass
childhood_status = input("Childhood status? \n")  # \w
marital_Status = input("Marital Status? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", marital_status) == None:
    is_three_wchar(marital_status)
else:
    pass
number_of_children = input("Number of Children? \n")  # \d{3}
is_three_dchar(number_of_children)


occupation = input("Occupation? \n")
# this should be pulled out from a pool based on occupation
occupation_2 = input("Occupation 2? \n")
# this needs to be pulled out from a pool based on occupation
occupation_3 = input("Occupation 3? \n")
military_service = input("Military Service? \n")
literacy = input("Literacy? \n")  # \w
education = input("Education \n")
criminal_history = input("Criminal History? \n")
crime_sentence_begins = input("Crime Sentence Begins? \n")
if re.match((r"\{4}-\d{2}-\d{2}"), crime_sentence_begins) == None:
    is_date(crime_sentence_begins)
else:
    pass
sentence_expires = input("Sentence Expires? \n")
if re.match((r"\d{4}-\d{2}-\d{2}"), sentence_expires) == None:
    is_date(sentence_expires)
else:
    pass
is_date(sentence_expires)
prison_term_day = input("Prison Term day? \n")
ransome = input("Ransome? \n")
associates = input("Associates? \n")
degree_of_the_crime = input("Degree of the Crime? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", degree_of_the_crime) == None:
    is_three_wchar(degree_of_the_crime)
else:
    pass
degree_of_the_punishment = input("Degree of the Punishment? \n")  # \w{3}
if re.match(r"\b\D{1,3}\b", degree_of_the_crime) == None:
    is_three_wchar(degree_of_the_crime)
else:
    pass
notes_arrest_site = input("Degree of the Punishment? \n")
# create the new Record
new_record = Record(Volume, ID, Name_with_aliases, Sex, Height_cm, Build, Dentition, Special_Peculiarities, Date_of_Birth, Place_of_Birth, Place_of_Residence, Address, Religion, Childhood_status, Marital_Status, Number_of_Children, Occupation, Occupation_2, Occupation_3, Military_Service, Literacy,  Education, Criminal_History,  Crime_Sentence_Begins, Sentence_Expires, Prison_Term_day, Ransome, Associates, Degree_of_the_Crime, Degree_of_the_Punishment, Notes_Arrest_Site.
