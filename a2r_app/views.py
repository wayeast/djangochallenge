import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render

from a2r_app.models import PurePower, EdgeCase


def a2r_convert(request):
    if request.method == 'POST' and doublecheck_valid(request.POST['num']):
        num = int(request.POST['num'])
        rn = convert(num)
    else:
        num = None
        rn = '<i>Please enter a valid number</i>'
    context = {'title': 'Convert Arabic to Roman',
               'num': num,
               'rn': rn}
    return render(request, 'a2r_app/main.html', context)


def doublecheck_valid(num):
    num = int(num)
    return num >= 1 and num <= 3999


def convert(num):
    magnitudes = get_magnitudes_as_dict(num)
    logger.debug("{} yields magnitudes {}".format(num, magnitudes))
    romnum = get_numeral_from_magnitudes(magnitudes)
    logger.debug("{} yields numeral {}".format(num, romnum))
    return romnum

def get_magnitudes_as_dict(num):
    magnitudes = dict()
    for v in PurePower.objects.values().order_by('-power'):
        pwr = v['power']
        magnitudes[pwr], rem = divmod(num, pow(10, pwr))
        num = rem
    return magnitudes


def get_numeral_from_magnitudes(magnitudes):
    romnum = ''
    edges = {i['invalid']: i['valid'] for i in EdgeCase.objects.values('invalid', 'valid')}
    for v in PurePower.objects.values().order_by('-power'):
        pwr = v['power']
        rep = v['roman_rep']
        n = ''
        for i in range(magnitudes[pwr]):
            n += rep
            if n in edges.keys():
                n = edges[n]
        romnum += n
    return romnum
