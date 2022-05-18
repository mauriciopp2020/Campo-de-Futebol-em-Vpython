from vpython import *
#Web VPython 3.2
campo = box(pos=vec(0,0,0) , size=vec(25,0.2,15),color = color.green,opacity=1)

designer = box(pos=vec(-7.8,0.2,0.02),size=vec(2,0.05,8.1),color = color.green,opacity=0.3)
designer = box(pos=vec(-3.8,0.22,0.02),size=vec(2,0.05,8.1),color = color.green,opacity=0.3)
designer = box(pos=vec(-0,0.22,0.02),size=vec(2,0.05,8.1),color = color.green,opacity=0.3)
designer = box(pos=vec(3.8,0.22,0.02),size=vec(2,0.05,8.1),color = color.green,opacity=0.3)
designer = box(pos=vec(7.7,0.22,0.02),size=vec(2,0.05,8.1),color = color.green,opacity=0.3)

linha_cima = box(pos=vec(0,0.09,-4.2) , size=vec(18,0.07,0.2))
linha_baixo = box(pos=vec(0,0.09,4.2) , size=vec(18,0.07,0.2))

linha_ladoE = box(pos=vec(-8.9,0.09,0) , size=vec(0.2,0.1,8.5))
linha_ladoD = box(pos=vec(8.9,0.09,0) , size=vec(0.2,0.1,8.5))

linha_centro = box(pos=vec(0,0.09,0) , size=vec(0.2,0.1,8.5))

traveE = box(pos=vec(-8.9,0.7,1.4) , size=vec(0.1,1.1,0.1))
traveE = box(pos=vec(-8.9,0.7,-0.9) , size=vec(0.1,1.1,0.1))
travessaE = box(pos=vec(-8.9,1.20,0.25) , size=vec(0.1,0.1,2.4))

traveD = box(pos=vec(8.9,0.7,1.4) , size=vec(0.1,1.1,0.1))
traveD = box(pos=vec(8.9,0.7,-0.9) , size=vec(0.1,1.1,0.1))
travessaD = box(pos=vec(8.9,1.20,0.25) , size=vec(0.1,0.1,2.4))

circiloCentral=ring(pos=vector(0,0.06,0.2),axis=vector(0,1,0),radius=1.9, thickness=0.07,color=color.white,opacity=1)

#======================================================================================================================


arquibancadanorte = box(pos=vec(0,2.9,-7.6) , size=vec(25,6,0.2))
arquibancadaleste = box(pos=vec(-12.6,2.9,-0.1) , size=vec(0.2,6,15))
arquibancadaoeste = box(pos=vec(12.6,2.9,-0.1) , size=vec(0.2,6,15))