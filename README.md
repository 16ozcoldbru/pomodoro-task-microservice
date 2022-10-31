# pomodoro-task-microservice
A simple microservice that tracks tasks using the Pomodoro technique

## Introduction
This is a super simple microservice (my first) that serves to keep track of task objects for a
Pomodoro Timer application. Don't know what a Pomodoro Timer is? Great! Neither did I until I
started this project.

>The Pomodoro Technique is a time management system involving 25 minute work intervals
>followed by short breaks

This microservice serves an application that organizes a user's tasks using this Pomodoro technique.

## Technologies

* Python 3.9
* Flask 2.2.2
* Flask-RESTful 0.3.9

## Usage

This microservice maintains a dictionary of tasks. As a developer, you can create, modify(update),
and delete these tasks.


### Create a task


Use a POST call to '/tasks' endpoint to create a new task with the following:

* id: A unique id
* action: use the 'start' action when creating a new task

Example POST call to create a new task using the /tasks endpoint:
```
{"id": 101, "action": "start"}
```

This will return the newly created task:
```
{
  "task": {
    "id": 101,
    "action": "start",
    "start_time": 1667178933,
    "duration": 0
  }
}
```

### Pause a task

Use a PUT call to '/task/<id>' endpoint to modify a task by temporarily stopping it. This will save the time elapsed for the task in the 
"duration" attribute.

* id: id of the task you wish to modify
* action: "stop" to pause the task

Example PUT call to pause a task using the '/task/<id>' endpoint:
```
{"id": 101, "action": "stop"}
```
This will respond with the modified task:
```
{
  "task": {
    "id": 101,
    "action": "stop",
    "start_time": 1667182203,
    "duration": 2
  }
}
```

## Inspiration

This app was inspired by the excellent tutorial by Swarnim Walavalkar found [here](https://dev.to/swarnimwalavalkar/build-and-deploy-a-rest-api-microservice-with-python-flask-and-docker-5c2d)

Thanks!

![microservice](https://user-images.githubusercontent.com/7835650/198924714-15adf3f3-8a80-49c4-9568-c5989a3cf37f.jpeg)



