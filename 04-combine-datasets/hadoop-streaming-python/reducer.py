import sys


def reducer():
    # previous key
    old_user = None
    # final row structure of data set
    row = {
        'user_id': None,
        'id': None,
        'title': None,
        'tagnames': None,
        'node_type': None,
        'parent_id': None,
        'abs_parent_id': None,
        'added_at': None,
        'score': None,
        'reputation': None,
        'gold': None,
        'silver': None,
        'bronze': None,
    }

    for line in sys.stdin:

        data = line.split('\t')
        # the line with user data will come first
        # due to shuffle sort
        if len(data) == 5:
            row['user_id'] = data[0]
            row['reputation'] = data[1]
            row['gold'] = data[2]
            row['silver'] = data[3]
            row['bronze'] = data[4]
            continue
        elif len(data) == 9:
            # fill data from forum post
            i = 0
            for key in row:
                if i >= 9:
                    break
                row[key] = data[i]
                i += 1
            print(row)

        # new user ?
    #     if old_user is not None and old_user != row['user_id']:
    #         print(row)
    #         # do not clear row as next line with
    #         # let it be overwritten by the next line
    #         # row = dict({key: None for key in row})
    #
    #     old_user = row['user_id']
    #
    # if old_user is not None:
    #     print(row)


if __name__ == '__main__':
    reducer()
