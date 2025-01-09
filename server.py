from door_unlocker import DoorUnlocker
from flask import Flask, jsonify

app = Flask(__name__)
door_unlocker = DoorUnlocker()

# Define your custom action for /unlock
def unlock_action():
    print("Unlock endpoint accessed!")
    door_unlocker.unlock_door()
    return {"unlocked": "true"}

@app.route('/unlock', methods=['GET'])
def unlock():
    try:
        # Execute the custom action
        result = unlock_action()
        return jsonify(result), 200
    except Exception as e:
        # Handle any errors
        return jsonify({"status": "error", "message": str(e)}), 500
        
# Define your custom action for /unlock
def get_status_action():
    print("Status endpoint accessed!")
    status = door_unlocker.get_status()
    if status == "UNLOCKED":
        return {"unlocked": "true"}
    else:
        return {"unlocked": "false"}

@app.route('/get_status', methods=['GET'])
def get_status():
    try:
        # Execute the custom action
        result = get_status_action()
        return jsonify(result), 200
    except Exception as e:
        # Handle any errors
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask server
    app.run(host='0.0.0.0', port=5000)
