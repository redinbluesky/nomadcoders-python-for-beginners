def make_juice(fruit):
  return f"{fruit}+🥫"

def add_ice(juice):
  return f"{juice}+🥚"

def add_sugar(ice_juice):
  return f"{ice_juice}+🧂"

juice = make_juice("🍭")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)
