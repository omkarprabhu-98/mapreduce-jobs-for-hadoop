# https://github.com/CodeMangler/udacity-hadoop-course/blob/master/src/forum-data/combine-datasets/mapper.py

import sys


def mapper():
    for line in sys.stdin:
        # strip unnecessary whitespaces from line and split line on tab
        data = line.strip().split('\t')

        # data for line forum nodes
        if len(data) == 19:
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
            print('\t'.join([author_id, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score]))
        # data for forum users
        elif len(data) == 5:
            user_ptr_id, reputation, gold, silver, bronze = data
            # if forum node data comes here because of newline in body
            # this data become of length 5
            # so body id identified by presence of <
            if '<' in bronze:
                continue
            print('\t'.join([user_ptr_id, reputation, gold, silver, bronze]))


if __name__ == '__main__':
    mapper()
