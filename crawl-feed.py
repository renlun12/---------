import sys
reload(sys)
from datetime import *
import time
import os
sys.setdefaultencoding('utf-8')

from rssfeed import Rssfeed
feed_url = 'http://n.rss.qq.com/rss/tech_rss.php'
feed1 = Rssfeed(feed_url)
articles = []
dt = datetime.now()
path = os.getcwd() + '/rss/'
title = path + dt.strftime('%Y-%m-%d %H:%M')+'.txt'
time_title = dt.strftime('%Y-%m-%d %H:%M\n')
file_object = open(title,'w')
file_object.write(time_title)

for counter in range(0, feed1.length):
    item = feed1.entries[counter]
    content = 'source:' + item.link + '\n' + item.author + ' ' + item.updated + '\n' + item.summary+'\n'
    article = {'title':item.title, 'content':content}
    file_object.write('title:'+item.title+'\n'+'content:'+content+'\n')
    articles.append(article)
