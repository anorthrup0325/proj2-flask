#! /usr/bin/env python3

""" For deployment on ix under CGI """

import site
site.addsitedir("/home/users/anthonyn/public_html/cis322/htbin/proj2-flask/env/lib/python3.4/site-packages")

import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from syllabus import app

CGIHandler().run(app)
