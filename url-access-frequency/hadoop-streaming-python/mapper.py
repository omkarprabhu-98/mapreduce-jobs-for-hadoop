import sys
import re


# variable to perform regex matching
regex = r'GET\s(.*?)\s'


def mapper():
    for line in sys.stdin:
        # get url from line using regular expression
        data = re.search(regex, line)
        # check if data exists
        if data is not None:
            if data.groups(0) is not None:
                # print(data.group())
                url = data.groups(0)[0]
                # intermediate record
                results = [url, "1"]
                # print out the pair
                print("\t".join(results))


def main():
    mapper()


if __name__ == "__main__":
    main()
