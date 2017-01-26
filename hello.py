#!/usr/bin/env python

# ^ This is called the "shebang" Tells the os how to run the file.
import os
import json
import cgi
import Cookie 


form = cgi.FieldStorage()
username = form.getvalue('user')
password = form.getvalue('password')
C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])

print "Content-Type: text/html"
if str(username) == 'user' and str(password) == 'swordfish':
    print "Set-Cookie: loggedin=true"
print 
#This print ends the header
print "<HTML><BODY>"
print "<H1>Hello World!</H1>"
print "Your magic tracking number is: "
print form.getvalue('magic_tracking_number')
print "<P>Your Browser is"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
    print "Firefox!"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
    print "Chrome."
else:
    print os.environ['HTTP_USER_AGENT']

print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

print "<P>Username: " + str(form.getvalue('user'))
print "<P>Password: " + str(form.getvalue('password'))

if str(username) == 'user' and str(password) == 'swordfish':
    print "<P>LOGIN SUCCESSFUL"
if "loggedin" in C:
    print "<P>Logged In: " + str(C['loggedin'].value)
else:
    print "No Cookie"
