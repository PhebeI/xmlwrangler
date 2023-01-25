# xmlwrangler

taskXML is a Python file for manipulating a movie xml file.

## HowTo

```bash
python taskXML.py
```

## Usage

```python
import xml.etree.ElementTree as ET

# gets the root of the xml file
tree = ET.parse('movie.xml')
root = tree.getroot()

# prints tags of the movie element
for movie_elem in root.iter('genre'):
    print(movie_elem.tag)

# prints movie descriptions
for movie_desc in root.iter('description'):
    print(''.join(movie_desc.itertext()))

# prints favorite and non-favourite movies
for movie_fav in root.iter('movie'):
    print(movie_fav.attrib)
```