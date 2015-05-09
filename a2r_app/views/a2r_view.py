from flask import render_template, request
from a2r_app import app
from a2r_app import forms


@app.route('/', methods=['GET', 'POST'])
@app.route('/arabic2roman', methods=['GET', 'POST'])
def a2r_convert():
    romnum = default_romnum
    fm = forms.A2RInputForm(formdata=request.form)
    if fm.validate_on_submit():
        romnum = convert(fm.num.data)
    return render_template('a2r_main.html',
                           title='Convert Arabic to Roman',
                           form=fm,
                           dirs=directions,
                           rn=romnum)


#############################################################
#####     Auxiliary structures and functions     ############
#############################################################
directions = 'Enter a number <i>i</i> such that 1 <= <i>i</i> <= 3999.'


default_romnum = '<i>Valid input required...</i>'


oms = range(3, -1, -1)


pure_powers = {3: 'M',
               2: 'C',
               1: 'X',
               0: 'I'}


edges = {'CCCC': 'CD',
         'CDC': 'D',
         'DCCCC': 'CM',
         'XXXX': 'XL',
         'XLX': 'L',
         'LXXXX': 'XC',
         'IIII': 'IV',
         'IVI': 'V',
         'VIIII': 'IX'}


def convert(num):
    magnitudes = get_magnitudes_as_dict(num)
    romnum = get_numeral_from_magnitudes(magnitudes)
    return romnum


def get_magnitudes_as_dict(num):
    magnitudes = {}
    for m in oms:
        magnitudes[m], rem = divmod(num, pow(10, m))
        num = rem
    return magnitudes


def get_numeral_from_magnitudes(magnitudes):
    romnum = ''
    for m in oms:
        n = ''
        for i in range(magnitudes[m]):
            n += pure_powers[m]
            if n in edges.keys():
                n = edges[n]
        romnum += n
    return romnum
