from icmplib import *
import time

host = input('Check Connectivity with host (IPAddress)\n> ')
pckts = 5
print('Keep Patients\nICMP packets sending... ')
sending_packets = ping(host, pckts, interval=1, timeout=2)

##The IP address of the gateway or host that responded to the request:
ip = sending_packets.address

##Reachable Host or Not:
reach = sending_packets.is_alive

##The number of packets transmitted to the destination host:
packets = sending_packets.packets_sent

##The number of packets sent by the remote host and received by the current host:
received_packets = sending_packets.packets_received

##Packet loss occurs when packets fail to reach their destination:
loss_packets = sending_packets.packet_loss

##The minimum round-trip time:
min_rtt = sending_packets.min_rtt

##The maximum round-trip time:
max_rtt = sending_packets.max_rtt

##The average round-trip time:
avg_rtt = sending_packets.avg_rtt
n = 1
if reach:
    time.sleep(0.5)
    print()
    while n <=5:
        time.sleep(0.5)
        print(f'Reply from {ip}: bytes=32 time= {min_rtt} TTL=128')
        n +=1
    print(f'\nPing statistics for {ip}:\n  Packets: Sent = {packets}, Received = {received_packets}, Lost = {int(loss_packets)}')
    print(f'Approximate round trip times in seconds:\n  Minimum = {min_rtt}s, Maximum = {max_rtt}s, Average = {avg_rtt}s')
else:
    print()
    while n <= 5:
        time.sleep(0.5)
        print(f'Request time out.')
        n += 1
##        break
    print(f'\nPing statistics for {ip}:\n  Packets: Sent = {packets}, Received = {received_packets}, Lost = {int(loss_packets)}')
    print(f'Approximate round trip times in seconds:\n  Minimum = {min_rtt}s, Maximum = {max_rtt}s, Average = {avg_rtt}s')
