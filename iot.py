class Device:
    count = 0
    def __init__(self, ip , mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name

        Device.count += 1
        #result = ping the device

        if result:
            self.status = 'active'
        else:
            self.status = 'unknown'

class TV(Device):
    def turn_on(self):
        #connect to self.ip and turn on
        pass
    def tunr_off(self):
        #connect to self.ip and turn off
        pass
class Thermo(Device):
    def get_degree(self):
        #connect to self.ip and read degree and return the result
        return result