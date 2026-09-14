import rclpy	
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from .NatNetClient import NatNetClient

class RigidbodyNode(Node):
	def __init__(self):
		super().__init__('rigidbody_node')
		self.publisher1 = self.create_publisher(PoseStamped, 'optitrack_pose_1',10)
		self.publisher2 = self.create_publisher(PoseStamped, 'optitrack_pose_2',10)
		self.publisher3 = self.create_publisher(PoseStamped, 'optitrack_pose_3',10)
		self.publisher4 = self.create_publisher(PoseStamped, 'optitrack_pose_4',10)
		self.publisher5 = self.create_publisher(PoseStamped, 'optitrack_pose_5',10)
		self.publisher6 = self.create_publisher(PoseStamped, 'optitrack_pose_6',10)
		self.publisher7 = self.create_publisher(PoseStamped, 'optitrack_pose_7',10)
		self.publisher8 = self.create_publisher(PoseStamped, 'optitrack_pose_traverse',10)

		self.client = NatNetClient()
		self.client_address="192.168.0.50"
		self.server_address="192.168.0.60"
		self.client.set_client_address(self.client_address)
		self.client.set_server_address(self.server_address)
		self.client.set_use_multicast(True)
		self.client.local_ip_address = "192.168.0.50"
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

		if new_id==1:		
			self.publisher1.publish(msg)
		if new_id==2:		
			self.publisher2.publish(msg)
		if new_id==3:		
			self.publisher3.publish(msg)
		if new_id==4:		
			self.publisher4.publish(msg)
		if new_id==5:		
			self.publisher5.publish(msg)
		if new_id==6:		
			self.publisher6.publish(msg)
		if new_id==7:		
			self.publisher7.publish(msg)
		if new_id==8:		
			self.publisher8.publish(msg)


def main():
	rclpy.init()
	node = RigidbodyNode()
	
	rclpy.spin(node)
	
	rclpy.shutdown()

		
if __name__ == '__main__':
		main()