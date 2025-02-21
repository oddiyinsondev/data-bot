import requests
from data import KantakOqish2,Videooqish,SMMoqish,Moboqish,Bugolteroqish,UserCheckadd,userscheck
import time 

url = "https://sheetdb.io/api/v1/wa33txehgmlyx"

def QoshishSheets():
    while True:
        for i in KantakOqish2():
            video = True if Videooqish(i[0]) else False
            ssm   = True if SMMoqish(i[0]) else False
            mob   = True if Moboqish(i[0]) else False
            bug   = True if Bugolteroqish(i[0]) else False

            data = {
                "telegram id": i[0],
                "username": i[1],
                "Ism Familya": i[2],
                "Telefon nomer": i[3],
                "SMM": ssm,
                "Mobilografiya": mob,
                "Buxgalteriya": bug,
                "Video": video
            }
            if userscheck(i[0]):
                continue
            else:
                UserCheckadd(i[0])
                response = requests.post(url, json=data)
        time.sleep(86400)
