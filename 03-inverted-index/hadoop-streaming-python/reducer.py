import sys


def reducer():
    old_word = None
    node_id_list = []

    for line in sys.stdin:
        # extract data
        data = line.strip().split('\t')
        # check
        if len(data) != 2:
            continue

        # key value
        word, node_id = data
        # start of new word
        if old_word is not None and old_word != word:
            # print the old index
            print('\t'.join([old_word, str(node_id_list)]))
            # empty the index list for current word
            node_id_list = []

        # store
        old_word = word
        # append
        node_id_list.append(node_id)


if __name__ == '__main__':
    reducer()
