#! /usr/bin/env python3.2
# -*- coding: utf-8 -*-

#описание: скрипт удаляет "лайкнутые" фотографии из "моё избранное" Вконтакта.


from urllib.request import urlopen
import json
import pprint
import time
import os
import os

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

touch('vk.txt')

#получаем список лайкнутых фоток в виде json
api_key='https://api.vk.com/method/fave.getPhotos?'
api_token='access_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
api_owner_id='owner_id=PUT_YOUR_APP_ID_HERE'
api_count='count=9999'
address = api_key+'&'+api_owner_id+'&'+api_count+'&'+api_token+'&v=5.21'

#достаём из массива json массив с 'items'
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

#кладем в массивы id и owner_id значения айдишников для удаления
for song in songs:
	id.append(song['id'])
	owner_id.append(song['owner_id'])
	iii+=1
	

#формируем запрос к API для удаления всех собранных айдишников	
api_key='https://api.vk.com/method/likes.delete?type=photo'	
#получили массив айдишников фото и юзеров, удоляем всё
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
	time.sleep(3)
	if kkk>12:
		kkk=0
		time.sleep(30) 
	if mmm>45:
		mmm=0
		time.sleep(600)
		
		
print('Finished!') 


