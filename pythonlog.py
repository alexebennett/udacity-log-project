#!/usr/bin/python3

import psycopg2

DBNAME = "news"


def connect(database='news'):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        return db, c
    except:
        print('<error message>')


def query_1():
    popular_articles = """select count(substring(path,10)), articles.title from
              log join articles on articles.slug = substring(path,10)
              group by articles.title order by count(substring(path,10))
              desc;"""
    db, c = connect()

    c.execute(popular_articles)
    print("Most popular articles:")
    for (title, count) in c.fetchall():
        print("     {} views - {}".format(title, count))
    db.close()


def query_2():
    popular_authors = """select count(substring(path,10)), authors.name from log
              join articles on articles.slug = substring(path,10)join
              authors on authors.id = articles.author group by authors.name
              order by count(substring(path,10)) desc;"""
    db, c = connect()

    c.execute(popular_authors)
    print("Most popular authors:")
    for (name, count) in c.fetchall():
        print("     {} views - {}".format(name, count))
    db.close()


def query_3():
    error_percent = """select to_char as date, percent from (select to_char, ok,
              notfound, Round(100.0 * notfound/ok,2) AS percent FROM
              (select to_char, count(status) as total, sum( case when
              status='200 OK' then 1 else 0 end) ok, sum( case when
              status='404 NOT FOUND' then 1 else 0 end) notfound
              from (select to_char(time, 'Month DD, YYYY'), status
              from log) as char group by to_char order by to_char) as
              percenttable) as resulttable where percent > 1;"""
    db, c = connect()

    c.execute(error_percent)
    print("Days with more than 1 percent of requests leading to errors:")
    for (date, percent) in c.fetchall():
        print("     {} - {}%".format(date, percent))
    db.close()


def text():
    print("Please input query 1, 2 or 3.")
    print("1. What are the most popular three articles of all time?")
    print("2. Who are the most popular article authors of all time?")
    print("""3. On which days did more than 1 per cent of requests
        lead to errors?""")
    query = input("Option: ")

    if query == '1':
        query_1()

    if query == '2':
        query_2()

    if query == '3':
        query_3()

    query2 = input("Would you like to query the database again? (Y/N)")

    if query2 == 'Y':
        text()

text()
