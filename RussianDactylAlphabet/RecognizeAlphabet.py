import numpy as np
import math


def alphabet(lmList):
    letter = ''

    if lmList[8][2] > lmList[5][2] and \
            lmList[12][2] > lmList[9][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[4][2] < lmList[5][2] and \
            lmList[4][1] > lmList[5][1] and \
            lmList[9][2] < lmList[0][2] and \
            lmList[19][1] < lmList[9][1]:
        letter = 'А'
    elif lmList[12][2] > lmList[8][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[4][1] < lmList[5][1] and \
            lmList[12][2] < lmList[9][2]:
        letter = 'Б'
    elif lmList[8][2] < lmList[7][2] and \
            lmList[12][2] < lmList[11][2] and \
            lmList[16][2] < lmList[15][2] and \
            lmList[20][2] < lmList[17][2] and \
            lmList[4][1] > lmList[5][1] and \
            math.hypot(lmList[4][1] - lmList[14][1], lmList[4][2] - lmList[14][2]) > \
            math.hypot(lmList[4][1] - lmList[1][1], lmList[4][2] - lmList[1][2]):
        letter = 'В'
    elif lmList[9][2] > lmList[0][2] and \
            lmList[4][1] > lmList[5][1] and \
            lmList[12][2] < lmList[10][2] and \
            lmList[8][2] > lmList[6][2]:
        letter = 'Г'
    elif lmList[12][2] < lmList[10][2] and \
            lmList[8][2] < lmList[6][2] and \
            lmList[16][2] > lmList[15][2] and \
            lmList[20][2] > lmList[19][2] and \
            lmList[4][1] < lmList[5][1] and \
            lmList[12][1] < lmList[8][1] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) < \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]):
        letter = 'Д'
    elif lmList[11][2] < lmList[9][2] and \
            lmList[11][2] > lmList[10][2] and \
            lmList[7][2] > lmList[6][2] and \
            lmList[7][2] < lmList[5][2] and \
            lmList[19][2] < lmList[17][2] and \
            lmList[19][2] > lmList[18][2] and \
            lmList[15][2] < lmList[16][2] and \
            lmList[15][2] > lmList[14][2] and \
            math.hypot(lmList[4][1] - lmList[12][1], lmList[4][2] - lmList[12][2]) < \
            math.hypot(lmList[12][1] - lmList[11][1], lmList[12][2] - lmList[11][2]):
        letter = 'E'
    elif lmList[18][1] > lmList[17][1] and \
            lmList[15][1] > lmList[14][1] and \
            lmList[11][1] > lmList[10][1] and \
            lmList[2][1] > lmList[5][1] and \
            lmList[10][1] > lmList[5][1] and \
            lmList[20][2] > lmList[5][2] and \
            lmList[18][1] > lmList[5][1] and \
            math.hypot(lmList[4][1] - lmList[12][1], lmList[4][2] - lmList[12][2]) < \
            math.hypot(lmList[12][1] - lmList[11][1], lmList[12][2] - lmList[11][2]):
        letter = 'Ж'
    elif lmList[12][2] > lmList[9][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[8][2] < lmList[5][2] and \
            lmList[4][1] < lmList[5][1] and \
            lmList[5][1] > lmList[17][1]:
        letter = 'З'
    elif lmList[8][2] > lmList[7][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[16][2] < lmList[15][2] and \
            lmList[20][2] < lmList[19][2] and \
            lmList[0][2] > lmList[5][2] and \
            lmList[10][1] > lmList[5][1]:
        letter = 'И'
    elif lmList[8][2] > lmList[7][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[16][2] < lmList[15][2] and \
            lmList[20][2] < lmList[19][2] and \
            lmList[0][2] > lmList[5][2] and \
            lmList[10][1] < lmList[5][1]:
        letter = 'Й'
    elif lmList[12][2] < lmList[10][2] and \
            lmList[8][2] < lmList[6][2] and \
            lmList[16][2] > lmList[15][2] and \
            lmList[20][2] > lmList[19][2] and \
            lmList[4][1] < lmList[5][1] and \
            lmList[12][1] < lmList[8][1] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) > \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]):
        letter = 'К'
    elif lmList[0][2] < lmList[9][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[8][2] > lmList[7][2] and \
            lmList[16][2] < lmList[14][2] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) > \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]):
        letter = 'Л'
    elif lmList[0][2] < lmList[9][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[8][2] > lmList[7][2] and \
            lmList[16][2] > lmList[14][2] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) > \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]) and \
            math.hypot(lmList[16][1] - lmList[12][1], lmList[16][2] - lmList[12][2]) > \
            math.hypot(lmList[13][1] - lmList[9][1], lmList[13][2] - lmList[9][2]):
        letter = 'М'
    elif lmList[8][2] < lmList[5][2] and \
            lmList[12][2] < lmList[9][2] and \
            lmList[16][2] > lmList[14][2] and \
            lmList[20][2] < lmList[17][2] and \
            lmList[4][1] < lmList[5][1]:
        letter = 'Н'
    elif lmList[12][2] < lmList[11][2] and \
            lmList[8][2] > lmList[6][2] and \
            lmList[20][2] < lmList[17][2] and \
            lmList[16][2] < lmList[13][2] and \
            math.hypot(lmList[8][1] - lmList[4][1], lmList[8][2] - lmList[4][2]) < \
            math.hypot(lmList[15][1] - lmList[14][1], lmList[15][2] - lmList[14][2]) and \
            math.hypot(lmList[12][1] - lmList[16][1], lmList[12][2] - lmList[16][2]) < \
            math.hypot(lmList[12][1] - lmList[4][1], lmList[12][2] - lmList[4][2]):
        letter = 'О'
    elif lmList[0][2] < lmList[9][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[8][2] > lmList[7][2] and \
            lmList[16][2] < lmList[14][2] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) <= \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]):
        letter = 'П'
    elif lmList[8][2] < lmList[5][2] and \
            lmList[12][2] > lmList[9][2] and \
            lmList[16][2] < lmList[14][2] and \
            lmList[20][2] < lmList[17][2] and \
            lmList[4][1] < lmList[5][1]:
        letter = 'Р'
    elif lmList[18][1] > lmList[13][1] and \
            lmList[14][1] > lmList[13][1] and \
            lmList[10][1] > lmList[13][1] and \
            lmList[2][1] > lmList[13][1] and \
            lmList[4][2] > lmList[6][2] and \
            lmList[8][2] < lmList[5][2] and \
            lmList[12][2] < lmList[9][2] and \
            lmList[16][2] < lmList[13][2] and \
            math.hypot(lmList[4][1] - lmList[12][1], lmList[4][2] - lmList[12][2]) > \
            math.hypot(lmList[12][1] - lmList[11][1], lmList[12][2] - lmList[11][2]):
        letter = 'С'
    elif lmList[0][2] < lmList[9][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[8][2] > lmList[7][2] and \
            lmList[16][2] > lmList[14][2] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) <= \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]) and \
            math.hypot(lmList[16][1] - lmList[12][1], lmList[16][2] - lmList[12][2]) <= \
            math.hypot(lmList[13][1] - lmList[9][1], lmList[13][2] - lmList[9][2]):
        letter = 'Т'
    elif lmList[18][2] < lmList[17][2] and \
            lmList[8][2] > lmList[5][2] and \
            lmList[12][2] > lmList[9][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[18][1] < lmList[13][1] and \
            math.hypot(lmList[4][1] - lmList[5][1], lmList[4][2] - lmList[5][2]) > \
            math.hypot(lmList[4][1] - lmList[3][1], lmList[4][2] - lmList[3][2]) and \
            math.hypot(lmList[8][1] - lmList[4][1], lmList[8][2] - lmList[4][2]) > \
            math.hypot(lmList[8][1] - lmList[6][1], lmList[8][2] - lmList[6][2]):
        letter = 'У'
    elif lmList[20][1] > lmList[19][1] and \
            lmList[16][1] > lmList[15][1] and \
            lmList[12][1] > lmList[11][1] and \
            lmList[8][1] > lmList[7][1] and \
            lmList[4][2] < lmList[6][2]:
        letter = 'Ф'
    elif lmList[18][1] > lmList[13][1] and \
            lmList[14][1] > lmList[13][1] and \
            lmList[10][1] > lmList[13][1] and \
            lmList[2][1] > lmList[13][1] and \
            lmList[4][2] > lmList[6][2] and \
            lmList[8][2] < lmList[5][2] and \
            lmList[12][2] > lmList[9][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[8][2] > lmList[6][2] and \
            math.hypot(lmList[4][1] - lmList[12][1], lmList[4][2] - lmList[12][2]) > \
            math.hypot(lmList[12][1] - lmList[11][1], lmList[12][2] - lmList[11][2]):
        letter = 'Х'
    elif lmList[20][2] > lmList[18][2] and \
            lmList[16][2] > lmList[14][2] and \
            lmList[10][1] > lmList[5][1] and \
            lmList[2][1] > lmList[5][1] and \
            math.hypot(lmList[8][1] - lmList[4][1], lmList[8][2] - lmList[4][2]) < \
            math.hypot(lmList[8][1] - lmList[6][1], lmList[8][2] - lmList[6][2]):
        letter = 'Ц'
    elif lmList[20][2] > lmList[18][2] and \
            lmList[16][2] > lmList[14][2] and \
            lmList[8][2] < lmList[7][2] and \
            lmList[12][2] < lmList[11][2] and \
            lmList[10][1] > lmList[5][1] and \
            lmList[2][1] > lmList[5][1]:
        letter = 'Ч'
    elif lmList[8][2] < lmList[5][2] and \
            lmList[12][2] < lmList[9][2] and \
            lmList[16][2] < lmList[14][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[4][1] < lmList[5][1] and \
            math.hypot(lmList[8][1] - lmList[16][1], lmList[8][2] - lmList[16][2]) <= \
            math.hypot(lmList[5][1] - lmList[13][1], lmList[5][2] - lmList[13][2]):
        letter = 'Ш'
    elif lmList[8][2] < lmList[5][2] and \
            lmList[12][2] < lmList[9][2] and \
            lmList[16][2] < lmList[14][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[4][1] < lmList[5][1] and \
            math.hypot(lmList[8][1] - lmList[12][1], lmList[8][2] - lmList[12][2]) > \
            math.hypot(lmList[5][1] - lmList[9][1], lmList[5][2] - lmList[9][2]) and \
            math.hypot(lmList[16][1] - lmList[12][1], lmList[16][2] - lmList[12][2]) > \
            math.hypot(lmList[13][1] - lmList[9][1], lmList[13][2] - lmList[9][2]):
        letter = 'Щ'
    elif lmList[12][2] > lmList[9][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[8][2] < lmList[5][2] and \
            lmList[4][1] > lmList[5][1] and \
            lmList[14][1] < lmList[5][1]:
        letter = 'Ъ'
    elif lmList[8][2] < lmList[5][2] and \
            lmList[12][2] > lmList[11][2] and \
            lmList[16][2] > lmList[15][2] and \
            lmList[20][2] < lmList[17][2] and \
            lmList[4][1] < lmList[5][1]:
        letter = 'Ы'
    elif lmList[12][2] > lmList[9][2] and \
            lmList[16][2] > lmList[13][2] and \
            lmList[20][2] > lmList[17][2] and \
            lmList[8][2] < lmList[5][2] and \
            lmList[4][1] < lmList[5][1] and \
            lmList[5][1] < lmList[17][1]:
        letter = 'Ь'
    elif lmList[11][2] > lmList[10][2] and \
            lmList[15][2] > lmList[14][2] and \
            lmList[19][2] > lmList[18][2] and \
            lmList[8][2] < lmList[5][2]:
        letter = 'Э'
    elif lmList[18][1] > lmList[17][1] and \
            lmList[15][1] > lmList[14][1] and \
            lmList[11][1] > lmList[10][1] and \
            lmList[2][1] > lmList[5][1] and \
            lmList[10][1] > lmList[5][1] and \
            lmList[20][2] < lmList[5][2] and \
            math.hypot(lmList[4][1] - lmList[12][1], lmList[4][2] - lmList[12][2]) < \
            math.hypot(lmList[12][1] - lmList[11][1], lmList[12][2] - lmList[11][2]) and \
            math.hypot(lmList[4][1] - lmList[16][1], lmList[4][2] - lmList[16][2]) < \
            math.hypot(lmList[14][1] - lmList[16][1], lmList[14][2] - lmList[16][2]):
        letter = 'Ю'
    elif lmList[12][2] < lmList[10][2] and \
            lmList[8][2] < lmList[6][2] and \
            lmList[16][2] > lmList[15][2] and \
            lmList[20][2] > lmList[19][2] and \
            lmList[4][1] < lmList[5][1] and \
            lmList[12][1] > lmList[8][1]:
        letter = 'Я'

    return letter


if __name__ == '__main__':
    print(alphabet(np.ones((21, 3))))
