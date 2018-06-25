# https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
# https://stackoverflow.com/questions/3031045/how-come-string-maketrans-does-not-work-in-python-3-1
# https://stackoverflow.com/questions/23175809/str-translate-gives-typeerror-translate-takes-one-argument-2-given-worked-i

import sys


def mapper():
    for line in sys.stdin:
        # strip unnecessary whitespaces from line and split line on tab
        data = line.strip().split('\t')

        # check if the line is valid field
        if len(data) != 19:
            continue

        # get body and node id
        body = data[4]
        node_id = data[0]

        # character to slit on
        split_chars = ',.!?:;"()<>[]#$=-/'
        # split body on these
        body = body.translate(str.maketrans('', '', split_chars))
        # get words
        words = body.strip().split()

        # make list unique as many same words can be in this node
        words = list(set(words))

        # generate the intermediate index
        for w in words:
            print('%s\t%s' % (w, node_id))


if __name__ == '__main__':
    mapper()
