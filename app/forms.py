from wtforms import Form, StringField, validators


class NewtripForm(Form):
    fromplace = StringField('fromplace', [validators.InputRequired(), validators.Length(min=3, max=25)])
