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
            yield scrapy.Request(url='https://popandplay.fr/sorties-cinema/sorties-cinema-du-mercredi-5-juillet-2023'.format(i),
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
    # def parse_item(self, response):
    #     titles = response.css('h2 ::text').getall()
    #     titles=titles[1:]
    #     acteurs=response.css('h2 strong ::text').getall()
    #     print(acteurs)

    #     print(titles)
        
    # def parse(self, response):
    #     # Sélectionner l'élément <p> avec la classe "has-text-align-center"
    #     p_element = response.css('p.has-text-align-center').get()

    #     # Extraire le contenu des acteurs, du réalisateur, du genre et du pays d'origine
    #     acteurs = p_element.css('strong:contains("Acteurs:") + ::text').get()
    #     realisateur = p_element.css('strong:contains("Réalisateur:") + ::text').get()
    #     genre = p_element.css('strong:contains("Genre:") + ::text').get()
    #     pays_origine = p_element.css('strong:contains("Pays d\'origine:") + ::text').get()
    #     print(acteurs.strip())
    #     print(realisateur.strip())
    #     print(genre.strip())
    #     print(pays_origine.strip())
        # print(acteurs.strip())
        # yield {
        #     'Acteurs': acteurs.strip() if acteurs else None,
        #     'Réalisateur': realisateur.strip() if realisateur else None,
        #     'Genre': genre.strip() if genre else None,
        #     'Pays d\'origine': pays_origine.strip() if pays_origine else None,
        # }
        # print[entries]
        # for i in range (0,120,4):
        #     film_item = {}
        #     film_item['title'] = titles[i]
        #     film_item['nbre_entrees'] = [entries[i].get()] #for i in range (0,120,4)]
        # print(entries1)
        # for i in range(30):
        #     film_item = {}
            
        #     film_item['title'] = titles[i]
        #     film_item['nbre_entrees'] = entries[i]
        #     film_item['annee']=all_digits[i]
        #     film_item['nbre_entrees'] = entries[i*4] if i*4 < len(entries) else None #[i*4] if i*4 < len(entries) else None
        #     yield film_item
            
    def parse_item(self, response):
        # Sélectionner l'élément <p> avec la classe "has-text-align-center"
        p_elements = response.css('p.has-text-align-center').getall()
        print(p_elements)
        
        for p_element in p_elements:
            # acteurs = extract_text_between_substrings(p_element, 'Acteurs:</strong>', '<br>')
            # realisateur = extract_text_between_substrings(p_element, 'Réalisateur:</strong>', '<br>')
            # genre = extract_text_between_substrings(p_element, 'Genre:</strong>', '<br>')
            # pays = extract_text_between_substrings(p_element, 'Pays d’origine:</strong>', '</p>')
            print (p_element)
            acteurs = extract_text_between_substrings(p_element, 'Acteurs: ', '<br>')
            realisateur = extract_text_between_substrings(p_element, 'Réalisateur:', '<br>')
            genre = extract_text_between_substrings(p_element, 'Genre:', '<br>')
            pays = extract_text_between_substrings(p_element, 'Pays d’origine: ', '</p>')

    # Print the extracted values
            print('acteur:',acteurs)
            print('real:',realisateur)
            print('genre',genre)
            print('pays',pays)
# 
