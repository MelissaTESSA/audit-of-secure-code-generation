import os

def analyze_packet(packets, packet_index, offset, bytes_to_extract):
    packet = packets[packet_index]
    payload = packet[offset:offset+bytes_to_extract]
    return list(payload)