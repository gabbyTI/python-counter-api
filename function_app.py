import azure.functions as func
import datetime
import json
import logging
import os
from azure.cosmosdb.table.tableservice import TableService
from functions.get_visitor_count import main as get_visitor_count_main
from functions.update_visitor_count import main as update_visitor_count_main
# from update_visitor_count import main as update_visitor_count_main

app = func.FunctionApp()
# table_service = TableService(endpoint_suffix="core.windows.net", connection_string=os.environ['conn_str'])

@app.route(route="getVisitorCount", auth_level=func.AuthLevel.ANONYMOUS)
def get_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    return get_visitor_count_main(req)

@app.route(route="updateVisitorCount", auth_level=func.AuthLevel.ANONYMOUS)
def update_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    return update_visitor_count_main(req)
