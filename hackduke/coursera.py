import requests
import simplejson as json
import random
import MySQLdb

db = MySQLdb.connect(host="localhost", db="HACKDUKE", user="root", passwd="hackduke", charset='utf8')
cursor = db.cursor()
r = requests.get("https://api.coursera.org/api/catalog.v1/courses?fields=language,shortDescription")
detailjson = json.loads(r.content)

parent_url = "https://www.coursera.org/course/"
for course in detailjson['elements']:
    shortname = course['shortName']
    name = course['name']
    #description = course['shortDescription'].encode('ascii', 'ignore')
    description = course['shortDescription']
    url = parent_url + shortname
    difficulty = random.randint(1,3)
    rating = random.randint(1,5)
    #print(name)
    #print(description)
    #print(url)
    #print(difficulty)
    #print(rating)
    try:
        cursor.execute("""INSERT INTO coursera VALUES(%s, %s, %s, %s, %s)""", (name, description, url, rating, difficulty))
        db.commit()
        print 'Inserted record: %s' % url
    except MySQLdb.Error:
        db.rollback()
        raise MySQLdb.Error

db.close() 



