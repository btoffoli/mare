from mare_db import MareService

mareService = MareService()

client = mareService.insertClient('Client Test1', 'CL1')

print(client)