from flask import render_template, request, redirect, flash, Blueprint
from app.models import TripDriver, Place, db
from app.forms import NewtripForm

mainroute = Blueprint('mainroute', __name__)

@mainroute.route('/savetrip',  methods=['POST'])
def savetrip():

    form = NewtripForm(request.form)
    if not form.validate():
        flash(request.url)
        towns = Place.query.all()
        driver = {'id': request.form.get('userid'), 'key': 222222, 'towns': towns}
        form.toplace.errors.append("!!!")
        return render_template('createtrip.html', driver=driver, form=form)

    townfrom = Place.query.filter_by(name_place=request.form.get('fromplace')).first()
    townto = Place.query.filter_by(name_place=request.form.get('toplace')).first()

    newtrip = TripDriver()
    newtrip.from_place = townfrom.id
    newtrip.to_place = townto.id
    newtrip.driver_id = request.form.get('userid')
    newtrip.seat = request.form.get('seatstrip')
    newtrip.date_order = request.form.get('datetrip')
    newtrip.pay = request.form.get('paytrip')
    newtrip.period_order = request.form.get('periodtrip')
    newtrip.comment = request.form.get('tripcomment')

    db.session.add(newtrip)
    db.session.commit()
    return render_template('gonetrip.html')


@mainroute.route('/createtrip/<userid>/<userkey>', methods=['GET', 'POST'])
def createtrip(userid, userkey):

    towns = Place.query.all()
    driver = {'id': userid, 'key': userkey, 'towns': towns}
    form = NewtripForm(request.form)
    return render_template('createtrip.html', driver=driver, form=form)
