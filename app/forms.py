from wtforms import Form, StringField, validators


class NewtripForm(Form):
    fromplace = StringField('fromplace', [validators.InputRequired(), validators.Length(min=6, max=25)])
    toplace = StringField('toplace', [validators.InputRequired(), validators.Length(min=3, max=25)])
    datetrip = StringField('datetrip', [validators.InputRequired(), validators.data_required()])
    periodtrip = StringField('periodtrip', [validators.InputRequired(), validators.Length(min=3, max=25)])
