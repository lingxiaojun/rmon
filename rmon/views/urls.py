from flask import Blueprint
from rmon.views.index import IndexView
# from rmon.views.server import (Servercommand, ServerDetail, ServerList, ServerMetrics)

api = Blueprint('api', __name__)

api.add_url_rule('/', view_func=IndexView.as_view('index'))

