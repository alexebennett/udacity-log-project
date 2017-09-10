# Python Log

Python Log is a Python DB API program used to interface with the news database and extract meaningful data from its contents.

# Requirments

Install VirtualBox onto your machine
Install Vagrant
Download the news data file
Download the Vagrant config file by cloning the original Udacity repository.

Run the vagrant virtual machine and change directories to the location of the newsdata.sql file. To load the relevant database, run:

```sh
$ psql -d news -f newsdata.sql
```

The program makes use of the psycopg2 Python library, used for querying Postgresql databases. 

Run the python;pg.py file:  

```sh
$ python3 pythonlog.py
```

in to your terminal after you have changed directories into the program's present working directory. This will load 3 questions into your terminal window, each of which is capable of being queried against the news database. 

After inputting your choice of question, the program will run the SQL query and output the results in to your terminal window. 
