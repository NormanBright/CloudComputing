from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json
import requests
import requests_cache
from cassandra.cluster import Cluster
# requests_cache.install_cache('crime_api_cache', backend='sqlite', expire_after=36000)
cluster = Cluster(contact_points =['172.17.0.2'], port = 9042)
session = cluster.connect()
app = Flask(__name__)
# this get all the information regarding the state please enter the state as their abbreviation
@app.route('/covid19/<state>', methods = ['GET'])
def profile(state):
    row = session.execute("""Select * From covid19.stats where state = '{}'""".format(state))
    for covid19 in row:
         return ('<h2>{} has a number of positive patients {},and the negative patients are: {}, and the number of dead people are: {}</h2>'.format(state,covid19.positive,covid19.negative,covid19.death))
    return jsonify({'try again': 'state not found'}), 404
#allows the user to remove positive results
@app.route('/covid19/<positive>', methods = ['DELETE'])
def deletepos(positive):
    row = session.execute("""Select * From covid19.stats where positive = '{}'""".format(positive))
    for positive in row:
        if positive is None:
            return jsonify({'error':'positive number not found'}), 404
        else:
            rows = session.execute( """Delete From covid19.stats where positive = '{}'""".format(positive))
            return jsonify({'success': True})
#allows the user to add another state
@app.route('/covid19/<state>', methods=['POST'])
def poststate(state):
    row = session.execute( """Select * From covid19.stats where state = '{}'""".format(state))
    for state in row:
        if state is None:
            return jsonify({'error':'the new state must have a name'}), 400
        return jsonify({'error':'the state already exist'}), 400
    rows = session.execute( """Insert into covid19.stats (state) values ('Canada')""")
    return jsonify({'message': 'created: /covid19/{}'.format(state)}), 201

if __name__=="__main__":
    app.run(host='0.0.0.0', port =80, debug = True)
