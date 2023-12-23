# importing the necessary libraries
import requests
from flask import Flask, render_template, request
import json 

# create flask application object
app = Flask(__name__)

# rendering the html webpage
# setting up route at homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# Defining weather function
# setting up api url along with parameters
# taking city parameter from the user
# api_key and units is pre-defined 
# sending the request and getting response and showcasing it in the .json format
# binding the route after clicking on submit button
# also setting up methods = POST
@app.route('/weatherapp', methods=['POST'])
def get_weatherdata():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': request.form.get("city"),
        'appid' : '44bf0d2f5cc166d5334cc150434614c5',
        'units' : 'metric'
    }
    response = requests.get(url, params=params)
    data = response.json()

    # formatting the json output
    formatted_data = json.dumps(data, indent=4)

    return render_template('index.html', weather_data=formatted_data)

if __name__ == '__main__':
    app.run()