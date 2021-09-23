import random as rd

esportes=["futebol", "basquete", "volei"]

for k in esportes:
    tabela=[[0,0],[0,0],[0,0],[0,0],[0,0]]
    
    for i in range(250):
        h=rd.randint(0, 4)
        a=rd.randint(0, 4)
        while a==h:
            a=rd.randint(0, 4)
            
        if h==4:
            p1=rd.randint(0, 80)
            p2=rd.randint(0, 80)
            p3=rd.randint(0, 80)
            ph=p1+p2+p3
        
        else:
            p1=rd.randint(1, 100)
            p2=rd.randint(1, 100)
            p3=rd.randint(1, 100)
            ph=p1+p2+p3
            
        if a==4:
            p1=rd.randint(0, 80)
            p2=rd.randint(0, 80)
            p3=rd.randint(0, 80)
            pa=p1+p2+p3
        
        else:
            p1=rd.randint(1, 100)
            p2=rd.randint(1, 100)
            p3=rd.randint(1, 100)
            pa=p1+p2+p3
            
        if pa>ph:
            tabela[a][1]+=1
            
        if ph>pa:
            tabela[h][1]+=1
            
        tabela[a][0]+=1
        tabela[h][0]+=1
        
    print(k, tabela)
    
    
    
    
    
    
    
    
    
    
    
    

    
    