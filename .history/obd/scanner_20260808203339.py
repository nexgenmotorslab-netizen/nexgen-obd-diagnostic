from multiprocessing import Value

import obd
def connect_to_car():
    print("Connecting to OBD2 adapter...")
    connection = obd.OBD()

    if connection.is_connected():
        print("✅ Connected to Car!")

    else:
        print("❌ Not Connected, Check Adapter")
    return connection

def get_rpm(conn)
    cmd = obd.commands.RPM
    reponse = conn.query(cmd)
    return response.value

if ___name___ == "___main___":
    conn = connect_to_car()
    print("RPM:")

