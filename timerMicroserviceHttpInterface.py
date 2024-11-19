from flask import Flask, request, jsonify
import zmq

# Flask HTTP interface
app = Flask(__name__)

# ZeroMQ client
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

# Time countdown HTTP route
@app.route('/time-countdown', methods=['POST'])
def time_countdown():
  data = request.json
  data['type'] = 'time_countdown'
  socket.send_json(data)
  response = socket.recv_json()
  return jsonify(response)

# Date countdown HTTP route
@app.route('/date-countdown', methods=['POST'])
def date_countdown():
  data = request.json
  data['type'] = 'date_countdown'
  socket.send_json(data)
  response = socket.recv_json()
  return jsonify(response)

# Pomodoro HTTP route
@app.route('/pomodoro', methods=['POST'])
def pomodoro():
  data = request.json
  data['type'] = 'pomodoro'
  socket.send_json(data) # Send request to ZeroMQ server with type as pomodoro
  response = socket.recv_json() # Receive responses from ZeroMQ server
  return jsonify(response)

if __name__ == '__main__':
  app.run(port=5000)