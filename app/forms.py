from wtforms import StringField, IntegerField, validators
from flask_wtf import FlaskForm


class NewtripForm(FlaskForm):
    fromplace = StringField('fromplace', [validators.InputRequired(), validators.Length(min=3, max=32)])
    toplace = StringField('toplace', [validators.InputRequired(), validators.Length(min=3, max=32)])
    datetrip = StringField('datetrip', [validators.InputRequired(), validators.data_required()])
    periodtrip = StringField('periodtrip', [validators.InputRequired(), validators.Length(min=1, max=1)])

    userid = StringField('userid', [validators.InputRequired()])
    userkey = StringField('userkey', [validators.InputRequired()])
    seatstrip = StringField('seatstrip', [validators.InputRequired()])
    paytrip = StringField('paytrip', [validators.InputRequired()])
    tripcomment = StringField('tripcomment', [validators.InputRequired()])

    townfromid = IntegerField('townfromid')
    towntoid = IntegerField('towntoid')
    userkeydb = StringField('userkeydb')

    def checklocate(self):
        result = True
        if self.townfromid is None:
            self.fromplace.errors.append('Not found location')
            result = False
        if self.towntoid is None:
            self.toplace.errors.append('Not found location')
            result = False
        return result

    def checkuser(self):
        if self.userkey.data == self.userkeydb:
            return True
        return False
