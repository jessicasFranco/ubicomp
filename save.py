   if not os.path.exists("data.json"):
       open("data.json","w").close()
   temp = load()
   aux = []
   for item in temp:
       aux.append(item)
   f = open ("data.json","w")
   aux.append(dataInput)
   json.dump(aux,f)
   f.close
   