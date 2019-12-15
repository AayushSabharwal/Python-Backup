from __future__ import absolute_import

from kdap_wikiArticleRevisions import get_revisions_of_article
from wikiExtract import wikiExtract
import time

def get_revisions_of_article_by_category(category_name):
    wExtract = wikiExtract()
    articles = wExtract.get_articles_by_category(category_name)
    monthly_revisions = {}
    for article in articles[category_name]:
        revisions = get_revisions_of_article(article['title'])[article['title']]
        monthly = {}
        for revision in revisions:
            timestamp = revision['timestamp']
            yyyydd = timestamp[:7]
            if yyyydd not in monthly:
                monthly[yyyydd] = 0
            monthly[yyyydd] += 1
        monthly_revisions[article['title']] = monthly

    return monthly_revisions


start = time.time()
d = get_revisions_of_article_by_category("Black Lives Matter");
end = time.time()
print(end-start, d)