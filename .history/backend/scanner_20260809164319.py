import obd


def connect_to_car():
    print("Connecting to OBD2 adapter...")
    connection = obd.OBD()

    if connection.is_connected():
        print("✅ Connected to Car!")
    else:
        print("❌ Not Connected, Check Adapter")
    return connection


def get_rpm(conn):
    cmd = getattr(obd.commands, "RPM")
    response = conn.query(cmd)
    return response.value

def get_coolant_temp(connection):
    cmd = obd.commands.COOLANT_TEMP  # type: ignore
    response = connection.query(cmd)
    return response.value

def get_engine_load(connection):
    cmd = obd.commands.ENGINE_LOAD  # type: ignore
    response = connection.query(cmd)
    return response.value

def get_throttle(connection):
    cmd = obd.commands.THROTTLE_POS  # type: ignore
    response = connection.query(cmd)
    return response.value


def get_dtc_codes(connection):
    cmd = obd.commands,GET_DTC  #type: ignore
    reponse = connection.query(cmd)
    return

if __name__ == "__main__":
    conn = connect_to_car()
    print("RPM:", get_rpm(conn))
