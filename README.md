### Prerequisite

1. Python v10 or higher
2. Azure CosmosDB for Table database connection string
3. Azure CLI
4. Install azure-functions-core-tools

```bash
npm install -g azure-functions-core-tools
```

### Setup

1. Clone repository

```bash
git clone https://github.com/gabbyTI/python-counter-api.git
```

2. Initialize the azure function to create the

```bash
cd python-counter-api
func init
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add connection string and table name to the local.settings.json file(this is created after the 2nd steps)

```json
{
  ...
  "Values": {
    ...
    "conn_str": "your connection string",
    "table_name": "your table name"
  }
}
```

### Running Azure Function Locally

1. Login to Azure

```bash
az login
```

2. Start the azure function locally

```bash
func start -p 7071
```
