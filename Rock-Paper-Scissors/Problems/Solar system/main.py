file = open("planets.txt", 'w', encoding='utf-8')
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for i in planets:
    if i == "Neptune":
        file.write((i))
    else:
        file.write(i + "\n")
file.close()