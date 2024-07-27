from flask import Blueprint, redirect, render_template, request, url_for
from jiit_tt_parser.parser import parse_events
from jiit_tt_parser.utils import load_worksheet
from jiit_tt_parser.utils.preprocessing import cache_tt_xls, cache_fac, os
from jiit_tt_parser.utils.cache import get_cache_file
from typing import List
from jiit_tt_parser.parser.parse_events import Event, datetime

router = Blueprint("router", "jiit-planner", template_folder="jiit_planner/templates")

@router.get("/")
def home():
    return redirect(url_for('router.planner'))

@router.get("/batch", strict_slashes=False)
def planner():
    batch = request.args.get("b")
    day = request.args.get("day")
    
    if (day is None):
        day = datetime.date.today().strftime("%A")
    print(batch, day)
    events = filter_events(batch, day)

    return render_template("index.html", events=events, day=day.capitalize(), batch=batch)


def jsonify_events(events: List[Event]):
    {"batches": ["B5"],
     "type": "L",
     "classroom": "CL03",
     "subject": "Computer Fundamentals",
     "subject-code": "CI111",
     }

    for ev in events:
        ...
        

def filter_events(batch: str, day: str):
    sheet, r, c = load_worksheet(get_cache_file("sem1.xlsx"))
    evs = parse_events(sheet, r, c)

    filtered_evs = []

    for ev in evs:
        if (batch is not None) and (batch.lower() not in [i.lower() for i in ev.batches]):
            continue

        if (day is not None) and (not ev.day.lower() == day.lower()):
            continue
        
        filtered_evs.append(ev)

    return filtered_evs
