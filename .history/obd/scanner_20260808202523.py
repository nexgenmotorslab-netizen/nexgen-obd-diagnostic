import obd
def connect_to_car():
    print("Connecting to OBD2 adapter...")
    connection = obd.OBD()

    if connection.is