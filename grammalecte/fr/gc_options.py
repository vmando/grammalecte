# -*- encoding: UTF-8 -*-

def getUI (sLang):
    if sLang in _dOptLabel:
        return _dOptLabel[sLang]
    return _dOptLabel["fr"]

lStructOpt = [('basic', [['typo', 'apos'], ['esp', 'nbsp'], ['tu', 'maj'], ['num', 'virg'], ['unit', 'nf'], ['liga', 'mapos'], ['chim', 'ocr']]), ('gramm', [['conf', 'sgpl'], ['gn']]), ('verbs', [['infi', 'gv'], ['imp', 'inte']]), ('style', [['bs', 'pleo'], ['redon1', 'redon2'], ['neg']]), ('misc', [['date', 'mc']]), ('debug', [['idrule']])]

dOpt = {'chim': False, 'apos': True, 'gv': True, 'liga': False, 'infi': True, 'date': True, 'imp': True, 'tu': True, 'maj': True, 'redon1': False, 'nbsp': True, 'virg': True, 'gn': True, 'sgpl': True, 'neg': False, 'num': True, 'pleo': True, 'bs': True, 'unit': True, 'redon2': False, 'ocr': False, 'esp': True, 'idrule': False, 'nf': True, 'mapos': False, 'mc': False, 'typo': True, 'inte': True, 'conf': True}

