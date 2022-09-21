from wtforms import Form, StringField, validators


class NewtripForm(Form):
    fromplace = StringField('fromplace', [validators.Length(min=5, max=25)])
