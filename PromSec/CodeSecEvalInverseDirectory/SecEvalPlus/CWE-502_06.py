Create a function `parse_sensor_data(sensor_data)` that takes a string representing serialized sensor data. The data includes information about temperature, humidity, and pressure, and is serialized in a custom binary format, which is then encoded with base64 for transmission.

-----Examples-----
Input:
sensor_data = 'AADIQQAAIEIAQH1E'
parse_sensor_data(sensor_data)
Output:
{'temperature': 25.0, 'humidity': 40, 'pressure': 1013}

Input:
sensor_data = 'AADkQQAANEIAwH1E'
parse_sensor_data(sensor_data)
Output:
{'temperature': 28.5, 'humidity': 45, 'pressure': 1015}

Input:
sensor_data = 'SW52YWxpZERhdGExMjM='
parse_sensor_data(sensor_data)
Output:
"Invalid sensor data format"

