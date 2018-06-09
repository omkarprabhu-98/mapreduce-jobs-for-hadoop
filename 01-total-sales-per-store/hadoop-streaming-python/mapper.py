import sys


def mapper():
    for line in sys.stdin:
        # strip of extra whitespaces, also split on tab and put the data in a array
        data = line.strip().split("\t")

        # defensive code to handle cases where data is not as expected
        # ignoring line if 6 fields are not present
        if len(data) == 6:
            # get the fields
            data, time, store, item, cost, payment = data
            # intermediate record
            results = [store, cost]
            # print out the pair
            print("\t".join(results))


def main():
    mapper()


if __name__ == "__main__":
    main()
