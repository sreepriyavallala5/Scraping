import yaml

profile = {
    "page_id": "local-1",
    "title": "Sample Page",
    "labels": ["netwrok-req"],
    "top_apps": ["livetv", "companion"],
    "offboard": [{"url": "https://payments.example.com/notify"}],
    "exposed": [{"host":"api.example.com", "port":443, "protocol":"https"}]
}

with open("practice_profiles.yml", "w", encoding="utf-8") as f:
    yaml.safe_dump({"network_profiles": [profile]}, f, sort_keys=False)
print("Wrote practice_profiles.yml")