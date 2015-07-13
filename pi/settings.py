# -*- coding: utf-8 -*-

# Scrapy settings for pi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pi'

SPIDER_MODULES = ['pi.spiders']
NEWSPIDER_MODULE = 'pi.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400
}
USER_AGENT_LIST = "/home/kaco/quevale/useragents.txt"

COOKIES_ENABLED = False

DOWNLOAD_DELAY = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pi (+http://www.yourdomain.com)'
