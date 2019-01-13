__author__ = 'Steve Cassidy'

from bottle import Bottle, template, static_file, request,redirect

import interface
import users

app = Bottle()

info = {
        'message': '',
        'rows':''
    }

@app.post('/login')
def login_req(db):
    """Authenticate user. If it is a valid user redirect to customized home page else redirect to mainpage"""

    #get post parameter
    username = request.forms.get("nick")
    password = request.forms.get("password")

    #check if user is valid if yes append username to greeting message else indicate login error message
    if(users.check_login(db,username,password)):
        users.generate_session(db,username)
        info['message']='Logged in as '+str(username)
        redirect('/')
    else:
        data = interface.position_list(db, 10)
        info['rows'] = data;
        info['message'] = 'Login Failed, please try again'
        return template("index",info)


@app.post('/post')
def post_job(db):
    """Save the new job details entered by user in the positions table"""

    #get post parameter
    username = users.session_user(db)
    position = request.forms.get("title")
    location = request.forms.get("location")
    company = request.forms.get("company")
    description = request.forms.get("description")

    #insert data into positions table
    interface.position_add(db,username,position,location,company,description);

    #reset error message
    info['message'] = ''
    return redirect("/")


@app.post('/logout')
def logout_req(db):
    """The method terminates the users session and redirects to mainpage"""
    username=users.session_user(db)

    #delete user cookie
    users.delete_session(db,username)

    # reset error message
    info['message'] = ''
    return redirect("/")


@app.route('/')
def index(db):
    """Computes the recent 10 job postings and displays it on mainpage"""
    data = interface.position_list(db, 10)
    info['rows']=data;

    user=request.get_cookie('sessionid')

    #if session  already exist display customized homepage else display mainpage
    if user == None:
        return template('index',info)
    else:
        info['message'] = 'Logged in as ' +users.session_user(db)
        return template('index_logout', info)


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


@app.route('/images/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='images')


@app.route('/positions/<DD>')
def read_more(db, DD):
    """displays detailed position job description when user clicks 'Read More' link """
    position_data = interface.position_get(db, DD)
    return template('positionDetails', rows=position_data)


@app.route('/about')
def index(db):
    """Returns the about page"""
    return template('about')


if __name__ == '__main__':

    from bottle.ext import sqlite
    from database import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
