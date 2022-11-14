from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import time
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# schema for pomodoro object
taskFields = {
    "id": fields.Integer,
    "action": fields.String,
    "start_time": fields.Integer,
    "duration": fields.Integer
}

# dictionary to store a list of tasks
tasks = [{
    "id": 1,
    "action": "start",
    "start_time": 1667095185,
    "duration": 0
},
{
    "id": 2,
    "action": "start",
    "start_time": 1667095185,
    "duration": 0
}]

class Task(Resource):
    def __init__(self):

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("id", type=int, location="json")
        self.reqparse.add_argument("action", type=str, location="json")
        self.reqparse.add_argument("start_time", type=int, location="json")
        self.reqparse.add_argument("duration", type=int, location="json")

        super(Task, self).__init__()

    # GET returns a single task given matching an id
    def get(self, id):

        task = [task for task in tasks if task["id"] == id]

        # if(len(task) == 0):
        #    abort(404)

        current_task = task[0]

        # Here the service takes the current time and subtracts from this the starting
        # time to get the time elapsed
        start_time = current_task.get("start_time")
        duration = round((time.time() - start_time) / 60) + current_task.get("duration")

        return{"task": marshal(current_task, taskFields), "total_duration": duration}

    # POST allows the user to start and stop a specific task
    def post(self, id):
        task = [task for task in tasks if task["id"] == id]

        # if(len(task) == 0):
        #     abort(404)

        task = task[0]

        # loop through any arguments passed to it
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                if v == "stop":
                    task["duration"] = task["duration"] + round((time.time() - task["start_time"]) / 60)
                if v == "start":
                    task["start_time"] = time.time()
                task[k] = v

        return{"task": marshal(task, taskFields)}

    
    # Delete
    def delete(self, id):

        task = [task for task in tasks if task["id"] == id]

        if(len(task) == 0):
            abort(404)

        tasks.remove(task[0])

        return 201


class TaskList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "id", type=int, required=True, help="The id of the task must be provided",location="json")
        self.reqparse.add_argument(
            "action", type=str, required=True, help="The action must be specified", location="json")
        self.reqparse.add_argument(
            "start_time", type=int, required=False, location="json")
        self.reqparse.add_argument(
            "duration", type=int, required=False, location="json")

    def get(self):
        return{"List of tasks": [marshal(task, taskFields) for task in tasks]}

    def post(self):
        args = self.reqparse.parse_args()

        start_time = time.time()

        new_task = {
            "id": args["id"],
            "action": args["action"],
            "start_time": start_time,
            "duration": 0
        }

        for task in tasks:
            if task["id"] == args["id"]:
                return{"already exists": marshal(task, taskFields)}, 418

        tasks.append(new_task)

        return{"task": marshal(new_task, taskFields)}, 201

class status (Resource):
    def get(self):
        try:
            return {'data': 'API is Running!'}
        except:
            return {'data': 'An Error Occurred during fetching API'}

api.add_resource(status, "/")
api.add_resource(TaskList, "/tasks")
api.add_resource(Task, "/task/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    #app.run()