import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from shifr import Caesar

token = 'de6352a6b02fbe79556b0f13e82e54d800958d1a97e2\
5d66b77bff2fbb5695750c0fab87d86057f2e45f8'
group_id = '200909407'
session = vk_api.VkApi(token=token)
vk = session.get_api()
longpoll = VkBotLongPoll(session, group_id)
f = 0
sh = False
caesar = Caesar()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if (event.message.text.lower() == 'caesar' or event.message.text.lower() == 'цезарь') and f == 0:
            f += 1
            vk.messages.send(
                message='Принято. Теперь введи Зашифровать/Расшифровать (текст) без скобок',
                peer_id=event.message.from_id,
                random_id=get_random_id()
            )
        elif f == 1 and (event.message.text.split()[0].lower() == 'зашифровать' or event.message.text.split()[0].lower() == 'расшифровать') and len(event.message.text.split()) > 1:
            text = event.message.text[event.message.text.index(' ') + 1:]
            f += 1
            if event.message.text.split()[0].lower() == 'расшифровать':
                sh = True
            vk.messages.send(
                message='Принято. Теперь введи сдвиг (число)',
                peer_id=event.message.from_id,
                random_id=get_random_id()
            )
        elif event.message.text.isdigit() and f == 2:
            if sh:
                f = 0
                vk.messages.send(
                    message=caesar.Decrypt(text, event.message.text),
                    peer_id=event.message.from_id,
                    random_id=get_random_id()
                )
            else:
                f = 0
                vk.messages.send(
                    message=caesar.Encrypt(text, event.message.text),
                    peer_id=event.message.from_id,
                    random_id=get_random_id()
                )
        else:
            vk.messages.send(
                message='Привет! Сначала введи тип шифровки (Цезарь/Caesar)',
                peer_id=event.message.from_id,
                random_id=get_random_id()
            )
