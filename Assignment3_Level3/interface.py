"""
Database Model interface for the COMP249 Web Application assignment

@author: steve cassidy
"""

import datetime


def position_list(db, limit=10):
    """Return a list of positions ordered by date
    db is a database connection
    return at most limit positions (default 10)

    Returns a list of tuples  (id, timestamp, owner, title, location, company, description)
    """

    """Get the positions data from database"""
    cursor = db.cursor()
    cursor.execute("SELECT * from positions order by timestamp DESC")
    result = cursor.fetchall()

    final_data = []

    """Reformatting the job description to display only first 100 characters and adding Read More link"""
    for x in result:
        lst = list(x)
        desc = lst[6]
        desc = str(desc[0:100])
        desc = desc+"  ... <a href=/positions/"+str(lst[0])+">Read More</a>"
        lst[6] = desc
        x = tuple(lst)

        final_data.append(x)

    my_result = []

    """If limit is greater than  records then return current list"""
    if limit > len(final_data):
        return result

    """If limit is less than  records then return only required records"""
    for count in range(0, limit):
        my_result.append(final_data[count])

    return my_result


def position_get(db, id):
    """Return the details of the position with the given id
    or None if there is no position with this id

    Returns a tuple (id, timestamp, owner, title, location, company, description)

    """
    """Get the positions data from database"""
    position_data=[]
    cursor = db.cursor()
    cursor.execute("SELECT * from positions where id =(?)", (id,))
    myresult = cursor.fetchall();

    """Return required details of position"""
    for record in myresult:
        for data in record:
            position_data.append(data)

    """Return None if no records are found"""
    if(len(position_data)==0):
        return None
    return position_data


def position_add(db, usernick, title, location, company, description):
    """Add a new post to the database.
    The date of the post will be the current time and date.
    Only add the record if usernick matches an existing user

    Return True if the record was added, False if not."""

    """Get the users data from database"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users where nick=(?)", (usernick,))
    result = cursor.fetchall()

    """Check if user exist if yes insert new position into the database and return true else return false"""
    if len(result) == 0:
        return False
    else:
        cursor.execute("INSERT INTO positions(timestamp,owner,title,location,company,description) VALUES(?,?,?,?,?,?)",
                       (str(datetime.datetime.now()),usernick,title,location,company,description,))

        db.commit()
        return True
