#python export concreto2()
# -*- coding: utf-8 -*-

from hpprime import *
import sys
import math

# Desenvolvido por Gilson Carvalho - Maceió - 2024

print("---------------------------------------")
print("---------------------------------------")
print("------- ESTRUTURAS DE CONCRETO 2 --------")
print("---------------------------------------")
print("---------------------------------------")
print("                                       ")

concreto2=1
while concreto2==1:
	print(" Selecione a questao: ")
	print(" [1] Questao 1")
	print(" [2] Questao 2")
	print(" [3] SAIR")
	acao=int(input())
	while (acao!=1 and acao!=2 and acao!=3):
		print(" Escolha apenas um numero entre 1 e 3:")
		print(" Selecione a questao: ")
		print(" [1] Questao 1")
		print(" [2] Questao 2")
		print(" [3] SAIR")
		acao=int(input())

	if acao==1:
		eval("PRINT()")
		print(" Torcao de equilibrio - O momento de torcao deve ser obrigatoriamente considerado, pois ele e necessario para o equilibrio da estrutura.")
		print(" Exemplos:")
		print(" Lajes em balanco engastadas em vigas de apoio (como as marquises).")
		print(" Vigas em balanco com carregamento excentrico.")
		print(" Vigas do tipo T invertido para apoio de estrutura de piso ou de cobertura.")
		print(" Vigas com mudanca de direcao e vigas curvas (com e sem mudanca de direcao).")
		print("                                       ")
		print(" Torcao de compatibilidade - A torcao que surge e consequencia da compatibilizacao de deformacoes da estrutura. Esses momentos de torcao nao sao imprecindiveis ao equilibrio do sistema, podendo assim serem desconsiderados.")
		print(" Exemplos:")
		print(" Lage apoiada sobre uma viga de borda.")
		print("---------------------------------------")
		print("                                       ")

	if acao==2:
		eval("PRINT()")
		print("                                       ")
		print("---------------------------------------")
		print("---------------------------------------")
		print("---- DIMENSIONAMENTO DE ARMADURAS ----")
		print("---- PARA VIGAS DE SECAO TRANSVERSAL ----")
		print("--------------- QUADRADA --------------")
		print("---------------------------------------")
		print("---------------------------------------")
		print("                                       ")

		def armadura_minima(fck):
			global tx_arm

			if fck<32.5:
				tx_arm=0.15
			if fck<37.5 and fck>=32.5:
				tx_arm=0.164
			if fck<42.5 and fck>=37.5:
				tx_arm=0.179
			if fck<47.5 and fck>=42.5:
				tx_arm=0.194
			if fck<52.5 and fck>=47.5:
				tx_arm=0.208
			if fck<57.5 and fck>=52.5:
				tx_arm=0.211
			if fck<62.5 and fck>=57.5:
				tx_arm=0.219
			if fck<67.5 and fck>=62.5:
				tx_arm=0.226
			if fck<72.5 and fck>=67.5:
				tx_arm=0.233
			if fck<77.5 and fck>=72.5:
				tx_arm=0.239
			if fck<82.5 and fck>=77.5:
				tx_arm=0.245
			if fck<87.5 and fck>=82.5:
				tx_arm=0.251
			if fck>=87.5:
				tx_arm=0.256
			return tx_arm

		def imprimir_dados(n_con=None, fck=None, tx_arm=None, fyk=None, d=None, c=None, fi_t=None, fi_l=None, L=None, b=None, h=None, Fk=None):
			print(" Dados:")
			print("---------------------------------------")
			print(" n_con = {} kN/cm3".format("vazio" if n_con is None else n_con))
			print(" fck = {} MPa".format("vazio" if fck is None else fck))
			print(" tx_arm_min = {} %".format("vazio" if tx_arm is None else tx_arm))
			print(" fyk = {} MPa".format("vazio" if fyk is None else fyk))
			print(" d = {} cm".format("vazio" if d is None else d))
			print(" c = {} mm".format("vazio" if c is None else c))
			print(" fi_t = {} mm".format("vazio" if fi_t is None else fi_t))
			print(" fi_l = {} mm".format("vazio" if fi_l is None else fi_l))
			print(" L = {} m".format("vazio" if L is None else L))
			print(" b = {} m".format("vazio" if b is None else b))
			print(" h = {} m".format("vazio" if h is None else h))
			print(" Fk = {} kN".format("vazio" if Fk is None else Fk))
			print("---------------------------------------")

		''''
		n_con=25
		fck=30
		tx_arm=armadura_minima(fck)
		fyk=500
		c=30
		fi_t=10
		fi_l=16
		L=2
		b=0.4
		h=0.4
		Fk=55
		d=34.5
		'''

		print(" Insira o n_con (kN/m3): ")
		n_con=float(input())
		eval("PRINT()")
		imprimir_dados(n_con)

		print(" Insira o fck (MPa): ")
		fck=float(input())
		eval("PRINT()")
		tx_arm=armadura_minima(fck)
		imprimir_dados(n_con,fck,tx_arm)

		print(" Insira o fyk (MPa): ")
		fyk=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk)

		print(" Insira o d (cm): ")
		d=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d)

		print(" Insira o c (mm): ")
		c=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c)

		print(" Insira o fi_t (mm): ")
		fi_t=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c,fi_t)

		print(" Insira o fi_l (mm): ")
		fi_l=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c,fi_t,fi_l)

		print(" Insira o L (m): ")
		L=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c,fi_t,fi_l,L)

		print(" Insira o b (m): ")
		b=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c,fi_t,fi_l,L,b)

		print(" Insira o h (m): ")
		h=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c,fi_t,fi_l,L,b,h)

		print(" Insira o Fk (kN): ")
		Fk=float(input())
		eval("PRINT()")
		imprimir_dados(n_con,fck,tx_arm,fyk,d,c,fi_t,fi_l,L,b,h,Fk)

		def calculodosesforcos1():

			global Md, qk, Tsk, Vsk, Vsd, Mk, Md, Kc, Ks, Bc, As_nece, As, As_min, alfa_v2, fcd, Vrd2, fctd, Vc, Vsw, fctm

			print("                                       ")
			print(" 1) ACOES ATUANTES NA ESTRUTURA:")
			print("---------------------------------------")
			print("                                       ")

			print(" Peso proprio:")
			print("                                       ")
			qk=n_con*b*h
			print(" qk = n_con * b * h = {} kN/m".format(round(qk,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Momento torsor:")
			print("                                       ")
			Tsk=Fk*b
			print(" Tsk = Fk * b = {} kN.m".format(round(Tsk,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" 2) ESFORCOS SOLICITANTES MAXIMOS:")
			print("---------------------------------------")
			print("                                       ")

			print(" Esforco cortante:")
			print("                                       ")
			Vsk=L*qk
			print(" Vsk = qk * L = {} kN".format(round(Vsk,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Momento fletor:")
			print("                                       ")
			Mk=((qk*(L**2))/2)*100
			print(" Mk = (qk * L^2 ) / 2 = {} kN.cm".format(round(Mk,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Momento torsor:")
			print("                                       ")
			Tsk=Fk*b
			print(" Tsk = Fk * b = {} kN.cm".format(round(Tsk*100,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" 3) DIMENSIONAMENTO A FLEXAO:")
			print("---------------------------------------")
			print("                                       ")

			print(" Taxa de armadura minima")
			print("                                       ")
			print(" ro_min = {} %".format(round(tx_arm,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Armadura minima:")
			print("                                       ")
			As_min=tx_arm*b*h*100
			print(" As_min = ro_min * b * h = {} cm2".format(round(As_min,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Momento fletor majorado:")
			print("                                       ")
			Md=1.4*Mk
			print(" Md = 1.4 * Mk = {} kN.cm".format(round(Md,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Calculo do Kc:")
			print("                                       ")
			Kc=(b*100*(d**2))/Md
			print(" Kc = b * d^2 / Md = {}".format(round(Kc,3)))
			print("---------------------------------------")

			'''
			Ks=0.023
			Bc=0.02

			'''
			print("                                       ")
			print(" Consulte a tabela e insira o Ks: ")
			Ks=float(input())
			print("                                       ")
			print(" Ks = ",Ks)
			print("---------------------------------------")

			print("                                       ")
			print(" Consulte a tabela e insira o Bc: ")
			Bc=float(input())
			print("                                       ")
			print(" Bc = ",Bc)

			if Bc<0.45:
				print("---------------------------------------")
				print(" Bc = {} < 0.45 (Ok)".format(Bc))
				print("---------------------------------------")
			if Bc>=0.45:
				print("---------------------------------------")
				print(" Bc = {} >= 0.45 (Nao ok)".format(Bc))
				print("---------------------------------------")

			print("                                       ")
			print(" Armadura necessaria:")
			print("                                       ")
			As_nece=(Ks*Md)/d
			print(" As_nece = (Ks * Md) / d = {} cm2".format(round(As_nece,3)))
			print("---------------------------------------")

			if As_nece<As_min:
				print(" As_nece < As_min -> Ac = As_min")
				As=As_min
				print("---------------------------------------")
			if As_nece>=As_min:
				print(" As_nece >= As_min -> Ac = As_nece")
				As=As_nece
				print("---------------------------------------")

			print(" As = {} cm2".format(round(As,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" 4) DIMENSIONAMENTO A FORCA CORTANTE:")
			print("---------------------------------------")
			print("                                       ")

			print(" Esforco cortante majorado:")
			print("                                       ")
			Vsd=Vsk*1.4
			print(" Vsd = Vsk * 1.4 = {} kN".format(round(Vsd,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Coeficiente de reducao de esbeltez lateral:")
			print("                                       ")
			alfa_v2=1-(fck/250)
			print(" alfa_v2 = 1 - (fck/250) = {}".format(round(alfa_v2,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Resistencia de calculo do concreto :")
			print("                                       ")
			fcd=fck/1.4
			print(" fcd = fck / 1.4 = {} MPa".format(round(fcd,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Verificacao das diagonais de compressao:")
			print("                                       ")
			Vrd2=0.27*alfa_v2*fcd*b*d*10
			print(" Vrd2 = 0.27 * alfa_v2 * fcd * b * d = {} kN".format(round(Vrd2,1)))
			print("---------------------------------------")

			if Vrd2>Vsd:
				print(" Vrd2 > Vsd (Ok)")
				print("---------------------------------------")
			if Vrd2<=Vsd:
				print(" Vrd2 <= Vsd (Nao ok)")
				print("---------------------------------------")

			print("                                       ")
			print(" Resistencia caracteristica a tracao do concreto:")
			print("                                       ")
			fctd=(0.7*0.3*(fck**(2/3)))/(1.4*10)
			print(" fctd = (0.7 * 0.3 * fck^(2/3)) / 1.4")
			print("---------------------------------------")
			print(" fctd = {} MPa = {} kN/cm2 ".format(round(fctd*10,3),round(fctd,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Capacidade de cisalhamento nominal:")
			print("                                       ")
			Vc=0.6*fctd*b*d*100
			print(" Vc = 0.6 * fctd * b * d = {} kN".format(round(Vc,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Forca de cisalham. resistida pelas armaduras:")
			print("                                       ")
			Vsw=Vsd-Vc
			print(" Vsw = Vsd - Vc = {} kN".format(round(Vsw,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Resistencia a tracao media do concreto:")
			print("                                       ")
			fctm=0.3*(fck**(2/3))
			print(" fctm = 0.3 * fck^(2/3) = {} MPa".format(round(fctm,3)))
			print("---------------------------------------")
			print("                                       ")

		def calculodosesforcos2():

			global A, mi, he_sup, he_inf, he, Ae, mie, Trd2, fyd, As_90, Asl, Veri1, Tsd, Asw

			print("                                       ")
			print(" Calculo da armadura transversal:")
			print("                                       ")
			Asw=(0.2/fyk)*0.3*(fck**(2/3))*b*100*math.sin(math.pi/2)
			print(" (Asw/s)min = (0.2/fyk)*0.3 * fck^(2/3) * b*sin90")
			print("---------------------------------------")
			print(" (Asw/s)min = {} cm2/cm".format(round(Asw,3)))
			print("---------------------------------------")
			print(" (Asw/s)min = {} cm2/m".format(round(Asw*100,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Para dois ramos, temos:")
			print("                                       ")
			print(" (Asw/s)min / 2 = {} cm2/cm".format(round(Asw/2,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" 5) DIMENSIONAMENTO A TORCAO:")
			print("---------------------------------------")
			print("                                       ")

			print(" Momento torsor majorado:")
			print("                                       ")
			Tsd=1.4*Tsk
			print(" Tsd = Tsk * 1,4 = {} kN.m = {} kN.cm".format(round(Tsd,3),round(Tsd*100,2)))
			print("---------------------------------------")

			print("                                       ")
			print(" Geometria da secao resistente:")
			print("---------------------------------------")

			print("                                       ")
			print(" Area da secao transversal:")
			print("                                       ")
			A=b*h*10000
			print(" A = b * h = {} cm2".format(round(A,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Perimetro da secao transversal:")
			print("                                       ")
			mi=2*((b*100)+(h*100))
			print(" mi = 2(b + h) = {} cm".format(round(mi,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Limite superior da altura efetiva:")
			print("                                       ")
			he_sup=A/mi
			print(" he_sup = A / mi = {} cm".format(round(he_sup,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Limite inferior da altura efetiva:")
			print("                                       ")
			he_inf=2*((c/10)+(fi_t/10)+(fi_l/20))
			print(" he_inf = 2*(c + fi_t + (fi_l/2)) = {} cm".format(round(he_inf,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Altura efetiva da secao transversal:")
			print("                                       ")
			print(" {} cm <= he <= {} cm ".format(round(he_inf,3),round(he_sup,3)))
			print("---------------------------------------")
			he=he_sup
			print(" Portanto: he = {} cm".format(round(he,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Area efetiva:")
			print("                                       ")
			Ae=((b*100)-he)*((h*100)-he)
			print(" Ae = (b-he)*(h-he) = {} cm2".format(round(Ae,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Coeficiente de elasticidade efetivo:")
			print("                                       ")
			mie=2*(((b*100)-he)+((h*100)-he))
			print(" mie = 2*((b-he)+(h-he)) = {} cm2".format(round(mie,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" Verifi. da compressao diagonal do concreto:")
			print("                                       ")
			Trd2=0.5*alfa_v2*fcd*Ae*he*math.sin(math.pi/2)/10
			print(" Trd2 = 0.5 * alfa_v2 * fcd * Ae * he * sin(2*45)") 
			print("---------------------------------------")
			print(" Trd2 = {} kN.cm".format(round(Trd2,3)))
			print("---------------------------------------")

			if Trd2>Tsd:
				print(" Trd2 > Tsd (Ok)")
				print("---------------------------------------")
			if Trd2<=Tsd:
				print(" Trd2 <= Tsd (Nao ok)")
				print("---------------------------------------")

			print("                                       ")
			print(" Calculo das armaduras de torcao:")
			print("---------------------------------------")
			print("                                       ")
			
			print(" Limite de escoamento do aco:")
			print("                                       ")
			fyd=fyk/1.15
			print(" fyd = fyk / 1.15 = {} MPa".format(round(fyd,3)))
			print("---------------------------------------")
			
			print("                                       ")
			print(" Estribos:")
			print("                                       ")
			As_90=((Tsd*math.tan(math.pi/4))/(2*Ae*fyd))*1000
			print(" As_90/s = (Tsd * tan45) / (2 * Ae * fyd)")
			print("---------------------------------------")
			print(" As_90/s = {} cm2/cm".format(round(As_90,4)))
			print("---------------------------------------")

			print("                                       ")
			print(" Armadura longitudinal:")
			print("                                       ")
			Asl=((mie*Tsd)/(2*Ae*fyd*(math.tan(math.pi/4))))*1000
			print(" Asl = (mie * Tsd) / (2 * Ae * fyd * tan45)")
			print("---------------------------------------")
			print(" Asl = {} cm2".format(round(Asl,3)))
			print("---------------------------------------")

			print("                                       ")
			print(" 6) VERIFICAO DAS SOLICITACOES COMBINADAS:")
			print("---------------------------------------")
			print("                                       ")

			print(" Torcao e Cisalhamento:")
			print("                                       ")
			Veri1=((Vsd/Vrd2)+((Tsd*100)/Trd2))

			if Veri1<1:
				print(" Vsd/Vrd2 + Tsd/Trd2 = {}".format(round(Veri1,3)))
				print("---------------------------------------")
				print(" {} < 1 (Ok)".format(round(Veri1,3)))
				print("---------------------------------------")
			if Veri1>=1:
				print(" Vsd/Vrd2 + Tsd/Trd2 = {}".format(round(Veri1,3)))
				print("---------------------------------------")
				print(" {} >= 1 (Nao ok)".format(round(Veri1,3)))
				print("---------------------------------------")
			print("                                       ")

		def calculodosesforcos3():

			global A_nece, As_sup_tor, aux1, a16, num_sup, As_inf_tor, aux2, num_inf, As_lat_tor, aux3, num_lat, num_tot, As_tot, As_tot_trans, At, s, comp, a

			print("                                       ")
			print(" 7) DETALHAMENTO DAS ARMADURAS:")
			print("---------------------------------------")
			print("                                       ")

			print(" Armadura longitudinal:")
			print("                                       ")
			A_nece=As+Asl
			print(" As_nece = As + Asl = {} cm2".format(round(A_nece,3)))
			print("---------------------------------------")
			print("                                       ")
			print(" A analise sera realizada por face")
			print("                                       ")
			print("---------------------------------------")

			print("                                       ")
			print(" Face superior:")
			print("---------------------------------------")
			print(" Flexao: As = {} cm2".format(round(As,3)))
			print("---------------------------------------")
			As_sup_tor=((b*100)-he)*(Asl/mie)
			print(" Torcao: As_sup_tor = (b-he)*(Asl/mie)")
			print("---------------------------------------")
			print(" As_sup_tor = {} cm2".format(round(As_sup_tor,3)))
			print("---------------------------------------")
			aux1=As+As_sup_tor
			print(" As_total = As + As_sup_tor = {} cm2".format(round(aux1,3)))
			print("---------------------------------------")
			
			a=math.pi*((fi_l/20)**2)
			print(" A_fi({}mm) = {} cm2".format(fi_l,round(a,3)))
			print("---------------------------------------")
			num_sup=math.ceil(aux1/a)
			print(" {} fi {} mm".format(num_sup,fi_l))
			print("                                       ")
			print("---------------------------------------")

			print("                                       ")
			print(" Face inferior:")
			print("---------------------------------------")
			print(" Flexao: As = 0 cm2")
			print("---------------------------------------")
			As_inf_tor=((b*100)-he)*(Asl/mie)
			print(" Torcao: As_inf_tor = (b-he)*(Asl/mie)")
			print("---------------------------------------")
			print(" As_inf_tor = {} cm2".format(round(As_inf_tor,3)))
			print("---------------------------------------")
			aux2=As_inf_tor
			print(" As_total = As + As_sup_tor = {} cm2".format(round(aux2,3)))
			print("---------------------------------------")
			
			num_inf=math.ceil(aux2/a)
			print(" {} fi {} mm".format(num_inf,fi_l))
			print("                                       ")
			print("---------------------------------------")

			print("                                       ")
			print(" Cada face lateral:")
			print("---------------------------------------")
			print(" Flexao: As = 0 cm2")
			print("---------------------------------------")
			As_lat_tor=((b*100)-he)*(Asl/mie)
			print(" Torcao: As_lat_tor = (b-he)*(Asl/mie)")
			print("---------------------------------------")
			print(" As_lat_tor = {} cm2".format(round(As_lat_tor,3)))
			print("---------------------------------------")
			aux3=As_lat_tor
			print(" As_total = As + As_lat_tor = {} cm2".format(round(aux3,3)))
			print("---------------------------------------")
			
			num_lat=math.ceil(aux3/a)
			print(" {} fi {} mm".format(num_lat,fi_l))
			print("                                       ")
			print("---------------------------------------")

			print("                                       ")
			print(" Total de barras na secao:")
			print("                                       ")
			num_tot=num_sup+num_inf+num_lat*2
			As_tot=num_tot*a
			print(" {} fi {} mm => As_tot = {} cm2".format(num_tot,fi_l,round(As_tot,3)))
			print("---------------------------------------")

			if As_tot>=As_nece:
				print(" As_tot >= As_nece (Ok)")
				print("---------------------------------------")
			if As_tot<As_nece:
				print(" As_tot < As_nece (Nao ok)")
				print("---------------------------------------")

			print("                                       ")
			print(" Armadura transversal:")
			print("                                       ")
			print(" A area total de esrtribos e calculada pela soma das areas relativas a forca cortante e a torcao")
			print("---------------------------------------")
			print(" Forca cortante:")
			print(" Asw,ramo/s = {} cm2/cm".format(round(Asw/2,3)))
			print("---------------------------------------")
			print(" Torcao:")
			print(" Asw,90/s = {} cm2/cm".format(round(As_90,3)))
			print("---------------------------------------")
			print(" As_total = Asw,ramo/s + Asw,90/s")
			print("---------------------------------------")
			As_tot_trans=(Asw/2)+As_90
			print(" As_total = {} cm2".format(round(As_tot_trans,3)))
			print("---------------------------------------")
			At=((math.pi*(fi_t**2))/4)/100
			print(" At = (pi * fi_t^2) / 4 = {} cm2".format(round(At,3)))
			print("---------------------------------------")
			s=At/As_tot_trans
			print(" s = At / As_total = {} cm".format(round(s,3)))
			comp=num_tot*((b*100)-2*(c/10))+fi_l
			print("---------------------------------------")
			print(" Adotaremos: fi {} c.{} = {}".format(fi_t,round(s,2),comp))
			print("---------------------------------------")
			print("                                       ")

		resolu=1
		while resolu==1:
			print(" Selecione a parte da resolucao: ")
			print(" [1] Parte 1")
			print(" [2] Parte 2")
			print(" [3] Parte 3")
			print(" [4] Sair")
			resp=int(input())
			while (resp!=1 and resp!=2 and resp!=3 and resp!=4):
				print(" Escolha apenas um numero entre 1 e 4:")
				print(" Selecione a parte da resolucao: ")
				print(" [1] Parte 1")
				print(" [2] Parte 2")
				print(" [3] Parte 3")
				print(" [4] Sair")
				resp=int(input())
			if resp==1:
				eval("PRINT()")
				calculodosesforcos1()
			if resp==2:
				eval("PRINT()")
				calculodosesforcos2()
			if resp==3:
				eval("PRINT()")
				calculodosesforcos3()
			if resp==4:
				eval("PRINT()")
				sys.exit(1)


	if acao==3:
		#quit()
		sys.exit(1)
#end