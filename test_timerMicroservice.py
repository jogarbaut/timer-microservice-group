import zmq
from datetime import datetime

# Create a ZeroMQ context
context = zmq.Context()

# Create a REQ (Request) socket
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def test_time_countdown():
  # Test time countdown with hours, minutes, and seconds
  request = {
      'type': 'time_countdown',
      'hours': 1,
      'minutes': 30,
      'seconds': 45
  }
  socket.send_json(request)
  response = socket.recv_json()

  print(f'Response from time_countdown: {response}')
  assert response['status'] == 'success', f'Failed: {response}'
  assert response['total_seconds'] == (1 * 3600 + 30 * 60 + 45), f'Unexpected result: {response}'


def test_date_count():
  # Test date countdown with start_date and end_date
  request = {
    'type': 'date_countdown',
    'start_date': '2024-11-19',
    'end_date': '2024-11-26'
  }
  socket.send_json(request)
  response = socket.recv_json()

  print(f'Response from date_countdown: {response}')
  assert response['status'] == 'success', f'Failed: {response}'
  assert response['days'] == 7, f'Unexpected result: {response}'


def test_pomodoro():
  request = {
    'type': 'pomodoro',
    'work_duration': 25,
    'break_duration': 5,
    'cycles': 3
  }
  socket.send_json(request)
  response = socket.recv_json()

  print(len(response['schedule']))

  print(f'Response from pomodoro: {response}')
  assert response['status'] == 'success', f'Failed: {response}'
  assert len(response['schedule']) == 5, f'Unexpected result: {response}'


# Run tests
if __name__ == "__main__":
  test_time_countdown()
  test_date_count()
  test_pomodoro()