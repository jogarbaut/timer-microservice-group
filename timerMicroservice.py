import zmq
from datetime import datetime, timedelta

# Set up ZeroMQ backend
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def handle_time_countdown(data):
  hours = data.get('hours', 0)
  minutes = data.get('minutes', 0)
  seconds = data.get('seconds', 0)
  total_seconds = hours * 3600 + minutes * 60 + seconds
  return { 'status': 'success', 'total_seconds': total_seconds }

def handle_date_countdown(data):
  start_date = datetime.fromisoformat(data.get('start_date'))
  end_date = datetime.fromisoformat(data.get('end_date'))
  delta = end_date - start_date
  days = delta.days
  return { 'status': 'success', 'days': days }

def handle_pomodoro(data):
  work_duration = data.get('work_duration', 25)
  break_duration = data.get('break_duration', 5)
  cycles = data.get('cycles', 5)
  schedule = []
  current_time = datetime.now()

  for cycle in range(cycles):
    # Add work cycle
    schedule.append({
      'type': 'work',
      'start_time': current_time.strftime("%Y-%m-%d %H:%M:%S"),
      'duration_minutes': work_duration
    })

    # Increment time by the work duration
    current_time += timedelta(minutes=work_duration)

    # Add a break if not last cycle
    if cycle < cycles - 1:
      schedule.append({
        'type': 'work',
        'start_time': current_time.strftime("%Y-%m-%d %H:%M:%S"),
        'duration_minutes': work_duration
      })
      # Increment time by the break duration
      current_time += timedelta(minutes=break_duration)
    
  return {
    'status': 'success',
    'schedule': schedule
  }

while True:
  message = socket.recv_json()
  request_type = message.get('type')

  if request_type == 'time_countdown':
    response = handle_time_countdown(message)
  elif request_type == 'date_countdown':
    response = handle_date_countdown(message)
  elif request_type == 'pomodoro':
    response = handle_pomodoro(message)
  else:
    response = {'status': 'error', 'message': 'Invalid request type'}

  socket.send_json(response)