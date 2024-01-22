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

@app.route(route="getVisitorCount", auth_level=func.AuthLevel.ANONYMOUS, methods=['GET'])
def get_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    return get_visitor_count_main(req)

@app.route(route="updateVisitorCount", auth_level=func.AuthLevel.ANONYMOUS, methods=['POST'])
def update_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    return update_visitor_count_main(req)




@app.route(route="hello_world", auth_level=func.AuthLevel.ADMIN)
def hello_world(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )