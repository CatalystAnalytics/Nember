import asyncio
import websockets
import json

async def connect():
    uri = "wss://api.nember.catalystanalytics.io/ws"
    connected = False
    async with websockets.connect(uri) as websocket:
        while True:
            if not connected:
                await websocket.send("9UotHduv4d519oPI6H2wWw")
            else:
                data = {
                    "api_key": "YOUR_API_KEY",
                    "strat_name": "example_strategy",
                    "model_name": "DecisionTree",
                    "model_type": "class",
                    "DataPoints": [
                        { "point1": 3, "point2": 2 },
                        { "point1": 1, "point2": 3 }
                    ]
                }
                await websocket.send(json.dumps(data))

            response = await websocket.recv()
            response_data = json.loads(response)

            if "message" in response_data and response_data["message"] == "valid" and not connected:
                connected = True
            elif connected:
                if response_data["type"] == "success":
                    print(response_data["prediction"])
                elif response_data["type"] == "error":
                    print(response_data["message"])
            else: 
                print("API key verification failed.")
                
            await asyncio.sleep(1)

# Run the event loop
asyncio.get_event_loop().run_until_complete(connect())