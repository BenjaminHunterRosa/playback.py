play = input("slow down: ")
back = []
if " " in play:
   back = play.split(" ")
   elipse = []
   for i in range(len(back)):
       elipse.append(back[i])
       elipse.append("..." + " "*i)
       _ = i
   elipse.remove("..."+" "*i)
for i in range(len(elipse)):
      print(elipse[i].strip(), end = " ")
