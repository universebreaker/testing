from PttWebCrawler.crawler import *
import json

# TODO: modify PttWebCrawler to add agent string(?), remove json file output
def PTT_crawler(page_start = 1, page_end = 100, zone = 'PublicServan'):
    c = PttWebCrawler(as_lib=True)
    c.parse_articles(page_start, page_end, zone)
    with open('./'+zone + '-' + str(page_start) + '-' + str(page_end) + '.json','r') as wp:
        buf = wp.read()
    load = json.loads(buf)
    for article in load['articles']:
        print('Date: ' + article['date'])
        print('Author: ' + article['author'])
        print('Title: ' + article['article_title'])
        print('Content: ' + article['content'])
        print('Board: ' + zone)
        print('===============')
