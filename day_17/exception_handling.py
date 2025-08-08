# Exercice day_17
# Unpacking using ennumarate
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

nordic_countries = []
for index, country in enumerate(names):
    if index  < 5 :
        nordic_countries.append(country)
    elif index == 5 :
        es = country
    elif index == 6:
        ru = country

print (nordic_countries, es, ru)

# Unpacking using star
*nordic_countries, es, ru = names
print (nordic_countries, es, ru)
