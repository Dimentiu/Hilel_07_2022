import webbrowser
import re

def remove_url_anchor(url):
    urls = "lms.ithillel.ua#about"
    result = re.sub("#about", "", urls)
    
    assert len(url) > 0
    for url in result:
        if webbrowser.Chrome(result):
            return webbrowser.open(result)
    return None 
    



assert remove_url_anchor("lms.ithillel.ua#about") == "lms.ithillel.ua"
assert remove_url_anchor("lms.ithillel.ua/groups/?page=1#example") == "lms.ithillel.ua/groups/?page=1"
assert remove_url_anchor("lms.ithillel.ua/groups/") == "lms.ithillel.ua/groups/"
