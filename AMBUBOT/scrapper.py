from bs4 import BeautifulSoup
import urllib.request

def innerHTML(element):
	return element.decode_contents(formatter="html")

def get_name(body):
	return body.find('span', {'class':'jcn'}).a.string

def get_phone_number(body):
	try:
		return body.find('p', {'class':'contact-info'}).span.a.string
	except AttributeError:
		return ''

def get_rating(body):
	rating = 0.0
	text = body.find('span', {'class':'star_m'})
	if text is not None:
		for item in text:
			rating += float(item['class'][0][1:])/10

	return rating

def get_rating_count(body):
	text = body.find('span', {'class':'rt_count'}).string

	# Get only digits
	rating_count =''.join(i for i in text if i.isdigit())
	return rating_count

def get_address(body):
	return body.find('span', {'class':'mrehover'}).text.strip()

def get_location(body):
	text = body.find('a', {'class':'rsmap'})
	if text == None:
		return
	text_list = text['onclick'].split(",")
	
	latitutde = text_list[3].strip().replace("'", "")
	longitude = text_list[4].strip().replace("'", "")
	
	return latitutde + ", " + longitude

page_number = 1
service_count = 1

fields = ['Name', 'Phone', 'Rating', 'Rating Count', 'Address', 'Location']

location = "Kolkata"
	
url = "https://www.justdial.com/{}/24-Hours-Ambulance-Services/nct-10000352/page-{}".format(location, page_number)

