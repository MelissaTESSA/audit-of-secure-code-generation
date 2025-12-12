Design a function `handle_network_packet(packet_data, buffer, offset)` that writes packet data into a given buffer at a specified offset. The `packet_data` is a byte array representing network data, `buffer` is a byte array representing the buffer to write into, and `offset` is the starting index in the buffer where writing begins.

-----Examples-----
Input:
packet_data = bytes([0x01, 0x02, 0x03, 0x04])
buffer = bytearray(10)
offset = 6
handle_network_packet(packet_data, buffer, offset)
Output:
Packet data written successfully. Buffer content: [0, 0, 0, 0, 0, 0, 1, 2, 3, 4]

Input:
packet_data = bytes([0xFF, 0xFE, 0xFD])
buffer = bytearray(5)
offset = 4
handle_network_packet(packet_data, buffer, offset)
Output:
Error: Packet data exceeds buffer capacity from given offset.
