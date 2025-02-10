def load_medium_tags():
    medium_tags = [
        [
            "paper",
            "watercolor",
            "card",
            "watercolour",
            "board",
            "chalk",
            "mixed",
            "print",
            "parchment",
            "graphic",
            "engraving",
            "etching",
            "dessin",
            "drawing",
            "manuscripts",
            "calligraphy",
            "ink",
            "poster",
            "miniature",
            "scenography",
            "estampe",
            "design",
            "periodical",
            "grafik",
            "tegning",
            "træsnit",
            "skabelontryk",
            "zinkografi",
            "fotogravure-heliogravure",
            "gouache",
            "linoleumssnit",
            "serigrafi",
            "akvarel",
            "monotypi",
            "litografi",
            "clairobscurtræsnit",
            "crayonstik",
            "dybtryk",
        ],  # graphics
        [
            "oil",
            "canvas",
            "paint",
            "fresco",
            "painting",
            "peinture",
            "maleri",
        ],  # painting
        [
            "bronze",
            "granite",
            "marble",
            "alabaster",
            "clay",
            "iron",
            "cement",
            "concrete",
            "plaster",
            "sculpture",
        ],  # sculpture
        [
            "film",
            "video",
            "cinéma",
            "moving image",
            "animation",
        ],  # video art
        [
            "fabric",
            "glass",
            "wood",
            "aluminium",
            "steel",
            "plastic",
            "book",
            "copper",
            "stone",
            "slate",
            "wool",
            "willow",
            "cedar",
            "wax",
            "walnut",
            "tin",
            "plate",
            "textile",
            "terracota",
            "mahogany",
            "pine",
            "oak",
            "iron",
            "suede",
            "brass",
            "sheet",
            "cast",
            "acacia",
            "metal",
            "beech",
            "celluloid",
            "cellulose",
            "ceramic",
            "rubber",
            "elm",
            "earthenware",
            "epoxy",
            "felt",
            "firebricks",
            "flint",
            "banknote",
            "ivory",
            "lead",
            "leather",
            "terracota",
            "perspex",
            "resin",
            "quartz",
            "porcelain",
            "object",
            "medal",
            "silk",
            "cotton",
            "cashmere",
            "tablets",
            "amber",
            "archery",
            "model",
            "armor",
            "bamboo",
            "banner",
            "bark",
            "basketry",
            "beads",
            "bindings",
            "blocks",
            "bone",
            "equipment",
            "sword",
            "daggers",
            "kriss",
            "weapon",
            "helmet",
            "pistol",
            "shield",
            "knives",
            "accessories",
            "gun",
            "mail",
            "surcoat",
            "costume",
            "firearms",
            "chess",
            "horn",
            "cylinder",
            "tools",
            "jade",
            "fans",
            "rubbing",
            "laquer",
            "furniture",
            "jewelry",
            "sharkskin",
            "shell",
            "seal",
            "masks",
            "manuscript",
            "tablet",
            "bamboo",
            "screen",
            "enamel",
            "bottle",
            "cricket",
            "pottery",
            "horn",
            "stencil",
            "amber",
            "instrument",
            "feather",
            "pouch",
            "fan",
            "clock",
            "coin",
            "wear",
            "dress",
            "rock",
            "papier",
            "gem",
            "gold",
            "silver",
            "vase",
            "terracotta",
            "album",
            "negative",
            "collage",
            "assemblage",
            "letter",
            "binding",
            "hide",
            "faience",
            "elephant",
            "crystal",
            "papyrus",
            "lute",
            "organ",
            "clavichord",
            "aerophone",
            "chordophone",
            "idiophone",
            "membranophone",
            "toy",
            "electrophone",
            "lamp",
            "box",
            "holly",
            "rope",
            "sand",
            "pewter",
            "mud",
            "nylon",
            "objet",
            "livre",
            "multiple",
            "furniture",
            "decorative",
            "assemblage",
            "collage",
            "craft",
            "artefact",
        ],  # object
        [
            "boat",
            "structure",
            "burlap",
            "bean",
            "hook",
            "knive",
            "hat",
            "light",
            "wall",
            "machine",
            "vinyl",
            "cleaner",
            "door",
            "mirror",
            "form",
            "metronome",
            "sock",
            "carpet",
            "latex",
            "installation",
            "variable",
            "compressor",
            "wire",
            "neon",
            "glitter",
            "oeuvre",
            "mixte",
            "multiple",
        ],  # installation
        ["photo", "fotografi"],  # photography
        [
            "software",
            "audio",
            "slide",
            "digital",
            "net",
            "sound",
            "nouveaux",
            "musique",
            "time-based",
            "media",
            "electronic",
        ],  # new media
        ["architecture"],  # architecture
        ["document", "archive"],  # document
    ]
    medium_name = [
        "graphics",
        "painting",
        "sculpture",
        "video art",
        "object",
        "installation",
        "photography",
        "new media",
        "architecture",
        "documents",
    ]
    return medium_tags, medium_name
