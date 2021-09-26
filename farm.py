try: import samino, os
except:
	import os
	os.system("pip install samino && clear")
	import samino

import time

def start():
	os.system("clear")
	print("""1 >> мои почты.
2 >> добавить почту.
3 >> удалить почту.
4 >> фарм.
5 >> выход.\n""")

	try:
		answ = int(input(">> "))
		os.system("clear")
		return answ
		
	except: start()
	
while True:
	answ = start()
	
	if answ == 1:
		for email in open("emails.txt", "r").read().split(): print(email)

	if answ == 2:
		try: open("emails.txt", "a").write(input("Введите почту >> ") + "\n")
		
		except:
			open("emails.txt", "w").write(input("Введите почту >> ") + "\n")
			
	elif answ == 3:
		del_mail = input("Введите почту >> ")
		return_mails = ""
		d = False
		
		for email in open("emails.txt", "r").read().split():
			if email != del_mail: return_mails += email + "\n"
			
			else: d = True
			
		open("emails.txt", "w").write(return_mails)
		
		if d == True: print("Почта удалена.")
		
		else: print("Ошибка поиска.")
		
	elif answ == 4:
		try:
			r = int(open("now.txt", "r").read())
			if int(time.time()) - r <= 84000:
				print("Бот еще не готов. Вы уверены?\n1 >> Да.\n2 >> Нет.\n")
			
				res = input(">> ")
				
				if res == "1":
					os.system("clear")
					break
				
			else: break
		
		except: break
		
	elif answ == 5: exit()
	
	input("\nПродолжить >> ")

from samino import Client

client = samino.Client("22E50672BDFC6C814592C4EC98A173597A8CCEE712E8A1573869B272A15DAF781E1282CC7EE2E010C8")

pswd = input("Password: ")
x = 1
result = 0
for email in open("emails.txt").read().split():
	client.login(email,pswd)
	old_coins = client.get_wallet_info().coins
	print(f"{x}. {email}: 0%.   ")
	for _ in range(25):
		client.watch_ad()
		print(f"\033[1A{x}. {email}: {int(((_ + 1) / 25) * 100)}%.")
	coins = client.get_wallet_info().coins
	print(f"\033[1A{x}. {email}: {int(old_coins)} >> {int(coins)}.")
	
	result += int(coins) - int(old_coins)
	x += 1
	
print(f"\nВсего собрано: {result}.")

open("now.txt", "w").write(str(int(time.time())))

input("\nПродолжить >> ")
import farm
