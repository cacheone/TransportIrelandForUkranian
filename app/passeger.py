from flask import render_template, request, flash
from app.models import TripDriver, Place, db
from app.forms import NewtripForm
from config import Config
import logging.config


logging.config.dictConfig(Config.LOGGING_CONFIG)
logger = logging.getLogger('passeger')


def index():
    return render_template('index.html')


def savetrip():
    form = NewtripForm(request.form)
    if not form.validate():
        logger.debug('Not valid form')
        return fill_form(form, flashtext='Not valid form')

    townfromId = Place.getidtown(town=form.fromplace.data)
    towntoId = Place.getidtown(town=form.toplace.data)

    if not checklocate(townfromId, towntoId, form):
        logger.debug('Not valid towns')
        logger.debug(form.fromplace.data)
        logger.debug(form.toplace.data)
        return fill_form(form, flashtext='Not valid towns')

    if not saveindatabase(townfromId, towntoId, form):
        logger.debug('Not work database')
        return fill_form(form, flashtext='Not work database')


    return render_template('gonetrip.html')


def checklocate(townfromId,towntoId, form):
    result = True
    if townfromId == None:
        form.fromplace.errors.append('Not found town')
        result = False
    if towntoId == None:
        form.toplace.errors.append('Not found town')
        result = False
    return result

def saveindatabase(townfrom, townto, form):
    newtrip = TripDriver()
    newtrip.from_place = townfrom.id
    newtrip.to_place = townto.id
    newtrip.driver_id = form.userid.data
    newtrip.seat = form.seatstrip.data
    newtrip.date_order = form.datetrip.data
    newtrip.pay = form.paytrip.data
    newtrip.period_order = form.periodtrip.data
    newtrip.comment = form.tripcomment.data
    try:
        db.session.add(newtrip)
        db.session.commit()
    except:
        return False
    return True

def fill_form(form, userid='', userkey='', flashtext=''):
    if userid == '':
        userid = form.userid.data
    if userkey == '':
        userkey = form.userkey.data
    if not flashtext == '':
        flash('Error: ' + flashtext)
    towns = Place.query.all()
    user = {'id': userid, 'key': userkey}

    return render_template('newtrip.html', user=user, towns=towns, form=form)


def newtrip(userid, userkey):
    form = NewtripForm(request.form)
    return fill_form(form, userid, userkey)
