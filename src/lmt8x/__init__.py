__version__ = '0.0.0'


def lmt8x_v2t(model, v):
    if model == 'lmt84':
        from .lmt84 import transfer_table
    elif model == 'lmt85':
        from .lmt85 import transfer_table
    elif model == 'lmt86':
        from .lmt86 import transfer_table
    elif model == 'lmt87':
        from .lmt87 import transfer_table
    else:
        raise ValueError('invalid model "%s"' % model)

    vout = transfer_table['vout']
    start = transfer_table['range'][0]

    if v > vout[0] or v < vout[-1]:
        raise ValueError('v out of range')

    # binary search
    left = 0
    right = len(vout) - 1

    while left < right - 1:
        middle = (left + right) // 2

        # found exact value
        if vout[middle] == v:
            return start + middle

        elif vout[middle] > v:
            left = middle

        else:
            right = middle

    return start + (vout[left] - v) / (vout[left] - vout[right]) + left


def lmt84_v2t(v):
    return lmt8x_v2t('lmt84', v)


def lmt85_v2t(v):
    return lmt8x_v2t('lmt85', v)


def lmt86_v2t(v):
    return lmt8x_v2t('lmt86', v)


def lmt87_v2t(v):
    return lmt8x_v2t('lmt87', v)
