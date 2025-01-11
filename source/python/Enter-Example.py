import requests

url = "https://api.nember.catalystanalytics.io/entry/enter-data"
headers = {"api_key": "YOUR_API_KEY"}
data = {
    "data": [
        {
            "StratName": "example_strategy",
            "Open": True,
            "EnterValue": 1.25,
            "ExitValue": 1.35,
            "EntryTime": 1629187200,
            "ExitTime": 1629190800,
            "Target": 1.40,
            "StopLoss": 1.20,
            "Outcome": 1,
            "Position": "Long",
            "DataPoints": [
                {"point1": 1.0, "point2": 2.5}, 
                {"point1": 2.0, "point2": 3.0}
            ]
        },
        {
            "StratName": "example_strategy",
            "Open": True,
            "EnterValue": 1.25,
            "ExitValue": 1.35,
            "EntryTime": 1629187200,
            "ExitTime": 1629190800,
            "Target": 1.40,
            "StopLoss": 1.20,
            "Outcome": 0,
            "Position": "Long",
            "DataPoints": [
                {"point1": 1.0, "point2": 2.5}, 
                {"point1": 2.0, "point2": 3.0}
            ]
        }
    ]
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
