"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Maps(Controller):
    def __init__(self, action):
        super(Maps, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def get_directions(self):
        data = {
            "origin" : request.form['origin'],
            "destination" : request.form['destination']
        }
        url = "https://maps.googleapis.com/maps/api/directions/json?"+urlencode(data)+"&sesnor=false"
        response = requests.get(url).content
        return response

