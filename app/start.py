from mare_db import MareService

mareService = MareService()

client = mareService.insert_client('Client Test1', 'CL1')

print(client)