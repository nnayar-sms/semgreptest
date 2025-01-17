import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # ruleid: ssc-6b63f2b3-0c9e-08c0-7d88-008348d77839
        cursor.execute(sql, {'one': 'webmaster@python.org', 'two': 'very-secret'})

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        # ok: ssc-6b63f2b3-0c9e-08c0-7d88-008348d77839
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
