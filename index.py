import bottle
import pymongo
import guestbookDAO

#This is the deault route, our index page. Here we need to read the documents from MongoDB.
@bottle.route('/')
def guestbook_index();
	mynames_list = guestbook.find_names()
	return bottle.template('index', dict(mynames = mynames_list))


#We will post new entries to this route so we can inset them into MongoDB
@bottle.route('newguest', method='POST')
def insert_newguest();
	name = bottle.request.forms.get("name")
	email = bottle.request.forms.get("email")
	guestbook.insert_name(name, email)
	bottle.redirect('/')

#This is to setup the connection

#First, setup a connection string. My server is running on this computer so localhost is OK
connection_string = "mongodb://localhost"
#Next, let PyMongo know about the MongoDB connection we want to use. PyMongo will manage the connection
connection = pymongo.MongoClient(connection_string)
#Now we want to set a contect to the names database we created using the mongo interactive shell
database = connection.names
#Finally, let our data access object class we built which acts as our data layer know about this
guestbook = guestbookDAO.guestbookDAO(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082)