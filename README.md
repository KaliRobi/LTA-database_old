# LTA-database



DBMS for Historical databse of Captive
This is an older, but not suprisingly life long, project of a couple of PhD and graduate students in 2015. As it turned out there is a historical resource in the Hungarian Archives which had recorded approx. 750 000 criminal accusations between 1932 and 1943. Each record kept the social-economic background of the accused person.This source is important for many fileds of researches, still, due to the mass of the records, processing takes time and effort. This is one of the reason why i decided to start this project. In short term the plan is to provide  an environment which provides a convenient platform  and country wide available for researchers who are willing to contribute.

Speaking of convenient... the html Ui pages at the moment are the bare minimum what i need for the backend. Memebers of the project 

 Obviously the project is also for my joy. To create something, enjoy and develope myself in Python, postgresql, frontend and IT infrastructure (AWS) at the same time.

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


