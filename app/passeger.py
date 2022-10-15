from flask import render_template, request, flash
from app.models import TripDriver, Place, User, db
from app.forms import NewtripForm
from config import Config
import logging.config

config = Config()
logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('passeger')


def check_user(function_to_decorate):
    def the_wrapper_around(form):
        if not check_user_key(int(form.userid.data), form.userkey.data):
            logger.debug('Not valid user')
            return fill_form(form, flashtext='Users error')
        return function_to_decorate(form)

    return the_wrapper_around


def check_user_key(userid: int, userkey: str) -> bool:
    return userkey == User.getkey(userid)


def index():
    return render_template('index.html')


def savetrip():
    form = NewtripForm(request.form)
    return sevetripform(form)


@check_user
def sevetripform(form):
    if not form.validate_on_submit():
        logger.debug('Not valid form')
        return fill_form(form, flashtext='Not valid form')
    form.townfromid = Place.getidtown(town=form.fromplace.data)
    form.towntoid = Place.getidtown(town=form.toplace.data)
    if not form.checklocate():
        logger.debug('Not valid towns')
        logger.debug(form.fromplace.data)
        logger.debug(form.toplace.data)
        return fill_form(form)
    saveindatabase(form)
    return render_template('gonetrip.html')


def saveindatabase(form):
    trip = TripDriver()
    trip.from_place = form.townfromid
    trip.to_place = form.towntoid
    trip.driver_id = form.userid.data
    trip.seat = form.seatstrip.data
    trip.date_order = form.datetrip.data
    trip.pay = form.paytrip.data
    trip.period_order = form.periodtrip.data
    trip.comment = form.tripcomment.data

    try:
        db.session.add(trip)
        db.session.commit()
    except:
        logging.error('Error database')
        raise
    return True


def fill_form(form, flashtext=''):
    if not flashtext == '':
        flash(flashtext)
    return open_form(form, form.userid.data, form.userkey.data)


def newtrip(userid, userkey):
    if not check_user_key(userid, userkey):
        logger.debug('Not valid user')
        return render_template('error.html')
    form = NewtripForm(request.form)
    return open_form(form, userid, userkey)


def open_form(form, userid, userkey):
    timetrip = config.TIMETRIP
    towns = Place.query.all()
    user = {'id': userid, 'key': userkey}
    return render_template('newtrip.html', user=user, towns=towns, form=form, timetrip=timetrip)
