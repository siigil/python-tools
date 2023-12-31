############################
# Daily News CLI Tool
# Dec 2023
# Pull the list of BBC top and most read articles, and display them back to CLI with appropriate links.
# Practice working with XML / web content
# Notes:
# ./daily-news-bbc.py
############################

import requests
import urllib3
from lxml import html

# Colors that make CLI formatting look nice
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    LINK = '\033[4m'

def get_news(site):
    # Disable the warning that shows up for verify=False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # verify = False to bypass SSL intercept warnings
    response = requests.get(site,verify=False)
    news = response.content
    return news

def news_format(titles,links,header,emoji):
    # If BBC is not in the link URL, add the base URL to the path.
    # Use links[i] to place the element back in as "path" is relative to the loop and not permanent.
    for i,path in enumerate(links):
        if "www.bbc.com" in path:
            continue
        else:
            links[i]=f"https://www.bbc.com{path}"
    
    # Create a nice header, colors.ENDC turns off the formatting at end of string
    print(f"{colors.HEADER}{header}{colors.ENDC}")
    # Length of max headline for pretty formatting
    length = len(max(titles,key=len))
    # zip lets you run down two lists at once in tandem, need that for titles & links display
    for line,link in zip(titles,links):
        # ljust to pad all lines to length of max headline
        prettyline = line.ljust(length)
        # print each article and link
        print(f"{emoji} {prettyline} | {colors.LINK}{colors.OKBLUE}{link}{colors.ENDC}")
    print()

def news_bbc(news):
    tree = html.fromstring(news)

    # Uncomment to print all <h2> headers for fun / testing
    #print(tree.xpath('//h2/text()'))

    # parse out headlines and links
    headlines = tree.xpath('//h2/text()')[0:9]
    headline_links = tree.xpath('//h2/ancestor::a[1]/@href')[0:9]
    headline_title=".: BBC Top Articles :."
    news_format(headlines,headline_links,headline_title,"🌸")

    # parse out most read section towards the bottom using reverse slice notation (e.g. -20 is 20-away-from-end-of-list)
    mostread = tree.xpath('//h2/text()')[-20:-10]
    mostread_links = tree.xpath('//h2/ancestor::a[1]/@href')[-19:-11]
    mostread_title=".: BBC Most Read :."
    news_format(mostread,mostread_links,mostread_title,"🌼")

def main():
    bbc = "https://www.bbc.com/news"
    b_news = get_news(bbc)
    news_bbc(b_news)

if __name__ == "__main__":
    main()