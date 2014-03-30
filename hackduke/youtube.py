import gdata.youtube
import gdata.youtube.service
import MySQLdb
from _mysql_exceptions import Warning, Error, InterfaceError, DataError,\
     DatabaseError, OperationalError, IntegrityError, InternalError,\
     NotSupportedError, ProgrammingError

db = MySQLdb.connect(host="localhost", db="HACKDUKE", user="root", passwd="hackduke")
cursor = db.cursor()
yt_service = gdata.youtube.service.YouTubeService()

# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
yt_service.ssl = True
yt_service.email = 'g.is.saraf@gmail.com'
yt_service.password = 'gaurav38'
yt_service.source = 'CrawlYouTube'
yt_service.developer_key = '341315258382-5rb3gc7s809ihcihqsd77hdaibo5rrt7@developer.gserviceaccount.com'
yt_service.client_id = '341315258382-5rb3gc7s809ihcihqsd77hdaibo5rrt7.apps.googleusercontent.com'
#yt_service.SetAuthSubToken(authsub_token)
#yt_service.UpgradeToSessionToken()

def PrintEntryDetails(entry):
    print 'Video title: %s' % entry.media.title.text
    title = entry.media.title.text
    #print 'Video published on: %s ' % entry.published.text
    print 'Video description: %s' % entry.media.description.text
    description = entry.media.description.text
    #print 'Video category: %s' % entry.media.category[[]0].text
    #print 'Video tags: %s' % entry.media.keywords.text
    print 'Video watch page: %s' % entry.media.player.url
    url = entry.media.player.url
    #print 'Video flash player URL: %s' % entry.GetSwfUrl()
    #print 'Video duration: %s' % entry.media.duration.seconds

    # non entry.media attributes
    #print 'Video geo location: %s' % entry.geo.location()
    print 'Video view count: %s' % entry.statistics.view_count
    view_count = entry.statistics.view_count
    #print 'Video rating: %s' % entry.rating.average
    #rating = float(entry.rating.average)

    # show alternate formats
    #for alternate_format in entry.media.content:
    #    if 'isDefault' not in alternate_format.extension_attributes:
    #        print 'Alternate format: %s | url: %s ' % (alternate_format.type,
    #                                             alternate_format.url)

    # show thumbnails
    thumbnail = ""
    for thumbnail in entry.media.thumbnail:
        print 'Thumbnail url: %s' % thumbnail.url
        thumbnail = thumbnail.url

    #sql = """INSERT INTO youtube VALUES(%s, %s, %s, %s, %s)""", (title, description, url, view_count, thumbnail)
    #print(sql)
    try:
        cursor.execute("""SELECT * FROM youtube where url = %s""", (url))
        results = cursor.fetchall()
        if(results.__len__() == 0):          
            cursor.execute("""INSERT INTO youtube VALUES(%s, %s, %s, %s, %s)""", (title, description, url, view_count, thumbnail))
            db.commit()
            print 'Inserted Record: %s' % entry.media.player.url
    except MySQLdb.Error:
        db.rollback()
        raise MySQLdb.Error

    print('--------------------------------------------------------------')


def GetAndPrintVideoFeed(uri):
    yt_service = gdata.youtube.service.YouTubeService()
    feed = yt_service.GetYouTubeVideoFeed(uri)
    for entry in feed.entry:
        PrintEntryDetails(entry)

def SearchAndPrint(search_terms):
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = search_terms
    query.orderby = 'viewCount'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)
    for entry in feed.entry:
        PrintEntryDetails(entry)

uri = 'http://gdata.youtube.com/feeds/api/standardfeeds/JP/most_popular'
#GetAndPrintVideoFeed(uri)
#PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))
SearchAndPrint('ruby on rails')
db.close()
