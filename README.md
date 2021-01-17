# LTA-database

RD for the Letartoztatottak torteneti adatabazis ( Historical databse of Captive)
16.12.2020 the data from the oroginal excel sheet was transformed to a sqlite databse.

LTA_input_to_database.py is the main file of the application planned to help build and analyze the database 

The python – sql project is established on the following: 

This is one of the largest historical databases in Middle-Europe which records such data. 

We are still receiving request from graduate students who are willing to work on the project. 

And! It is a really good playground for me to learn coding. 

 

##stages  between the <# #> stager are done: 

<#1. Input goes to an intermediate dict where the user can see/modify the input before sends it to the database.
1/a  mograte from sqlite to mysql to have more datatype and have chance for more complex analysis.  
   The test of this stage is performed by the old research team. #> 

2. GUI is needed to make it usable for others. In this stage a local database should be created which will make the upload possible via emails. 
   a. Flask and FLASKWTF is used to create the needed API-s
   b. logon system 
   b. grid styling on the css layer (looking for inspiring form ideas. Visual design is not my strong suit, they tend to say ...)

3. the third stage will happen when the database and the front will be migrated to the AWS 
   a. AWS design is 'ready' Although it is tempting to build a decent (ALB-ELB <-> 2(or3) EC2 instance in autoscaling groups <-> RDS on postgres)  infrastructure at the moment EC2 price scaled spot instances and self-managed nginx and postgresql databases are the most possible. 
   b.Additional features like the visualized data or Gis might bring more visitors and support. So this can be changed over time.


