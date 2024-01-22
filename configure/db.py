import os
from azure.cosmosdb.table.tableservice import TableService

class TableServiceHelper:

    def __init__(self, table_name="VisitorCountTable", conn_str=None):
        self.table_name = table_name 
        self.conn_str = conn_str if conn_str else os.environ['conn_str']
        self.table_service = TableService(endpoint_suffix="core.windows.net", connection_string=self.conn_str)
        
        if not self.table_service.exists(self.table_name):
            self.table_service.create_table(self.table_name)   
            # Create default entity if table is empty
        try:
            self.table_service.get_entity(self.table_name, "VisitorCountPartition", "1")
        except:
            self.table_service.insert_entity(
                self.table_name,
                {
                    'PartitionKey': "VisitorCountPartition",
                    'RowKey': "1",
                    'visitorCount': 0,
                    # Add other properties if needed
                }
            )
 
    def table(self):
        return self.table_service

    def get_entity(self,partitionKey,rowKey):
        return self.table_service.get_entity(self.table_name, partitionKey, rowKey)

    def update_entity(self,entity):
        return self.table_service.update_entity(self.table_name, entity)