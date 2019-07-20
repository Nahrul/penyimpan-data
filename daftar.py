import getpass
import time

def tambah():
	file = open('data.txt','a')
	id = input("id/email: ")
	pwd = getpass.getpass("password: ")
	file_baru = ("\nemail: "+ id +"[✓]" + "\npass: " + pwd +"[✓]" + "\n\n")
#	file2=
	file.write(file_baru)
	
	file.close()
	print("sedang menyimpan...")
	time.sleep(0.5)
	print("data tersimpan.")
	pilih = input("tambah lagi? (y/n) ")
	if pilih == "y":
		tambah()
	else:
		print("sampai ketemu lagi :)")
		exit
	

print("===== SCRIPT PENYIMPAN DATA =====")
print("#Nahrul")
print("")
print("")
print("masukin akun nya :\n")
		
tambah()