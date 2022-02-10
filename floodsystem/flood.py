from . import datafetcher

def stations_highest_rel_level(stations, N):
    data = datafetcher.fetch_latest_water_level_data()