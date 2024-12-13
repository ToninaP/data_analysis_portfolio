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
