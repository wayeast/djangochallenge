from a2r_app import app


class Arabic2Roman(object):
    def __init__(self, num):
        self._baseten = num
        self.romnum = convert(self._baseten)


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


def convert(baseten_num):
    magnitudes = get_magnitudes_as_dict(baseten_num)
    app.logger.debug("Base ten {} yields magnitudes {}".format(
        baseten_num, str(magnitudes)))
    romnum = get_numeral_from_magnitudes(magnitudes)
    app.logger.debug("Magnitudes {} yields RN {}".format(
        str(magnitudes), romnum))
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
