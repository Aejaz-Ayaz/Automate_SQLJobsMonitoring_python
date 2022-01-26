# Automate_SQLJobsMonitoring_python

Using python 3rd party modules we can automate the job of getting list of all the failed SQL agents jobs in the given SQL server instance.
You need below 3 modules to be installed

pip install pandas

pip install sqlalchemy

pip install pyodbc        # Though this module is not imported in the code, but it has the dependency. Hence installation is mandatory.

You can either run it manually or put the code file in Task Scheduler, to run it everyday on its own and output the results in a text file. 
