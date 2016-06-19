import requests
from flask import Flask, render_template, request, json
from bs4 import BeautifulSoup
status = Flask(__name__)

@status.route("/")
def main() :
	return render_template("index.html")

#triggered after the user enters a URL
@status.route("/func", methods = ['POST'])
def func() :
	#status codes
	code = {
		"None" : "Input a valid HTTP URL",
		200 : "OK",
		201 : "The POST command was a success!",
		202 : "Request for processing accepted but it may be disallowed when processing actually takes place.",
		203 : "The returned metainformation is not a definitive set of the object from a" + 
		" server with a copy of the object, but is from a private overlaid web.",
		204 : "No information to send back from the server. Please stay in the same document"+
		" view to allow input for scripts without changing the document at the same time.",
		400 : "Either the request had bad syntax or is inherently impossible to be satisfied",
		401 : "Retry the request with a suitable Authorization header.",
		402 : "Retry the request with a suitable ChargeTo header.",
		403 : "The request is for something forbidden and unfortunately, authorization will not help.",
		404 : "Nothing that matches the URI was found by the server.",
		500 : "Unexpected condition encountered by the server is preventing it from fulfilling"+
		" the request.",
		501 : "The server does not support the facility required.",
		502 : "The server cannot process the request due to a high load but the"+
		" good news is that this is a temporary condition which maybe alleviated at other times!",
		503 : "The respose from the other service which the server tried to access did not return"+
		" within a time that the gateway was prepared to wait.",
		301 : "The data requested has been assigned a new URI and the change is permanent.",
		302 : "The data requested actually resides under a different URL, however, the redirection may be "+
		"altered on occasion as for 'Forward'.",
		303 : "You should try another network address.",
		304 : "The server did not send the document body since the document has not been modified "+
		"since the date and time specified in If-Modified-Since field."
		}
	#gets the URL entered in the form vis method POST 
	_url = request.form['inputName']
	#invalid URL entered
	if _url[:4] != "http" :
		return render_template("index.html", text = "Invalid URL")
	try:
		link = requests.get(_url)
	except Exception, e:
		return render_template("index.html", text = "The host "+_url+" couldn't be resolved")
	message = link.status_code
	for key in code.keys():
		if message == key :
			return render_template("index.html", text = code[key])


@status.route()
def hyperlinks() :
	all_links = soup.find_all("a")
	check_links = []
	if len(all_links) == 0 :
		return render_template("index.html", "No hyperlinks to check") 
	for i in all_links :
		check_links.append(i)
	check(check_links)
		



if __name__ == "__main__" :
	status.run()