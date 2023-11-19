import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.sendto('["","746071015097","set",{"hw_temp_set":20,"seq":3,"p_w":"69689050","version":1}]'.encode("utf-8"), ("192.168.2.206", 60002))

    udp_socket.close()


if __name__ == "__main__":
    main()