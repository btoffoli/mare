from mare_db import MareService

mareService = MareService()

# client = mareService.insert_client(name="LALA1", identify="lala2")

# client = mareService.insert("Client", name="LALA1", identify="lala2")

# print(client)

print(mareService.get_by_id('Client', 1))

clients = mareService.list("Client", name="LALA1")

print(clients)

