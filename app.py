from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Event Management API"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "Missing required field: 'title'"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "Missing required field: 'title'"}), 400

    event.title = data["title"]

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404
    events.remove(event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify({"message": f"Event {event_id} deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
