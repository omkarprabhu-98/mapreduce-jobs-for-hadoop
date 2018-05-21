import sys


def reducer():
    # final result pair
    old_key = None
    total_sales = 0

    for line in sys.stdin:
        # strip of extra whitespaces, also split on tab and put the data in a array
        data = line.strip().split("\t")

        # defensive code to handle cases where data is not as expected
        if len(data) == 2:
            # get the fields
            key, cost = data
            # check if this key belongs to the same key computed earlier
            # this is possible due to shuffling & sorting which will merge the intermediate keys
            # produced by mapper
            if old_key and key != old_key:
                # display sales computed for the previous key
                results = [old_key, str (total_sales)]
                print("\t".join(results))
                # reset total sales value
                total_sales = 0

            old_key = key
            total_sales = total_sales + float(cost)

    # print out the last key:value
    if old_key is not None:
        results = [old_key, str(total_sales)]
        print("\t".join(results))


def main():
    reducer()


if __name__ == "__main__":
    main()