import random
import json

import os


chemin = "/storage/emulated/0/Mods/"

memoire_mods = {}
for f in os.listdir(chemin):
    if f.endswith(".NayMOD"):
        with open(chemin + f, "r", encoding="utf-8") as file:
            for ligne in file:
                if ":" in ligne:
                    cle, rep = ligne.split(":", 1)
                    memoire_mods[cle.strip().lower()] = rep.strip()
                    

                    
for f in os.listdir(chemin):
    if f.endswith(".NayMOD"):
        print(f"SYSTÈME : Le mod {f} a été chargé avec succès !")
        
        with open(chemin + f, "r", encoding="utf-8") as file:
            for ligne in file:
                if ":" in ligne:
                    cle, rep = ligne.split(":", 1)
                    memoire_mods[cle.strip().lower()] = rep.strip()
 
# --- TEST DU LECTEUR ---
# NayIA_Pro = lecteur_fastmd("BetterPerf.FastMD")




# =============================================================================
# PROJET : NAYIA 2.1 - L'INTELLIGENCE ARTIFICIELLE MODULABLE
# AUTEUR ORIGINAL : [Nayane Ahamadi @NayCode]
# VERSION : 2.1
# LICENCE : CREATIVE COMMONS ATTRIBUTION (MODDING AUTORISE)
# -----------------------------------------------------------------------------
# GUIDE DE MODDING POUR LES UTILISATEURS :
# 1. Vous pouvez modifier ce code pour ajouter vos propres commandes.
# 2. Si vous publiez une version modifiee, merci de citer l'auteur original.
# 3. Ne modifiez pas la structure des espaces (indentation) sous peine de bug.
# 4. Pour ajouter des connaissances, utilisez la commande /learn dans l'IA
#    ou ajoutez des blocs 'elif' dans la section 'LOGIQUE DE REPONSE'.
# =============================================================================


# --- LOGO DE BIENVENUE ---
logo = """
  _   _                 ___   _        ____    
 | \ | |  __ _  _   _  |_ _| / \      |___ \  
 |  \| | / _` || | | |  | | / _ \       __) |
 | |\  || (_| || |_| |  | |/ ___ \     / __/_
 |_| \_| \__,_| \__, | |___/_/   \_\  |_____|
                |___/                               
      >> SYSTEME NAYIA VERSION 2.1 CHARGÉ <<
      >> DEVELOPPEUR : NAYANE             <<
      >> STATUT : OPERATIONNEL            <<
----------------------------------------------------------------------------
"""

print(logo)# On affiche le logo au demarrage


# --- BLOC MÉMOIRE ---
try:
    with open("memoire.json", "r") as f:
        memoire = json.load(f)
except:
    memoire = {}


