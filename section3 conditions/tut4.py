device_status = "active"
temprature = 38


if device_status  == "active":
    if temprature > 35:
        print("High temprature  alert!")
    else:
        print("temprature is normal")
else:
    print("device is offline")