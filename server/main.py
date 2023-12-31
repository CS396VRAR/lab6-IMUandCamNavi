from flask import Flask, send_from_directory
from flask_cors import CORS
import json

#g.imu_x = 0
imu_y = 0
imu_z = 0
imu_w = 0

app = Flask(__name__,
            static_url_path='',
            static_folder='../static')
app.config['x'] = 0
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/static/<path:path>")
def webglfun(path):
    #print(path)
    return send_from_directory('static',path)

@app.route("/getimu")
def get_imu():
    imu_x = app.config['x']

    app.config['x'] = imu_x +  0.1
    print(imu_x)
    fake_str = '{},{},{}'.format(imu_x,imu_y,imu_z)
    fake_json = json.dumps(fake_str).encode('utf-8')
    print(fake_json)
    return json.dumps(fake_str).encode('utf-8')


    #return json.dumps(bno.game_quaternion).encode('utf-8')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)