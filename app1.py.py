from flask import Flask, render_template, request, jsonify
import json
import requests
import requests_cache
requests_cache.install_cache('crime_api_cache', backend='sqlite', expire_after=36000)
app = Flask(__name__)
stop_url_template = 'https://data.police.uk/api/stops-street?lat={lat}&lng={lng}&date={data}' #stop and search by area api
@app.route('/crimestat', methods=['GET'])
def crimechart():
    my_latitude = request.args.get('lat','52.629729')
    my_longitude = request.args.get('lng','-1.131592')
    my_date = request.args.get('date','2018-06')
    stop_url = stop_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
    resp = requests.get(stop_url)
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)
if __name__=="__main__":
    app.run(host='0.0.0.0',port = 80, debug =True)
