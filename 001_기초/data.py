days_of_week = ["Mon","Tue","Wed","Thur","Fri"]
print(days_of_week)
days_of_week.append(["🍔🍕"])
print(days_of_week[-1])

# tuple 생성 후 변경 할 수 없다.
days = ("Mon","Tue","Wed","Thur","Fri")
print(days[-5])

# Dictionary
player = {
    'name': 'nico',
    'age': 12,
    'alive': True,
    'fav_food': ["🍕","🍔"]
}

print(player.get('age'))
print(player.get('fav_food'))
print(player['fav_food'])

player.pop('age')
print(player)

player['xp'] = 1500
print(player)

player['fav_food'].append("🍿")
print(player)


