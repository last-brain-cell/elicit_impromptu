import pandas as pd
from ydata_profiling import ProfileReport

local_authority_traffic_df = pd.read_csv("data/local_authority_traffic.csv")
region_traffic_df = pd.read_csv("data/region_traffic.csv")

local_authority_traffic_profile = ProfileReport(local_authority_traffic_df, title="Local Authority Analysis")
local_authority_traffic_profile.to_file("LAA_report.html")

region_traffic_profile = ProfileReport(region_traffic_df, title="Regional Traffic Analysis")
region_traffic_profile.to_file("RTA_report.html")