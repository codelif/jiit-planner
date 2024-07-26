from flask import Blueprint, render_template
from jiit_tt_parser.parser import parse_events
from jiit_tt_parser.utils import load_worksheet
from jiit_tt_parser.utils.preprocessing import cache_tt_xls, cache_fac, os
from jiit_tt_parser.utils.cache import get_cache_file

router = Blueprint("router", "jiit-planner", template_folder="jiit_planner/templates")

@router.get("/")
def home():
    return render_template("index.html")


@router.get("/planner/<batch>")
@router.get("/<batch>")
def planner(batch):
    evs = filter_events(batch)

    return render_template("planner.html", events=evs)


def filter_events(batch: str):
    sheet, r, c = load_worksheet(get_cache_file("sem1.xlsx"))
    evs = parse_events(sheet, r, c)

    filtered_evs = []

    for ev in evs:
        if batch.lower() in [i.lower() for i in ev.batches]:
            filtered_evs.append(ev)

    return filtered_evs
