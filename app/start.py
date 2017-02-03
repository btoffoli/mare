from mare_db import MareService

mareService = MareService()

# client = mareService.insert_client(name="LALA1", identify="lala2")

client = mareService.insert("Client", name="LALA1", identify="lala2")