def load_nationality_tags():

    nationality_tags = [
        [
            "american",
            "américaine",
            "usa",
            "united states",
            "amerikansk",
            "united",
            "hawaii",
            "u.s.a.",
            "us",
        ],  # United States
        ["allemande", "germany", "german", "tysk"],  # Germany
        ["canadian", "canadienne", "canada", "canadisk"],  # Canada
        ["japanese", "japonaise", "japan", "japansk"],  # Japan
        ["mexican", "mexicaine", "mexico"],  # Mexico
        ["indian", "india", "indisk"],  # India
        ["française", "france", "french", "fransk", "paris", "martinique"],  # France
        ["russe", "russia", "soviétique", "russian", "russisk"],  # Russia
        ["suisse", "switzerland", "swiss", "schweizisk"],  # Switzerland
        [
            "britannique",
            "united kingdom",
            "england",
            "scotland",
            "english",
            "engelsk",
            "wales",
            "british",
            "scottish",
            "welsh",
            "skotsk",
            "britisk",
            "uk",
        ],  # United Kingdom
        ["hongroise", "hungary", "hungarian", "ungarsk"],  # Hungary
        ["argentine", "argentina", "argentinian"],  # Argentina
        ["polonaise", "poland", "polish", "polsk"],  # Poland
        ["suédoise", "sweden", "swedish", "svensk"],  # Sweden
        ["italienne", "italy", "italian", "italiensk", "sicily"],  # Italy
        [
            "espagnole",
            "spain",
            "spanish",
            "león",
            "barcelona",
            "madrid",
            "gran canaria",
            "pontevedra",
            "españa",
            "seville",
            "valencia/valència",
            "catalan",
            "spansk",
        ],  # Spain
        ["brésilienne", "brazil", "brazilian", "brasiliansk"],  # Brazil
        ["égyptienne", "egypt", "coptic"],  # Egypt
        ["vénézuélienne", "venezuela"],  # Venezuela
        ["israélienne", "israel"],  # Israel
        ["cubaine", "cuba", "cuban", "matanzas"],  # Cuba
        ["iranienne", "iran", "iranian", "persian", "persia"],  # Iran
        ["algérienne", "algeria", "algerian"],  # Algeria
        ["ukrainienne", "ukraine", "ukrainian"],  # Ukraine
        ["roumaine", "romania", "romanian", "rumænsk"],  # Romania
        ["belge", "belgium", "belgian", "belgisk", "flamsk"],  # Belgium
        [
            "néerlandaise",
            "netherlands",
            "holland",
            "nederlandsk",
            "hollandsk",
            "dutch",
        ],  # Netherlands
        ["autrichienne", "austria", "austrian", "østrigsk", "østrig"],  # Austria
        ["irlandaise", "ireland", "irish", "irsk"],  # Ireland
        [
            "portugaise",
            "portugal",
            "portugese",
            "portuguese",
            "portugisisk",
        ],  # Portugal
        ["jordanienne", "jordan"],  # Jordan
        [
            "australienne",
            "australia",
            "australian",
            "queensland",
            "victoria",
            "northern",
        ],  # Australia
        ["croate", "croatia", "croatian", "kroatisk"],  # Croatia
        [
            "tchèque",
            "czechia",
            "czech republic",
            "tchécoslovaque",
            "czech",
            "tjekkisk",
            "bohemia",
        ],  # Czech Republic
        ["albanaise", "albania"],  # Albania
        ["sud-africaine", "south africa", "sydafrikansk", "south"],  # South Africa
        ["irakienne", "iraq"],  # Iraq
        ["libanaise", "lebanon", "lebanese"],  # Lebanon
        ["estonienne", "estonia"],  # Estonia
        ["kosovare", "kosovo", "kosova"],  # Kosovo
        ["marocaine", "morocco", "moroccan"],  # Morocco
        [
            "ivoirienne",
            "ivory coast",
            "ivorian",
            "côte",
            "cote",
            "ivory",
        ],  # Ivory Coast
        ["arménienne", "armenia"],  # Armenia
        ["chinoise", "china", "chinese", "kinesisk", "tibet"],  # China
        ["vietnamienne", "vietnam", "viet"],  # Vietnam
        ["guatemala"],  # Guatemala
        ["bermuda"],  # bermuda
        ["new zealand", "new"],  # new zealand
        ["turkey", "turkish", "tyrkisk", "nicomedia"],  # turkey
        ["kirghiztan", "kyrgyz", "kyrgyzstan"],  # Kyrgyzstan
        ["uruguay"],  # uruguay
        ["nigeria", "nigeriansk", "niger"],  # nigeria
        ["paraguay"],  # paraguay
        ["serbia", "serbisk"],  # serbia
        ["peru"],  # peru
        ["chile"],  # chile
        ["denmark", "danish", "dansk", "færøsk"],  # denmark
        [
            "bosnia-herzegovina",
            "bosnian",
            "bosnia",
            "herzegovina",
        ],  #'bosnia-herzegovina'
        ["norway", "norwegian", "norsk"],  # norway
        ["finnish", "finland", "finsk"],  # finland
        ["croatia"],  # croatia
        ["colombia"],  # colombia
        ["sri lanka", "sri"],  # sri lanka
        ["iceland", "islandsk"],  # iceland,
        ["isle of man"],  # isle of man
        ["costa rica", "costa"],  # costa rica
        ["lithuania", "litauisk", "lithuanian"],  # lithuania
        ["indonesia", "java", "sulawesi", "sumatra"],  # indonesia
        ["philippines", "filipino", "ivatan", "philippine"],  # philippines
        ["dominican republic", "dominican"],  # dominican republic
        ["slovenia", "slovensk"],  # slovenia
        ["luxembourg"],  # luxembourg
        ["puerto rico", "puerto rican", "puerto"],  # puerto rico
        ["panama"],  # panama
        ["latvian", "latvia"],  # latvia
        [
            "greek",
            "greece",
            "græsk",
        ],  # greece
        ["georgian", "georgia"],  # georgia
        ["thai", "thaland"],  # thailand
        ["korean", "korea"],  # korea
        ["ethiopian", "ethiopia"],  # ethiopia
        ["kuwaiti", "kuwait"],  # kuwait
        ["haitian", "haiti"],  # haiti
        ["zimbabwean", "zimbabwe"],  # zimbabwe
        ["ecuadorian", "ecuador"],  # ecuador
        ["congolese", "congo", "democratic"],  # Democratic Republic of the Congo
        ["azerbaijani", "azerbaijan"],  # Azerbaijan
        ["malian", "mali"],  # mali
        ["cambodian", "cambodia"],  # cambodia
        ["slovak", "slovakia"],  # slovakia
        ["pakistani", "pakistan"],  # pakistan
        ["bulgarian", "bulgaria"],  # bulgaria
        ["bolivian", "bolivia"],  # bolivia
        ["palestinian", "palestine"],  # palestine
        ["taiwanese", "taiwan"],  # taiwan
        ["nicaraguan", "nicaragua"],  # nicaragua
        ["tunisian", "tunisia", "tunesia"],  # tunisian
        ["sudanese", "sudan", "nubia"],  # sudan
        ["tanzanian", "tanzania", "zanzibar"],  # tanzania
        ["senegalese", "senegal"],  # senegal
        ["bahamian", "bahamas"],  # the bahamas
        ["kenyan", "kenya"],  # kenya
        ["malaysian", "malaysia", "borneo"],  # malaysia
        ["singaporean", "singapore"],  # singapore
        ["namibian", "namibia"],  # namibia
        ["ghanaian", "ghana"],  # ghana
        ["afghan", "afghanistan"],  # afghanistan
        ["ugandan", "uganda"],  # uganda
        ["cameroonian", "cameroon"],  # cameroon
        ["macedonian", "macedonia"],  # North Macedonia
        ["syrian", "syria"],
        ["bangladeshi", "bangladesh"],
        ["burkinabé", "burkina"],  # Burkina Faso
        ["beninese", "benin"],  # benin
        ["sierra leonean", "sierra"],  # Sierra Leone
        ["emirati", "uae"],  # United Arab Emirates
        ["salvadoran", "salvador"],  # El Salvador
        ["mozambican"],  # Mozambique
        ["trinidad"],  # Trinidad and Tobago
        ["nepali", "nepal"],  # nepal
        ["grønlandsk"],  # greenland
        ["belarussisk", "belarus"],  # Belarus
        ["uzbekistan"],  # Uzbekistan
        ["myanmar", "Bburma"],  # Myanmar
        ["laos"],  # laos
        ["kazakhstan"],
        ["tahiti", "marquesas"],  # French Polynesia
        ["bhutan"],  # Bhutan
        ["solomon"],  # Solomon Islands
        ["mongolia"],
        ["samoa"],
        ["tonga"],
        ["madagascar"],
        ["liberia"],
        ["saudi"],  #
        ["papua"],
        ["honduras"],
        ["angola"],
        ["togo"],
        ["fiji"],
        ["gabon"],
        ["surinam", "suriname"],
        ["guinea"],
        ["rwanda"],
        ["zambia"],
        ["chad"],
        ["cook"],  # The Cook Islands
        ["yemen"],
        ["montenegro"],
        ["guyana"],
        ["malta"],
        ["lesotho"],
        ["tajikistan"],
        ["mauritania"],
        ["cyprus"],
        ["belize"],
    ]

    country_name = [
        "United States",
        "Germany",
        "Canada",
        "Japan",
        "Mexico",
        "India",
        "France",
        "Russia",
        "Switzerland",
        "United Kingdom",
        "Hungary",
        "Argentina",
        "Poland",
        "Sweden",
        "Italy",
        "Spain",
        "Brazil",
        "Egypt",
        "Venezuela",
        "Israel",
        "Cuba",
        "Iran",
        "Algeria",
        "Ukraine",
        "Romania",
        "Belgium",
        "Netherlands",
        "Austria",
        "Ireland",
        "Portugal",
        "Jordan",
        "Australia",
        "Croatia",
        "Czech Republic",
        "Albania",
        "South Africa",
        "Iraq",
        "Lebanon",
        "Estonia",
        "Kosovo",
        "Morocco",
        "Côte d'Ivoire",
        "Armenia",
        "China",
        "Vietnam",
        "Guatemala",
        "Bermuda",
        "New Zealand",
        "Turkey",
        "Kyrgyzstan",
        "Uruguay",
        "Nigeria",
        "Paraguay",
        "Serbia",
        "Peru",
        "Chile",
        "Denmark",
        "Bosnia-Herzegovina",
        "Norway",
        "Finland",
        "Croatia",
        "Colombia",
        "Sri Lanka",
        "Iceland",
        "Isle of Man",
        "Costa Rica",
        "Lithuania",
        "Indonesia",
        "Philippines",
        "Dominican Republic",
        "Slovenia",
        "Luxembourg",
        "Puerto Rico",
        "Panama",
        "Latvia",
        "Greece",
        "Georgia",
        "Thailand",
        "Korea",
        "Ethiopia",
        "Kuwait",
        "Haiti",
        "Zimbabwe",
        "Ecuador",
        "Democratic Republic of the Congo",
        "Azerbaijan",
        "Mali",
        "Cambodia",
        "Slovakia",
        "Pakistan",
        "Bulgaria",
        "Bolivia",
        "Palestine",
        "Taiwan",
        "Nicaragua",
        "Tunisia",
        "Sudan",
        "Tanzania",
        "Senegal",
        "The Bahamas",
        "Kenya",
        "Malaysia",
        "Singapore",
        "Namibia",
        "Ghana",
        "Afghanistan",
        "Uganda",
        "Cameroon",
        "North Macedonia",
        "Syria",
        "Bangladesh",
        "Burkina Faso",
        "Benin",
        "Sierra Leone",
        "United Arab Emirates",
        "El Salvador",
        "Mozambique",
        "Trinidad and Tobago",
        "Nepal",
        "Greenland",
        "Belarus",
        "Uzbekistan",
        "Myanmar",
        "Laos",
        "Kazakhstan",
        "French Polynesia",
        "Bhutan",
        "Solomon Is.",
        "Mongolia",
        "Samoa",
        "Tonga",
        "Madagascar",
        "Liberia",
        "Saudi Arabia",
        "Papua New Guinea",
        "Honduras",
        "Angola",
        "Togo",
        "Fiji",
        "Gabon",
        "Suriname",
        "Guinea",
        "Rwanda",
        "Zambia",
        "Chad",
        "The Cook Islands",
        "Yemen",
        "Montenegro",
        "Guyana",
        "Malta",
        "Lesotho",
        "Tajikistan",
        "Mauritania",
        "Cyprus",
        "Belize",
    ]

    return nationality_tags, country_name

