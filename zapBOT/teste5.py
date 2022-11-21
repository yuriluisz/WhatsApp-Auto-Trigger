import pywhatkit as kit

msgs = open("zapBOT/numeros.txt")
numeros = msgs.readlines()
print(numeros)

for pau in numeros:
    kit.sendwhatmsg_instantly(f"{pau}", "oi")
    