# api stands for application programming interface
# .json stands for javascript object notation-set of key value pairs

import requests # requests library
import pprint #pretty print

r = requests.get('https://api.dailysmarty.com/posts%27') # store in r variable- requests.get and then pass in the api correctly
r.json() # to view what what the json looks like
pprint.pprint(r.json()['posts'][0]) # call pprint and then called r json and the function
                                    # next lets reach out to the posts (and treated like a dictionary) call the first post with [0]
pprint.pprint(r.json()['posts'][0]['url_for_post'])  # this command will bring in the URL using 