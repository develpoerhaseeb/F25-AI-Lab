 #Lab 01 

def symbolic(score, complete):
    return "Review "          if complete and score >= 70 else   " Hold"

def threshold(probability):
    return     "Review"         if probability >= 0.70 else"Hold"

cases = [
    ("complete_high" , 82 , True , 0.81) ,
    ("complete_low" , 68 , True ,   0.74) ,
    ("incomplete_high" , 91 , False , 0.88) ,
    ("boundary" , 70 , True , 0.70) ,

]

print("case  |  symbolic  |  threshold  |  disagreement " )

for name, score, complete, probability in cases:
    a ,b = symbolic  (score, complete),threshold   (probability)
    print ( name ,  a,b ,a  != b ,sep= "  |  ")