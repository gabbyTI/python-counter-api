import azure.functions as func
import datetime
import json
import logging
import os
from configure.db import TableServiceHelper

table_service = TableServiceHelper().table()

def main(req: func.HttpRequest) -> func.HttpResponse:
    entity = table_service.get_entity(os.environ['table_name'], 'VisitorCountPartition', '1')
    print(entity)
    visitor_count = entity.get('visitorCount')
    visitor_count += 1
    table_service.update_entity(os.environ['table_name'], {'PartitionKey': 'VisitorCountPartition', 'RowKey': '1', 'visitorCount': visitor_count})
    result = {
      "message" : "Visitor count updated successfully",
    }
    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json",
    )
