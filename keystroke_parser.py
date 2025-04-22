import pandas as pd

def parse_keystrokes(user_id, task_id, keystrokes):
    data = []
    for entry in keystrokes:
        timestamp = entry["timestamp"]
        action = entry["delta"]["action"]
        data.append({"user_id": user_id, "task_id": task_id, "timestamp": timestamp, "action": action})
    
    return data


