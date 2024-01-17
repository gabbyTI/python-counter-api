from flask import Flask, jsonify, request
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from dotenv import load_dotenv
from models.VisitorCount import VisitorCountEntity  # Import your model

import os

load_dotenv()

app = Flask(__name__)
# Azure Cosmos DB Table API configuration
table_name = "VisitorCountTable"
partition_key = "VisitorCountPartition"
row_key = "1"
the_connection_string = os.getenv("CONNECTION_STRING")

table_service =  TableService(endpoint_suffix = "core.windows.net", connection_string= the_connection_string)

# Create the table if it does not exist
if not table_service.exists(table_name):
    table_service.create_table(table_name)
    
# Check if the entity exists; if not, insert a default entity
entity_exists = table_service.exists(table_name, partition_key, row_key)

if not entity_exists:
    table_service.insert_entity(
        table_name,
        {
            'PartitionKey': partition_key,
            'RowKey': row_key,
            'visitorCount': 0,
        }
    )

@app.route('/getVisitorCount', methods=['GET'])
def get_visitor_count():
    try:

      # Fetch the current visitor count from the table
        entity = table_service.get_entity(table_name, partition_key, row_key)
        # Convert entity to VisitorCountEntity instance
        visitor_count_entity = VisitorCountEntity.from_dict(entity)
        
        # Convert entity instance to dictionary for JSON response
        entity_dict = visitor_count_entity.to_dict()

        return jsonify(entity_dict), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/updateVisitorCount', methods=['POST'])
def update_visitor_count():
    try:
        
       # Fetch the current entity from the table
        entity = table_service.get_entity(table_name, partition_key, row_key)
        
        # Convert entity to VisitorCountEntity instance
        visitor_count_entity = VisitorCountEntity.from_dict(entity)

        # Update the visitor count in the entity
        visitor_count_entity.visitorCount = visitor_count_entity.visitorCount + 1

        entity_to_update = visitor_count_entity.to_dict()
        entity_to_update['PartitionKey'] = partition_key
        entity_to_update['RowKey'] = row_key

        # Update the entity in the table
        table_service.update_entity(table_name, entity_to_update )

        return jsonify({'status': 'Visitor count updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
