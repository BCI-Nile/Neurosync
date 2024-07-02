from websocket_server import WebsocketServer
import time
import threading
import random
import websocket
import json


# uri = "ws://192.168.84.247:8765" #on my phone hotspot
# uri = "ws://192.168.1.42:8765"  # Starlink IP

# Enter the hotspot you connect the raspberry pi to
uri = "ws://192.168.1.42:8765" 

actions = ['right', 'push', 'left', 'pull']
previous_action_time = 0
action_interval = 2  # seconds between actions
count = 7

def send_to_websocket(ws, data):
    ws.send(json.dumps(data))

def printSubData(ws, data):
    # print("data sent")
    print(data['action'])
    if data['action'] != 'neutral':
        send_to_websocket(ws, data['action'])

def generate_data(ws):
    global previous_action_time
    global count
    
    current_time = time.time()
    action = 'neutral'
    
    # Change action approximately every action_interval seconds
    if current_time - previous_action_time >= action_interval:
        if count > 0:
                action = 'push'
                count = count - 1
        else:
            action = random.choice(actions)
    
    data = {
        'action': action,
        'power': 0.0,
        'time': current_time
    }
    printSubData(ws, data)
    
    # Schedule the function to run again in 0.1 seconds
    threading.Timer(1, generate_data, [ws]).start()

def on_open(ws):
    print("WebSocket connection established")
    generate_data(ws)

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(uri,
                                on_open=on_open,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
