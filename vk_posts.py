#! /usr/bin/env python3.2
# -*- coding: utf-8 -*-


#описание: скрипт удаляет "лайкнутые" фотографии из "моё избранное" Вконтакта.
#алгоритм действий: идём на https://vk.com/apps?act=manage и создаем свое пустое приложение (stand-alone)
#открываем его настройки, копируем сервисный ключ доступа и ID приложения в скрипт (acess_token=   owner_id=)
#даем своему приложению права на работу со своей стеной (открываем ссылку ниже, заменив PUT_YOUR_APP_ID_HERE на ID своего приложения):
#https://oauth.vk.com/authorize?client_id=PUT_YOUR_APP_ID_HERE&scope=friends+wall,offline&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.21&response_type=token
#ставим Python 3 (если еще нет), запускаем скрипты, смотрим результат.
#каждый скрипт удаляет примерно 20 записей за раз, после чего VK требует ввод капчи. Можно добавить скрипт в планировщик, чтобы он вызывался, к примеру, каждый час.



from urllib.request import urlopen
import json
import pprint
import time
import os


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

touch('vm.txt')


#получаем список лайкнутых фоток в виде json
api_key='https://api.vk.com/method/fave.getPosts?'
api_token='access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api_owner_id='owner_id=PUT_YOUR_APP_ID_HERE'
api_count='count=9999'
address = api_key+'&'+api_owner_id+'&'+api_count+'&'+api_token+'&v=5.21'

#достаЄм из массива json массив с 'items'
data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)

try:
	songs = final_data['response']['items']
except:
	print('error. answer was:') 
	print(final_data) 
	quit() # quit at this point
	
photos= {}
id=[]
owner_id=[]
iii=0

#кладем в массивы id и owner_id значени¤ айдишников дл¤ удалени¤
for song in songs:
	id.append(song['id'])
	owner_id.append(song['owner_id'])
	iii+=1
	

#формируем запрос к API дл¤ удалени¤ всех собранных айдишников	
api_key='https://api.vk.com/method/likes.delete?type=post'	
#получили массив айдишников фото и юзеров, удол¤ем всЄ
iii=0
kkk=0
mmm=0

for photo in id:
	api_item_id='item_id={}'.format(id[iii])
	api_owner_id='owner_id={}'.format(owner_id[iii])
	
	address = api_key+'&'+api_owner_id+'&'+api_item_id+'&'+api_token+'&v=5.21'
	
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	try:
		likes = final_data['response']['likes']
		#print(likes)
		print('like ID={} deleted...'.format(id[iii]))
	except:
		print('error deleting like ID={}'.format(id[iii])) 
		print(final_data) 
		quit() # quit at this point
	iii+=1
	kkk+=1
	mmm+=1
	time.sleep(1)
	if kkk>14:
		kkk=0
		time.sleep(60) 
	if mmm>45:
		mmm=0
		#time.sleep(120)
		
		
print('Finished!') 
