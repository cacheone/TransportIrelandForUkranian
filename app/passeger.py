from flask import render_template, request, flash
from app.models import TripDriver, Place, User, db
from app.forms import NewtripForm
from config import Config
import logging.config

config = Config()
logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('passeger')


def index():
    return render_template('index.html')


def savetrip():
    form = NewtripForm(request.form)
    if not form.validate_on_submit():
        logger.debug('Not valid form')
        return fill_form(form)

    form.userkeydb = User.getkey(userid=form.userid.data)
    if not form.checkuser():
        logger.debug('Not valid user')
        return fill_form(form, flashtext='Users error')

    form.townfromid = Place.getidtown(town=form.fromplace.data)
    form.towntoid = Place.getidtown(town=form.toplace.data)

    if not form.checklocate():
        logger.debug('Not valid towns')
        logger.debug(form.fromplace.data)
        logger.debug(form.toplace.data)
        return fill_form(form)

    if not saveindatabase(form):
        logger.debug('Not work database')
        return fill_form(form, flashtext='Not work database')

    return render_template('gonetrip.html')


def saveindatabase(form):
    newtrip = TripDriver()
    newtrip.from_place = form.townfromid
    newtrip.to_place = form.towntoid
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
        logging.error('Error database')
        return False
    return True


def fill_form(form, flashtext=''):
    if not flashtext == '':
        flash(flashtext)
    timetrip = config.TIMETRIP
    towns = Place.query.all()
    user = {'id': form.userid.data, 'key': form.userkey.data}

    return render_template('newtrip.html', user=user, towns=towns, form=form, timetrip=timetrip)


def newtrip(userid, userkey):
    form = NewtripForm(request.form)
    timetrip = config.TIMETRIP
    towns = Place.query.all()
    user = {'id': userid, 'key': userkey}
    return render_template('newtrip.html', user=user, towns=towns, form=form, timetrip=timetrip)
