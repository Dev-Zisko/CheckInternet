import winsound
import subprocess, time

def doping(ip):
  #response = os.system("ping -n 1 "+ip)
  global validacion
  response = subprocess.call(['ping', '-n', '1', ip])
  if response == 0:
    print ("SI HAY INTERNET")
    if validacion == 1:
      winsound.PlaySound('llegoelinternet.wav', winsound.SND_FILENAME)
      validacion = 0
  else:
    print ("NO HAY INTERNET")
    winsound.PlaySound('nohayinternet.wav', winsound.SND_FILENAME)
    validacion = 1

ip = input("Introduce la ip para hacer ping: ")
validacion = 1
while(True):
  doping(ip)
  time.sleep(8)