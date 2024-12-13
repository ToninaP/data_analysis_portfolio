def load_acquisition_tags():
    acqusition_tags = [
        ["gift", "given", "memory", "donors", "git", "gif"],  # gift
        ["fund", "foundation"],  # assisted purchase
        ["bequest", "memory"],  # bequest
        ["museum accession", "purchase", "purchase", "exchange"],
        ["jointly"],  # co-owned
        ["loan", "collection"],
    ]
    acquisition_methods = [
        "gift",
        "assisted purchase",
        "bequest",
        "museum accession",
        "jointly owned",
        "loan",
    ]

    return acqusition_tags, acquisition_methods
