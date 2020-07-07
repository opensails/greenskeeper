from pga.explorer.Workday.Manager import DataManager


manager = DataManager()

manager.set_collection('golfer_stats')

manager.table_names()

manager.get_dataframes()