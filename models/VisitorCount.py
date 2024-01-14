from azure.cosmosdb.table.models import Entity

class VisitorCountEntity(Entity):
    def __init__(self, visitor_count):
        super(VisitorCountEntity, self)
        self.visitorCount = visitor_count
        # Add other properties if needed

    @classmethod
    def from_dict(cls, data):
        return cls(
            # partition_key=data.get('PartitionKey', ''),
            # row_key=data.get('RowKey', ''),
            visitor_count=data.get('visitorCount', 0),
            # Add other properties if needed
        )

    def to_dict(self):
        print(self.visitorCount)
        return {
          'visitorCount': self.visitorCount,
        }
