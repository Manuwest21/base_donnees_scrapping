import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from fonctions import convert_to_minutes
from mongodb_crawler.items import FilmItem
from fonctions import extract_text_between_substrings
import re

id=2
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
            yield scrapy.Request(url='https://www.jpbox-office.com/comparaisons.php?id={}&id2=15'.format(i),
                                headers={'User-Agent': self.user_agent},
                                callback=self.parse_item)#, cb_kwargs={'film_id': i})

    # def parse_item(self, response):
    #     film_items = response.css('td.col_poster_titre h3 a')
    #     nbre_entrees = response.css('td.col_poster_contenu_majeur::text').getall()

    #     for i, item in enumerate(film_items):
    #         film_item = {}boxoff_FRANCAIS_1st
    #         film_item['title'] = item.css('::text').get()
    #         film_item['nbre_entrees'] = nbre_entrees[i] if i < len(nbre_entrees) else None
    #         yield film_item
    def parse_item(self, response):
        global id
        
        film_id = int(re.search(r'id=(\d+)', response.url).group(1))
        realisateur = response.css('td.col_poster_titre a::text').get()
        prendre_tt=response.css('td.col_poster_contenu_majeur::text').getall()
        print(prendre_tt)
        budget=prendre_tt[18]#prendre 18éme valeur
        print(budget)
       
        durée=prendre_tt[16]
        print(durée)
        
        public=prendre_tt[12]
        print(public)
        
        genre=prendre_tt[14]
        print(genre)

        if budget=='60 000 000 $' and durée=='1h46':
            budget1=prendre_tt[17]#prendre 18éme valeur
            print(budget)
       
            durée1=prendre_tt[15]
            print(durée)
        
            public1=prendre_tt[11]
            print(public)
        
            genre1=prendre_tt[13]
            print(genre)
            
            film_item = {}
            # film_item['id'] =str(film_id)
            film_item['id'] = film_id
            film_item['budget'] = budget1
            film_item['public']=public1
            film_item['durée']=durée1
            # film_item['date']=cleaned_date
            id+=1
            
            yield film_item
            
        else:
            film_item = {}
            # film_item['id'] =str(film_id)
            film_item['id'] = film_id  # Ajouter la clé 'id' avec la valeur i en cours
            film_item['genre']=genre
            film_item['budget'] = budget
            film_item['public']=public
            film_item['durée']=durée
            # film_item['date']=cleaned_date
            id+=1
            
            yield film_item

        # title = response.css('td.texte_2022titre h1::text').get()
        # date = response.css('div.bloc_infos_center.tablesmall1b p a[href^="v9_avenir.php"]::text').get()
        # chiffres_vrac=response.css('td.col_poster_contenu_majeur ::text').getall()
        # print(chiffres_vrac)
        # first_day_boxoffice=chiffres_vrac[4]
        # first_we_boxoffice=chiffres_vrac[5]
        # first_week_boxoffice=chiffres_vrac[6]
        # public=response.css('div.bloc_infos_center.tablesmall1::text').getall()
        # vrai_public=public[-1]
        # otr_distri=public[1]
      
        # if genre:
        #     cleaned_genre = genre.strip()
        # if country:
        #     cleaned_country = country.strip()
        # if date:
        #     cleaned_date = date.strip()
        # print(cleaned_country)
        # titles_ori=response.css('td.texte_2022titre h2::text').get()
        # print("la distri:",distri_list)
        # #for distri in distri_list[0]:
        # #    print(1)
        # distributor = extract_text_between_substrings(distri_list[0])
        #    print(distributor)
        #    print('8')
        
    # def parse_item(self, response):
    #     # titles = response.css('h3 a::text').getall()
    #     # entries = response.css('td.col_poster_contenu_majeur::text').getall()
    #     # annee=response.css('td.col_poster_contenu a::text').getall()
    #     distri=response.css('div.bloc_infos_center.tablesmall1').getall()
    #     print(distri)
    #     ditri3=extract_text_between_substrings(distri)
    #     print(distri)
        # print(annee)
        # # annee=[annee[i] for i in range (4,64,2)]
        # # print (annee)
        # entries1=[entries[i] for i in range (0,120,4)]
        # digits = [re.findall(r'\d+', item) for item in annee]
        # print(digits)
# Aplatir la liste de listes en une seule liste de chiffres
        # all_digits = [digit for sublist in digits for digit in sublist]
        # print (all_digits)
        # # print[entries]
        # # for i in range (0,120,4):
        # #     film_item = {}
        # #     film_item['title'] = titles[i]
        # #     film_item['nbre_entrees'] = [entries[i].get()] #for i in range (0,120,4)]
        # print(entries1)
        # for i in range(30):
        #     film_item = {}
            
        #     film_item['title'] = titles[i]
        #     film_item['nbre_entrees'] = entries[i]
        #     film_item['annee']=all_digits[i]
        #     film_item['nbre_entrees'] = entries[i*4] if i*4 < len(entries) else None #[i*4] if i*4 < len(entries) else None
        #     yield film_item