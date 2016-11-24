import pygame
import random
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
cor = [(75,174,79),(120,84,71),(156,157,157)]

maca = pygame.mixer.Sound('testefinal.ogg')
cobra = pygame.mixer.Sound('gameover.ogg')

#cria uma maçã
def novaMaca(nivel):
    global maca_x
    global maca_y
    global buraco_x
    global buraco_y
    if nivel==1:
        while True:
            maca_x = random.randrange(0,690,10)
            passa = 0
            for i in range(len(snake)):
                if maca_x != snake[i][0]:
                    passa += 1
            if passa == len(snake):
                break         
        while True:
            maca_y = random.randrange(0,490,10)
            passa = 0
            for i in range(len(snake)):
                if maca_y != snake[i][1]:
                    passa += 1
            if passa == len(snake):
                break
    elif nivel ==2 or nivel ==3:
        while True:
            maca_x = random.randrange(10,690,10)
            passa = 0
            for i in range(len(snake)):
                if maca_x != snake[i][0]:
                    passa += 1
            if passa == len(snake):
                break         
        while True:
            maca_y = random.randrange(10,480,10)
            passa = 0
            for i in range(len(snake)):
                if maca_y != snake[i][1]:
                    passa += 1
            if passa == len(snake):
                break
    
    elif nivel == 4:
        while True:
            while True:
                maca_x = random.randrange(10,690,10)
                passa = 0
                for i in range(len(snake)):
                    if maca_x != snake[i][0]:
                        passa += 1
                if passa == len(snake):
                    break         
            while True:
                maca_y = random.randrange(10,480,10)
                passa = 0
                for i in range(len(snake)):
                    if maca_y != snake[i][1]:
                        passa += 1
                if passa == len(snake):
                    break
            if (maca_y == 70 or maca_y == 430)and(maca_x > 130 or (maca_x > 280  and maca_x < 420) or maca_x > 580):
                break
            elif (maca_x == 120 or maca_x == 580)and(maca_y < 70 or (maca_y > 180 and maca_y < 310) or maca_y > 430):
                break
            elif (maca_x == 350 and(maca_y < 120 or maca_y > 380))or(maca_y == 250 and(maca_x < 170 or maca_x >520)):
                break
            else:
                break

