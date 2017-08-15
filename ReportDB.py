#!/usr/bin/python3
import psycopg2  # importin psycopg2 module to deal
# with postgresql database system


class report:
    """a calas which is responsiple for connectiiong to database 'news' and contain
     methods for all required tasks in the reporting tool
    """
# initializing public conn variable to None
    conn = None
# __init__ function or the constructor of the report class
# , initialize the instance , connect to the databse 'news'
#  and allocate a space in the memory for every
# object form the class

    def __init__(self):
        # try making connection to the databse
        try:
            # assign global conn variable to an connection
            # object by connecting to database
            self.conn = psycopg2.connect(database="news")
            print("\nconnection to Database is successfuly done ... ")
        # if there is an exception , print an error message to the user
        except:
            print("\nit is unable to connect to database ")


# definig popular articale method to get the most popular three articles

    def popular_article(self):

        cursor = self.conn.cursor()  # define cursor variable as public and
        # initialized it with cursor  object
        # query string to get the most popular articles using top_articles view
        query_string = """select title , num from
        top_articles order by num desc limit 3"""
        # execute the query string
        cursor.execute(query_string)
        # return results which is list of tuples
        return cursor.fetchall()
# definig popular author method to get the most popular three authors

    def popular_author(self):

        # define cursor variable as public and initialized it
        cursor = self.conn.cursor()
        # with cursor  object
        # query string to get the most popular authors , it is using a view
        # called top_articles
        query_string = """select authors.name , total from authors
                         , (select author , sum(num) as total from
                        top_articles group by author ) as cc where
                         authors.id = cc.author"""
        # execute the query string
        cursor.execute(query_string)
        # return results which is list of tuples
        return cursor.fetchall()

# definig error days method to get which days get 1% of requests lead to error

    def bad_day(self):
        # define cursor variable as public and initialized
        # it with cursor  object
        cursor = self.conn.cursor()
        # query string to get the Bad days , it is using
        # views error and total_queries
        query_string = """select error.day , error.total as errors ,
                         total_queries.total as queries , error.
                        total/cast(total_queries.total as float)
                         as err_percent from error join total_queries on
                        error.day = total_queries.day where error.total
                         > 0.01*total_queries.total order by err_percent desc
                     """
        # execute the query string
        cursor.execute(query_string)
        # return results which is list of tuples
        return cursor.fetchall()
# __del__ function or the destructor of the report class
# close connection to the databse 'news'
# deallocate a space in the memory for every
# object form the class

    def __del__(self):
        self.conn.close()
