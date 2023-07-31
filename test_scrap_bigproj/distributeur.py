import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from fonctions import convert_to_minutes
from mongodb_crawler.items import FilmItem
import re
from fonctions import extract_text_between_substrings


class TopfilmsspiderSpider(CrawlSpider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'mongodb_crawler.pipelines.TopFilmsPipeline': 400
        }
    }
    
    name = 'crawlerfilm'
    allowed_domains = ['popandplay.fr']
    #Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
    # user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
    
    # def start_requests(self):
    #     yield scrapy.Request(url='https://www.jpbox-office.com/v9_demarrage.php?view=2', headers={
    #         'User-Agent': self.user_agent
    #     })

    # rules = (
    #     Rule(LinkExtractor(), callback='parse_item'),
    # )
    
    def start_requests(self):
        for i in range(0, 10000, 30):
            yield scrapy.Request(url='https://www.jpbox-office.com/v9_demarrage.php?view=2&filtre=classg&limite={}&infla=0&variable=0&tri=champ0&order=DESC&limit5=0'.format(i),
                                headers={'User-Agent': self.user_agent},
                                callback=self.parse_titles
            )

    def parse_titles(self, response):
        film_items = response.css('td.col_poster_titre h3 a')
        for film_item in film_items:
            title = film_item.css('::text').get()
            print(title)
            movie_page_link = film_item.attrib['href']
            print(movie_page_link)
            url2="https://www.jpbox-office.com/"+movie_page_link
            print(url2)
            yield scrapy.Request(
                url=url2,
                headers={'User-Agent': self.user_agent},
                callback=self.parse_movie_page
            )

    def parse_movie_page(self, response):
        otr=response.css('h1 ::text')
        print(otr)
        title = response.meta.get('title')
        distributor = response.css('div.bloc_infos_center h3:contains("Distribué par") + text()').get()
        print(title)
        print(distributor)