#basic example of retrieving output
#first example, this worked in the spss syntax editor screen then output data in the spss output/viewer screen
#this is a python program in spss syntax, next we will try a python script in spss syntax, they offer different python functionalities and have to be separated due to how SPSS is configured

* Encoding: UTF-8.
* We start by creating some test data.
DATA LIST /VAR1 1-2 VAR2 4-5.
BEGIN DATA
23 11
48 15
62 17
END DATA.
* The Python block starts here.
BEGIN PROGRAM.
#Import the SPSS and SPSS Client modules.
import spss, SpssClient
 
# Start the SPSS Client. Always do this first.
SpssClient.StartClient()
 
# Submit some syntax string to SPSS.
spss.Submit("FREQ var1.")
END PROGRAM.

BEGIN   PROGRAM.
import spss
import SpssClient
SpssClient.StartClient()
i=0
while i<20:
   spss.Submit("FREQ VAR1.")
   i+=1
END PROGRAM.


*used this tutorial https://datascienceprojects.wordpress.com/2016/05/23/tutorial-using-python-programming-in-spss/


