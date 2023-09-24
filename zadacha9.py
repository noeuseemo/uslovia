rangeshoot = float(input('введите дальность выстрела - '))
if rangeshoot >28 and rangeshoot <30:
    
    print ('попал прям в цель')

elif rangeshoot >=30:
    
    print ('перелетело')

elif rangeshoot >0 and rangeshoot <=28:
    
    print ('недолёт!')

elif rangeshoot >=0:
    
    print ('не бей по своим !!')