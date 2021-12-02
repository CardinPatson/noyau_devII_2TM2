#Nathan Sancke
import os
import sys
import requests


class News:
    def __init__(self, limit: str = "5", country: str = "be", languages: str = "fr"):
        self.__max_articles = int(limit)
        self.__limit = "&limit="+limit
        self.__country = "&country="+country
        self.__languages = "&languages="+languages
        self.__api_link = f"http://api.mediastack.com/v1/news?access_key=4a9e07d9cfd75c8d73c70f90ed4846f5"

    @property
    def max_articles(self):
        return self.__max_articles

    @property
    def limit(self):
        return self.__limit

    @property
    def country(self):
        return self.__country

    @property
    def api_link(self):
        return self.__api_link

    @property
    def languages(self):
        return self.__languages

    def get_news(self):
        """
        Renvoie les news

        PRE : Utilise le parametre weather qui est la ville possible que l'utilisateur doit entrer
        POST : Renvoie une chaine contenant la température qu'il fait dans la ville
        """
        response = requests.get(self.api_link+self.country+self.languages+self.limit)
        current = response.json()
        #current = {'pagination': {'limit': 25, 'offset': 0, 'count': 25, 'total': 10000}, 'data': [{'author': 'Diéry DIALLO', 'title': '(Vidéo) Foot – El Hadji Diouf: “Je n’ai jamais écouté mes entraîneurs et sur le terrain c’est …”', 'description': 'De nos jours, les joueurs sont plus importants que le coach dans une équipe de football. C&#8217;est l&#8217;avis de l’ancien international sénégalais, El Hadji Ousseynou Diouf qui était l&#8217;invité dans l’émission Walf Sports de Walf TV. Au cours de ladite émission, l&#8217;ancien capitaine des Lions de la Téranga révèle qu&#8217;il n&#8217;écoutait pas les consignes de [&#8230;]L’article (Vidéo) Foot &#8211; El Hadji Diouf: “Je n’ai jamais écouté mes entraîneurs et sur le terrain c&#8217;est &#8230;&#8221; est apparu en premier sur Senego.com - Actualité au Séné...', 'url': 'https://senego.com/video-foot-el-hadji-diouf-je-nai-jamais-ecoute-mes-entraineurs-et-sur-le-terrain-cest_1315607.html', 'source': 'Senego', 'image': 'https://www.youtube.com/embed/FGlrX2WCaI0', 'category': 'general', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T09:48:00+00:00'}, {'author': 'Marine Magnien', 'title': 'Des balises avifaunes pour préserver les espèces protégées', 'description': 'La ligne très haute tension Bras de la Plaine - Le Gol va être équipée d\'une soixantaine de balises dites "avifaunes". Avec ces équipements, EDF et la SEOR se lancent dans un projet expérimental de préservation des espèces d\'oiseaux marins protégées de La Réunion.-Toutes nos vidéos/ JT 12h30', 'url': 'https://www.linfo.re/videos/toutes-nos-videos/des-balises-avifaunes-pour-preserver-les-especes-protegees', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T09:04:43+00:00'}, {'author': 'Marine Magnien', 'title': 'Musique : retour sur le chanteur Gramoun Lélé !', 'description': "Allez ce mercredi on va vous parler d'un chanteur Réunionnais, Julien Phileas, plus connu sous le nom de Gramoun Lélé ! Son portrait avec l'historien Prosper Eve dans la minute du 12h30 réalisée par Sylvain Ducasse !-Toutes nos vidéos/ Home Page, JT 12h30", 'url': 'https://www.linfo.re/videos/toutes-nos-videos/musique-retour-sur-le-chanteur-gramoun-lele', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T09:01:50+00:00'}, {'author': 'Merzouk Abdelaziz', 'title': 'Pluies orageuses et vents\xa0: les prévisions météo pour ce mercredi', 'description': 'Après les fortes chaleurs caniculaires du mois d’août dernier, l’automne s’installe désormais en Algérie. Depuis plusieurs jours, les pluies orageuses ont s’abattent sur plusieurs régions du nord et du centre du pays. C’est le cas, d’ailleurs, pour aujourd’hui. Dans un bulletin météo spécial (BMS), l’office national de météorologie a placé, ce mercredi 1er septembre, sept [&#8230;]L’article Pluies orageuses et vents\xa0: les prévisions météo pour ce mercredi est apparu en premier sur .', 'url': 'https://www.algerie360.com/pluies-orageuses-et-vents-les-previsions-meteo-pour-ce-mercredi/', 'source': 'Algerie360.com', 'image': 'https://www.algerie360.com/wp-content/uploads/2021/09/meteo-1024x576.jpg', 'category': 'general', 'language': 'fr', 'country': 'dz', 'published_at': '2021-09-01T08:57:38+00:00'}, {'author': 'Antoine Sarr', 'title': 'Kaolack: Une militante de Pastef traîne en justice des policiers', 'description': 'La responsable de Pastef à Kaolack, Adji Ndao, a décidé de traîner en justice trois policiers qui l’avaient tabassée lors de son interpellation. La dame qui vit à l’étranger s’était retrouvée avec un œil enflé avant d’être évacuée à l’hôpital. Citation directe&#8230; Les militants de Pastef organisaient une caravane de sensibilisation pour les inscriptions sur [&#8230;]L’article Kaolack: Une militante de Pastef traîne en justice des policiers est apparu en premier sur Senego.com - Actualité au Sénégal, toute actualité du jour.', 'url': 'https://senego.com/kaolack-une-militante-de-pastef-traine-en-justice-des-policiers_1315509.html', 'source': 'Senego', 'image': None, 'category': 'general', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T08:17:49+00:00'}, {'author': 'Mandaw Mbengue', 'title': 'Eliminatoires Mondial 2022: Le Sénégal débute contre le Togo, ce mercredi', 'description': 'Le Sénégal débute sa Campagne dans les éliminatoires de la Coupe du Monde 2022, ce Jeudi. Aliou Cissé et ses hommes ont rendez-vous avec le Togo au Stade Lat Dior de Thiès à partir de 16h. Une victoire pour bien démarrer les éliminatoires de la Coupe du Monde 2022 est l&#8217;objectif des Lions. Un match [&#8230;]L’article Eliminatoires Mondial 2022: Le Sénégal débute contre le Togo, ce mercredi est apparu en premier sur Senego.com - Actualité au Sénégal, toute actualité du jour.', 'url': 'https://senego.com/eliminatoires-mondial-2022-le-senegal-debute-contre-le-togo-ce-mercredi_1315520.html', 'source': 'Senego', 'image': None, 'category': 'general', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T08:48:31+00:00'}, {'author': None, 'title': "Présidentielle : l'ex-LREM Aurélien Taché soutient Eric Piolle", 'description': "Aurélien Taché, ancien député LREM, déçu de la macronie, va voter à la primaire des écologistes et s'engagé aux côtés d'Eric Piolle, dans la campagne en vue de la présidentielle de 2022.", 'url': 'https://www.republicain-lorrain.fr/politique/2021/09/01/presidentielle-l-ex-lrem-aurelien-tache-soutient-eric-piolle', 'source': 'La Republicain', 'image': 'https://cdn-s-www.republicain-lorrain.fr/images/902CB409-D3BF-419E-A13C-F1F93E477468/NW_listB/photo-christophe-petit-tesson-afp-1630484830.jpg', 'category': 'general', 'language': 'fr', 'country': 'ne', 'published_at': '2021-09-01T08:27:00+00:00'}, {'author': None, 'title': 'Sorties cinéma: Quels films aller voir en salles cette semaine?', 'description': 'Se creuser les méninges avec «Cinq nouvelles du cerveau», râler avec «Tout nous sourit», applaudir «Un triomphe», etc.', 'url': 'https://www.tdg.ch/quels-films-aller-voir-en-salles-cette-semaine-255138039508', 'source': 'Tribune de Geneve', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/f0BbVPqS8-o/Aoyl6-gzK9XB29ztJ1Xdij.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-01T09:39:38+00:00'}, {'author': 'Amina Diagne', 'title': 'Jeux paralympiques Tokyo 2021 : Fatou Kiné Ndiaye termine 6ème avec un record', 'description': 'L&#8217;athlète Fatou Kiné Ndiaye qui faisait son entrée en lice aux jeux paralympiques de Tokyo...', 'url': 'https://wiwsport.com/2021/09/01/jeux-paralympiques-tokyo-2021-fatou-kine-ndiaye-termine-6eme-avec-un-record/', 'source': 'WIW Sport', 'image': None, 'category': 'sports', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T09:27:04+00:00'}, {'author': None, 'title': '«\xa0Le Point\xa0» fait sa rentrée', 'description': 'Chroniques, editos, decryptages, entretiens, lettres... > fait le plein de rendez-vous pour suivre une saison pas comme les autres.', 'url': 'https://www.lepoint.fr/medias/le-point-fait-sa-rentree-01-09-2021-2440954_260.php#xtor=RSS-221', 'source': 'lepoint', 'image': 'https://www.lepoint.fr/images/2021/09/01/22125101lpw-22129271-article-jpg_8193391.jpg', 'category': 'general', 'language': 'fr', 'country': 'fr', 'published_at': '2021-09-01T08:12:00+00:00'}, {'author': 'Amine Ait', 'title': 'France : longue file d’attente devant l’agence Opéra d’air Algérie', 'description': 'Chez Air Algérie, rien ne va plus, et ce, malgré les efforts dernièrement fournis par ses responsables. Suite à la crise sanitaire, la diaspora est la première à avoir souffert du gel des activités commerciales de la compagnie aérienne nationale. Après l&#8217;ouverture des frontières, les choses commencent à se régler, mais pour un retour à [&#8230;]L’article France : longue file d&rsquo;attente devant l&rsquo;agence Opéra d&rsquo;air Algérie est apparu en premier sur .', 'url': 'https://www.algerie360.com/france-longue-file-dattente-devant-lagence-opera-dair-algerie/', 'source': 'Algerie360.com', 'image': 'https://www.algerie360.com/wp-content/uploads/2021/09/241033893_1901839469987134_3925002526799295267_n-1024x651.jpg', 'category': 'general', 'language': 'fr', 'country': 'dz', 'published_at': '2021-09-01T16:35:53+00:00'}, {'author': 'Manuel Yepes', 'title': 'Suivi de la brigade de violences intra-familiales', 'description': "Les violences intra-familiales, violences faites aux femmes, aux hommes, aux enfants sont un fléau à La Réunion. De nouveaux moyens sont mis en place pour tenter de l'endiguer…L'objectif c'est surtout de libérer la parole des victimes. Certaines méthodes sont expérimentées, parfois pour la première fois en France. Témoignage et reportage de Thibault Cordier, Sylvain Ducasse et Mathilde (...)-Toutes nos vidéos/ JT 19h00", 'url': 'https://www.linfo.re/videos/toutes-nos-videos/suivi-de-la-brigade-de-violences-intra-familiales', 'source': 'LINFO.re', 'image': 'http://cdn.antenne.re/nas/ChroniqueThibault_2109011900.mp4', 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T15:49:08+00:00'}, {'author': 'Stéphane Pierrard', 'title': 'Violences urbaines à Saint-Louis : six majeurs condamnés', 'description': "Les soirs du 19 et du 20 août dernier, des jeunes encagoulés, armés de projectiles avaient tendu un guet-apens à l'encontre des forces de l'ordre au niveau du Ouaki. Jugés ce 1er septembre en comparution immédiate, ils ont été condamnés à des heures de travail d'intérêt général ou à des peines mixtes. Durant deux nuits de suite, à Saint-Louis, une quinzaine de jeunes encagoulés ont voulu en découdre avec les forces de l'ordre. Dans un premier temps, ils ont dérobé du matériel urbain, et même des biens dans (...)-Faits Divers/ Saint-Louis, gendarmerie, Newsletter, A la une...", 'url': 'https://www.linfo.re/la-reunion/faits-divers/violences-urbaines-a-saint-louis-six-majeurs-condamnes', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T15:40:00+00:00'}, {'author': 'Oly', 'title': "Covid-19 en métropole : des étudiants, recrutés pour réaliser des tests en avril, attendent toujours d'être payés", 'description': "Des étudiants en pharmacie ont été embauchés en urgence pour réaliser des tests et ils n'ont pas été payés depuis avril. Dans des laboratoires et des pharmacies, environ 800 000 tests Covid ont été réalisés chaque jour et pour les assurer, des étudiants ont été embauchés. La plupart d'entre eux ont répondu à des offres d'emploi disponibles sur le site 'Juste un test' avec un salaire plutôt alléchant allant jusqu'à 35 euros nets de l'heure pour réaliser des tests de dépistage du Covid-19. Depuis des mois, (...)-Société/ actualité france, Coronavirus", 'url': 'https://www.linfo.re/france/societe/covid-19-en-metropole-des-etudiants-recrutes-pour-realiser-des-tests-en-avril-attendent-toujours-d-etre-payes', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T16:24:00+00:00'}, {'author': 'APA', 'title': 'Afrique du Sud : hausse du prix de l’essence', 'description': "Les automobilistes sud-africains se sont réveillés, ce mercredi, avec une hausse de quatre cents du prix du litre d'essence et une baisse de 15,22 cents de celui du diesel.Le ministre des Ressources minérales et de l'énergie, Gwede Mantashe, les prix des deux catégories d'essence sans plomb (ULP) 93 octanes et 95 octanes ont été augmentés de quatre cents par litre.Cela signifie qu'un litre d'ULP 95 à Gauteng, qui coûtait 18,30 R (environ 1,26 USD), coûte désormais 18,34 R.Quant au prix du diesel à 0,05% de soufre, il a diminué de 15,22 cents par litre, là ou celui du diesel à 0,...", 'url': 'https://www.journaldumali.com/2021/09/01/afrique-du-sud-hausse-du-prix-de-lessence/', 'source': 'JournalDuMali.com', 'image': None, 'category': 'general', 'language': 'fr', 'country': 'ml', 'published_at': '2021-09-01T17:18:02+00:00'}, {'author': None, 'title': 'Vaccination contre le Covid: Vaud met le paquet pour convaincre les jeunes de passer sous l’aiguille', 'description': 'La campagne de vaccination du Canton se joue auprès des jeunes en formation, en plein jour mais aussi à la tombée de la nuit.', 'url': 'https://www.24heures.ch/vaud-met-le-paquet-pour-convaincre-les-jeunes-de-passer-sous-laiguille-602051338903', 'source': '24 heures', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/_Lzi4lv6jAo/EnESmHJQ4ylBQCK8v0I-hj.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-01T16:56:23+00:00'}, {'author': None, 'title': 'École, écologie, politique… Comment les Français voient leur pays', 'description': 'Inquiets, mais ni en colere ni profondement divises. > revele un sondage exceptionnel qui dresse un portrait inattendu de la societe francaise.', 'url': 'https://www.lepoint.fr/societe/ecole-ecologie-politique-comment-les-francais-voient-leur-pays-01-09-2021-2441079_23.php#xtor=RSS-221', 'source': 'lepoint', 'image': 'https://www.lepoint.fr/images/2021/09/01/22132797lpw-22133022-article-jpg_8194686.jpg', 'category': 'general', 'language': 'fr', 'country': 'fr', 'published_at': '2021-09-01T15:59:00+00:00'}, {'author': 'Nafy Amar Fall', 'title': 'AfroBasket 2021 – En demi-finale, le Sénégal jouera la Cote d’Ivoire', 'description': 'Après l&#8217;Angola qu&#8217;il a éliminé cet après-midi, le Sénégal sera opposé à la Cote d&#8217;Ivoire...', 'url': 'https://wiwsport.com/2021/09/01/afrobasket-2021-en-demi-finale-le-senegal-jouera-la-cote-divoire/', 'source': 'WIW Sport', 'image': None, 'category': 'sports', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T17:40:24+00:00'}, {'author': 'wiwsport', 'title': 'LIVE – Suivez Sénégal vs Togo en direct sur wiwsport.com', 'description': 'Le Sénégal reçoit le Togo ce mercredi au Stade Lat Dior de Thiès en match...', 'url': 'https://wiwsport.com/2021/09/01/live-suivez-senegal-vs-togo-en-direct-sur-wiwsport-com/', 'source': 'WIW Sport', 'image': None, 'category': 'sports', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T16:01:15+00:00'}, {'author': 'Jeannie', 'title': 'Sondage - Présidentielle 2022 : Emmanuel Macron devance légèrement Marine Le Pen au premier tour', 'description': "Une enquête Harris Interactive sur l'élection présidentielle 2022 a été réalisée pour Challenges. Les résultats montrent une légère avance d'Emmanuel Macron. Un sondage en ligne du 27 au 30 août Ce sondage Harris Interactive pour Challenges, concernant sur la présidentielle 2022, a été effectué en ligne du 27 au 30 août selon la méthode des quotas. Comme le rapporte BFMTV, il a été réalisé sur un échantillon de 1 328 personnes issues de la population française, âgée de 18 ans et plus, dont 1 083 inscrites (...)-Politique/ sondage, Election Présidentielle, Marine Le Pen...", 'url': 'https://www.linfo.re/france/politique/sondage-presidentielle-2022-emmanuel-macron-devance-legerement-marine-le-pen-au-premier-tour', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-02T06:49:11+00:00'}, {'author': None, 'title': 'Mais que se passe-t-il entre l’Arménie et l’Azerbaïdjan ?', 'description': "Un soldat arménien est mort ce mercredi à la frontière avec l'Azerbaïdjan, laissant craindre une nouvelle montée des violences entre les deux pays. Mais pourquoi la région du Karabakh cristallise-t-elle toutes les tensions ? Pour comprendre, il faut remonter un siècle en arrière.", 'url': 'https://www.republicain-lorrain.fr/defense-guerre-conflit/2021/09/02/mais-que-se-passe-t-il-entre-l-armenie-et-l-azerbaidjan', 'source': 'La Republicain', 'image': 'https://cdn-s-www.republicain-lorrain.fr/images/51576CB5-DB66-472D-90A5-C45A69EE0D44/NW_listB/depuis-de-nombreuses-annees-armenie-et-azerbaidjan-se-disputent-le-territoire-situe-entre-leurs-deux-pays-photo-d-illustration-aris-messinis-afp-1630524455.jpg', 'category': 'general', 'language': 'fr', 'country': 'ne', 'published_at': '2021-09-02T06:33:00+00:00'}, {'author': None, 'title': 'Deux mois après la promotion: Les handballeurs genevois vont découvrir le tout haut niveau', 'description': 'Chênois Genève se rend ce jeudi à Aarau affronter l’une des meilleures équipes du pays. Son entraîneur, Juan Basmalis Gomez, fait le point avant ce premier match en Quickline Handball League.', 'url': 'https://www.tdg.ch/les-handballeurs-genevois-vont-decouvrir-le-tout-haut-niveau-889016933693', 'source': 'Tribune de Geneve', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/j_kmX_tx-AU/2dRKCKZCKqTAXB8h890xJW.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:06:33+00:00'}, {'author': None, 'title': 'Rénovation d’une locomotive: Leur «maîtresse rouge» ouvre ses portes après un chantier d’une décennie', 'description': 'À Givrins, les travaux de rénovation d’une automotrice de 1914 commencés en 2010 semblaient s’éterniser, mais l’engin rouge flambant neuf sera finalement présenté au grand public ce samedi.', 'url': 'https://www.24heures.ch/leur-maitresse-rouge-ouvre-ses-portes-apres-un-chantier-dune-decennie-128025225801', 'source': '24 heures', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/HLWYiaf2p0M/4SGNUJ1da519ed8sn3OZ6N.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:30:23+00:00'}, {'author': None, 'title': 'Immobilier en Suisse: Les prix des appartements grimpent encore', 'description': 'Les annonceurs immobiliers demandaient en moyenne 7916 francs par mètre carré pour les appartements en copropriété à la fin du mois d’août, soit une hausse de 1,8% en un mois. Les loyers ont toutefois baissé.', 'url': 'https://www.tdg.ch/les-prix-des-appartements-grimpent-encore-368671903454', 'source': 'Tribune de Geneve', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/PpY4KCAC-fU/ElZBcSfkKKK8HPDpZgn-s_.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:40:05+00:00'}, {'author': None, 'title': 'Avant la Champions League: Le LHC se cherche encore à plusieurs niveaux', 'description': 'Lausanne va profiter des rencontres de Champions League de ce jeudi (Lukko Rauma) et de samedi (Cardiff) pour soigner ses automatismes. Il doit aussi affiner son contingent de joueurs.', 'url': 'https://www.24heures.ch/le-lhc-se-cherche-encore-a-plusieurs-niveaux-884428683272', 'source': '24 heures', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/7dQBmN8hvUE/BCc3NQQuKebBmasvhx1zJX.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:00:04+00:00'}]}
        result = ""
        for i in range(self.max_articles):
            result += f"{current['data'][i]['title']}\n" \
            f"de {current['data'][i]['author']}\n" \
            f"publié le : {current['data'][i]['published_at']}\n\n" \
            f"{current['data'][i]['description']}\n\n" \
            f"url: {current['data'][i]['url']}\n\n\n" \

        return result

