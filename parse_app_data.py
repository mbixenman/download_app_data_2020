import json
import pandas as pd

f = open("app_ranking_list.json","r")

soup = json.load(f) #making our soup with the json parser in python package titled json


f.close()

df = pd.DataFrame()

for i in soup:
	for j in i:
		df = df.append(j, ignore_index=True)

df.to_csv('results.csv')

# old program method: not as good, since we break up the json list into values and then save values in a list...
# so, why not just save the whole json list???

# 	for j in i:
# 		df = df.append({
# 				'app_id': j['app_id'],
# 				'name': j['name'],
# 				'os': j['os']
# 			}, ignore_index=True)

# print(df)
		
