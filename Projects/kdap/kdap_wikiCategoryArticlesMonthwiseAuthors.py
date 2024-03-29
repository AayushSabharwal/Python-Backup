from kdap_wikiArticleRevisions import get_revisions_of_article
from wikiExtract import wikiExtract
# import time


def get_monthly_revision_count_by_category(category_name):
    w = wikiExtract()
    category_dict = w.get_articles_by_category(category_name)
    article_list = category_dict[category_name]
    monthly_revisions_dict = {}
    for article in article_list:
        article_authors_dict = {}
        revisions = get_revisions_of_article(article['title'])[article['title']]
        for revision in revisions:
            timestamp = revision['timestamp'][:7]
            if timestamp not in article_authors_dict:
                article_authors_dict[timestamp] = []
            if 'user' in revision:
                author = revision['user']
                if author not in article_authors_dict[timestamp]:
                    article_authors_dict[timestamp].append(author)
        monthly_revisions_dict[article['title']] = article_authors_dict

    return monthly_revisions_dict

'''
s = time.time()
d = get_monthly_revision_count_by_category('Black Lives Matter')
e = time.time()
print(e-s, d, sep='\n')
'''