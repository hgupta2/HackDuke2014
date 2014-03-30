import requests
import simplejson as json
import random
import MySQLdb

db = MySQLdb.connect(host="localhost", db="HACKDUKE", user="root", passwd="hackduke", charset='utf8')
cursor = db.cursor()
r = requests.get("https://www.khanacademy.org/api/v1/topictree")
detailjson = json.loads(r.content)

#parent_url = "https://www.coursera.org/course/"
for category in detailjson['children']:
    #blah = detailjson['children'][0]
    for course in category['children']:
        title = course['title']
        description = course['description']
        url = course['ka_url']
        difficulty = random.randint(1,3)
        rating = random.randint(1,5)
        #print(name)
        #print(description)
        #print(url)
        #print(difficulty)
        #print(rating)
        try:
            cursor.execute("""INSERT INTO khanacademy VALUES(%s, %s, %s, %s, %s)""", (title, description, url, rating, difficulty))
            db.commit()
            print 'Inserted record: %s' % url
        except MySQLdb.Error:
            db.rollback()
            raise MySQLdb.Error

db.close() 



