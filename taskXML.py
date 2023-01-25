import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

print('Printing child tags of the movie element.')
for movie_elem in root.iter('genre'):
    print(movie_elem.tag)

print('\nPrinting out the movie descriptions.')
for movie_desc in root.iter('description'):
    print(''.join(movie_desc.itertext()))

print('\nPrinting the number of movies that are favourites and the number of movies that are not.')
for movie_fav in root.iter('movie'):
    print(movie_fav.attrib)
    
    
if __name__ == '__main__':
    
    # Create a new list called albums1, add 5 albums to it and print it out.
    albums1 = []

    # Appending instances to albums1
    albums1.append(Album("3HC", "The Prophets", 15))
    albums1.append(Album("Africa Rising", "Black Coffee", 21))
    albums1.append(Album("Noble Vine", "Princess of Israel", 12))
    albums1.append(Album("12 Gates", "Kingdom Melody", 7))
    albums1.append(Album("24 Elders", "Counsellors", 24))

    # Accesing object value using a for loop
    for obj in albums1:
        print(obj.__str__())
        
    def getKey(obj):
        return obj.numberOfSongs
    
    albums1.sort(key= getKey)
    print("Sort by Name")
    print(albums1)