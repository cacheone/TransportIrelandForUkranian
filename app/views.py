from flask import render_template, request, redirect, flash

from app.models import TripDriver, Place, db
from app.forms import NewtripForm
from app import app, config


country = '/' + config.COUNTRY


@app.route('/')
def index():
    return render_template('index.html')


@app.route(country+'/savetrip/', methods=['POST'])
def savetrip():

    form = NewtripForm(request.form)
    if not form.validate():
        flash(request.url)

        return redirect(country+'/createtrip/1/2222222')

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
    return render_template('gonedriver.html')


@app.route(country+'/createtrip/<userid>/<userkey>')
def createtrip(userid, userkey):
    towns = Place.query.all()
    driver = {'id': userid, 'key': userkey, 'towns': towns}
    return render_template('createdriver.html', driver=driver)
