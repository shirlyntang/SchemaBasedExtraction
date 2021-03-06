import requests

'''
person_json = requests.get('http://dbpedia.org/data/Barack_Obama.json').json()
person_data = person_json['http://dbpedia.org/resource/Barack_Obama']
#person_attr = person_data['http://dbpedia.org/ontology/' + attribute][0]['value']
gender = person_data['http://xmlns.com/foaf/0.1/gender'][0]['value']
print(gender)


for thing in person_data:
    if 'gender' in thing or 'spouse' in thing:
        print(thing)



spears_json = requests.get('http://dbpedia.org/data/Britney_Spears.json').json()
spears_data = spears_json['http://dbpedia.org/resource/Britney_Spears']
for thing in spears_data:
    print(thing)
'''
'''
data = requests.get('http://dbpedia.org/data/')
for thing in data:
    pass
    #print(thing)

x = requests.get('http://dbpedia.org/resource/')
for thing in x:
    print(thing)
'''

'''
def formatName(name):
    words = name.split()
    name = ""
    for i in range(len(words)):
        name += words[i]
        if i != len(words) - 1:
             name += "_"
    return name


print(formatName("Andrew Gaut"))
'''
'''
def getAttributeForPerson(person_name, attribute):
    person_json = requests.get('http://dbpedia.org/data/' + person_name + '.json').json()
    person_data = person_json['http://dbpedia.org/resource/' + person_name]
    try:
        person_attr = person_data['http://dbpedia.org/ontology/' + attribute][0]['value']
    except:
        try:
            person_attr = person_data['http://xmlns.com/foaf/0.1/' + attribute][0]['value']
        except:
            try:
                person_attr = person_data['http://dbpedia.org/property/' + attribute][0]['value']
            except:
                return 'ERROR: could not find attribute'

    if('/' in person_attr or '_' in person_attr):
        person_attr = getNameFromUrl(person_attr)
    return person_attr

def formatName(name):
    words = name.split()
    name = ""
    for i in range(len(words)):
        name += words[i]
        if i != len(words) - 1:
             name += "_"
    return name


def getGenderedLists():
    males = dict()
    females = dict()

    names = ['Barack Obama', 'Britney Spears', 'Hillary Clinton']

    for name in names:
        formattedName = formatName(name)
        try:
            gender = getAttributeForPerson(formattedName, 'gender')
        except:
            continue
        if(gender == 'male'):
            if name not in males:
                males[name] = name
        if(gender == 'female'):
            if name not in females:
                females[name] = name

    return males, females

def writeKeysToFiles(males, females):
    with open('male_names.txt', 'w') as file:
        for name in males:
            file.write(name+'\n')
    with open('female_names.txt', 'w') as file:
        for name in females:
            file.write(name+'\n')

males, females = getGenderedLists()

print(males)
print("********")
print(females)

writeKeysToFiles(males, females)
'''

def getNameFromUrl(url):
    words = url.split('/')
    name = words[-1]
    if '(' in name:
        name = name[0:name.rindex('(') - 1]
    name = name.replace('_', ' ')
    return name

print(getNameFromUrl('http://dbpedia.org/resource/John_Kemeny_Jr._(film_producer)'))