import sys


def reducer():
    # variables
    old_key = None
    total_value = 0

    for line in sys.stdin:
        # strip of extra whitespaces, also split on tab and put the data in a array
        data = line.strip().split()

        # check for correct length of data
        if len(data) == 2:
            # get key value pair
            key, value = data

            # if not the same key then gather result
            if old_key and key != old_key:
                # print out final key value result
                results = [key, str(total_value)]
                print("\t".join(results))

                # reset total value
                total_value = 0

            # set old key
            old_key = key
            # update total value
            total_value += int(value)

    # print out the last key:value
    if old_key is not None:
        results = [old_key, str(total_value)]
        print("\t".join(results))


def main():
    reducer()


if __name__ == "__main__":
    main()