def load_acquisition_tags():
    acqusition_tags = [
        [
            "gift",
            "given",
            "memory",
            "donors",
            "git",
            "gif",
            "donor",
            "gfit",
            "girf",
            "girt",
            "gilft",
            "presented",
            "donation",
            "don",
            "dation",
            "friends",
            "courtesy",
            "gratitude",
        ],  # gift
        [
            "fund",
            "foundation",
            "trust",
            "generosity",
        ],  # assisted purchase
        [
            "bequest",
            "memory",
            "beqest",
            "beguest",
            "bequeathed",
            "will",
            "inheritance",
            "legs",
            "estate",
            "honor",
            "endowment",
        ],  # bequest
        [
            "museum",
            "purchase",
            "purchase",
            "exchange",
            "administration",
            "achat",
            "puchase",
            "acquired",
        ],  # museum accession
        ["jointly", "attribution"],  # co-owned
        ["loan", "collection", "transfer", "lent", "dépôt"],  # loan
        ["tax", "attribution etat", "saisie"],  # tax
        ["echange", "barter"],  # exchange
        ["artist", "photographer"],  # courtesy of the artist
        ["commissioned"],  # comissioned
    ]
    acquisition_methods = [
        "gift",
        "assisted purchase",
        "bequest",
        "museum accession",
        "jointly owned",
        "loan",
        "tax",
        "exchange",
        "courtesy of the artist",
        "commissioned",
    ]

    return acqusition_tags, acquisition_methods
