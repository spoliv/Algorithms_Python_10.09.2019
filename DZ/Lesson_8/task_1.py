import hashlib


def count_subs(string):
    subs_set = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            h_subs = hashlib.sha1(string[i:j + 1].encode('utf-8')).hexdigest()
            subs_set.add(h_subs)
    print(len(subs_set) - 1)


count_subs('papa')
count_subs('Я тут')
count_subs('А не спеть ли нам песню?')
count_subs('I wanna be free!')
