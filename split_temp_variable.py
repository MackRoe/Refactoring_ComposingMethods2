# Starter Code by Kami Bigdely
# Split temporary variable
# Refactor by Laine (Music)

patty = 70  # [gr]
pickle = 20  # [gr]
tomatoes = 25  # [gr]
lettuce = 15  # [gr]
buns = 95  # [gr]
kimchi = 30  # [gr]
mayo = 5  # [gr]
golden_fried_onion = 20  # [gr]

ny_burger = {patty: 2, pickle: 4, tomato: 3, lettuce: 1, buns: 2}

seoul_kimchi_burger = {
    patty: 2,
    pickle: 4,
    tomatoes: 3,
    kimchi: 1,
    mayo: 1,
    golden_fried_onion: 1,
    buns: 2}


def build_that_burger(burger_type):
    weight = 0
    for ingredient, amount in burger_type:
        weight += (ingredient * amount)
    return weight


print("NY Burger Weight", build_that_burger(ny_burger))
print("Seoul Kimchi Burger Weight ", build_that_burger(seoul_kimchi_burger))
