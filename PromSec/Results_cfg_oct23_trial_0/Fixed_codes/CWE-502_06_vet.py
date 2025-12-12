import base64

def parse_sensor_data(sensor_data):
    try:
        decoded_data = base64.b64decode(sensor_data)
        temperature = int.from_bytes(decoded_data[0:2], byteorder='big')
        humidity = int.from_bytes(decoded_data[2:4], byteorder='big')
        pressure = int.from_bytes(decoded_data[4:6], byteorder='big')
        return {'temperature': temperature, 'humidity': humidity, 'pressure': pressure}
    except:
        return "Invalid sensor data format"