#!/usr/bin/python3

#Message whose all possible letter combinations in Kinyarwanda
message = "a e i o u b c d f g h j k l m n p r s t v w y z nd ng ny sh kw mb ts nz rw by nt mw tw bw cy ry my nk nj mv mp jy pf zw nw ns mby shy nsh gw jw nny nyw njy ngw shw mbw mf ndw nzw sw hw nsw tsw ntw ty nkw py njw dw sy fw ndy cw nshy nty mpy pw mpw nsy mvw byw ncy shyw nshw myw nshyw mbyw mfw mvy mvyw pfw pfy vw vy ryw"

#Change it into a n array.
mylist = message.split(" ")

#Classify them into respecitve arrays
inyuguti = []
ingombajwi1 = []
ingombajwi2 = []
ingombajwi3 = []
ingombajwi4 = []
ingombajwi5 = []

#List whose ascii letter for vowels.
ascii_values = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
kubara = 0

#Classify them into respecitve lists using an array.
for i in mylist:
    if len(i) == 1:
        if ord(i) in ascii_values:
            inyuguti.append(i)
        else:
            ingombajwi1.append(i)
    if len(i) == 2:
        ingombajwi2.append(i)
        kubara += 1
    if len(i) == 3:
        ingombajwi3.append(i)
        kubara += 1
    if len(i) == 4:
        ingombajwi4.append(i)
        kubara += 1
    if len(i) == 5:
        ingombajwi5.append(i)
        kubara += 1
#Sort each array following latin alphabetical order.
ingombajwi1 = sorted(ingombajwi1)
ingombajwi2 = sorted(ingombajwi2)
ingombajwi3 = sorted(ingombajwi3)
ingombajwi4 = sorted(ingombajwi4)
ingombajwi5 = sorted(ingombajwi5)


# print("Inyuguti \n{} \n \nIngombajwi: \n{} \n \nIbihekane by'ingombajwi 2: \n{} \n \nIbihekane by'ingombajwi 3: \n{} \n \nIbihekane by'ingombajwi 4: \n{} \n \nIbihekane by'ingombajwi 5: \n{} \n \n".format(
#     ' '.join(inyuguti), ' '.join(ingombajwi1), ' '.join(ingombajwi2), ' '.join(ingombajwi3), ' '.join(ingombajwi4), ' '.join(ingombajwi5)
#     ))

ingombajwi_zose = ingombajwi1 + ingombajwi2 + ingombajwi3 + ingombajwi4 + ingombajwi5

amasaku_yose = ['a', 'â', 'aa', 'âa', 'aâ', 'ââ', 'e', 'ê', 'ee', 'êe', 'eê', 'êê', 'i', 'î', 'ii', 'îi', 'iî', 'îî', 'o', 'ô', 'oo', 'ôo', 'oô', 'ôô', 'u', 'û', 'uu', 'ûu', 'uû', 'ûû']

print(f"Ibihekane byose ni: {kubara}")
print(f"Amajwi yose ashoboka ni: {kubara * 30}")

print("Ibikurikira, ni ibihekane byose, hamwe n'amasaku yose ashoboka mu rurimi rw'Ikinyarwanda")

for ikintu in ingombajwi_zose:
    for akantu in amasaku_yose:
        print(ikintu + akantu, end=' ')
    print()
    print()