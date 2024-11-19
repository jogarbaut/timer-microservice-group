# Timer Microservice 

This repository contains a microservice built with **Flask** and **ZeroMQ** that provides the following functionalities:
1. **Time Countdown**: Calculates the total time in seconds based on provided hours, minutes, and seconds.
2. **Date Countdown**: Calculates the number of days between two given dates.
3. **Pomodoro Timer**: Generates a schedule of work and break periods for the Pomodoro technique.

## **Communication Contract**

### **Available Endpoints**
1. `/time-countdown`: Calculates total time in seconds.
2. `/date-countdown`: Calculates the number of days between two dates.
3. `/pomodoro`: Generates a Pomodoro work/break schedule.


## **Endpoint Details**

### **1. Time Countdown**
#### **Request**
- **URL**: `/time-countdown`
- **Method**: POST
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "hours": 1,
    "minutes": 30,
    "seconds": 45
  }
  ```
#### **Example Call**
- **Programmatic Request**:
  ```python
  import requests

  response = requests.post(
      "http://127.0.0.1:5000/time-countdown",
      json={"hours": 1, "minutes": 30, "seconds": 45}
  )

  ```
- **Response Body**:
  ```json
  {
    "status": "success",
    "total_seconds": 5445
  }
  ```

### **2. Date Countdown**
#### **Request**
- **URL**: `/date-countdown`
- **Method**: POST
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "start_date": "2024-11-18",
    "end_date": "2025-01-01"
  }
  ```
#### **Example Call**
- **Programmatic Request**:
  ```python
  import requests

  response = requests.post(
      "http://127.0.0.1:5000/date-countdown",
      json={"start_date": "2024-11-18", "end_date": "2025-01-01"}
  )
  ```
- **Response Body**:
  ```json
  {
    "status": "success",
    "days": 44
  }

  ```

### **3. Pomodoro**
#### **Request**
- **URL**: `/pomodoro`
- **Method**: POST
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "work_duration": 25,
    "break_duration": 5,
    "cycles": 3
  }
  ```
#### **Example Call**
- **Programmatic Request**:
  ```python
  import requests
  response = requests.post(
      "http://127.0.0.1:5000/pomodoro",
      json={"work_duration": 25, "break_duration": 5, "cycles": 3}
  )
  ```
- **Response Body**:
  ```json
  {
    "status": "success",
    "schedule": [
      {
        "type": "work",
        "start_time": "2024-11-18 10:00:00",
        "duration_minutes": 25
      },
      {
        "type": "break",
        "start_time": "2024-11-18 10:25:00",
        "duration_minutes": 5
      },
      {
        "type": "work",
        "start_time": "2024-11-18 10:30:00",
        "duration_minutes": 25
      }
    ]
  }
  ```

## UML Sequence Diagram
* Main Program (Client) sends an HTTP POST request with a JSON payload to the Flask Interface.
* Flask Interface receives the request, processes the payload, and forwards it as a message to the ZeroMQ Backend via ZeroMQ.
* ZeroMQ Backend processes the request (e.g., calculates results or generates schedules) and sends a JSON response back to the Flask Interface.
* Flask Interface formats the response as an HTTP response and sends it back to the Main Program (Client).

![App Screenshot](https://github.com/user-attachments/assets/ebcc154e-55d5-45f6-a848-45b7e63c1460)




## Run Locally

Install Flask and ZeroMQ using pip3
```bash
  pip3 install flask pyzmq
```

Run the backend
```bash
  python3 timerMicroservice.py
```

Run the HTTP Interface
```bash
  python3 timerMicroserviceHttpInterface.py
```

## Authors

[@jogarbaut](https://github.com/jogarbaut)

