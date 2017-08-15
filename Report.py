#!/usr/bin/python3
from ReportDB import report
# creating an object from the main Report class at ReportDb module
logreport = report()
# creating flag variable
count = 0
# start getting data of the most popular articles in the database
print("\nthe most popular articles are :\n=================================")
# execute popular_article() method and assign results to
# articles variable which is a list of tuples
articles = logreport.popular_article()
# looping on articles and print its data
for row in articles:
    count = count + 1
    print(
        "\n Article #  " + str(count) + "  is :" +
        str(row[0] + "\t number of View is : " + str(row[1]))
        )
# start getting data of the most popular articles in the database
print("\nthe Most Popular authors are :\n=================================")
# execute popular_author() method and assign results to
# authors variable which is a list of tuples
authors = logreport.popular_author()
count = 0
# looping on authors and print its data
for row in authors:
    count = count + 1
    print(
        "\nName of Author #  " + str(count) + "  is :" +
        str(row[0] + "\t  his articles Viewed : " + str(row[1]))
        )

# start getting data of the Bad Day in the database
print("\nThe Bad Days are :\n===============")
# execute bad_day() method and assign results to Bad_Day
# variable which is a list of tuples
Bad_Day = logreport.bad_day()
count = 0
# looping on Bad_Day and print its data
for row in Bad_Day:
    count = count + 1
    print(
        "\n Day # " + str(count) + " is :    " + str(row[0]) +
        "\nError Queries:     " + str(row[1]) + "\ntotal queries:     " +
        str(row[2]) + "\npercent of error:    " +
        str(round(row[3] * 100, 2)) + " %\n"
        )
