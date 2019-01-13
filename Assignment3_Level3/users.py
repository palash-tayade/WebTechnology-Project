"""
Created on Mar 26, 2012

@author: steve
"""
import database
import bottle
import random
import string

# this variable MUST be used as the name for the cookie used by this application
COOKIE_NAME = 'sessionid'


def check_login(db, usernick, password):
    """returns True if password matches stored"""

    #get password hash
    pass_hash= database.password_hash(password)

    #get actual password hash stored in database
    cursor = db.cursor();
    cursor.execute("SELECT * FROM users where nick=(?) AND password=(?)", (usernick,pass_hash))
    result = cursor.fetchall()

    #if both are same return true
    if(len(result)!=0):
        return True


def generate_session(db, usernick):
    """create a new session and add a cookie to the response object (bottle.response)
    user must be a valid user in the database, if not, return None
    There should only be one session per user at any time, if there
    is already a session active, use the existing sessionid in the cookie
    """
    cursor = db.cursor();
    cursor.execute("SELECT * FROM users where nick=(?)", (usernick,))
    result = cursor.fetchall()

    #check if valid user
    if (len(result) == 0):
        return None

    cursor.execute("SELECT sessionid FROM sessions where usernick=(?)", (usernick,))
    session_id=cursor.fetchall()

    #check if session already exist if yes return the same session else create new session
    if(len(session_id) != 0):
        for temp in session_id:
            bottle.response.set_cookie("sessionid", str(temp[0]))
            return temp[0]
    else:
        session_key=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))
        cursor.execute("INSERT INTO sessions(sessionid,usernick) VALUES(?,?)",
                       ( session_key,usernick))
        db.commit()
        bottle.response.set_cookie("sessionid",session_key)
        return session_key


def delete_session(db, usernick):
    """remove all session table entries for this user"""

    #terminate session
    cursor=db.cursor()
    cursor.execute("DELETE FROM sessions where usernick=(?)", (usernick,))
    db.commit()

    #remove any stale cookie
    bottle.response.set_cookie("sessionid","",expires=0)

def session_user(db):
    """try to
    retrieve the user from the sessions table
    return usernick or None if no valid session is present"""
    session_id=bottle.request.get_cookie("sessionid")
    cursor=db.cursor();
    cursor.execute("SELECT usernick FROM sessions where sessionid=(?)", (session_id,))
    user=cursor.fetchall()

    #return username of currently logged in user
    if(len(user)==0):
        return None
    else:
        for row in user:
            return row[0]