import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from fonctions import convert_to_minutes
from mongodb_crawler.items import FilmItem
from fonctions import extract_text_between_substrings
import re


class TopfilmsspiderSpider(CrawlSpider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'mongodb_crawler.pipelines.TopFilmsPipeline': 400
        }
    }
    
    name = 'crawlerfilm'
    allowed_domains = ['jpbox-office.com']
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
        for i in range(2, 23114 ):
            print(i)
            print(i)
            print(i)
            yield scrapy.Request(url='https://www.jpbox-office.com/fichfilm.php?id={}&view=7'.format(i),
                                headers={'User-Agent': self.user_agent},
                                callback=self.parse_item)

    # def parse_item(self, response):
    #     film_items = response.css('td.col_poster_titre h3 a')
    #     nbre_entrees = response.css('td.col_poster_contenu_majeur::text').getall()

    #     for i, item in enumerate(film_items):
    #         film_item = {}boxoff_FRANCAIS_1st
    #         film_item['title'] = item.css('::text').get()
    #         film_item['nbre_entrees'] = nbre_entrees[i] if i < len(nbre_entrees) else None
    #         yield film_item
    def parse_item(self, response):
        film_id = int(re.search(r'id=(\d+)', response.url).group(1))
        print(film_id)
        acteur_realisateur=response.css('h3 a::text').getall()
        print(acteur_realisateur)
        filtered_film = [val for val in acteur_realisateur if "\r\n" in val]

# Enlever '\r\n\' et les espaces en utilisant la méthode replace
        cleaned_film = [val.replace('\r\n', '').strip() for val in filtered_film]

        #for distri in distri_list[0]:
        #    print(1)
        
        #    print(distributor)
        #    print('8')
        film_item = {}
        film_item['id']=film_id
        
        film_item['acteurs_real']=cleaned_film
        # 
        
        # print(title)
        # print(cleaned_title)
        # print(distributor)
        yield film_item