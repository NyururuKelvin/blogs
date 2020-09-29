
import urllib.request,json
# base_url = None

def get_blogs():
    get_blogs_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_blogs_url) as url:
        quotes = url.read()
        get_blogs_response = json.loads(quotes)
        
    return get_blogs_response