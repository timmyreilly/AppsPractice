import urllib

def find_photo(url):
    try:
        urllib.urlretrieve(url, "static/photo.jpg")
    except:
        print "not a valid url"
        urllib.urlretrieve("http://i0.wp.com/timmyreilly.azurewebsites.net/wp-content/uploads/2016/07/wazzupdogimdex.png", "static/photo.jpg")