while True:
    question = input("Toi : ").lower().strip()

    # 1. SI ON TAPE STOP : On sauvegarde et on ferme
    if question == "stop":
        print("NayIA : Au revoir !")
        with open("memoire.json", "w") as f:
            json.dump(memoire, f)
        break 

    # 2. 
    elif question in memoire:
        print("NayIA :", memoire[question])

    # 3. Logique reponse
    elif "bonjour" in question:
        reponses = ["Bonjour humain !", "Salut ! Comment ça va ?", "Hello ! Ravi de te voir !"]
        print("NayIA :", random.choice(reponses))
        
    elif question in memoire_mods:
        print(f"NayIA : {memoire_mods[question]}")

        
        
    elif "cine" in question:
            films = [
                "Star Wars: Un jeune fermier rejoint une alliance rebelle pour sauver la galaxie.",
                "Le Roi Lion: Un jeune lion doit retrouver sa place de roi apres la mort de son pere.",
                "Titanic: Une histoire d'amour tragique a bord d'un paquebot qui coule en 1912.",
                "Harry Potter: Un orphelin decouvre qu'il est sorcier et combat un mage noir.",
                "Inception: Un voleur s'infiltre dans les reves pour implanter une idee.",
                "Avatar: Un soldat paralyse explore un monde extraterrestre appele Pandora.",
                "Gladiator: Un general romain trahi devient gladiateur pour se venger.",
                "Matrix: Un hacker decouvre que le monde reel est une simulation informatique.",
                "Jurassic Park: Des scientifiques creent un parc avec des dinosaures vivants.",
                "Le Seigneur des Anneaux: Un hobbit doit detruire un anneau maléfique.",
                "Forrest Gump: La vie extraordinaire d'un homme simple a travers l'histoire des USA.",
                "The Dark Knight: Batman affronte le Joker, un criminel qui veut semer le chaos.",
                "Interstellar: Des astronautes cherchent une nouvelle planete pour l'humanite.",
                "Jaws: Un grand requin blanc terrorise une ville balneaire.",
                "Toy Story: Les jouets d'un enfant prennent vie quand il n'est pas la.",
                "Pulp Fiction: Les histoires croisees de criminels a Los Angeles.",
                "Le Parrain: L'ascension et la chute d'une famille de la mafia italienne.",
                "Braveheart: Un guerrier ecossais mene son peuple vers la liberte.",
                "Retour vers le futur: Un adolescent voyage dans le passe avec une voiture.",
                "Le Silence des Agneaux: Une agente du FBI demande l'aide d'un tueur cannibale.",
                "Shrek: Un ogre vert part sauver une princesse pour recuperer son marais.",
                "Seven: Deux policiers traquent un tueur inspire par les sept peches capitaux.",
                "Fight Club: Un homme cree un club de combat clandestin pour se sentir vivant.",
                "Independance Day: La Terre doit se defendre contre une invasion extraterrestre.",
                "Grease: Une histoire d'amour entre deux lyceens dans les annees 50.",
                "E.T.: Un enfant se lie d'amitie avec un extraterrestre perdu sur Terre.",
                "Alien: L'equipage d'un vaisseau spatial est traque par une creature mortelle.",
                "Ratatouille: Un rat doue en cuisine aide un jeune homme a devenir chef.",
                "Coco: Un jeune mexicain voyage au pays des morts pour trouver son ancetre.",
                "La Reine des Neiges: Une princesse cherche sa soeur dont les pouvoirs ont gele le royaume.",
                "Up: Un vieil homme voyage dans une maison portee par des ballons.",
                "Spider-Man: Un lyceen acquiert des super-pouvoirs apres une morsure d'araignee.",
                "Iron Man: Un milliardaire construit une armure pour combattre le terrorisme.",
                "Black Panther: Le roi du Wakanda doit defendre son trone et son peuple.",
                "Le Loup de Wall Street: L'ascension folle d'un courtier en bourse malhonnete.",
                "Indiana Jones: Un archeologue cherche des reliques perdues a travers le monde.",
                "Ghostbusters: Des scientifiques chassent les fantomes dans New York.",
                "The Truman Show: Un homme decouvre que sa vie est une emission de tele-realite.",
                "Men in Black: Des agents secrets surveillent les extraterrestres sur Terre.",
                "Kill Bill: Une femme cherche a se venger de ceux qui ont tente de la tuer.",
                "La Ligne Verte: Un gardien de prison decouvre qu'un condamne a des pouvoirs.",
                "Inglourious Basterds: Des soldats juifs preparent un attentat contre les nazis.",
                "Django Unchained: Un esclave libere devient chasseur de primes pour sauver sa femme.",
                "Mad Max: Dans un futur desertique, un homme aide des femmes a fuir un tyran.",
                "The Revenant: Un trappeur survit dans le froid pour se venger de son equipe.",
                "Leon: Un tueur a gages prend sous son aile une petite fille orpheline.",
                "Amelie Poulain: Une serveuse parisienne decide de changer la vie des autres.",
                "Intouchables: L'amitie entre un riche paralyse et son aide soignant.",
                "Taxi: Un chauffeur de taxi marseillais aide la police avec sa voiture rapide.",
                "Le Cinquieme Element: Un chauffeur de taxi doit sauver le monde au futur."
            ]
            import random
            print("NayIA 2.1 - Suggestion de film :")
            print(random.choice(films))

        



    elif "python" in question:
        reponses = ["Python est un langage de programmation.", "Python est très utilisé pour l'IA.", "Beaucoup de développeurs adorent Python.", "Moi meme je suis fait en Python !"]
        print("NayIA :", random.choice(reponses))
        
    elif "omelette" in question or "oeufs" in question:
        recette_chef = """
        --- LA RECETTE EXCLUSIVE DU CREATEUR DE NAYIA ---
        Attention : Cette recette demande de la rapidite !
        
        PREPARATION :
        1. Prenez 3 ou 4 oeufs frais (selon votre faim).
        2. Mettez une noisette de beurre dans une PETITE poele.
        3. Allumez le feu au MAXIMUM (C'est le secret !).
        
        CUISSON FLASH :
        4. Versez les oeufs directement dans la poele chaude.
        5. Melangez rapidement mais PAS TROP : il faut qu'il reste
           du blanc d'oeuf visible, non melange au jaune.
        6. Assaisonnez immediatement : Sel, Poivre, Herbes de Provence.
        7. Ajoutez la touche finale : de la CORIANDRE fraiche.
        
        FINITION :
        8. Remelangez une derniere fois tres brievement.
        9. Ne laissez pas trop longtemps ! L'omelette doit rester
           BIEN JUTEUSE et on doit voir les morceaux de blanc.
        10. Servez dans une assiette et regalez-vous !
        --------------------------------------------------
        """
        print(recette_chef)

    elif "merci" in question or "thanks" in question:
            import random
            reponses_merci = [
                "De rien ! C'est un plaisir d'aider un chef cuistot comme toi.",
                "Je t'en prie ! N'oublie pas de surveiller la cuisson de l'omelette.",
                "A ton service ! C'est ma mission de t'accompagner.",
                "Pas de souci ! NayIA est la pour ca.",
                "C'est tout naturel. On forme une bonne equipe, non ?",
                "De rien ! N'hesite pas si tu as d'autres questions sur le cine ou les monuments.",
                "Avec plaisir ! Content que mes conseils te soient utiles."
            ]
            print("NayIA : " + random.choice(reponses_merci))

    elif "burger" in question or "hamburger" in question:
        recette_burger = """
        --- LE BURGER MAISON FACON NAYIA ---
        
        LE SECRET : Le pain (bun) doit etre toaster avec du beurre !
        
        INGREDIENTS :
        - 1 pain burger de qualite
        - 150g de viande hachee (15% de matiere grasse)
        - 2 tranches de cheddar veritable
        - Oignons carame lises (cuits doucement a la poele)
        - Sauce secrete : Melange Mayo, Ketchup et une pointe de Moutarde.
        
        TECHNIQUE :
        1. Formez un palet de viande bien froid.
        2. Saisissez la viande a la poele TRES CHAUDE (1 min 30 par face).
        3. Posez le fromage sur la viande en fin de cuisson et couvrez.
        4. Toastez le pain. Tartinez de sauce.
        5. Ajoutez la viande, les oignons et une feuille de salade.
        --------------------------------------------------
        """
        print(recette_burger)

    elif "carbonara" in question or "pates" in question:
        recette_pates = """
        --- LA VRAIE CARBONARA ITALIENNE (SANS CREME !) ---
        
        ATTENTION : Les Italiens disent que mettre de la creme est un crime !
        
        INGREDIENTS :
        - 100g de Spaghetti de qualite
        - 50g de Guanciale (ou pancetta/lardons de qualite)
        - 1 oeuf entier + 1 jaune d'oeuf
        - 30g de Pecorino Romano ou Parmesan fraichement rape
        - BEAUCOUP de poivre noir concasse.
        
        TECHNIQUE :
        1. Faites cuire les pates dans l'eau bouillante (SANS SEL car le fromage l'est deja).
        2. Faites griller le lard dans une poele sans matiere grasse.
        3. Dans un bol, melangez les oeufs et le fromage pour faire une creme.
        4. Egouttez les pates (gardez un peu d'eau de cuisson).
        5. Melangez les pates au lard, ETEIGNEZ LE FEU (important !).
        6. Versez le melange oeuf/fromage et remuez vite pour faire une sauce onctueuse.
        --------------------------------------------------
        """
        print(recette_pates)

    elif "chocolat" in question or "dessert" in question:
        recette_choc = """
        --- LE FONDANT AU CHOCOLAT EXPRESS ---
        
        INGREDIENTS :
        - 200g de chocolat noir (70% de cacao)
        - 100g de beurre
        - 3 oeufs
        - 50g de sucre
        - 50g de farine
        
        TECHNIQUE :
        1. Faites fondre le chocolat et le beurre ensemble au bain-marie.
        2. Battez les oeufs et le sucre jusqu'a ce que le melange blanchisse.
        3. Ajoutez le chocolat fondu, puis la farine tamisee.
        4. Versez dans des moules beurres.
        5. Faites cuire 8 a 10 minutes a 180 degres. 
        6. Le coeur doit rester coulant !
        --------------------------------------------------
        """
        print(recette_choc)


    elif "nayia" in question:
        reponses = ["Tu parles de moi ? Je suis encore en développement.", "Oui c'est moi !", "Je ne suis pas la meilleure IA mais on peut discuter."]
        print("NayIA :", random.choice(reponses))

    elif "nayane" in question:
        reponses = ["C'est lui qui m'a créé !", "Oui, c'est mon créateur.", "Grace à lui je peux parler."]
        print("NayIA :", random.choice(reponses))

    elif "salut" in question:
        reponses = ["Salut !", "Salut à toi aussi !"]
        print("NayIA :", random.choice(reponses))
        
    elif "fait" in question or "insolite" in question or "savais-tu" in question:
        faits = [
            "L'eau chaude gele plus vite que l'eau froide.", "La Joconde n'a pas de sourcils.",
            "Le muscle le plus fort par rapport a sa taille est la langue.", "Les fourmis ne dorment jamais vraiment.",
            "Coca-Cola etait a l'origine vert.", "Le miel est le seul aliment qui ne pourrit jamais.",
            "Les pieuvres ont trois coeurs.", "Il est impossible de se lecher le coude.",
            "Les elephants sont les seuls animaux qui ne peuvent pas sauter.", "Le cri d'un canard ne fait pas d'echo.",
            "Les etoiles de mer n'ont pas de cerveau.", "Les cafards peuvent vivre plusieurs semaines sans tete.",
            "La France est le pays le plus visite au monde.", "Le Japon a un festival pour tout, meme pour les nombrils.",
            "Les chats ont 32 muscles dans chaque oreille.", "Un hippopotame peut courir plus vite qu'un homme.",
            "Le coeur d'une crevette se trouve dans sa tete.", "Les empreintes digitales des koalas sont proches des humains.",
            "Il y a plus de vaches que d'humains en Nouvelle-Zelande.", "Le record du vol de poule le plus long est de 13 secondes.",
            "Les autruches ont des yeux plus gros que leur cerveau.", "Les rats rigolent quand on leur fait des chatouilles.",
            "Un escargot peut dormir pendant trois ans.", "Le drapeau des USA a ete dessine par un lyceen pour un projet.",
            "La Russie a une surface plus grande que la planete Pluton.", "Les scorpions brillent sous la lumiere ultra-violette.",
            "Les manchots peuvent sauter a 2 metres de haut.", "Le nom complet de Barbie est Barbara Millicent Roberts.",
            "Les girafes n'ont pas de cordes vocales.", "Le ketchup etait vendu comme medicament en 1830.",
            "La peur des longs mots s'appelle l'hippopotomonstrosesquippedaliophobie.", "Les abeilles peuvent reconnaitre les visages humains.",
            "L'Islande n'a aucun moustique.", "Les moutons peuvent reconnaitre d'autres moutons sur des photos.",
            "Le premier nom de Google etait Backrub.", "Un humain produit assez de salive pour remplir deux piscines.",
            "Les requins existent depuis plus longtemps que les arbres.", "Le Nutella a ete cree a cause d'une penurie de cacao.",
            "Le briquet a ete invente avant l'allumette.", "Les hippocampes sont les seuls poissons qui nagent verticalement.",
            "Le son ne se propage pas dans l'espace.", "Les astronautes grandissent de quelques centimetres dans l'espace.",
            "La Lune s'eloigne de la Terre de 3,8 cm par an.", "Le soleil represente 99% de la masse du systeme solaire.",
            "Venus est la planete la plus chaude, meme si elle n'est pas la plus proche.", "Une journee sur Venus est plus longue qu'une annee sur Venus.",
            "Les diamants sont faits de carbone pur.", "L'or est tellement rare qu'on en trouve plus dans les smartphones que dans les mines.",
            "Le mont Everest grandit de quelques millimetres chaque annee.", "Le Sahara etait une foret tropicale il y a 6000 ans.",
            "L'Amazonie produit 20% de l'oxygene de la planete.", "Il y a plus de bacteries dans votre bouche que d'humains sur Terre.",
            "Votre cerveau utilise autant d'energie qu'une ampoule de 10 watts.", "Les os humains sont plus solides que le beton.",
            "Un quart de vos os se trouvent dans vos pieds.", "Le nez peut se souvenir de 50 000 odeurs differentes.",
            "L'oeil humain peut distinguer 10 millions de couleurs.", "Cleopatre vivait plus proche de l'invention de l'iPhone que des pyramides.",
            "Napoleon n'etait pas petit, il faisait 1m68.", "La guerre la plus courte a dure 38 minutes.",
            "Les pyramides ont ete construites par des ouvriers payes, pas des esclaves.", "Le Titanic avait trois cheminees fonctionnelles, la quatrieme etait decorative.",
            "Le premier ordinateur pesait 30 tonnes.", "Le mot robot vient d'un mot tcheque signifiant corvee.",
            "Le premier message SMS disait Merry Christmas.", "Il y a plus de mobiles que d'humains sur la planete.",
            "Youtube a ete cree a l'origine pour etre un site de rencontre.", "Le premier objet vendu sur eBay etait un pointeur laser casse.",
            "Le code source du premier site web est toujours disponible.", "Les pigeons peuvent faire des maths.",
            "Les loups ne hurlent pas a la Lune, ils communiquent entre eux.", "Le cri du lion peut s'entendre a 8 kilometres.",
            "Les ours polaires ont la peau noire sous leurs poils blancs.", "Le papillon goute avec ses pattes.",
            "Une vache peut monter des escaliers mais pas les descendre."
        ]
        print("NayIA 2.0 : Saviez-vous que... " + random.choice(faits))

        
    elif "blague" in question:
        reponses = [
            "Pourquoi les serveurs n'aiment pas la pluie ? Parce qu'ils ont peur du Cloud !",
            "Un programmateur va au lit. Il met deux verres sur sa table de nuit : un plein au cas où il aurait soif, et un vide au cas où il n'aurait pas soif.",
            "Pourquoi les développeurs détestent la nature ? Parce qu'il y a trop de bugs.",
            "Que dit un informaticien quand il veut prendre l'air ? Il ouvre une fenêtre Windows !",
            "Toc toc ! - Qui est là ? (long silence...) - C'est Java.",
            "Un SQL entre dans un bar, va voir deux tables et demande : 'Je peux me joindre à vous ?'",
            "Comment appelle-t-on un développeur qui n'a plus d'ordinateur ? Un SDF (Sans Data Fixe)."
        ]
        print("NayIA :", random.choice(reponses))
        
    elif "espace" in question or "planète" in question:
        infos = [
            "Le Soleil est tellement gros qu'on pourrait mettre 1,3 million de Terres à l'intérieur !",
            "Sur Vénus, il fait tellement chaud (460°C) que le plomb fondrait comme de l'eau.",
            "Il existe une planète appelée 55 Cancri e qui est composée en grande partie de diamant !",
            "Le record du monde du plus long vol d'un poulet est de 13 secondes... bon ok, c'est pas vraiment l'espace, mais c'est un début !",
            "Savais-tu qu'une année sur Mercure ne dure que 88 jours ?"
        ]
        print("NayAI :", random.choice(infos))
        
    elif "jeu" in question or "gaming" in question or "console" in question:
        reponses_gaming = [
            "Le premier jeu vidéo de l'histoire s'appelait 'Tennis for Two', créé en 1958 !",
            "Savais-tu que Mario s'appelait au début 'Jumpman' ?",
            "Minecraft est le jeu le plus vendu de tous les temps avec plus de 300 millions de copies.",
            "La PlayStation 2 reste la console la plus vendue de l'histoire (155 millions d'unités).",
            "Le savais-tu ? Pac-Man a été inspiré par une pizza à laquelle il manquait une part !",
            "E-sport : Le tournoi 'The International' sur Dota 2 a déjà proposé plus de 40 millions de dollars de récompense !"
        ]
        print("NayAI :", random.choice(reponses_gaming))

    elif question.startswith("/"):
        if "/stats" in question:
            print(f"NayAI : J'ai actuellement {len(memoire)} phrases personnalisées en mémoire !")
            
        elif "/param" in question:
            print("====== PARAMETRES NAYIA 2.1 ======")
            print("NayAI : Paramètres -> Version: 2.1 | Développeur: Nayane Ahamadi @Naycode | Mode: Apprentissage Actif")
            
        elif "/cleanjson" in question:
            confirm = input("NayAI : Es-tu sûr de vouloir effacer MA MÉMOIRE ? (oui/non) : ")
            if confirm.lower() == "oui":
                memoire = {}
                print("NayAI : Ma mémoire a été réinitialisée. Je suis toute neuve !")
            else:
                print("NayAI : Ouf ! J'ai failli tout oublier.")
                
        elif "/exit" in question or "/quit" in question:
            print("NayAI : Fermeture sécurisée... À bientôt !")
            with open("memoire.json", "w") as f:
                json.dump(memoire, f)
            break
            
        elif "/info"  in question:
            guide = """
            --- MANUEL COMPLET DE NAYIA 2.1 ---
            Bienvenue dans le guide officiel de votre intelligence artificielle locale.
            
            1. FONCTIONNEMENT DE LA MEMOIRE :
            NayIA utilise un fichier 'memoire.json'. Si vous lui apprenez quelque chose
            avec la commande /learn, cela est stocke physiquement sur votre appareil.
            
            2. LES MOTS-CLES DE REACTION (MODE NATUREL) :
            - 'capitale' : NayIA choisira une capitale mondiale au hasard.
            - 'departement' : Affiche un departement francais et son numero.
            - 'insolite' ou 'fait' : Decouvrez l'une des 75 anecdotes mondiales.
            - 'cine' : NayIA vous suggere un film avec son resume complet.
            - 'monuments' : Apprenez l'histoire d'un monument celebre du monde.
            
            3. LES COMMANDES SYSTEME (AVEC /) :
            - /cgu : Affiche les conditions generales d'utilisation du logiciel.
            - /version : Affiche la version actuelle (2.1) et le changelog.
            - /stats : Permet de voir combien de choses NayIA a apprises.
            - /cleanjson : ATTENTION ! Cette commande efface toute la memoire.
            - /quiz : Lance le grand jeu interactif de 10 questions.
            - /scan : Lance une analyse fictive de votre systeme Android/iOS.
            
            4. CONSEILS POUR LES MODDEURS :
            NayIA est concue pour etre modifiee. Vous pouvez ajouter des blocs 'elif'
            en respectant scrupuleusement l'indentation de 4 espaces. Ne mettez pas 
            d'accents dans vos chaines de caracteres pour eviter les erreurs ASCII.
            
            5. LIMITES DU SYSTEME :
            NayIA 2.1 est une IA hors-ligne. Elle ne peut pas naviguer sur internet
            ni acceder a votre appareil photo (rassurez-vous !). Elle ne fonctionne
            que par traitement de texte local.
            --------------------------------------------------
            """
            print(guide)

            
        elif "/aide" in question:
            print("=== MENU AIDE NAYIA 2.1 ===")
            print("Console: Commandes disponibles : /stats, /param, /cleanjson, /exit, /quit, /version, /quiz, /scan, /cine")
            print("Sujets : bonjour, python, nayia, blague, espace, gaming, jeu, console, departement, prefecture, france, capitale, pays, monuments")
            
        elif "/scan" in question:
            import platform
            import datetime
            import time
            print("--- ANALYSE SYSTEME NAYIA 2.1 ---")
            print("temps restant 13 seconde")
            time.sleep(13.5)
            print("Date actuelle :", datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
            print("Plateforme detectee :", platform.system())
            print("Machine :", platform.machine())
            print("Statut : Analyse des secteurs de donnees...")
            # On simule un chargement pour le style
            import time
            for i in range(1, 4):
                print(f"Scan en cours : {i*10}%...")
                time.sleep(1.5)
            print("Resultat : Votre systeme est optimal pour NayIA.")
            print("Memoire JSON :", len(memoire), "entrees detectees.")
            print("---------------------------------")
            
        elif "/quiz" in question:
            print("--- BIENVENUE DANS LE NAYIA QUIZ ---")
            score = 0
            
            # Liste des questions (Question, Option A, Option B, Option C, Reponse)
            # Chaque ligne ajoute du poids a ton fichier !
            questions_quiz = [
                ["Quel est le cerveau de l'ordinateur ?", "A. Le Disque Dur", "B. Le Processeur", "C. La Souris", "b"],
                ["En quel langage est code NayIA ?", "A. Python", "B. Java", "C. HTML", "a"],
                ["Combien de coeurs a une pieuvre ?", "A. 1", "B. 5", "C. 3", "c"],
                ["Quel aliment ne pourrit jamais ?", "A. Le Riz", "B. Le Miel", "C. Le Chocolat", "b"],
                ["Quelle est la capitale de la France ?", "A. Lyon", "B. Paris", "C. Marseille", "b"],
                ["Le premier SMS disait quoi ?", "A. Hello", "B. Joyeux Noel", "C. Ca va ?", "b"],
                ["Quel animal dort 3 ans ?", "A. L'escargot", "B. Le Lion", "C. Le Chat", "a"],
                ["Planete la plus chaude ?", "A. Mars", "B. Mercure", "C. Venus", "c"],
                ["L'Everest grandit chaque annee ?", "A. Vrai", "B. Faux", "C. Il retrecit", "a"],
                ["La peau de l'ours polaire est...", "A. Blanche", "B. Noire", "C. Rose", "b"]
            ]

            for q in questions_quiz:
                print("\n" + q[0])
                print(q[1])
                print(q[2])
                print(q[3])
                rep = input("Votre reponse (A/B/C) : ").lower().strip()
                if rep == q[4]:
                    print("BRAVO ! C'est correct.")
                    score += 1
                else:
                    print("DOMMAGE... La reponse etait la", q[4].upper())

            print(f"\n--- FIN DU QUIZ ---")
            print(f"Ton score final : {score}/10")
            if score == 10:
                print("Tu es un genie, comme NayIA !")
            elif score > 5:
                print("Pas mal du tout !")
            else:
                print("Tu peux faire mieux, réessaye !")


            
        elif "/learn" in question:
            mot_cle = input("NayIA : Quel mot ou phrase dois-je apprendre ? ").lower().strip()
            nouvelle_rep = input(f"NayIA : Que dois-je répondre quand tu dis '{mot_cle}' ? ")
            memoire[mot_cle] = nouvelle_rep
            print(f"NayIA : C'est noté ! Ma mémoire contient maintenant '{mot_cle}'.")
            
    elif "departement" in question or "prefecture" in question or "france" in question:
        geo_data = [
            "01 Ain : Bourg-en-Bresse", "02 Aisne : Laon", "03 Allier : Moulins", "04 Alpes-de-Haute-Provence : Digne-les-Bains",
            "05 Hautes-Alpes : Gap", "06 Alpes-Maritimes : Nice", "07 Ardeche : Privas", "08 Ardennes : Charleville-Mezieres",
            "09 Ariege : Foix", "10 Aube : Troyes", "11 Aude : Carcassonne", "12 Aveyron : Rodez",
            "13 Bouches-du-Rhone : Marseille", "14 Calvados : Caen", "15 Cantal : Aurillac", "16 Charente : Angouleme",
            "17 Charente-Maritime : La Rochelle", "18 Cher : Bourges", "19 Correze : Tulle", "2A Corse-du-Sud : Ajaccio",
            "2B Haute-Corse : Bastia", "21 Cote-d'Or : Dijon", "22 Cotes-d'Armor : Saint-Brieuc", "23 Creuse : Gueret",
            "24 Dordogne : Perigueux", "25 Doubs : Besancon", "26 Drome : Valence", "27 Eure : Evreux",
            "28 Eure-et-Loir : Chartres", "29 Finistere : Quimper", "30 Gard : Nimes", "31 Haute-Garonne : Toulouse",
            "32 Gers : Auch", "33 Gironde : Bordeaux", "34 Herault : Montpellier", "35 Ille-et-Vilaine : Rennes",
            "36 Indre : Chateauroux", "37 Indre-et-Loire : Tours", "38 Isere : Grenoble", "39 Jura : Lons-le-Saunier",
            "40 Landes : Mont-de-Marsan", "41 Loir-et-Cher : Blois", "42 Loire : Saint-Etienne", "43 Haute-Loire : Le Puy-en-Velay",
            "44 Loire-Atlantique : Nantes", "45 Loiret : Orleans", "46 Lot : Cahors", "47 Lot-et-Garonne : Agen",
            "48 Lozere : Mende", "49 Maine-et-Loire : Angers", "50 Manche : Saint-Lo", "51 Marne : Chalons-en-Champagne",
            "52 Haute-Marne : Chaumont", "53 Mayenne : Laval", "54 Meurthe-et-Moselle : Nancy", "55 Meuse : Bar-le-Duc",
            "56 Morbihan : Vannes", "57 Moselle : Metz", "58 Nievre : Nevers", "59 Nord : Lille",
            "60 Oise : Beauvais", "61 Orne : Alencon", "62 Pas-de-Calais : Arras", "63 Puy-de-Dome : Clermont-Ferrand",
            "64 Pyrenees-Atlantiques : Pau", "65 Hautes-Pyrenees : Tarbes", "66 Pyrenees-Orientales : Perpignan", "67 Bas-Rhin : Strasbourg",
            "68 Haut-Rhin : Colmar", "69 Rhone : Lyon", "70 Haute-Saone : Vesoul", "71 Saone-et-Loire : Macon",
            "72 Sarthe : Le Mans", "73 Savoie : Chambery", "74 Haute-Savoie : Annecy", "75 Paris : Paris",
            "76 Seine-Maritime : Rouen", "77 Seine-et-Marne : Melun", "78 Yvelines : Versailles", "79 Deux-Sevres : Niort",
            "80 Somme : Amiens", "81 Tarn : Albi", "82 Tarn-et-Garonne : Montauban", "83 Var : Toulon",
            "84 Vaucluse : Avignon", "85 Vendee : La Roche-sur-Yon", "86 Vienne : Poitiers", "87 Haute-Vienne : Limoges",
            "88 Vosges : Epinal", "89 Yonne : Auxerre", "90 Territoire de Belfort : Belfort", "91 Essonne : Evry",
            "92 Hauts-de-Seine : Nanterre", "93 Seine-Saint-Denis : Bobigny", "94 Val-de-Marne : Creteil", "95 Val-d'Oise : Pontoise",
            "971 Guadeloupe : Basse-Terre", "972 Martinique : Fort-de-France", "973 Guyane : Cayenne", "974 La Reunion : Saint-Denis",
            "976 Mayotte : Mamoudzou"
        ]
        print("NayIA :", random.choice(geo_data))
        
    elif "monuments" in question:
            monuments = [
                "Tour Eiffel (France): Une tour de fer de 330 metres construite pour l'Exposition universelle de 1889.",
                "Grande Muraille (Chine): Une serie de fortifications de plus de 21 000 km construite pour proteger la Chine.",
                "Pyramides de Gizeh (Egypte): Les seules merveilles du monde antique encore debout aujourd'hui.",
                "Statue de la Liberte (USA): Un cadeau de la France pour celebrer le centenaire de l'independance americaine.",
                "Colisee (Italie): Un immense amphitheatre romain ou se deroulaient les combats de gladiateurs.",
                "Taj Mahal (Inde): Un mausolee de marbre blanc construit par l'empereur pour son epouse defunte.",
                "Machu Picchu (Perou): Une ancienne cité inca perchee dans les montagnes des Andes.",
                "Petra (Jordanie): Une cite antique sculptee directement dans la roche rose du desert.",
                "Sagrada Familia (Espagne): Une basilique monumentale dessinee par Gaudi, toujours en construction.",
                "Big Ben (Royaume-Uni): Le nom de la cloche de 13 tonnes situee dans la tour du Parlement a Londres.",
                "Acropole d'Athenes (Grece): Un ensemble de temples antiques dominant la ville d'Athenes.",
                "Chateau de Versailles (France): La residence somptueuse des rois de France, celebre pour sa Galerie des Glaces.",
                "Mont Saint-Michel (France): Une abbaye construite sur un ilot rocheux entoure de grandes marees.",
                "Empire State Building (USA): Un gratte-ciel art deco qui fut le plus haut du monde pendant 40 ans.",
                "Opera de Sydney (Australie): Un batiment aux toits en forme de voiles, symbole de l'Australie.",
                "Christ Redempteur (Bresil): Une statue geante de 30 metres surplombant la ville de Rio de Janeiro.",
                "Angkor Wat (Cambodge): Le plus grand temple religieux du monde, construit au 12eme siecle.",
                "Alhambra (Espagne): Un palais forteresse magnifique temoignant de l'architecture maure.",
                "Basilique Saint-Pierre (Vatican): La plus grande eglise catholique du monde, situee au coeur de Rome.",
                "Chateau de Neuschwanstein (Allemagne): Le chateau qui a inspire celui de la Belle au Bois Dormant de Disney.",
                "Golden Gate Bridge (USA): Le celebre pont suspendu orange qui relie San Francisco a l'ocean.",
                "Burj Khalifa (Emirats): La plus haute structure humaine du monde avec ses 828 metres de haut.",
                "Louvre (France): Le plus grand musee d'art du monde, installe dans un ancien palais royal.",
                "Kremlin (Russie): Une forteresse historique a Moscou abritant le gouvernement russe.",
                "Tours Petronas (Malaisie): Deux gratte-ciel jumeaux de 452 metres relies par un pont suspendu.",
                "Stonehenge (Royaume-Uni): Un monument megalithique mysterieux datant de la prehistoire.",
                "Chichen Itza (Mexique): Une pyramide maya celebre pour ses phenomenes astronomiques.",
                "Moais de l'Ile de Paques (Chili): Des statues de pierre geantes sculptees par le peuple Rapa Nui.",
                "Cathédrale Notre-Dame (France): Un chef-d'oeuvre gothique situe sur l'Ile de la Cite a Paris.",
                "Mont Rushmore (USA): Les visages de quatre presidents americains sculptes dans la montagne.",
                "Pont du Gard (France): Un ancien aqueduc romain sur trois niveaux tres bien conserve.",
                "Palais de Buckingham (Royaume-Uni): La residence officielle de la monarchie britannique a Londres.",
                "Table Mountain (Afrique du Sud): Une montagne a sommet plat offrant une vue incroyable sur Le Cap.",
                "Pantheon (Italie): Un ancien temple romain possedant la plus grande coupole en beton non arme.",
                "Tower Bridge (Royaume-Uni): Un pont basculant celebre qui s'ouvre pour laisser passer les bateaux.",
                "Forbidden City (Chine): L'ancien palais imperial des dynasties Ming et Qing a Pekin.",
                "Hagia Sophia (Turquie): Un monument historique ayant ete une eglise puis une mosquee.",
                "Grand Canyon (USA): Une gorge immense sculptee par le fleuve Colorado depuis des millions d'annee.",
                "Baie d'Halong (Vietnam): Un paysage marin compose de milliers de rochers calcaires.",
                "Uluru (Australie): Un immense rocher de gres rouge sacre pour les Aborigenes.",
                "Chateau d'Osaka (Japon): Un symbole historique de la puissance et de l'unification du Japon.",
                "Basilique Saint-Basile (Russie): Une eglise aux domes multicolores situee sur la Place Rouge.",
                "Pompei (Italie): Une ville antique figee dans le temps par l'eruption du volcan Vesuve.",
                "Cathédrale de Cologne (Allemagne): Une église gothique monumentale aux deux tours de 157 metres.",
                "Meteores (Grece): Des monasteres construits au sommet de pitons rocheux inaccessibles.",
                "Mezquita de Cordoue (Espagne): Une ancienne mosquee devenue cathedrale, unique au monde.",
                "Sainte-Chapelle (France): Celebre pour ses vitraux exceptionnels racontant la Bible.",
                "Carcassonne (France): Une cite medievale fortifiee parfaitement preservee avec ses remparts.",
                "Mont Fuji (Japon): Un volcan sacre au sommet enneige, symbole national du Japon.",
                "Grand Bazar (Turquie): L'un des plus grands et des plus anciens marches couverts au monde."
            ]
            import random
            print("NayIA 2.1 - Decouverte du monde :")
            print(random.choice(monuments))

        
    elif "capitale" in question or "pays" in question:
        capitales = [
            # EUROPE
            "Allemagne : Berlin", "Autriche : Vienne", "Belgique : Bruxelles", "Espagne : Madrid", 
            "France : Paris", "Italie : Rome", "Grece : Athenes", "Portugal : Lisbonne", 
            "Royaume-Uni : Londres", "Suisse : Berne", "Pays-Bas : Amsterdam", "Suede : Stockholm",
            # AFRIQUE
            "Algerie : Alger", "Maroc : Rabat", "Tunisie : Tunis", "Senegal : Dakar", 
            "Cote d'Ivoire : Yamoussoukro", "Cameroun : Yaounde", "Egypte : Le Caire", "Mali : Bamako",
            # AMERIQUE
            "USA : Washington", "Canada : Ottawa", "Mexique : Mexico", "Bresil : Brasilia", 
            "Argentine : Buenos Aires", "Chili : Santiago", "Colombie : Bogota", "Cuba : La Havane",
            # ASIE & OCEANIE
            "Japon : Tokyo", "Chine : Pekin", "Inde : New Delhi", "Coree du Sud : Seoul", 
            "Australie : Canberra", "Nouvelle-Zelande : Wellington", "Thailande : Bangkok", "Russie : Moscou"
            ]
    
        print("NayIA :", random.choice(capitales))
       
        
    elif "/version" in question:
        print("NayIA Version 2.1.0")

    # 4. SI ELLE NE CONNAÎT PAS : Elle apprend (Priorité 3)
    else:
        print("NayIA : Je ne connais pas ça. Apprends-moi !")
        nouvelle_reponse = input("Quelle réponse je dois donner ? ")
        memoire[question] = nouvelle_reponse
        print("NayIA : Merci ! Je vais m'en souvenir.")
        
    
        
        # --- CONTRAT DE LICENCE UTILISATEUR FINAL - NAYIA 2.0 ---
# CE DOCUMENT EST UN CONTRAT LEGAL ENTRE L'UTILISATEUR ET LE DEVELOPPEUR.
# EN UTILISANT NAYIA 2.1, VOUS ACCEPTEZ LES TERMES SUIVANTS :

licence_texte = """
1. DEFINITIONS DU SYSTEME
Le logiciel NayIA 2.1 est une intelligence artificielle de traitement de donnees locale.
Elle fonctionne via un fichier de script Python et une base de donnees JSON.
L'utilisateur est defini comme toute personne ayant telecharge le script.

2. PROPRIETE INTELLECTUELLE
Le code source de NayIA 2.1 est la propriete exclusive du developpeur original.
Toute reproduction non autorisee est strictement surveillee par la communaute.
Le nom NayIA est une marque deposee pour ce projet de 10 jours.

3. UTILISATION DES DONNEES ET VIE PRIVEE
NayIA 2.1 stocke les informations dans un fichier nomme memoire.json.
Ce fichier est stocke LOCALEMENT sur votre ordinateur. 
Aucune donnee n'est envoyee sur un serveur externe ou dans le cloud.
Vous etes responsable de la securite de votre fichier memoire.json.
Si vous supprimez ce fichier, NayIA perdra toute sa memoire apprise.

4. LIMITES DE RESPONSABILITE
Le developpeur ne peut etre tenu responsable des reponses generees par l'IA.
Le mode apprentissage (/learn) permet a l'utilisateur de modifier le comportement de l'IA.
L'utilisateur s'engage a ne pas apprendre de contenus illegaux a l'IA.
NayIA 2.0 est fournie EN L'ETAT, sans garantie de perfection totale.

5. MODE APPRENTISSAGE ET EVOLUTION
L'intelligence de NayIA 2.1 evolue selon les interactions de l'utilisateur.
Le developpeur se reserve le droit de mettre a jour le moteur de base.
La version actuelle 2.0 est consideree comme STABLE.

6. MAINTENANCE ET SUPPRESSION
La commande /cleanjson permet de supprimer definitivement la base de donnees.
Cette action est IRREVERSIBLE et efface tous les apprentissages precedents.
La sauvegarde s'effectue automatiquement lors de la commande /exit ou /quit.

7. CLAUSE DE NON-RECOURS
En cas de bug ou de crash du script, veuillez contacter le support via le canal officiel.
Le projet etant un defi de 10 jours, les mises a jour sont frequentes.

8. ACCEPTATION DES CONDITIONS
L'utilisation de NayIA 2.1 implique l'acceptation sans reserve de ce document.
Si vous n'etes pas d'accord, veuillez fermer la console et supprimer le fichier .py.

9. HISTORIQUE DES VERSIONS
- Version 1.0 : Prototype initial (base dictionnaires).
- Version 1.1 : Amelioration du moteur de recherche et apprentissage actif.
- Version 2.0 : Ajout des commandes systeme, Geo-France, Gaming, Espace et ASCII Art.
-Version actuelle (2.1) : ajout de compatiblite au mod .Naymod
---------------------------------------------------------------------------------------
"""

# Tu peux choisir d'afficher la licence avec /param ou juste la laisser en commentaire.


# --- CONDITIONS GENERALES D'UTILISATION (CGU) ---
cgu_texte = """
ARTICLE 1 : OBJET DES CGU
Les presentes Conditions Generales d'Utilisation ont pour objet de definir les modalites 
de mise a disposition du logiciel NayIA 2.0 et les conditions d'utilisation du systeme 
par l'utilisateur final. Tout acces au programme implique l'acceptation des CGU.

ARTICLE 2 : ACCES AU SYSTEME
NayIA 210 est accessible gratuitement a tout utilisateur disposant d'un interpreteur 
Python 3. Le developpeur s'efforce de maintenir le script fonctionnel mais ne peut 
garantir une absence totale de bugs techniques.

ARTICLE 3 : COLLECTE DES DONNEES
Le logiciel NayIA 2.1 ne collecte aucune donnee personnelle a l'insu de l'utilisateur.
Les seules donnees enregistrees sont les paires de questions/reponses stockees dans 
le fichier local memoire.json. Ce fichier appartient a l'utilisateur et reste sur 
sa machine physique. Aucune transmission reseau n'est effectuee.

ARTICLE 4 : RESPONSABILITE DE L'UTILISATEUR
L'utilisateur est responsable des contenus qu'il choisit d'apprendre a l'IA via 
la commande /learn. Il est interdit d'utiliser NayIA 2.1 pour generer ou stocker 
des contenus haineux, illegaux ou dangereux. Le developpeur decline toute 
responsabilite en cas de mauvaise utilisation du mode apprentissage.

ARTICLE 5 : PROPRIETE ET MODIFICATION
Le code source est libre de modification pour un usage prive. Toute redistribution 
commerciale sans mention du developpeur original est interdite. L'utilisateur 
est encourage a contribuer a l'augmentation de la base de donnees (ko).

ARTICLE 6 : EVOLUTION DU CONTRAT
Le developpeur se reserve le droit de modifier les termes de ce contrat a tout 
moment pour les futures versions (ex: version 3.0). L'utilisation continue du 
logiciel apres modification vaut acceptation des nouveaux termes.

ARTICLE 7 : SUPPRESSION DE COMPTE (LOBOTOMIE)
L'utilisateur peut a tout moment reinitialiser l'IA via la commande /cleanjson. 
Cela entraine la suppression immediate et definitive de toutes les donnees 
apprises par le systeme depuis sa premiere installation.
---------------------------------------------------------------------------------------
"""

print("hello world")
