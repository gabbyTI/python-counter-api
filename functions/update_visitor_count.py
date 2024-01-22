import azure.functions as func
import datetime
import json
import logging
import os
from configure.db import TableServiceHelper

table_service = TableServiceHelper()

def main(req: func.HttpRequest) -> func.HttpResponse:
    entity = table_service.get_entity("VisitorCountPartition", "1")
    visitor_count = entity.visitorCount
    visitor_count += 1
    entity.visitorCount = visitor_count
    table_service.update_entity(entity)
    result = {
      "message" : "Visitor count updated successfully",
    }
    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json",
    )
