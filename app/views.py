from flask import Blueprint
from app import passeger

mainroute = Blueprint('mainroute', __name__)


@mainroute.route('/')
def index():
    return passeger.index()


@mainroute.route('/savetrip',  methods=['POST'])
def savetrip():
    return passeger.savetrip()


@mainroute.route('/newtrip/<userid>/<userkey>', methods=['GET', 'POST'])
def newtrip(userid, userkey):
    return passeger.newtrip(userid, userkey)
