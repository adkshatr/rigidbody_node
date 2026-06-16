#import DataDescriptions
#import MoCapData
from NatNetClient import NatNetClient

def rigid_body_callback(new_id, position, rotation):
    print("RIGID BODY:", new_id, position)

def new_frame_callback(data):
    print("FRAME RECEIVED")

if __name__ == "__main__":
    client = NatNetClient()

    
    client.set_client_address("192.168.0.70") # your machine
    client.set_server_address("192.168.0.80") # Motive machine
    client.set_use_multicast(True)

    # Extra safety (VERY IMPORTANT)
    client.local_ip_address = "192.168.0.70"

    # Callbacks
    client.rigid_body_listener = rigid_body_callback
    client.new_frame_listener = new_frame_callback

    print("Starting NatNet client...")

    client.run(0)

    print("Client started. Waiting for data...")

    # Keep alive
    import time
    while True:
        time.sleep(1)