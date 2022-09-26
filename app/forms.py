from wtforms import Form, StringField, validators


class NewtripForm(Form):
    fromplace = StringField('fromplace', [validators.InputRequired(), validators.Length(min=3, max=32)])
    toplace = StringField('toplace', [validators.InputRequired(), validators.Length(min=3, max=32)])
    datetrip = StringField('datetrip', [validators.InputRequired(), validators.data_required()])
    periodtrip = StringField('periodtrip', [validators.InputRequired(), validators.Length(min=1, max=1)])

    userid = StringField('userid', [validators.InputRequired()])
    userkey = StringField('userkey', [validators.InputRequired()])
    seatstrip = StringField('seatstrip', [validators.InputRequired()])
    paytrip = StringField('paytrip', [validators.InputRequired()])
    tripcomment = StringField('tripcomment', [validators.InputRequired()])






