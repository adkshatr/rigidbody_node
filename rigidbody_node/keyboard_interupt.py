import sys
import termios
import tty
import time
import rclpy
def keyboard_listener(node):
    print("Press 'q' to stop node")

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)

        while True:
            ch = sys.stdin.read(1) # read 1 character
            if ch == 'q':
                print("\nStopping node...")

                node.client.stop_threads = True
                time.sleep(0.5)
                print('noe stopped')

                try:
                    node.client.data_socket.close()
                    node.client.command_socket.close()
                except:
                    pass

                #node.destroy_node()
                rclpy.shutdown()

                break

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)