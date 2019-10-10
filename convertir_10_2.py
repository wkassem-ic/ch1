x=int(input("Saisir un entier positif decimal:"))
n=""
if x==0:
  print("0")
else:
  while x>0:
    if x%16==0:
      n="0"+n
    elif x%16==1:
      n="1"+n
    elif x%16==2:
      n="2"+n
    elif x%16==3:
      n="3"+n
    elif x%16==4:
      n="4"+n
    elif x%16==5:
      n="5"+n
    elif x%16==6:
      n="6"+n
    elif x%16==7:
      n="7"+n
    elif x%16==8:
      n="8"+n
    elif x%16==9:
      n="9"+n
    elif x%16==10:
      n="A"+n
    elif x%16==11:
      n="B"+n
    elif x%16==12:
      n="C"+n
    elif x%16==13:
      n="D"+n
    elif x%16==14:
      n="E"+n
    else:
      n="F"+n
    x=x//16
  print(n)
