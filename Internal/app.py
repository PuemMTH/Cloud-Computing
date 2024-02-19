from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import psutil  # You'll likely need to install this: pip install psutil

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    data = {
        'status': 200,
        'message': 'Success',
    }
    return jsonify(data)

@app.route('/api')
def api():
    data = {
        'status': 200,
        'message': 'Success',
    }
    return jsonify(data)


@app.route('/api/ipaddress')
def ipaddress():
    client_ip = request.remote_addr

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        hostname = "unknown"
        local_ip = "unknown"

    # Interface details
    interfaces = psutil.net_if_addrs()
    interface_data = []
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET:  # IPv4
                interface_data.append({
                    'name': interface_name,
                    'ip': address.address,
                    'netmask': address.netmask
                })

    data = {
        'status': 200,
        'message': 'Success',
        'client_ip': client_ip,
        'hostname': hostname,
        'local_ip': local_ip,
        'interfaces': interface_data
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)