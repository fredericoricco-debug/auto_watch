# standard imports
import json

from qbittorrent import Client

# Function that opens a json based on a path and returns the structure as a dictionary
def open_json(path):
    with open(path, 'r') as file:
        return json.load(file)
    

# Function that creates client, logs in and returns the client
def create_client(config):
    # Port
    port = config["qbittorrent"]["port"]
    # Create the client
    client = Client(f'http://localhost:{port}/')
    # Login
    client.login(config["qbittorrent"]["username"], config["qbittorrent"]["password"])
    return client

if __name__ == "__main__":
    # Get the config
    config = open_json("config.json")
    # Create the client
    client = create_client(config)
    
