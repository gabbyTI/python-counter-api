import azure.functions as func
import datetime
import json
import logging
import os
from configure.db import TableServiceHelper

table_service = TableServiceHelper().table()


def main(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')
    entity = table_service.get_entity(os.getenv("table_name"), 'VisitorCountPartition', '1')
    
    result = {
      "count" : entity.get('visitorCount'),
    }

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json",
    )

