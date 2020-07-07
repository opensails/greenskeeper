import pymongo
import pandas as pd


class DataManager:


    def __init__(self):
        mongoclient = pymongo.MongoClient(
            "mongodb+srv://Austin:Kummel91@golf-qegq1.mongodb.net/<dbname>?retryWrites=true&w=majority")

        database = mongoclient.PGA

        print('Collections that are able to use.', '\n')
        print(database.collection_names())

    def set_collection(self, collection):

        data = database[collection]

    def table_names(self):
        putting_table = []
        approach_the_green_table = []
        streaks_table = []
        scoring_table = []
        off_the_tee_table = []
        money_finishes_table = []
        around_the_green_table = []

        putting = collection.find({}, {'PUTTING-table_name': 1, '_id': 0})
        approach_the_green = collection.find(
            {}, {'APPROACH THE GREEN-table_name': 1, '_id': 0})
        streaks = collection.find({}, {'STREAKS-table_name': 1, '_id': 0})
        scoring = collection.find({}, {'SCORING-table_name': 1, '_id': 0})
        off_the_tee = collection.find(
            {}, {'OFF THE TEE-table_name': 1, '_id': 0})
        money_finishes = collection.find(
            {}, {'MONEY/FINISHES-table_name': 1, '_id': 0})
        around_the_green = collection.find(
            {}, {'AROUND THE GREEN-table_name': 1, '_id': 0})

        for table in putting:
            putting_table.append(table)
        for table in approach_the_green:
            approach_the_green_table.append(table)
        for table in streaks:
            streaks_table.append(table)
        for table in scoring:
            scoring_table.append(table)
        for table in off_the_tee:
            off_the_tee_table.append(table)
        for table in money_finishes:
            money_finishes_table.append(table)
        for table in around_the_green:
            around_the_green_table.append(table)

        # for table in tables:
        #     table_list.append(table)

        unique_table_names_putting = list(
            set(val for dic in putting_table for val in dic.values()))
        unique_table_names_approach = list(
            set(val for dic in approach_the_green_table for val in dic.values()))
        unique_table_names_streaks = list(
            set(val for dic in streaks_table for val in dic.values()))
        unique_table_names_scoring = list(
            set(val for dic in scoring_table for val in dic.values()))
        unique_table_names_off_the_tee = list(
            set(val for dic in off_the_tee_table for val in dic.values()))
        unique_table_names_money_finishes = list(
            set(val for dic in money_finishes_table for val in dic.values()))
        unique_table_names_around = list(
            set(val for dic in around_the_green_table for val in dic.values()))


data1 = {}

for table in unique_table_names_putting:
    data1[table] = pd.DataFrame(
        list(collection.find({"PUTTING-table_name": table}, projection={'_id': False})))
    print(table)
for table in unique_table_names_approach:
    data1[table] = pd.DataFrame(
        list(collection.find({"APPROACH THE GREEN-table_name": table}, projection={'_id': False})))
    print(table)
for table in unique_table_names_streaks:
    data1[table] = pd.DataFrame(
        list(collection.find({"STREAKS-table_name": table}, projection={'_id': False})))
    print(table)
for table in unique_table_names_scoring:
    data1[table] = pd.DataFrame(
        list(collection.find({"SCORING-table_name": table}, projection={'_id': False})))
    print(table)
for table in unique_table_names_off_the_tee:
    data1[table] = pd.DataFrame(
        list(collection.find({"OFF THE TEE-table_name": table}, projection={'_id': False})))
    print(table)
for table in unique_table_names_money_finishes:
    data1[table] = pd.DataFrame(
        list(collection.find({"MONEY/FINISHES-table_name": table}, projection={'_id': False})))
    print(table)
for table in unique_table_names_around:
    data1[table] = pd.DataFrame(
        list(collection.find({"AROUND THE GREEN-table_name": table}, projection={'_id': False})))
    print(table)




