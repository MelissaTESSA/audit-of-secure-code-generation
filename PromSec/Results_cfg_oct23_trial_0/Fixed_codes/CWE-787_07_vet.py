import os

def handle_network_packet(packet_data, buffer, offset):
    if offset + len(packet_data) > len(buffer):
        return
    
    for i in range(len(packet_data)):
        buffer[offset + i] = packet_data[i]