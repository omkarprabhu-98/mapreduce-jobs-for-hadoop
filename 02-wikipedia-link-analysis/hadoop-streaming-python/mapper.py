import sys
from bs4 import BeautifulSoup
import requests


# download web page
def web_page(url):
    soup = None
    # get source code of the web site
    source_code = requests.get(url)

    # check connection status
    if source_code.status_code == 200:
        # convert into plain_text
        plain_text = source_code.text

        # parse the text and store the parsed tree
        soup = BeautifulSoup(plain_text, "lxml")

    return soup


# get links from beautiful soup obj of a page
def get_all_links(soup):
    link_list = []

    if not soup:
        return link_list
    # moving through a links get href tag
    for link in soup.findAll('a'):
        link_list.append(link.get('href')) if link_list.append(link.get('href')) else None

    return link_list


def mapper():
    for line in sys.stdin:

        line = line.strip()

        if line == '' or line is None:
            return

        # articles
        if 'wgArticleId' in line:
            key = 'Articles'
            value = 1
            result = [key, value]
            print("%t".join(result))
        else:
            # get all links
            soup_obj = web_page(line)
            links = get_all_links(soup_obj)

            # categorize all links
            for l in links:
                # if 'href=' in line:
                key = None
                value = None
                if '.jpg' in l or '.png' in l or '.svg' in l or '.gif' in l or '.jpeg' in l or '.tiff' in l or '.xcf' in l:
                    key = 'Image Links'
                    value = 1
                elif 'en.wikipedia.org' in l or '/w/' in l:
                    key = 'Internal but Irrelevant'
                    value = 1
                elif '.wikipedia.org' in l:
                    key = 'Non-English Wikipedia Link'
                    value = 1
                elif 'wikimedia.org' in l or 'wikimediafoundation.org' in l:
                    key = 'Organizational Link'
                    value = 1
                elif '/wiki/' in l:
                    key = 'Internal Link'
                    value = 1
                else:
                    key = 'External Link'
                    value = 1
                result = [key, value]
                print("%t".join(result))


def main():
    mapper()


if __name__ == "__main__":
    main()