_dOptLabel = {'fr': {'chim': ('Chimie [!]', 'Typographie des composés chimiques (H₂O, CO₂, etc.).'), 'eif': ('Espaces insécables fines [!]', 'Pour placer des espaces insécables fines avant les ponctuations « ? ! ; »'), 'apos': ('Apostrophe typographique', 'Correction des apostrophes droites. Automatisme possible dans le menu Outils > Options d’autocorrection > Options linguistiques > Guillemets simples > Remplacer (à cocher)'), 'gv': ('Conjugaisons', 'Accord des verbes avec leur sujet.'), 'ocr': ('Erreurs de ROC (OCR) [!]', 'Erreurs de reconnaissance optique des caractères.'), 'liga': ('Signaler ligatures typographiques', 'Ligatures de fi, fl, ff, ffi, ffl, ft, st.'), 'infi': ('Infinitif', 'Confusion entre l’infinitif et d’autres formes.'), 'date': ('Validité des dates', ''), 'imp': ('Impératif', 'Vérifie notamment la deuxième personne du singulier (par exemple, les erreurs : « vas … », « prend … », « manges … »).'), 'tu': ('Traits d’union', 'Cherche les traits d’union manquants ou inutiles.'), 'bs': ('Populaire', 'Souligne un langage courant considéré comme erroné, comme « malgré que ».'), 'maj': ('Majuscules', 'Vérifie l’utilisation des majuscules et des minuscules (par exemple, « la raison d’État », « les Européens »).'), 'redon1': ('Répétitions dans le paragraphe [!]', 'Sont exclus les mots grammaticaux, ceux commençant par une majuscule, ainsi que “être” et “avoir”.'), 'nbsp': ('Espaces insécables', 'Vérifie les espaces insécables avec les ponctuations « ! ? : ; » (à désactiver si vous utilisez une police Graphite)'), 'gramm': ('Accords, pluriels et confusions', ''), 'gn': ('Accords de genre et de nombre', 'Accords des noms et des adjectifs.'), 'sgpl': ('Pluriels (locutions)', 'Vérifie l’usage du pluriel ou du singulier dans certaines locutions.'), 'neg': ('Adverbe de négation [!]', 'Ne … pas, ne … jamais, etc.'), 'num': ('Nombres', 'Espaces insécables sur les grands nombres (> 10 000). Vérifie la présence de « O » au lieu de « 0 ».'), 'pleo': ('Pléonasmes', 'Repère des redondances sémantiques, comme « au jour d’aujourd’hui », « monter en haut », etc.'), 'debug': ('Débogage', ''), 'virg': ('Virgules', 'Virgules manquantes avant “mais”, “car” et “etc.”.'), 'style': ('Style', ''), 'unit': ('Espaces insécables avant unités de mesure', ''), 'verbs': ('Verbes', ''), 'basic': ('Typographie', ''), 'esp': ('Espaces surnuméraires', 'Signale les espaces inutiles en début et en fin de ligne.'), 'idrule': ('Identifiant des règles de contrôle [!]', 'Affiche l’identifiant de la règle de contrôle dans les messages d’erreur.'), 'nf': ('Normes françaises', ''), 'mapos': ('Apostrophes manquantes après lettres isolées [!]', 'Apostrophes manquantes après les lettres l d s n c j m t ç. Cette option sert surtout à repérer les défauts de numérisation des textes et est déconseillée pour les textes scientifiques.'), 'redon2': ('Répétitions dans la phrase [!]', 'Sont exclus les mots grammaticaux, ainsi que “être” et “avoir”.'), 'mc': ('Mots composés [!]', 'Vérifie si les mots composés à trait d’union existent dans le dictionnaire (hormis ceux commençant par ex-, mi-, quasi-, semi-, non-, demi- et d’autres préfixes communs).'), 'typo': ('Signes typographiques', ''), 'inte': ('Interrogatif', 'Vérifie les formes interrogatives et suggère de lier les pronoms personnels avec les verbes.'), 'conf': ('Confusions, homonymes et faux-amis', 'Cherche des erreurs souvent dues à l’homonymie (par exemple, les confusions entre « faîte » et « faite »).'), 'misc': ('Divers', '')}, 'en': {'chim': ('Chemistry [!]', 'Typography for molecules (H₂O, CO₂, etc.)'), 'eif': ('Narrow non breaking spaces [!]', 'To set narrow non breaking spaces before the characters “? ! ;”'), 'apos': ('Typographical apostrophe', 'Detects typewriter apostrophes. You may get automatically typographical apostrophes in Tools > Autocorrect options > Localized options > Single quote > Replace (checkbox).'), 'gv': ('Conjugation', 'Agreement between verbs and their subject.'), 'ocr': ('OCR errors [!]', ''), 'liga': ('Report typographical ligatures', 'Ligatures of fi, fl, ff, ffi, ffl, ft, st.'), 'infi': ('Infinitive', 'Checks confusions between infinitive forms and other forms.'), 'date': ('Date validity', ''), 'imp': ('Imperative mood', 'Checks particularly verbs at second person singular (i.e. errors such as: « vas … », « prend … », « manges … »).'), 'tu': ('Hyphens', 'Checks missing or useless hyphens.'), 'bs': ('Popular style', 'Underlines misuse of language though informal and commonly used.'), 'maj': ('Capitals', 'Checks the use of uppercase and lowercase letters (i.e. « la raison d’État », « les Européens »).'), 'redon1': ('Duplicates in paragraph [!]', 'Are excluded grammatical words, words beginning by a capital letter, and also “être” and “avoir”.'), 'nbsp': ('Non-breakable spaces', 'Checks the use of non-breakable spaces with the following punctuation marks: « ! ? : ; » (deactivate it if you use a Graphite font)'), 'gramm': ('Agreement, plurals, confusions', ''), 'gn': ('Agreement (gender and number)', 'Agreement between nouns and adjectives.'), 'sgpl': ('Plural (locutions)', 'Checks the use of plural and singular in locutions.'), 'neg': ('Negation adverb [!]', 'Ne … pas, ne … jamais, etc.'), 'num': ('Numbers', 'Large numbers and « O » instead of « 0 ».'), 'pleo': ('Pleonasms', 'Semantic replications, like « au jour d’aujourd’hui », « monter en haut », etc.'), 'debug': ('Debug', ''), 'virg': ('Commas', 'Missing commas before “mais”, “car” and “etc.”.'), 'style': ('Style', ''), 'unit': ('Non-breaking spaces before units of measurement', ''), 'verbs': ('Verbs', ''), 'basic': ('Typography', ''), 'esp': ('Unuseful spaces', 'Checks spaces at the beginning and the end of lines.'), 'idrule': ('Display control rule identifier [!]', 'Display control rule identifier in the context menu message'), 'nf': ('French standards', ''), 'mapos': ('Missing apostrophes after single letters [!]', 'Missing apostrophes after l d s n c j m t ç. This option is mostly useful to detect defects of digitized texts and is not recommended for scientific texts.'), 'redon2': ('Duplicates in sentence [!]', 'Are excluded grammatical words, and also “être” and “avoir”.'), 'mc': ('Compound words [!]', 'Check if words with hyphen exist in the dictionary (except those beginning by ex-, mi-, quasi-, semi-, non-, demi- and other common prefixes)'), 'typo': ('Typographical glyphs', ''), 'inte': ('Interrogative mood', 'Checks interrogative forms and suggests linking the personal pronouns with verbs.'), 'conf': ('Confusions, homonyms and false friends', 'Seeks errors often due to homonymy (i.e. confusions between « faîte » et « faite »).'), 'misc': ('Miscellaneous', '')}}
