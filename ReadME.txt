Student: Norman Wagner Bright
Student ID:160424285

The goal of this assignment is to be able to perform get from an API , and then GET,POST,DELETE and PUT from a database.

the 
The API used to get the GET is from the data police API specifically the stop and search.
For the API the get function was implemented this was done by launching an instance on putty from aws EC2, once it was launched a folder called week 10 was created which is where the code will be inserted as a Python file.
After the container is created which include e dockerfile and a requirements.txt, once the container is launched it will allow the user thanks to the pubblic aws IP to see the api.

the next task is to create a database with the API file,TheAPI used for this task is the Covid19 state current value in the US (https://covidtracking.com/api) , this can be done by using the csv, luckily this dataset already comes in both json and csv file so it was only a matter of downloading.
once it has been downloaded it is time to adding the dataset on the aws instance, to do this first we need to create the folder in our case week10, after we need to run a Cassandra instance within the docker once this is done we can then upload our dataset into it.
Once the dataset is uploaded it is time to create a table which is done in the following steps:
1) creation of keyspaces
2) Creation of the table
3) Copyy of the csv data into the table

Once this is done as visible from the code it is possible to execute a GET which will allow the user to check some statistics depending on the selected state, a DELETE which allow the user to delete a number of positive outcomes from the table, the POST method allows the user to add a new state:
the various url are:

- GET http://IP/covid19/AK
- DELETE curl -X "DELETE" http://IP/covid19/1777
- POST curl -X "POST" http://IP/Canada

Each has to be executed in a new terminal

Please note that app1.py is for the police API while app.py is for the covid19 API please change the CMD section in the Dockerfile accordingly