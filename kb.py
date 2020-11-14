import vk_api
from time import sleep

intro="""
 m    m          m           mmmmm
 #  m"   mmm   mm#mm   mmm   #    #  mmm   m mm
 #m#    #" "#    #    "   #  #mmmm" "   #  #"  #
 #  #m  #   #    #    m" "#  #    # m" "#  #   #
 #   "m "#m#"    "mm  "mm"#  #mmmm" "mm"#  #   #
 
 Утилита для рейда by kotan
 удаляем всех подписчиков чата по скрипту
"""

print(intro)
tok = input('[TOKEN] : ')
token = vk_api.VkApi(token = tok)
vk = token.get_api()
mess = vk.messages.getConversations(countoffset=0)['items']
for i in mess:
	try:
		type = i['conversation']['peer']['type']
		if type == "chat":
			print("======chat=======")
			t = i['conversation']['chat_settings']['title']
			id = i['conversation']['peer']['local_id']
			print("\033[32m[NAME] : " + t + "\n[CHAT_ID] : " + str(id) + "\033[0m")
	except Exception as er:
		print(er)	
iid = int(input('\n[CHAT_ID] : '))
print('\nВведите ваш цифровой айди, это нужно для того что бы скрипт не забанил вас в чате')
myid = int(input('[ID] : '))
info = vk.messages.getChat(chat_id=iid)['users']       
for ii in info:
    try:
        if ii == myid:
            continue
        vk.messages.removeChatUser(chat_id=iid, user_id=ii)
        print("Успешно удаленно!")
    except:
        print('Не удалось удалить юзера!')
