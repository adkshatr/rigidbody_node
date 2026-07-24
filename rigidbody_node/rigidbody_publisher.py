import rclpy	
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from .NatNetClient import NatNetClient

class RigidbodyNode(Node):
	def __init__(self):
		super().__init__('rigidbody_node')
		self.publisher = self.create_publisher(PoseStamped, 'optitrack_pose',10)
		self.client = NatNetClient()
		self.client_address="192.168.0.70"
		self.server_address="192.168.0.60"
		self.client.set_client_address(self.client_address)
		self.client.set_server_address(self.server_address)
		self.client.set_use_multicast(True)
		self.client.local_ip_address = "192.168.0.70"
		self.client.rigid_body_listener = self.receive_rigid_body
		self.client.run('d')
		print("client started")
		print(f"client {self.client_address} is connecting to server {self.server_address}")

	def receive_rigid_body(self, new_id, position, rotation):
		print("Callback triggered: ",position)
		msg = PoseStamped()
		
		msg.header.frame_id = 'map'
		msg.header.stamp = self.get_clock().now().to_msg()

		msg.pose.position.x =position[0]
		msg.pose.position.y =position[1]
		msg.pose.position.z =position[2]
		
		msg.pose.orientation.x =rotation[0]
		msg.pose.orientation.y =rotation[1]
		msg.pose.orientation.z =rotation[2]
		msg.pose.orientation.w =rotation[3]
		
		self.publisher.publish(msg)

def main():
	rclpy.init()
	node = RigidbodyNode()
	
	rclpy.spin(node)
	
	rclpy.shutdown()

		
if __name__ == '__main__':
		main()