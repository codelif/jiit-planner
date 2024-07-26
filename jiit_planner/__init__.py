from flask import Flask
from jiit_planner.routes import router

PROG = "jiit-planner"
app = Flask(PROG, static_folder="jiit_planner/static", template_folder="jiit_planner/templates")
app.register_blueprint(router)
