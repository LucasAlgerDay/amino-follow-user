import aminofix
from os import path
import json
from time import sleep
from pyfiglet import figlet_format
from colored import fore, style

print(
    f"""{fore.CADET_BLUE_1 + style.BOLD}
    Follow accounts.json
Script by Lucas Day
Github : https://github.com/LucasAlgerDay"""
)
print(figlet_format("Follow with accounts.json", font="fourtops"))



THIS_FOLDER=path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,'accounts.json')
dictlist=[]
chatlink = input("User link: ")
cooldown = int(input("Cooldown for account: "))
print("1.- Global \n2.- Community")
selection = int(input("Option: "))

cliente = aminofix.Client()

user_info = cliente.get_from_code(chatlink)
community_id = user_info.path[1:user_info.path.index('/')]

with open(emailfile)as f:dictlist=json.load(f)


print(f"{len(dictlist)} accounts loadeds")

for acc in dictlist:
    email = acc['email']
    password =  acc['password']
    device = acc['device']
    client = aminofix.Client(deviceId = device)
    try:
        client.login(email=email, password=password)
        user_id = user_info.objectId
        if selection == 1:
            client.follow(user_id)
            print(f"{email} Followed the user {user_id}, waitting {cooldown} seconds for the next account")
            sleep(cooldown)
        elif selection == 2:
            community_id = user_info.path[1:user_info.path.index('/')]
            client.join_community(community_id)
            sub_client = aminofix.SubClient(comId=community_id, profile=client.profile)
            sub_client.follow(user_id)
            print(f"{email} Followed the user {user_id}, waitting {cooldown} seconds for the next account")
            sleep(cooldown)
    except Exception as e:
        print(f"Error en la siguiente cuenta {email}: {e} \n\n\n Esperando {cooldown} para la siguiente cuenta.")
        sleep(cooldown)
        pass