fimDeJogo = False
while not fimDeJogo: 
    #cria a cobra inicial
    curva = []
    cobra_x = random.randrange(0,600,10)
    cobra_y = random.randrange(0,490,10)
    cor1 = random.randint(0,2)
    cor2 = random.randint(0,2)
    x = 10
    y = 0
    snake = [[cobra_x,cobra_y,cor[cor1],x,y],[cobra_x-10,cobra_y,cor[cor2],x,y]]
    
    #definindo as variaveis iniciais
    buraco_x = random.randrange(10,680,20)
    buraco_y = random.randrange(10,480,20)
    maca_x = 0
    maca_y = 0
    novaMaca(1)
    fechar = False
    w,a,s,d = 0,0,0,0
    vw, va, vs, vd = False,False,False,False
    velocidade = 200
    nivel = 1

    #fluxo do jogo
    while not fechar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar = True
                fimDeJogo = True
                break
            #adiciona as curvas da cobra a um vetor
            if event.type == pygame.KEYDOWN:
                #só adiciona a curva se não for em sentido oposto ao atual e se a cabeça estiver dentro do campo
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake[0][3]!=10 and snake[0][1]>=0 and snake[0][1]<500:
                    curva.append([snake[0][0],snake[0][1],-10,0])
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake[0][3]!=-10 and snake[0][1]>=0 and snake[0][1]<500:
                    curva.append([snake[0][0],snake[0][1],10,0])
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and snake[0][4]!=10 and snake[0][0]>=0 and snake[0][0]<700:
                    curva.append([snake[0][0],snake[0][1],0,-10])
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake[0][4]!=-10 and snake[0][0]>=0 and snake[0][0]<700:
                    curva.append([snake[0][0],snake[0][1],0,10])

        #remove as curvas quando todo o corpo já o tiver atravessado
        if len(curva)>0:
            i = 0
            while i < len(curva):
                vazio = 0
                for j in range(1,len(snake)):
                    if curva[i][0]!=snake[j][0] and curva[i][1]!=snake[j][1]:
                        vazio += 1
                if vazio >= len(snake)-1:
                    curva.remove([curva[i][0],curva[i][1],curva[i][2],curva[i][3]])
                    if i == 0:
                        break
                else:
                    i += 1

        #atualiza o display
        screen.fill((232,221,203))
        pygame.draw.rect(screen,(249,7,7),[maca_x,maca_y,10,10])
        for k in range(len(snake)):
            for j in range(len(curva)):
                if snake[k][0] == curva[j][0] and snake[k][1] == curva[j][1]:
                    snake[k][3] = curva[j][2]
                    snake[k][4] = curva[j][3]
            snake[k][0] = snake[k][0]+snake[k][3]
            snake[k][1] = snake[k][1]+snake[k][4]
            
            #game over se a cabeça encontrar com o corpo
            if k == len(snake)-1:
                for p in range(1,len(snake)):
                    if snake[0][0]==snake[p][0] and  snake[0][1]==snake[p][1]:
                        fechar = True
                        break
                if fechar:
                    break

            #game over se a cobra escostar na parede
            if nivel == 2 and k==0:
                if (snake[0][0] == 0 or snake[0][0] == 690) and (snake[0][1] < buraco_y or snake[0][1]>=buraco_y+20):
                    fechar = True
                    break
                elif (snake[0][1] == 0 or snake[0][1] == 490) and (snake[0][0] < buraco_x or snake[0][0]>=buraco_x+20):
                    fechar = True
                    break
            elif nivel == 3 and k==0:
                if (snake[0][0] == 0 or snake[0][0] == 690)or(snake[0][1] == 0 or snake[0][1] == 490):
                    fechar = True
                    break
            elif nivel == 4 and k==0:
                if (snake[0][0] == 0 or snake[0][0] == 690)or(snake[0][1] == 0 or snake[0][1] == 490):
                    fechar = True
                    break
                elif (snake[0][1] == 70 or snake[0][1] == 430)and((snake[0][0] >= 130 and snake[0][0] <= 280) or (snake[0][0] >= 420 and snake[0][0] <= 580)):
                    fechar = True
                    break
                elif (snake[0][0] == 120 or snake[0][0] == 580)and((snake[0][1] >= 70 and snake[0][1] <= 180) or (snake[0][1] >= 310 and snake[0][1] <= 430)):
                    fechar = True
                    break
                elif (snake[0][0] == 350 and(snake[0][1] >= 120 and snake[0][1] <= 380))or(snake[0][1] == 250 and(snake[0][0] >= 170 and snake[0][0] <= 520)):
                    fechar = True
                    break   
                    
                
                

                
            pygame.draw.rect(screen,snake[k][2],[snake[k][0],snake[k][1],10,10])        
        if fechar:
            break

        #come maçã
        if snake[0][0]== maca_x and snake[0][1]== maca_y:
            maca.play()
            novaMaca(nivel)
            ultima = len(snake)-1
            c = random.randint(0,2)
            snake.append([snake[ultima][0]+10*-int((snake[ultima][3])/10),snake[ultima][1]+10*-int(snake[ultima][4]/10),cor[c],snake[ultima][3],snake[ultima][4]])
            if len(snake)>14 and velocidade>10:
                velocidade -= 1

        #-----sobe de nível-----
        if len(snake)==17:
            nivel = 2
        elif len(snake)==32:
            nivel = 3
        elif len(snake)==47:
            nivel = 4


        if nivel == 1:        
            #---teletrasporte---
            #direita
            if(snake[0][0] >= 700)or vd:
                if d==len(snake):
                    vd = False
                    d=0
                else:
                    snake[d][0] = -10
                    vd = True
                    d += 1

            #esquerda
            if((snake[0][0] < 0)or va)and vd == False:
                if a==len(snake):
                    va = False
                    a=0
                else:
                    snake[a][0] = 700
                    va = True
                    a += 1
            #pra baixo
            if(snake[0][1] >= 500)or vs:
                if s==len(snake):
                    vs = False
                    s=0
                else:
                    snake[s][1] = -10
                    vs = True
                    s += 1
            #pra cima
            if((snake[0][1] < 0)or vw)and vs == False:
                if w==len(snake):
                    vw = False
                    w=0
                else:
                    snake[w][1] = 500
                    vw = True
                    w += 1
        elif nivel == 2:
            #---teletrasporte---
            #direita
            if(snake[0][0] >= 700)or vd:
                if d==len(snake):
                    vd = False
                    d=0
                else:
                    snake[d][0] = -10
                    vd = True
                    d += 1

            #esquerda
            if((snake[0][0] < 0)or va)and vd == False:
                if a==len(snake):
                    va = False
                    a=0
                else:
                    snake[a][0] = 700
                    va = True
                    a += 1
            #pra baixo
            if(snake[0][1] >= 500)or vs:
                if s==len(snake):
                    vs = False
                    s=0
                else:
                    snake[s][1] = -10
                    vs = True
                    s += 1
            #pra cima
            if((snake[0][1] < 0)or vw)and vs == False:
                if w==len(snake):
                    vw = False
                    w=0
                else:
                    snake[w][1] = 500
                    vw = True
                    w += 1    
            #desenha as paredes
            pygame.draw.line(screen, (3,54,73),( 0, 4),(buraco_x-1,4), 10)
            pygame.draw.line(screen, (3,54,73),(buraco_x+20, 4),(700,4), 10)
            pygame.draw.line(screen, (3,54,73),( 0, 494),(buraco_x-1,494), 10)
            pygame.draw.line(screen, (3,54,73),(buraco_x+20, 494),(700,494), 10)

            pygame.draw.line(screen, (3,54,73),( 4, 0),(4,buraco_y), 10)
            pygame.draw.line(screen, (3,54,73),( 4, buraco_y+20),(4,496), 10)
            pygame.draw.line(screen, (3,54,73),( 694, 0),(694,buraco_y), 10)
            pygame.draw.line(screen, (3,54,73),( 694, buraco_y+20),(694,496), 10)

        elif nivel == 3:
            pygame.draw.rect(screen,(4,54,73),[4,4,691,491],10)
                
        elif nivel == 4:
            
            pygame.draw.rect(screen,(4,54,73),[4,4,691,491],10)
            #linhas superiores
            pygame.draw.line(screen, (3,54,73),( 130, 74),(289,74), 10)
            pygame.draw.line(screen, (3,54,73),( 420, 74),(588,74), 10)
            #linhas inferiores
            pygame.draw.line(screen, (3,54,73),( 130, 434),(289,434), 10)
            pygame.draw.line(screen, (3,54,73),( 420, 434),(589,434), 10)
            #linhas a esquerda
            pygame.draw.line(screen, (3,54,73),( 124, 70),(124,189), 10)
            pygame.draw.line(screen, (3,54,73),( 124, 310),(124,439), 10)
            #linhas a direita
            pygame.draw.line(screen, (3,54,73),( 584, 70),(584,189), 10)
            pygame.draw.line(screen, (3,54,73),( 584, 310),(584,430), 10)
            #cruz
            pygame.draw.line(screen, (3,54,73),( 354, 120),(354,389), 10)
            pygame.draw.line(screen, (3,54,73),( 170, 254),(529,254), 10)

        #apresenta a tela 
        pygame.display.flip()
        pygame.time.delay(velocidade)
        clock.tick(30)
        
    
    if not fimDeJogo:
        cobra.play()
        fundo = pygame.image.load("gameover.jpg")
        font = pygame.font.SysFont("Arial", 30)
        pontos = (len(snake)-2)*10
        pontosCont = 0
        nivel = str(nivel)
        nivel = "Nível: "+nivel
        nivelImg = font.render(nivel,0,(255,255,255))
        mensagem = "Digite seu nome: "
        nome = ""
        digitado = False
        fechar = False
        while (len(nome)<8):
            if fechar or digitado:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar = True
                    fimDeJogo = True
                    break
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_a):
                        nome+="a"
                    elif (event.key == pygame.K_b):
                        nome+="b"
                    elif (event.key == pygame.K_c):
                        nome+="c"
                    elif (event.key == pygame.K_d):
                        nome+="d"
                    elif (event.key == pygame.K_e):
                        nome+="e"
                    elif (event.key == pygame.K_f):
                        nome+="f"
                    elif (event.key == pygame.K_g):
                        nome+="g"
                    elif (event.key == pygame.K_h):
                        nome+="h"
                    elif (event.key == pygame.K_i):
                        nome+="i"
                    elif (event.key == pygame.K_j):
                        nome+="j"
                    elif (event.key == pygame.K_k):
                        nome+="k"
                    elif (event.key == pygame.K_l):
                        nome+="l"
                    elif (event.key == pygame.K_m):
                        nome+="m"
                    elif (event.key == pygame.K_n):
                        nome+="n"
                    elif (event.key == pygame.K_o):
                        nome+="o"
                    elif (event.key == pygame.K_p):
                        nome+="p"
                    elif (event.key == pygame.K_q):
                        nome+="q"
                    elif (event.key == pygame.K_r):
                        nome+="r"
                    elif (event.key == pygame.K_s):
                        nome+="s"
                    elif (event.key == pygame.K_t):
                        nome+="t"
                    elif (event.key == pygame.K_u):
                        nome+="u"
                    elif (event.key == pygame.K_v):
                        nome+="v"
                    elif (event.key == pygame.K_w):
                        nome+="w"
                    elif (event.key == pygame.K_x):
                        nome+="x"
                    elif (event.key == pygame.K_y):
                        nome+="y"
                    elif (event.key == pygame.K_z):
                        nome+="z"
                    elif (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                        digitado = True
                        break
            if pontosCont<pontos:
                pontosCont += 1
            pontosEscreve = str(pontosCont)
            score = "Pontuação: "+pontosEscreve
            scoreImg = font.render( score, 0, (255,255,255))            
            nomeImg = font.render(mensagem+nome,0,(255,255,255))
            screen.blit(fundo,(0,0))
            screen.blit( scoreImg, (220,215) )
            screen.blit(nivelImg, (220,265) )
            screen.blit(nomeImg,(220,315))
            pygame.display.flip()
            clock.tick(30)
            
        if fimDeJogo:
            break
    
        pygame.time.wait(800)
        
        campeoes = open("lista.txt","r")
        nomes = (campeoes.readline()).split("|")
        campeoes.close()
        for i in range(len(nomes)):
            nomes[i]=nomes[i].split(":")

        for i in range(len(nomes)):
            if(int(pontosCont)>int(nomes[i][1])):
                nomes.insert(i,[nome,pontosCont])
                break
        if len(nomes)>5:
            del nomes[5]
        novoNome = ""
        
        #apresenta os campeões
        sair = False
        pontos = [0,0,0,0,0]
        while not sair:
            for i in range(len(nomes)):
                if int(nomes[i][1])>pontos[i]:
                    pontos[i]+=2
            screen.fill((0,0,0))
            y = 130
            grande = pygame.font.SysFont("Impact Regular", 40)
            pequena = pygame.font.SysFont("Arial", 15)
            top = grande.render("TOP 5",0,(255,255,255))
            screen.blit(top,(310,40))
            for i in range(len(nomes)):
                pessoa = str(nomes[i][0])+" - "+str(pontos[i])
                pessoaImg = font.render(pessoa,0,(255,255,255))
                screen.blit(pessoaImg,(280,y))
                y += 50
            continuar = pequena.render("Tecle qualquer letra para jogar novamente.",0,(255,255,255))
            screen.blit(continuar,(455,450))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    fimDeJogo = True
                    break
                if event.type == pygame.KEYDOWN:
                    sair = True
                    break
        
        
        for i in range(len(nomes)):
            nomes[i] = str(nomes[i][0])+":"+str(nomes[i][1])
        for i in range(len(nomes)):
            novoNome += nomes[i]+"|"
        novoNome=novoNome[0:len(novoNome)-1]
        
        campeoes = open("lista.txt","w")
        campeoes.write(novoNome)
        campeoes.close()

    
    
    
    
pygame.quit()




























