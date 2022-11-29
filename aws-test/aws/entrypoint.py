import pymongo
import json
import subprocess

client = pymongo.MongoClient(
    "mongodb+srv://steampipeadmin:steampipeadmin@cluster0.806ymg0.mongodb.net/?retryWrites=true&w=majority", ServerSelectionTimeoutMS=5000)
db = client["Inventory"]
collection = db["AWS"]

with open("aws_tables.json", "r") as jsonfile:
    data = jsonfile.read()
    tables = json.loads(data)["aws"]
    #print(tables)
    for table in tables:
        print(table)
        steam_op = subprocess.run(["steampipe", "query", "select * from {}".format(
            table), "--output", "json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(steam_op)
        stdout = steam_op.stdout.decode("utf-8")
        stderr = steam_op.stderr.decode("utf-8")
        print({"table_name": table, "table_data": stdout})
        if stderr == "":
            collection.insert_one({"table_name": table, "table_data": stdout})
        else:
            collection.insert_one(
                {"table_name": table, "table_data": "Steampipe Error: No proper required arguments provided"})
        #break
    jsonfile.close()

