locations = {'North America': {'USA': ['Mountain View', 'Atlanta']},
             'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']},
             'Africa': {'Egypt': ['Cairo']},
             }

print(1)
print(locations['North America']['USA'][1])
print(locations['North America']['USA'][0])
print(2)
print(locations['Asia']['India'][0] + ' - ' + str(list(locations['Asia'].keys())[0]))
print(locations['Asia']['China'][0] + ' - ' + str(list(locations['Asia'].keys())[1]))
