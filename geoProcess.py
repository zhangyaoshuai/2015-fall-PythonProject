import json

# Tweets are stored in "fname"
with open('football.json', 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['coordinates']:
        
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)
print(len(geo_data['features']))
# Save geo data
with open('geo_data_football.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))
fout.close()

