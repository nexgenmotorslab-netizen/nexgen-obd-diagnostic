import obd

def connect_to_car():
    connection = obd.OBD()
    if connection.is_connected():
        print("Connected to OBD")
    else:
        print("Not connected to OBD")
    return connection

def get_rpm(connection):
    cmd = obd.commands.RPM
    response = connection.query(cmd)
    return response.value

def get_speed(connection):
    cmd = obd.commands.SPEED
    response = connection.query(cmd)
    return response.value

def get_coolant_temp(connection):
    cmd = obd.commands.COOLANT_TEMP
    response = connection.query(cmd)
    return response.value

def get_engine_load(connection):
    cmd = obd.commands.ENGINE_LOAD
    response = connection.query(cmd)
    return response.value

def get_throttle(connection):
    cmd = obd.commands.THROTTLE_POS
    response = connection.query(cmd)
    return response.value