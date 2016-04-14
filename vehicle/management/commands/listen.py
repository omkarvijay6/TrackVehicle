from twisted.internet import protocol, reactor, endpoints
from vehicle.services import update_vehicle_location


class Echo(protocol.Protocol):
    """
    socket server listener using twisted on 9000 port to accept incoming packets
    from the gps tracker
    """
    def dataReceived(self, data):
        """
        It is called when the gps tracker device sends current location via tcp/ip
        updates the current location of the vehicle to the database each time when the
        gps tracker updates the location
        """
        location_data = dict(item.split("=") for item in data.split(";"))
        update_vehicle_location(location_data)
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


print "socket server listening on 9000 port"
endpoints.serverFromString(reactor, "tcp:9000").listen(EchoFactory())
reactor.run()