# exemple de retour{'pagination': {'limit': 25, 'offset': 0, 'count': 25, 'total': 10000}, 'data': [{'author': 'Diéry DIALLO', 'title': '(Vidéo) Foot – El Hadji Diouf: “Je n’ai jamais écouté mes entraîneurs et sur le terrain c’est …”', 'description': 'De nos jours, les joueurs sont plus importants que le coach dans une équipe de football. C&#8217;est l&#8217;avis de l’ancien international sénégalais, El Hadji Ousseynou Diouf qui était l&#8217;invité dans l’émission Walf Sports de Walf TV. Au cours de ladite émission, l&#8217;ancien capitaine des Lions de la Téranga révèle qu&#8217;il n&#8217;écoutait pas les consignes de [&#8230;]L’article (Vidéo) Foot &#8211; El Hadji Diouf: “Je n’ai jamais écouté mes entraîneurs et sur le terrain c&#8217;est &#8230;&#8221; est apparu en premier sur Senego.com - Actualité au Séné...', 'url': 'https://senego.com/video-foot-el-hadji-diouf-je-nai-jamais-ecoute-mes-entraineurs-et-sur-le-terrain-cest_1315607.html', 'source': 'Senego', 'image': 'https://www.youtube.com/embed/FGlrX2WCaI0', 'category': 'general', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T09:48:00+00:00'}, {'author': 'Marine Magnien', 'title': 'Des balises avifaunes pour préserver les espèces protégées', 'description': 'La ligne très haute tension Bras de la Plaine - Le Gol va être équipée d\'une soixantaine de balises dites "avifaunes". Avec ces équipements, EDF et la SEOR se lancent dans un projet expérimental de préservation des espèces d\'oiseaux marins protégées de La Réunion.-Toutes nos vidéos/ JT 12h30', 'url': 'https://www.linfo.re/videos/toutes-nos-videos/des-balises-avifaunes-pour-preserver-les-especes-protegees', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T09:04:43+00:00'}, {'author': 'Marine Magnien', 'title': 'Musique : retour sur le chanteur Gramoun Lélé !', 'description': "Allez ce mercredi on va vous parler d'un chanteur Réunionnais, Julien Phileas, plus connu sous le nom de Gramoun Lélé ! Son portrait avec l'historien Prosper Eve dans la minute du 12h30 réalisée par Sylvain Ducasse !-Toutes nos vidéos/ Home Page, JT 12h30", 'url': 'https://www.linfo.re/videos/toutes-nos-videos/musique-retour-sur-le-chanteur-gramoun-lele', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T09:01:50+00:00'}, {'author': 'Merzouk Abdelaziz', 'title': 'Pluies orageuses et vents\xa0: les prévisions météo pour ce mercredi', 'description': 'Après les fortes chaleurs caniculaires du mois d’août dernier, l’automne s’installe désormais en Algérie. Depuis plusieurs jours, les pluies orageuses ont s’abattent sur plusieurs régions du nord et du centre du pays. C’est le cas, d’ailleurs, pour aujourd’hui. Dans un bulletin météo spécial (BMS), l’office national de météorologie a placé, ce mercredi 1er septembre, sept [&#8230;]L’article Pluies orageuses et vents\xa0: les prévisions météo pour ce mercredi est apparu en premier sur .', 'url': 'https://www.algerie360.com/pluies-orageuses-et-vents-les-previsions-meteo-pour-ce-mercredi/', 'source': 'Algerie360.com', 'image': 'https://www.algerie360.com/wp-content/uploads/2021/09/meteo-1024x576.jpg', 'category': 'general', 'language': 'fr', 'country': 'dz', 'published_at': '2021-09-01T08:57:38+00:00'}, {'author': 'Antoine Sarr', 'title': 'Kaolack: Une militante de Pastef traîne en justice des policiers', 'description': 'La responsable de Pastef à Kaolack, Adji Ndao, a décidé de traîner en justice trois policiers qui l’avaient tabassée lors de son interpellation. La dame qui vit à l’étranger s’était retrouvée avec un œil enflé avant d’être évacuée à l’hôpital. Citation directe&#8230; Les militants de Pastef organisaient une caravane de sensibilisation pour les inscriptions sur [&#8230;]L’article Kaolack: Une militante de Pastef traîne en justice des policiers est apparu en premier sur Senego.com - Actualité au Sénégal, toute actualité du jour.', 'url': 'https://senego.com/kaolack-une-militante-de-pastef-traine-en-justice-des-policiers_1315509.html', 'source': 'Senego', 'image': None, 'category': 'general', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T08:17:49+00:00'}, {'author': 'Mandaw Mbengue', 'title': 'Eliminatoires Mondial 2022: Le Sénégal débute contre le Togo, ce mercredi', 'description': 'Le Sénégal débute sa Campagne dans les éliminatoires de la Coupe du Monde 2022, ce Jeudi. Aliou Cissé et ses hommes ont rendez-vous avec le Togo au Stade Lat Dior de Thiès à partir de 16h. Une victoire pour bien démarrer les éliminatoires de la Coupe du Monde 2022 est l&#8217;objectif des Lions. Un match [&#8230;]L’article Eliminatoires Mondial 2022: Le Sénégal débute contre le Togo, ce mercredi est apparu en premier sur Senego.com - Actualité au Sénégal, toute actualité du jour.', 'url': 'https://senego.com/eliminatoires-mondial-2022-le-senegal-debute-contre-le-togo-ce-mercredi_1315520.html', 'source': 'Senego', 'image': None, 'category': 'general', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T08:48:31+00:00'}, {'author': None, 'title': "Présidentielle : l'ex-LREM Aurélien Taché soutient Eric Piolle", 'description': "Aurélien Taché, ancien député LREM, déçu de la macronie, va voter à la primaire des écologistes et s'engagé aux côtés d'Eric Piolle, dans la campagne en vue de la présidentielle de 2022.", 'url': 'https://www.republicain-lorrain.fr/politique/2021/09/01/presidentielle-l-ex-lrem-aurelien-tache-soutient-eric-piolle', 'source': 'La Republicain', 'image': 'https://cdn-s-www.republicain-lorrain.fr/images/902CB409-D3BF-419E-A13C-F1F93E477468/NW_listB/photo-christophe-petit-tesson-afp-1630484830.jpg', 'category': 'general', 'language': 'fr', 'country': 'ne', 'published_at': '2021-09-01T08:27:00+00:00'}, {'author': None, 'title': 'Sorties cinéma: Quels films aller voir en salles cette semaine?', 'description': 'Se creuser les méninges avec «Cinq nouvelles du cerveau», râler avec «Tout nous sourit», applaudir «Un triomphe», etc.', 'url': 'https://www.tdg.ch/quels-films-aller-voir-en-salles-cette-semaine-255138039508', 'source': 'Tribune de Geneve', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/f0BbVPqS8-o/Aoyl6-gzK9XB29ztJ1Xdij.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-01T09:39:38+00:00'}, {'author': 'Amina Diagne', 'title': 'Jeux paralympiques Tokyo 2021 : Fatou Kiné Ndiaye termine 6ème avec un record', 'description': 'L&#8217;athlète Fatou Kiné Ndiaye qui faisait son entrée en lice aux jeux paralympiques de Tokyo...', 'url': 'https://wiwsport.com/2021/09/01/jeux-paralympiques-tokyo-2021-fatou-kine-ndiaye-termine-6eme-avec-un-record/', 'source': 'WIW Sport', 'image': None, 'category': 'sports', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T09:27:04+00:00'}, {'author': None, 'title': '«\xa0Le Point\xa0» fait sa rentrée', 'description': 'Chroniques, editos, decryptages, entretiens, lettres... > fait le plein de rendez-vous pour suivre une saison pas comme les autres.', 'url': 'https://www.lepoint.fr/medias/le-point-fait-sa-rentree-01-09-2021-2440954_260.php#xtor=RSS-221', 'source': 'lepoint', 'image': 'https://www.lepoint.fr/images/2021/09/01/22125101lpw-22129271-article-jpg_8193391.jpg', 'category': 'general', 'language': 'fr', 'country': 'fr', 'published_at': '2021-09-01T08:12:00+00:00'}, {'author': 'Amine Ait', 'title': 'France : longue file d’attente devant l’agence Opéra d’air Algérie', 'description': 'Chez Air Algérie, rien ne va plus, et ce, malgré les efforts dernièrement fournis par ses responsables. Suite à la crise sanitaire, la diaspora est la première à avoir souffert du gel des activités commerciales de la compagnie aérienne nationale. Après l&#8217;ouverture des frontières, les choses commencent à se régler, mais pour un retour à [&#8230;]L’article France : longue file d&rsquo;attente devant l&rsquo;agence Opéra d&rsquo;air Algérie est apparu en premier sur .', 'url': 'https://www.algerie360.com/france-longue-file-dattente-devant-lagence-opera-dair-algerie/', 'source': 'Algerie360.com', 'image': 'https://www.algerie360.com/wp-content/uploads/2021/09/241033893_1901839469987134_3925002526799295267_n-1024x651.jpg', 'category': 'general', 'language': 'fr', 'country': 'dz', 'published_at': '2021-09-01T16:35:53+00:00'}, {'author': 'Manuel Yepes', 'title': 'Suivi de la brigade de violences intra-familiales', 'description': "Les violences intra-familiales, violences faites aux femmes, aux hommes, aux enfants sont un fléau à La Réunion. De nouveaux moyens sont mis en place pour tenter de l'endiguer…L'objectif c'est surtout de libérer la parole des victimes. Certaines méthodes sont expérimentées, parfois pour la première fois en France. Témoignage et reportage de Thibault Cordier, Sylvain Ducasse et Mathilde (...)-Toutes nos vidéos/ JT 19h00", 'url': 'https://www.linfo.re/videos/toutes-nos-videos/suivi-de-la-brigade-de-violences-intra-familiales', 'source': 'LINFO.re', 'image': 'http://cdn.antenne.re/nas/ChroniqueThibault_2109011900.mp4', 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T15:49:08+00:00'}, {'author': 'Stéphane Pierrard', 'title': 'Violences urbaines à Saint-Louis : six majeurs condamnés', 'description': "Les soirs du 19 et du 20 août dernier, des jeunes encagoulés, armés de projectiles avaient tendu un guet-apens à l'encontre des forces de l'ordre au niveau du Ouaki. Jugés ce 1er septembre en comparution immédiate, ils ont été condamnés à des heures de travail d'intérêt général ou à des peines mixtes. Durant deux nuits de suite, à Saint-Louis, une quinzaine de jeunes encagoulés ont voulu en découdre avec les forces de l'ordre. Dans un premier temps, ils ont dérobé du matériel urbain, et même des biens dans (...)-Faits Divers/ Saint-Louis, gendarmerie, Newsletter, A la une...", 'url': 'https://www.linfo.re/la-reunion/faits-divers/violences-urbaines-a-saint-louis-six-majeurs-condamnes', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T15:40:00+00:00'}, {'author': 'Oly', 'title': "Covid-19 en métropole : des étudiants, recrutés pour réaliser des tests en avril, attendent toujours d'être payés", 'description': "Des étudiants en pharmacie ont été embauchés en urgence pour réaliser des tests et ils n'ont pas été payés depuis avril. Dans des laboratoires et des pharmacies, environ 800 000 tests Covid ont été réalisés chaque jour et pour les assurer, des étudiants ont été embauchés. La plupart d'entre eux ont répondu à des offres d'emploi disponibles sur le site 'Juste un test' avec un salaire plutôt alléchant allant jusqu'à 35 euros nets de l'heure pour réaliser des tests de dépistage du Covid-19. Depuis des mois, (...)-Société/ actualité france, Coronavirus", 'url': 'https://www.linfo.re/france/societe/covid-19-en-metropole-des-etudiants-recrutes-pour-realiser-des-tests-en-avril-attendent-toujours-d-etre-payes', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-01T16:24:00+00:00'}, {'author': 'APA', 'title': 'Afrique du Sud : hausse du prix de l’essence', 'description': "Les automobilistes sud-africains se sont réveillés, ce mercredi, avec une hausse de quatre cents du prix du litre d'essence et une baisse de 15,22 cents de celui du diesel.Le ministre des Ressources minérales et de l'énergie, Gwede Mantashe, les prix des deux catégories d'essence sans plomb (ULP) 93 octanes et 95 octanes ont été augmentés de quatre cents par litre.Cela signifie qu'un litre d'ULP 95 à Gauteng, qui coûtait 18,30 R (environ 1,26 USD), coûte désormais 18,34 R.Quant au prix du diesel à 0,05% de soufre, il a diminué de 15,22 cents par litre, là ou celui du diesel à 0,...", 'url': 'https://www.journaldumali.com/2021/09/01/afrique-du-sud-hausse-du-prix-de-lessence/', 'source': 'JournalDuMali.com', 'image': None, 'category': 'general', 'language': 'fr', 'country': 'ml', 'published_at': '2021-09-01T17:18:02+00:00'}, {'author': None, 'title': 'Vaccination contre le Covid: Vaud met le paquet pour convaincre les jeunes de passer sous l’aiguille', 'description': 'La campagne de vaccination du Canton se joue auprès des jeunes en formation, en plein jour mais aussi à la tombée de la nuit.', 'url': 'https://www.24heures.ch/vaud-met-le-paquet-pour-convaincre-les-jeunes-de-passer-sous-laiguille-602051338903', 'source': '24 heures', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/_Lzi4lv6jAo/EnESmHJQ4ylBQCK8v0I-hj.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-01T16:56:23+00:00'}, {'author': None, 'title': 'École, écologie, politique… Comment les Français voient leur pays', 'description': 'Inquiets, mais ni en colere ni profondement divises. > revele un sondage exceptionnel qui dresse un portrait inattendu de la societe francaise.', 'url': 'https://www.lepoint.fr/societe/ecole-ecologie-politique-comment-les-francais-voient-leur-pays-01-09-2021-2441079_23.php#xtor=RSS-221', 'source': 'lepoint', 'image': 'https://www.lepoint.fr/images/2021/09/01/22132797lpw-22133022-article-jpg_8194686.jpg', 'category': 'general', 'language': 'fr', 'country': 'fr', 'published_at': '2021-09-01T15:59:00+00:00'}, {'author': 'Nafy Amar Fall', 'title': 'AfroBasket 2021 – En demi-finale, le Sénégal jouera la Cote d’Ivoire', 'description': 'Après l&#8217;Angola qu&#8217;il a éliminé cet après-midi, le Sénégal sera opposé à la Cote d&#8217;Ivoire...', 'url': 'https://wiwsport.com/2021/09/01/afrobasket-2021-en-demi-finale-le-senegal-jouera-la-cote-divoire/', 'source': 'WIW Sport', 'image': None, 'category': 'sports', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T17:40:24+00:00'}, {'author': 'wiwsport', 'title': 'LIVE – Suivez Sénégal vs Togo en direct sur wiwsport.com', 'description': 'Le Sénégal reçoit le Togo ce mercredi au Stade Lat Dior de Thiès en match...', 'url': 'https://wiwsport.com/2021/09/01/live-suivez-senegal-vs-togo-en-direct-sur-wiwsport-com/', 'source': 'WIW Sport', 'image': None, 'category': 'sports', 'language': 'fr', 'country': 'sn', 'published_at': '2021-09-01T16:01:15+00:00'}, {'author': 'Jeannie', 'title': 'Sondage - Présidentielle 2022 : Emmanuel Macron devance légèrement Marine Le Pen au premier tour', 'description': "Une enquête Harris Interactive sur l'élection présidentielle 2022 a été réalisée pour Challenges. Les résultats montrent une légère avance d'Emmanuel Macron. Un sondage en ligne du 27 au 30 août Ce sondage Harris Interactive pour Challenges, concernant sur la présidentielle 2022, a été effectué en ligne du 27 au 30 août selon la méthode des quotas. Comme le rapporte BFMTV, il a été réalisé sur un échantillon de 1 328 personnes issues de la population française, âgée de 18 ans et plus, dont 1 083 inscrites (...)-Politique/ sondage, Election Présidentielle, Marine Le Pen...", 'url': 'https://www.linfo.re/france/politique/sondage-presidentielle-2022-emmanuel-macron-devance-legerement-marine-le-pen-au-premier-tour', 'source': 'LINFO.re', 'image': None, 'category': 'general', 'language': 'fr', 'country': 're', 'published_at': '2021-09-02T06:49:11+00:00'}, {'author': None, 'title': 'Mais que se passe-t-il entre l’Arménie et l’Azerbaïdjan ?', 'description': "Un soldat arménien est mort ce mercredi à la frontière avec l'Azerbaïdjan, laissant craindre une nouvelle montée des violences entre les deux pays. Mais pourquoi la région du Karabakh cristallise-t-elle toutes les tensions ? Pour comprendre, il faut remonter un siècle en arrière.", 'url': 'https://www.republicain-lorrain.fr/defense-guerre-conflit/2021/09/02/mais-que-se-passe-t-il-entre-l-armenie-et-l-azerbaidjan', 'source': 'La Republicain', 'image': 'https://cdn-s-www.republicain-lorrain.fr/images/51576CB5-DB66-472D-90A5-C45A69EE0D44/NW_listB/depuis-de-nombreuses-annees-armenie-et-azerbaidjan-se-disputent-le-territoire-situe-entre-leurs-deux-pays-photo-d-illustration-aris-messinis-afp-1630524455.jpg', 'category': 'general', 'language': 'fr', 'country': 'ne', 'published_at': '2021-09-02T06:33:00+00:00'}, {'author': None, 'title': 'Deux mois après la promotion: Les handballeurs genevois vont découvrir le tout haut niveau', 'description': 'Chênois Genève se rend ce jeudi à Aarau affronter l’une des meilleures équipes du pays. Son entraîneur, Juan Basmalis Gomez, fait le point avant ce premier match en Quickline Handball League.', 'url': 'https://www.tdg.ch/les-handballeurs-genevois-vont-decouvrir-le-tout-haut-niveau-889016933693', 'source': 'Tribune de Geneve', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/j_kmX_tx-AU/2dRKCKZCKqTAXB8h890xJW.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:06:33+00:00'}, {'author': None, 'title': 'Rénovation d’une locomotive: Leur «maîtresse rouge» ouvre ses portes après un chantier d’une décennie', 'description': 'À Givrins, les travaux de rénovation d’une automotrice de 1914 commencés en 2010 semblaient s’éterniser, mais l’engin rouge flambant neuf sera finalement présenté au grand public ce samedi.', 'url': 'https://www.24heures.ch/leur-maitresse-rouge-ouvre-ses-portes-apres-un-chantier-dune-decennie-128025225801', 'source': '24 heures', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/HLWYiaf2p0M/4SGNUJ1da519ed8sn3OZ6N.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:30:23+00:00'}, {'author': None, 'title': 'Immobilier en Suisse: Les prix des appartements grimpent encore', 'description': 'Les annonceurs immobiliers demandaient en moyenne 7916 francs par mètre carré pour les appartements en copropriété à la fin du mois d’août, soit une hausse de 1,8% en un mois. Les loyers ont toutefois baissé.', 'url': 'https://www.tdg.ch/les-prix-des-appartements-grimpent-encore-368671903454', 'source': 'Tribune de Geneve', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/PpY4KCAC-fU/ElZBcSfkKKK8HPDpZgn-s_.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:40:05+00:00'}, {'author': None, 'title': 'Avant la Champions League: Le LHC se cherche encore à plusieurs niveaux', 'description': 'Lausanne va profiter des rencontres de Champions League de ce jeudi (Lukko Rauma) et de samedi (Cardiff) pour soigner ses automatismes. Il doit aussi affiner son contingent de joueurs.', 'url': 'https://www.24heures.ch/le-lhc-se-cherche-encore-a-plusieurs-niveaux-884428683272', 'source': '24 heures', 'image': 'https://cdn.unitycms.io/image/ocroped/400,400,1000,1000,0,0/7dQBmN8hvUE/BCc3NQQuKebBmasvhx1zJX.jpg', 'category': 'general', 'language': 'fr', 'country': 'ch', 'published_at': '2021-09-02T06:00:04+00:00'}]}