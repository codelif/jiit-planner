from flask import Blueprint, render_template
from jiit_tt_parser.parser import parse_events
from jiit_tt_parser.utils import load_worksheet
from jiit_tt_parser.utils.preprocessing import cache_tt_xls, cache_fac, os
from jiit_tt_parser.utils.cache import get_cache_file
from typing import List
from jiit_tt_parser.parser.parse_events import Event

router = Blueprint("router", "jiit-planner", template_folder="jiit_planner/templates")

@router.get("/")
def home():
    return render_template("index.html")


@router.get("/planner/<batch>")
@router.get("/<batch>")
def planner(batch):
    evs = filter_events(batch)

    return render_template("index.html", events=evs)



def jsonify_events(events: List[Event]):
    {"batches": ["B5"],
     "type": "L",
     "classroom": "CL03",
     "subject": "Computer Fundamentals",
     "subject-code": "CI111",
     }

    for ev in events:
        ev.eventcode
        

def filter_events(batch: str):
    sheet, r, c = load_worksheet(get_cache_file("sem1.xlsx"))
    evs = parse_events(sheet, r, c)

    filtered_evs = []

    for ev in evs:
        if batch.lower() in [i.lower() for i in ev.batches]:
            filtered_evs.append(ev)

    return filtered_evs
