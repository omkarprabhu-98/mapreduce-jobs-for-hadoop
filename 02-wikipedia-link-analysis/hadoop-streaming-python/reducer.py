import sys


def reducer():
    # final result pair
    old_key = None
    total_count = 0

    for line in sys.stdin:
        # strip of extra whitespaces, also split on tab and put the data in a array
        data = line.strip().split("\t")

        # defensive code to handle cases where data is not as expected
        if len(data) == 2:
            # get the fields
            category, count = data
            # check if this key belongs to the same key computed earlier
            # this is possible due to shuffling & sorting which will merge the intermediate keys
            # produced by mapper
            if old_key and category != old_key:
                # display sales computed for the previous key
                results = [old_key, str(total_count)]
                print("\t".join(results))
                # reset total count value
                total_count = 0

            old_key = category
            total_count += float(count)

    # print out the last key:value
    if old_key is not None:
        results = [old_key, str(total_count)]
        print("\t".join(results))


def main():
    reducer()


if __name__ == "__main__":
    main()