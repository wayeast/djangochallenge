from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange


class A2RInputForm(Form):
    num = IntegerField('num',
                       validators=[DataRequired(),
                                   NumberRange(1, 3999)])
