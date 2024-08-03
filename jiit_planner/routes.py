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
    batch = request.args.get("bt")
    day = request.args.get("day")
    branch = request.args.get("br")
    
    if (day is None):
        day = datetime.date.today().strftime("%A")


    events, batches = filter_events(branch, batch, day)
    branches = {"btech-sem1":"B.Tech Semester 1", "bca-sem1": "BCA Semester 1", "bca-sem3": "BCA Semester 3"}


    if (batch is None):
        batch = ''

    return render_template("index.html", events=events, day=day.capitalize(), batch=batch, batches=batches, branches=branches)


def split_on_number(key: str):
    for i,k in enumerate(key):
        if k.isdigit():
            return key[:i], int(key[i:])

    return key,0

def jsonify_events(events: List[Event]):
    {"batches": ["B5"],
     "type": "L",
     "classroom": "CL03",
     "subject": "Computer Fundamentals",
     "subject-code": "CI111",
     }

    for ev in events:
        ...
        

def filter_events(branch: str, batch: str, day: str):

    branches = {"btech-sem1":"sem1.xlsx", "bca-sem1": "bca_sem1_new.xlsx", "bca-sem3": "bca_sem1_new.xlsx"}
    branch_xl = branches.get(branch)
    
    if not branch_xl:
        return [], []

    sheet, r, c = load_worksheet(get_cache_file(branch_xl))
    evs = parse_events(sheet, r, c)
    
    filtered_evs = []
    batches = set()

    for ev in evs:
        batches = batches.union(ev.batches)
        if (batch is None) or (batch not in ev.batches):
            continue

        if (day is not None) and (not ev.day.lower() == day.lower()):
            continue
        
        filtered_evs.append(ev)

    return (filtered_evs, sorted(batches, key=split_on_number))
