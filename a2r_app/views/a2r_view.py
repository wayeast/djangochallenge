from flask import render_template, request
from a2r_app import app
from a2r_app import forms
from a2r_app import Arabic2Roman


@app.route('/', methods=['GET', 'POST'])
@app.route('/arabic2roman', methods=['GET', 'POST'])
def a2r_convert():
    a2r = None
    fm = forms.A2RInputForm(formdata=request.form)
    if fm.validate_on_submit():
        a2r = Arabic2Roman(fm.num.data)
    return render_template('a2r_main.html',
                           title='Convert Arabic to Roman',
                           form=fm,
                           rn=(a2r.romnum if a2r
                               else '<i>Valid input required...</i>'))
