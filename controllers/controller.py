from app import app
from flask import render_template
from flask import request
from flask import redirect
from models.events import event_list
from models.event_class import Event
from datetime import date


@app.route("/")
def home():
    return render_template("index.html", events = event_list)


@app.route("/planner", methods=["GET", "POST"])
def task_planer():
    if request.method == "POST":
        event_data = {**request.form}
        
        if not "repeat" in event_data:
            event_data["repeat"] = False
        
        elif request.form["repeat"] == "on":
            event_data["repeat"] = True    
        
        event = Event(**event_data)  
        event_list.append(event)
        return redirect("/")
        
    return render_template("planner.html")  

@app.route("/event/<int:index>")
def event_info(index):
    event = event_list[index]
    return render_template("event_info.html", event = event)


@app.route("/event/delete/<int:index>")
def delete_event(index):
    event_list.remove(event_list[index])
    return redirect("/")