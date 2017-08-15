# reporting tool :
  it will use information from the database to discover what kind of articles the site's readers like.

#Installation:
  you have to follow the following steps to make the project run : 

    1- you have to download and install Python backage from [here](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi) 
    2- use terminal like Git Bash that comes with Git software
	2- install virtual box  to run virtual machine 
	3- install vagrant which enable you to configure virtual machine and let you share files between your host computer and the vm's file system , install it from vagrantup.com 
	4- download VM configuration from here : https://github.com/udacity/fullstack-nanodegree-vm.
	5- start virtual machine , from your terminal and inside vagrant directory at vm configuration directory , run thisa command Vagrant up  which will download linux operating system and install it 
	6- log into linux operating system by type vagrant ssh after previous step
	7- change directory to vagrant which is shared directory by  typing cd /vagrant
	8- load database data by running this command  psql -d news -f newsdata.sql where news is database name
	9- run psql news to connect to the database 
	10- create views top_articles , error , total_queries  as shows below in views defination section
	11- return back to vagrant directory by click on ctrl+d 
	12- create a directory called AnalysisReport inside vagrant directory and copy project files(reportDB.py,Report.py) into it
	13- change to AnalysisReport Directory 
	14 run the project by running this command  python Report.py


#Project Files : 

    1-ReportDB.py:
		is the main module which has the definition of the Report Class that is responsiple for connecting to database and has 3 methods beside condtrcutor and destructor of the class which are : 
		a- popular_article() : to get the most three popular articles in database 
		b- popular_author() : to get the most three popular authors in database
		c- bad_day() : to get which days did more than 1% of requests lead to errors 
		d- constructor __init__(): to connect to database when an object from the class is created 
		e- destructor __del__() : to close any connection and return resources to pc 

    2-Report.py:
		is the running python file which used to handle ReportDB module and run its methods then print output to the command line  


#Views Definitions:
 
	1- top_articles:
		create view top_articles as
		SELECT articles.author, articles.title, tt.num
		FROM articles, ( SELECT log.path, count(log.path) AS num FROM log where log.status = '200 OK'
        GROUP BY log.path) AS tt WHERE tt.path like concat('%', articles.slug, '%')
        ORDER BY tt.num DESC;


	2- error : 
		create view error as 
		SELECT date(log.time) AS day, count(log.status) AS total FROM log
  		WHERE log.status like '%404%'
  		GROUP BY date(log.time)
  		ORDER BY date(log.time);

  	3- total_queries:
		create view total_queries as
		SELECT date(log.time) AS day, count(log.status) AS total FROM log
  		GROUP BY date(log.time)
  		ORDER BY date(log.time);
  
#License: 
	The contents of this repository are covered under the [MIT License](https://github.com/udacity/ud777-writing-readmes/blob/master/LICENSE).