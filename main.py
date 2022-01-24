tekst = input("Ievadi Tekstu: ")
def Replace(tekst):
  if tekst.count("o")>0 or tekst.count("O")>0:
   tekst = tekst.replace("o", "%")
   tekst = tekst.replace("O", "%")
   print(tekst)
  else:
   tekst - "Nekas Netika Aizvietots!"
   print(tekst)
Replace(tekst)