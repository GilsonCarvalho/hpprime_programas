#python export madeira_ab2()
# -*- coding: utf-8 -*-
import sys
import math

# Desenvolvido por Gilson Carvalho - Maceio - 2023

madeira=1
madeira=1
while madeira==1:
	print("---------------------------------------")
	print("-------- ESTRUTURAS DE MADEIRA --------")
	print("---------------------------------------")
	print("---------------- AB2 ------------------")
	print("---------------------------------------")
	print("--- Desenvolvido por GILSON CARVALHO --")
	print("                                       ")
	print("Selecione o exercicio: ")
	print("[1] FLEXAO SIMPLES SESSAO RETANGULAR")
	print("[2] FLEXAO COMPOSTA OBLIQUA")
	print("[3] SAIR")
	acao=int(input())

	if acao==1:
		print("                                       ")
		print("---------------------------------------")
		print("--- FLEXAO SIMPLES SESSAO RETANGULAR --")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")

		'''

		b=15
		h=35
		c=10
		d=4.9
		fc0k=6
		fmk=6
		fvk=0.8
		Ec0m=1950
		g=2.5
		q=7.5
		P=10
		gama_g=1.3
		gama_qq=1.5
		gama_qP=1.5
		psi_2qq=0.3
		psi_2qP=0.3
		kmod=0.56
		gama_w1=1.4
		alfa_n=1.1
		gama_w2=1.8
		fi=0.8

		'''

		print("                                       ")
		print("Dados da viga")
		print("---------------------------------------")

		print("Insira o b (cm): ")
		b=float(input())
		print(b)
		print("---------------------------------------")

		print("Insira o h (cm): ")
		h=float(input())
		print(h)
		print("---------------------------------------")

		print("Insira o c (cm): ")
		c=float(input())
		print(c)
		print("---------------------------------------")

		print("Insira o d (m): ")
		d=float(input())
		print(d)
		print("---------------------------------------")

		print("                                       ")
		print("Dados da madeira")
		print("---------------------------------------")

		print("Insira o fc0k (kN/cm2): ")
		fc0k=float(input())
		print(fc0k)
		print("---------------------------------------")

		print("Insira o fmk (kN/cm2): ")
		fmk=float(input())
		print(fmk)
		print("---------------------------------------")

		print("Insira o fvk (kN/cm2): ")
		fvk=float(input())
		print(fvk)
		print("---------------------------------------")

		print("Insira o Ec0m (kN/cm2): ")
		Ec0m=float(input())
		print(Ec0m)
		print("---------------------------------------")

		print("                                       ")
		print("Dados do carre. e seus fato. de ponder.")
		print("---------------------------------------")

		print("Insira o g (kN/m): ")
		g=float(input())
		print(g)
		print("---------------------------------------")

		print("Insira o q (kN/m): ")
		q=float(input())
		print(q)
		print("---------------------------------------")

		print("Insira o P (kN): ")
		P=float(input())
		print(P)
		print("---------------------------------------")

		print("Insira o gama_g: ")
		gama_g=float(input())
		print(gama_g)
		print("---------------------------------------")

		print("Insira o gama_qq: ")
		gama_qq=float(input())
		print(gama_qq)
		print("---------------------------------------")

		print("Insira o gama_qP: ")
		gama_qP=float(input())
		print(gama_qP)
		print("---------------------------------------")

		print("Insira o psi_2qq: ")
		psi_2qq=float(input())
		print(psi_2qq)
		print("---------------------------------------")

		print("Insira o psi_2qP: ")
		psi_2qP=float(input())
		print(psi_2qP)
		print("---------------------------------------")

		print("                                       ")
		print("Coeficientes da NBR 7190 (2022)")
		print("---------------------------------------")

		print("Insira o kmod: ")
		kmod=float(input())
		print(kmod)
		print("---------------------------------------")

		print("Insira o gama_w1: ")
		gama_w1=float(input())
		print(gama_w1)
		print("---------------------------------------")

		print("Insira o alfa_n: ")
		alfa_n=float(input())
		print(alfa_n)
		print("---------------------------------------")

		print("Insira o gama_w2: ")
		gama_w2=float(input())
		print(gama_w2)
		print("---------------------------------------")

		print("Insira o fi: ")
		fi=float(input())
		print(fi)



		print("                                       ")
		print("---------------------------------------")
		print("1. Dados do problema:")
		print("---------------------------------------")
		print("                                       ")

		print("Dados da viga")
		print("---------------------------------------")

		print("b = {} (cm)".format(b))
		print("---------------------------------------")

		print("h = {} (cm)".format(h))
		print("---------------------------------------")

		print("c = {} (cm)".format(c))
		print("---------------------------------------")

		print("d = {} (m)".format(d))
		print("---------------------------------------")

		h_apoio=0.75*h
		print("h_apoio = {} (cm)".format(h_apoio))
		print("---------------------------------------")

		print("                                       ")
		print("Dados da madeira")
		print("---------------------------------------")

		print("fc0k = {} (kN/cm2)".format(fc0k))
		print("---------------------------------------")

		print("fmk = {} (kN/cm2)".format(fmk))
		print("---------------------------------------")

		print("fvk = {} (kN/cm2)".format(fvk))
		print("---------------------------------------")

		print("Ec0m = {} (kN/cm2)".format(Ec0m))
		print("---------------------------------------")

		print("                                       ")
		print("Dados do carre. e seus fato. de ponder.")
		print("---------------------------------------")

		print("g = {} (kN/m)".format(g))
		print("---------------------------------------")

		print("q = {} (kN/m)".format(q))
		print("---------------------------------------")

		print("P = {} (kN)".format(P))
		print("---------------------------------------")

		print("gama_g = {}".format(gama_g))
		print("---------------------------------------")

		print("gama_qq = {}".format(gama_qq))
		print("---------------------------------------")

		print("gama_qP = {}".format(gama_qP))
		print("---------------------------------------")

		print("psi_2qq = {}".format(psi_2qq))
		print("---------------------------------------")

		print("psi_2qP = {}".format(psi_2qP))
		print("---------------------------------------")

		print("                                       ")
		print("Coeficientes da NBR 7190 (2022)")
		print("---------------------------------------")

		print("kmod = {}".format(kmod))
		print("---------------------------------------")

		print("gama_w1 = {}".format(gama_w1))
		print("---------------------------------------")

		print("alfa_n = {}".format(alfa_n))
		print("---------------------------------------")

		print("gama_w2 = {}".format(gama_w2))
		print("---------------------------------------")

		print("fi = {}".format(fi))

		print("                                       ")
		print("---------------------------------------")
		print("2. Vao da viga:")
		print("---------------------------------------")
		print("                                       ")

		L0=d+(c/(2*100))+(c/(2*100))
		print("L0 = {} (m)".format(round(L0,3)))
		print("---------------------------------------")

		L1=d+(h/100)
		print("L1 = {} (m)".format(round(L1,3)))
		print("---------------------------------------")

		L2=d+(10/100)
		print("L2 = {} (m)".format(round(L2,3)))
		print("---------------------------------------")

		Lv=[[round(L0,2)],[round(L1,2)],[round(L2,2)]]
		Lv1=[[L0],[L1],[L2]]
		menor = Lv1[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
		for linha in Lv1:
			for elemento in linha:
				if elemento < menor:
					menor = elemento
		L=menor
		print("Lv = {} (m)".format(Lv))
		print("---------------------------------------")
		print("L = {} (m)".format(round(L,3)))

		print("                                       ")
		print("---------------------------------------")
		print("3. Carregamentos de projeto:")
		print("---------------------------------------")
		print("                                       ")

		qd=(gama_g*g)+(gama_qq*q)
		print("qd = {} (kN/m)".format(round(qd,3)))
		print("---------------------------------------")

		Pd=gama_qP*P
		print("Pd = {} (kN)".format(round(Pd,3)))

		print("                                       ")
		print("---------------------------------------")
		print("4. Esfor. inte. solic. e rea. de apoio:")
		print("---------------------------------------")
		print("                                       ")

		Msdx=((qd*(L**2)/8)+(Pd*L/4))*100
		print("Msdx = {} (kN.cm)".format(round(Msdx,3)))
		print("---------------------------------------")

		Vsdy=(qd*L/2)+(Pd/2)
		print("Vsdy = {} (kN)".format(round(Vsdy,3)))
		print("---------------------------------------")

		Rd=(qd*L/2)+(Pd/2)
		print("Rd = {} (kN)".format(round(Rd,3)))

		print("                                       ")
		print("---------------------------------------")
		print("5. Propri. geom. da secao transversal:")
		print("---------------------------------------")
		print("                                       ")

		Ix=(b*(h**3))/12
		print("Ix = {} (cm4)".format(round(Ix,3)))
		print("---------------------------------------")

		Wx=(b*(h**2))/6
		print("Wx = {} (cm3)".format(round(Wx,3)))
		print("---------------------------------------")
		print("                                       ")

		print("[1] Resolucao - Parte 2 (2/2)")
		print("[2] SAIR")
		r12=int(input())

		if(r12==2):
			sys.exit(1)
		if(r12==1):

			print("                                       ")
			print("---------------------------------------")
			print("6. Propriedades de projeto da madeira:")
			print("---------------------------------------")
			print("                                       ")

			fc0d=kmod*(fc0k/gama_w1)
			print("fc0d = {} (kN/cm2)".format(round(fc0d,3)))
			print("---------------------------------------")

			fmd=kmod*(fmk/gama_w1)
			print("fmd = {} (kN/cm2)".format(round(fmd,3)))
			print("---------------------------------------")

			fvd=kmod*(fvk/gama_w2)
			print("fvd = {} (kN/cm2)".format(round(fvd,3)))
			print("---------------------------------------")

			fc90d=0.25*fc0d*alfa_n
			print("fc90d = {} (kN/cm2)".format(round(fc90d,3)))

			print("                                       ")
			print("---------------------------------------")
			print("7. Verificacao da tensao normal:")
			print("---------------------------------------")
			print("                                       ")

			sigma_Msdx=(Msdx/Wx)
			print("sigma_Msdx = {} (kN/cm2)".format(round(sigma_Msdx,3)))
			print("---------------------------------------")

			Verif_Tens_Norm=(sigma_Msdx/fmd)
			print("Verif_Tens_Norm = {}".format(round(Verif_Tens_Norm,3)))
			print("---------------------------------------")

			if Verif_Tens_Norm>1:
				print("Verif_Tens_Norm > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Verif_Tens_Norm <= 1")
				print("---------------------------------------")
				print("Atende!")

			print("                                       ")
			print("---------------------------------------")
			print("8. Verificacao da tensao cisalhante:")
			print("---------------------------------------")
			print("                                       ")

			tau_Vsdy=(3/2)*(Vsdy/(b*h_apoio))*(h/h_apoio)
			print("tau_Vsdy = {} (kN/cm2)".format(round(tau_Vsdy,3)))
			print("---------------------------------------")

			Verif_Tens_Cisa=(tau_Vsdy/fvd)
			print("Verif_Tens_Cisa = {}".format(round(Verif_Tens_Cisa,3)))
			print("---------------------------------------")

			if Verif_Tens_Cisa>1:
				print("Verif_Tens_Cisa > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Verif_Tens_Cisa <= 1")
				print("---------------------------------------")
				print("Atende!")

			print("                                       ")
			print("---------------------------------------")
			print("9. Veri. da ten. perp. as fib. no apo.:")
			print("---------------------------------------")
			print("                                       ")

			A_apoio=b*c
			print("A_apoio = {} (cm2)".format(round(A_apoio,3)))
			print("---------------------------------------")

			sigma_c90d=(Rd/A_apoio)
			print("sigma_c90d = {} (kN/cm2)".format(round(sigma_c90d,3)))
			print("---------------------------------------")

			Verif_Tens_Apoi=sigma_c90d/fc90d
			print("Verif_Tens_Apoi = {}".format(round(Verif_Tens_Apoi,3)))
			print("---------------------------------------")

			if Verif_Tens_Apoi>1:
				print("Verif_Tens_Apoi > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Verif_Tens_Apoi <= 1")
				print("---------------------------------------")
				print("Atende!")

			print("                                       ")
			print("---------------------------------------")
			print("10. Verificacao estabilidade lateral:")
			print("---------------------------------------")
			print("                                       ")

			Ec0ef=kmod*Ec0m
			print("Ec0ef = {} (kN/cm2)".format(round(Ec0ef,3)))
			print("---------------------------------------")

			Beta_m=(1/(0.26*math.pi))*(4/1.4)*(((h/b)**1.5)/(((h/b)-0.63)**0.5))
			print("Beta_m = {}".format(round(Beta_m,3)))
			print("---------------------------------------")

			L1max=b*(Ec0ef/(Beta_m*fc0d))/100
			print("L1max = {} (m)".format(round(L1max,3)))
			print("---------------------------------------")

			Verif_Tens_Est_Lat=L/L1max
			print("Verif_Tens_Est_Lat = {}".format(round(Verif_Tens_Est_Lat,3)))
			print("---------------------------------------")

			if Verif_Tens_Est_Lat>1:
				print("Verif_Tens_Est_Lat > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Verif_Tens_Est_Lat <= 1")
				print("---------------------------------------")
				print("Atende!")

			print("                                       ")
			print("---------------------------------------")
			print("11. Verificacao da flecha instatanea:")
			print("---------------------------------------")
			print("                                       ")

			delta_instGk=((5*g*((L*100)**4))/(384*Ec0m*Ix))/100
			print("delta_instGk = {} (cm)".format(round(delta_instGk,3)))
			print("---------------------------------------")

			delta_instQk=((5*q*((L*100)**4))/(384*Ec0m*Ix))/100
			print("delta_instQk = {} (cm)".format(round(delta_instQk,3)))
			print("---------------------------------------")

			delta_instPk=(P*((L*100)**3))/(48*Ec0m*Ix)
			print("delta_instPk = {} (cm)".format(round(delta_instPk,3)))
			print("---------------------------------------")

			delta_inst=delta_instPk+delta_instGk+delta_instQk
			print("delta_inst = {} (cm)".format(round(delta_inst,3)))
			print("---------------------------------------")

			Delta_inst=(L/300)*100
			print("Delta_inst = {} (cm)".format(round(Delta_inst,3)))
			print("---------------------------------------")

			Verif_delta_inst=delta_inst/Delta_inst
			print("Verif_delta_inst = {}".format(round(Verif_delta_inst,3)))
			print("---------------------------------------")

			if Verif_delta_inst>1:
				print("Verif_delta_inst > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Verif_delta_inst <= 1")
				print("---------------------------------------")
				print("Atende!")

			print("                                       ")
			print("---------------------------------------")
			print("12. Verificacao da flecha final:")
			print("---------------------------------------")
			print("                                       ")

			delta_finalGk=delta_instGk*(1+fi)
			print("delta_finalGk = {} (cm)".format(round(delta_finalGk,3)))
			print("---------------------------------------")

			delta_finalQk=delta_instQk*(1+(psi_2qq*fi))
			print("delta_finalQk = {} (cm)".format(round(delta_finalQk,3)))
			print("---------------------------------------")

			delta_finalPk=delta_instPk*(1+(psi_2qP*fi))
			print("delta_finalPk = {} (cm)".format(round(delta_finalPk,3)))
			print("---------------------------------------")

			delta_final=delta_finalPk+delta_finalGk+delta_finalQk
			print("delta_final = {} (cm)".format(round(delta_final,3)))
			print("---------------------------------------")

			Delta_final=(L/150)*100
			print("Delta_final = {} (cm)".format(round(Delta_final,3)))
			print("---------------------------------------")

			Verif_delta_final=delta_final/Delta_final
			print("Verif_delta_final = {}".format(round(Verif_delta_final,3)))
			print("---------------------------------------")

			if Verif_delta_final>1:
				print("Verif_delta_final > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Verif_delta_final <= 1")
				print("---------------------------------------")
				print("Atende!")
			("---------------------------------------")
			print("                                       ")

	if acao==2:
		print("                                       ")
		print("---------------------------------------")
		print("------- FLEXAO COMPOSTA OBLIQUA -------")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")

		

		print("                                       ")
		print("Dados da viga")
		print("---------------------------------------")

		print("Insira o b (cm): ")
		b=float(input())
		print(b)
		print("---------------------------------------")

		print("Insira o h (cm): ")
		h=float(input())
		print(h)
		print("---------------------------------------")

		print("Insira o d (m): ")
		d=float(input())
		print(d)
		print("---------------------------------------")

		print("Insira o c (cm): ")
		c=float(input())
		print(c)
		print("---------------------------------------")

		print("                                       ")
		print("Dados da madeira")
		print("---------------------------------------")

		print("Insira o fc0k (kN/cm2): ")
		fc0k=float(input())
		print(fc0k)
		print("---------------------------------------")

		print("Insira o fmk (kN/cm2): ")
		fmk=float(input())
		print(fmk)
		print("---------------------------------------")

		print("Insira o fvk (kN/cm2): ")
		fvk=float(input())
		print(fvk)
		print("---------------------------------------")

		print("Insira o Ec0m (kN/cm2): ")
		Ec0m=float(input())
		print(Ec0m)
		print("---------------------------------------")

		print("                                       ")
		print("Dados do carre. e seus fato. de ponder.")
		print("---------------------------------------")

		print("Insira o g (kN/m): ")
		g=float(input())
		print(g)
		print("---------------------------------------")

		print("Insira o gama_g: ")
		gama_g=float(input())
		print(gama_g)
		print("---------------------------------------")

		print("Insira o q (kN/m): ")
		q=float(input())
		print(q)
		print("---------------------------------------")

		print("Insira o gama_qq: ")
		gama_qq=float(input())
		print(gama_qq)
		print("---------------------------------------")

		print("Insira o psi_0q: ")
		psi_0q=float(input())
		print(psi_0q)
		print("---------------------------------------")

		print("Insira o psi_1q: ")
		psi_1q=float(input())
		print(psi_1q)
		print("---------------------------------------")

		print("Insira o psi_2q: ")
		psi_2q=float(input())
		print(psi_2q)
		print("---------------------------------------")

		print("Insira o w (kN/m): ")
		w=float(input())
		print(w)
		print("---------------------------------------")

		print("Insira o gama_qw: ")
		gama_qw=float(input())
		print(gama_qw)
		print("---------------------------------------")

		print("Insira o psi_0w: ")
		psi_0w=float(input())
		print(psi_0w)
		print("---------------------------------------")

		print("Insira o psi_1w: ")
		psi_1w=float(input())
		print(psi_1w)
		print("---------------------------------------")

		print("Insira o psi_2w: ")
		psi_2w=float(input())
		print(psi_2w)
		print("---------------------------------------")

		print("Insira o N (kN): ")
		N=float(input())
		print(N)
		print("---------------------------------------")

		print("Insira o gama_qN: ")
		gama_qN=float(input())
		print(gama_qN)
		print("---------------------------------------")

		print("                                       ")
		print("Coeficientes da NBR 7190 (2022)")
		print("---------------------------------------")

		print("Insira o kmod: ")
		kmod=float(input())
		print(kmod)
		print("---------------------------------------")

		print("Insira o beta_c: ")
		beta_c=float(input())
		print(beta_c)
		print("---------------------------------------")

		print("Insira o alfa_n: ")
		alfa_n=float(input())
		print(alfa_n)
		print("---------------------------------------")

		print("Insira o km: ")
		km=float(input())
		print(km)
		print("---------------------------------------")

		print("Insira o fi: ")
		fi=float(input())
		print(fi)
		print("---------------------------------------")

		print("Insira o gama_w1: ")
		gama_w1=float(input())
		print(gama_w1)
		print("---------------------------------------")

		print("Insira o gama_w2: ")
		gama_w2=float(input())
		print(gama_w2)

		'''

		b=12
		h=30
		c=10
		d=4
		ex=0.3*b
		ey=0.4*h
		fc0k=6
		fmk=6
		fvk=0.8
		Ec0m=1950
		g=3
		q=1.5
		w=2
		N=10
		gama_g=1.3
		gama_qN=1.4
		gama_qq=1.5
		gama_qw=1.4
		psi_0q=0.5
		psi_1q=0.4
		psi_2q=0.3
		psi_0w=0.6
		psi_1w=0.3
		psi_2w=0
		kmod=0.63
		beta_c=0.2
		alfa_n=1.1
		km=0.7
		gama_w1=1.4
		gama_w2=1.8
		fi=0.8
		'''

		print("                                       ")
		print("---------------------------------------")
		print("1. Dados do problema:")
		print("---------------------------------------")
		print("                                       ")

		print("Dados da viga")
		print("---------------------------------------")

		print("b = {} (cm)".format(b))
		print("---------------------------------------")

		print("h = {} (cm)".format(h))
		print("---------------------------------------")

		print("d = {} (m)".format(d))
		print("---------------------------------------")

		print("c = {} (cm)".format(c))
		print("---------------------------------------")

		ex=0.3*b
		print("ex = {} (cm)".format(round(ex,3)))
		print("---------------------------------------")

		ey=0.4*h
		print("ey = {} (cm)".format(round(ey,3)))
		print("---------------------------------------")

		print("                                       ")
		print("Dados da madeira")
		print("---------------------------------------")

		print("fc0k = {} (kN/cm2)".format(fc0k))
		print("---------------------------------------")

		print("fmk = {} (kN/cm2)".format(fmk))
		print("---------------------------------------")

		print("fvk = {} (kN/cm2)".format(fvk))
		print("---------------------------------------")

		print("Ec0m = {} (kN/cm2)".format(Ec0m))
		print("---------------------------------------")

		print("                                       ")
		print("Dados do carr. e seus fat. de ponde.")
		print("---------------------------------------")

		print("g = {} (kN/m)".format(g))
		print("---------------------------------------")

		print("gama_g = {}".format(gama_g))
		print("---------------------------------------")

		print("q = {} (kN/m)".format(q))
		print("---------------------------------------")

		print("gama_qq = {}".format(gama_qq))
		print("---------------------------------------")

		print("psi_0q = {}".format(psi_0q))
		print("---------------------------------------")

		print("psi_1q = {}".format(psi_1q))
		print("---------------------------------------")

		print("psi_2q = {}".format(psi_2q))
		print("---------------------------------------")

		print("w = {} (kN/m)".format(w))
		print("---------------------------------------")

		print("gama_qw = {}".format(gama_qw))
		print("---------------------------------------")

		print("psi_0w = {}".format(psi_0w))
		print("---------------------------------------")

		print("psi_1w = {}".format(psi_1w))
		print("---------------------------------------")

		print("psi_2w = {}".format(psi_2w))
		print("---------------------------------------")

		print("N = {} (kN)".format(N))
		print("---------------------------------------")

		print("gama_qN = {}".format(gama_qN))
		print("---------------------------------------")

		print("                                       ")
		print("Coeficientes da NBR 7190 (2022)")
		print("---------------------------------------")

		print("kmod = {}".format(kmod))
		print("---------------------------------------")

		print("beta_c = {}".format(beta_c))
		print("---------------------------------------")

		print("alfa_n = {}".format(alfa_n))
		print("---------------------------------------")

		print("km = {}".format(km))
		print("---------------------------------------")

		print("fi = {}".format(fi))
		print("---------------------------------------")

		print("gama_w1 = {}".format(gama_w1))
		print("---------------------------------------")

		print("gama_w2 = {}".format(gama_w2))

		print("                                       ")
		print("---------------------------------------")
		print("2. Vao livre da barra:")
		print("---------------------------------------")
		print("                                       ")

		L0=d+(c/(2*100))+(c/(2*100))
		print("L0 = {} (m)".format(round(L0,3)))
		print("---------------------------------------")

		L1=d+(h/100)
		print("L1 = {} (m)".format(round(L1,3)))
		print("---------------------------------------")

		L2=d+(10/100)
		print("L2 = {} (m)".format(round(L2,3)))
		print("---------------------------------------")

		Lv=[[round(L0,2)],[round(L1,2)],[round(L2,2)]]
		Lv1=[[L0],[L1],[L2]]
		menor = Lv1[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
		for linha in Lv1:
			for elemento in linha:
				if elemento < menor:
					menor = elemento
		L=menor
		print("Lv = {} (m)".format(Lv))
		print("---------------------------------------")
		print("L = {} (m)".format(round(L,3)))

		print("                                       ")
		print("---------------------------------------")
		print("3. Propri. geomet. da secao transv.:")
		print("---------------------------------------")
		print("                                       ")

		A=b*h
		print("A = {} (cm2)".format(round(A,3)))
		print("---------------------------------------")

		Ix=(b*(h**3))/12
		print("Ix = {} (cm4)".format(round(Ix,3)))
		print("---------------------------------------")

		Iy=((b**3)*h)/12
		print("Iy = {} (cm4)".format(round(Iy,3)))
		print("---------------------------------------")

		Wx=(b*(h**2))/6
		print("Wx = {} (cm3)".format(round(Wx,3)))
		print("---------------------------------------")

		Wy=((b**2)*h)/6
		print("Wy = {} (cm3)".format(round(Wy,3)))
		print("---------------------------------------")

		rx=(Ix/A)**(1/2)
		print("rx = {} (cm)".format(round(rx,3)))
		print("---------------------------------------")

		ry=(Iy/A)**(1/2)
		print("ry = {} (cm)".format(round(ry,3)))
		
		print("                                       ")
		print("---------------------------------------")
		print("4. Propriedades de projeto da madeira:")
		print("---------------------------------------")
		print("                                       ")

		fc0d=kmod*(fc0k/1.4)
		print("fc0d = {} (kN/cm2)".format(round(fc0d,3)))
		print("---------------------------------------")

		fmd=kmod*(fmk/gama_w1)
		print("fmd = {} (kN/cm2)".format(round(fmd,3)))
		print("---------------------------------------")

		fc90d=0.25*fc0d*alfa_n
		print("fc90d = {} (kN/cm2)".format(round(fc90d,3)))
		print("---------------------------------------")

		fvd=kmod*(fvk/gama_w2)
		print("fvd = {} (kN/cm2)".format(round(fvd,3)))
		print("---------------------------------------")

		E005=0.7*Ec0m
		print("E005 = {} (kN/cm2)".format(round(E005,3)))

		print("---------------------------------------")
		print("                                       ")

		print("[1] Resolucao - Parte 2 (2/4)")
		print("[2] SAIR")
		r22=int(input())

		if(r22==2):
			sys.exit(1)
		if(r22==1):
		
			print("                                       ")
			print("---------------------------------------")
			print("5. Esforcos internos de projeto:")
			print("---------------------------------------")
			print("                                       ")

			print("5.1. Esforco normal:")
			print("---------------------------------------")
			print("                                       ")

			NcSd=gama_qN*N
			print("NcSd = {} (kN)".format(round(NcSd,3)))
			print("---------------------------------------")

			print("                                       ")	
			print("5.2. Forca distribuida na direcao y:")
			print("---------------------------------------")
			print("                                       ")

			qdy=(gama_g*g)+(gama_qq*q)
			print("qdy = {} (kN/m)".format(round(qdy,3)))
			print("---------------------------------------")

			print("                                       ")
			print("5.3. Forca distribuida na direcao x:")
			print("---------------------------------------")
			print("                                       ")

			qdx=gama_qw*w
			print("qdx = {} (kN/m)".format(round(qdx,3)))
			print("---------------------------------------")

			print("                                       ")
			print("5.4. Momento fletores de projeto:")
			print("---------------------------------------")
			print("                                       ")

			MxSd=(((qdy/100)*((L*100)**2))/8)+(NcSd*ey)
			print("MxSd = {} (kN/cm)".format(round(MxSd,3)))
			print("---------------------------------------")

			MySd=(((qdx/100)*((L*100)**2))/8)+(NcSd*ex)
			print("MySd = {} (kN/cm)".format(round(MySd,3)))
			print("---------------------------------------")
			
			print("                                       ")
			print("5.5. Esforcos cortantes de projeto:")
			print("---------------------------------------")
			print("                                       ")

			VySd=(qdy*L)/2
			print("VySd = {} (kN)".format(round(VySd,3)))
			print("---------------------------------------")

			VxSd=(qdx*L)/2
			print("VxSd = {} (kN)".format(round(VxSd,3)))
			
			print("                                       ")
			print("---------------------------------------")
			print("6. Verificacao da tensao normal:")
			print("---------------------------------------")
			print("                                       ")

			print("6.1. Verificacao da tensao provocada")
			print("     pelo esforco axial de compressao")
			print("---------------------------------------")
			print("                                       ")

			print("Ten. norm. provo. pelos esfor. de proj.")
			print("---------------------------------------")

			sigma_NcSd=NcSd/A
			print("sigma_NcSd = {} (kN/cm2)".format(round(sigma_NcSd,3)))
			print("---------------------------------------")

			sigma_MxSd=MxSd/Wx
			print("sigma_MxSd = {} (kN/cm2)".format(round(sigma_MxSd,3)))
			print("---------------------------------------")

			sigma_MySd=MySd/Wy
			print("sigma_MySd = {} (kN/cm2)".format(round(sigma_MySd,3)))

			print("---------------------------------------")
			print("                                       ")

			print("Estabilidade do eixo x")
			print("---------------------------------------")

			L0x=L*100
			print("L0x = {} (cm)".format(round(L0x,3)))
			print("---------------------------------------")

			Lamb_x=(L0x/rx)
			print("Lamb_x = {}".format(round(Lamb_x,3)))
			print("---------------------------------------")

			Lamb_xrel=(Lamb_x/math.pi)*((fc0k/E005)**(1/2))
			print("Lamb_xrel = {}".format(round(Lamb_xrel,3)))
			print("---------------------------------------")

			kx=0.5*(1+(beta_c*(Lamb_xrel-0.3))+(Lamb_xrel**2))
			print("kx = {}".format(round(kx,3)))
			print("---------------------------------------")

			kcx=1/(kx+(((kx**2)-(Lamb_xrel**2)))**(1/2))
			print("kcx = {}".format(round(kcx,3)))
			print("---------------------------------------")

			Eq1=(sigma_NcSd/(kcx*fc0d))+(sigma_MxSd/fmd)+(km*(sigma_MySd/fmd))
			print("Eq1 = {}".format(round(Eq1,3)))
			print("---------------------------------------")

			if Eq1>1:
				print("Eq1 > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Eq1 <= 1")
				print("---------------------------------------")
				print("Atende!")
			("---------------------------------------")

			print("                                       ")
			print("Estabilidade do eixo y")
			print("---------------------------------------")

			L0y=L*100
			print("L0y = {} (cm)".format(round(L0y,3)))
			print("---------------------------------------")

			Lamb_y=L0y/ry
			print("Lamb_y = {}".format(round(Lamb_y,3)))
			print("---------------------------------------")

			Lamb_yrel=(Lamb_y/math.pi)*((fc0k/E005)**(1/2))
			print("Lamb_yrel = {}".format(round(Lamb_yrel,3)))
			print("---------------------------------------")

			ky=0.5*(1+(beta_c*(Lamb_yrel-0.3))+(Lamb_yrel**2))
			print("ky = {}".format(round(ky,3)))
			print("---------------------------------------")

			kcy=1/(ky+(((ky**2)-(Lamb_yrel**2)))**(1/2))
			print("kcy = {}".format(round(kcy,3)))
			print("---------------------------------------")

			Eq2=(sigma_NcSd/(kcy*fc0d))+(sigma_MxSd/fmd)+(km*(sigma_MySd/fmd))
			print("Eq2 = {}".format(round(Eq2,3)))
			print("---------------------------------------")

			if Eq2>1:
				print("Eq2 > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("Eq2 <= 1")
				print("---------------------------------------")
				print("Atende!")

			print("---------------------------------------")
			print("                                       ")

			print("[1] Resolucao - Parte 3 (3/4)")
			print("[2] SAIR")
			r23=int(input())

			if(r23==2):
				sys.exit(1)
			if(r23==1):

				print("                                       ")
				print("---------------------------------------")
				print("7. Verificacao da flexocompressao:")
				print("---------------------------------------")
				print("                                       ")

				print("Equacao 3")
				print("---------------------------------------")

				Eq3=((sigma_NcSd/fc0d)**2)+(sigma_MxSd/fmd)+(km*(sigma_MySd/fmd))
				print("Eq3 = {}".format(round(Eq3,3)))
				print("---------------------------------------")

				if Eq3>1:
					print("Eq3 > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Eq3 <= 1")
					print("---------------------------------------")
					print("Atende!")
				print("---------------------------------------")
				print("                                       ")

				print("Equacao 4")
				print("---------------------------------------")

				Eq4=((sigma_NcSd/fc0d)**2)+(sigma_MySd/fmd)+(km*(sigma_MxSd/fmd))
				print("Eq4 = {}".format(round(Eq4,3)))
				print("---------------------------------------")

				if Eq4>1:
					print("Eq4 > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Eq4 <= 1")
					print("---------------------------------------")
					print("Atende!")

				print("                                       ")
				print("---------------------------------------")
				print("8. Verificacao da tensao cisalhante:")
				print("---------------------------------------")
				print("                                       ")

				print("8.1. Ten. cis. prov. pel. for. atua. y:")
				print("---------------------------------------")
				print("                                       ")

				tau_VySd=(3/2)*(VySd/(b*h))
				print("tau_VySd = {} (kN/cm2)".format(round(tau_VySd,3)))
				print("---------------------------------------")

				Eq4y=tau_VySd/fvd
				print("Eq4y = {}".format(round(Eq4y,3)))
				print("---------------------------------------")

				if Eq4y>1:
					print("Eq4 > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Eq4y <= 1")
					print("---------------------------------------")
					print("Atende!")

				print("---------------------------------------")
				print("                                       ")

				print("8.2. Ten. cis. prov. pel. for. atua. x:")
				print("---------------------------------------")
				print("                                       ")

				tau_VxSd=(3/2)*(VxSd/(b*h))
				print("tau_VxSd = {} (kN/cm2)".format(round(tau_VxSd,3)))
				print("---------------------------------------")

				Eq4x=tau_VxSd/fvd
				print("Eq4x = {}".format(round(Eq4x,3)))
				print("---------------------------------------")

				if Eq4x>1:
					print("Eq4x > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Eq4x <= 1")
					print("---------------------------------------")
					print("Atende!")

				print("                                       ")
				print("---------------------------------------")
				print("9. Veri. da ten. perp. as fib. no apo.:")
				print("---------------------------------------")
				print("                                       ")

				print("9.1. Reacoes de apoio:")
				print("---------------------------------------")
				print("                                       ")

				Rdy=(qdy*L)/2
				print("Rdy = {} (kN)".format(round(Rdy,3)))
				print("---------------------------------------")

				Rdx=(qdx*L)/2
				print("Rdx = {} (kN)".format(round(Rdx,3)))
				print("---------------------------------------")

				print("                                       ")
				print("9.2. Areas de apoio da barra:")
				print("---------------------------------------")
				print("                                       ")

				A_apoio_Rdy=b*c
				print("A_apoio_Rdy = {} (cm2)".format(round(A_apoio_Rdy,3)))
				print("---------------------------------------")

				A_apoio_Rdx=h*c
				print("A_apoio_Rdx = {} (cm2)".format(round(A_apoio_Rdx,3)))
				print("---------------------------------------")

				print("                                       ")
				print("9.3. Tens. prov. pela forc. atua. em y:")
				print("---------------------------------------")
				print("                                       ")

				sigma_c90dy=Rdy/A_apoio_Rdy
				print("sigma_c90dy = {} (kN/cm2)".format(round(sigma_c90dy,3)))
				print("---------------------------------------")

				print("fc90d = {} (kN/cm2)".format(round(fc90d,3)))
				print("---------------------------------------")

				Eq5y=sigma_c90dy/fc90d
				print("Eq5y = {}".format(round(Eq5y,3)))
				print("---------------------------------------")

				if Eq5y>1:
					print("Eq5y > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Eq5y <= 1")
					print("---------------------------------------")
					print("Atende!")
				print("---------------------------------------")

				print("                                       ")
				print("9.4. Tens. prov. pela forc. atua. em x:")
				print("---------------------------------------")
				print("                                       ")

				sigma_c90dx=Rdx/A_apoio_Rdx
				print("sigma_c90dx = {} (kN/cm2)".format(round(sigma_c90dx,3)))
				print("---------------------------------------")

				print("fc90d = {} (kN/cm2)".format(round(fc90d,3)))
				print("---------------------------------------")

				Eq5x=sigma_c90dx/fc90d
				print("Eq5x = {}".format(round(Eq5x,3)))
				print("---------------------------------------")

				if Eq5x>1:
					print("Eq5x > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Eq5x <= 1")
					print("---------------------------------------")
					print("Atende!")
				print("---------------------------------------")

				print("                                       ")

				print("[1] Resolucao - Parte 4 (4/4)")
				print("[2] SAIR")
				r24=int(input())

				if(r24==2):
					sys.exit(1)
				if(r24==1):

					print("---------------------------------------")
					print("                                       ")
					print("10. Verific. da estabilidade lateral:")
					print("---------------------------------------")
					print("                                       ")

					Ec0ef=kmod*Ec0m
					print("Ec0ef = {} (kN/cm2)".format(round(Ec0ef,3)))
					print("---------------------------------------")

					Beta_m=(1/(0.26*math.pi))*(4/1.4)*(((h/b)**(1.5))/(((h/b)-0.63)**(1/2)))
					print("Beta_m = {}".format(round(Beta_m,3)))
					print("---------------------------------------")

					L1max=b*(Ec0ef/(Beta_m*fc0d))
					print("L1max = {} (cm)".format(round(L1max,3)))
					print("---------------------------------------")

					Verif_Est_late=(L*100)/L1max
					print("Verif_Est_late = {}".format(round(Verif_Est_late,3)))
					print("---------------------------------------")

					if Verif_Est_late>1:
						print("Verif_Est_late > 1")
						print("---------------------------------------")
						print("Nao atende!")
					else:
						print("Verif_Est_late <= 1")
						print("---------------------------------------")
						print("Atende!")
					print("---------------------------------------")

					print("                                       ")
					print("11. Verificacao da flecha instatanea:")
					print("---------------------------------------")
					print("                                       ")

					print("11.1. Deslo. inst. max. perm. p. nomr.:")
					print("---------------------------------------")
					print("                                       ")

					Delta_inst=(L*100)/300
					print("Delta_inst = {} (cm)".format(round(Delta_inst,3)))
					print("---------------------------------------")
					L=L*100
					g=g/100
					q=q/100
					w=w/100

					print("                                       ")
					print("11.2. Desl. inst. max. perm. pel. nor.:")
					print("---------------------------------------")
					print("                                       ")

					delta_instGky=(5*g*(L**4))/(384*Ec0m*Ix)
					print("delta_instGky = {} (cm)".format(round(delta_instGky,3)))
					print("---------------------------------------")

					delta_instQky=(5*q*(L**4))/(384*Ec0m*Ix)
					print("delta_instQky = {} (cm)".format(round(delta_instQky,3)))
					print("---------------------------------------")
					
					delta_instWkx=(5*w*(L**4))/(384*Ec0m*Ix)
					print("delta_instWkx = {} (cm)".format(round(delta_instWkx,3)))
					print("---------------------------------------")

					print("                                       ")
					print("11.3. Verif. dos desl. inst. em y:")
					print("---------------------------------------")
					print("                                       ")

					delta_insty=delta_instGky+delta_instQky
					print("delta_insty = {} (cm)".format(round(delta_insty,3)))
					print("---------------------------------------")

					Verif_delta_insty=delta_insty/Delta_inst
					print("Verif_delta_insty = {}".format(round(Verif_delta_insty,3)))
					print("---------------------------------------")

					if Verif_delta_insty>1:
						print("Verif_delta_insty > 1")
						print("---------------------------------------")
						print("Nao atende!")
					else:
						print("Verif_delta_insty <= 1")
						print("---------------------------------------")
						print("Atende!")
					print("---------------------------------------")

					print("                                       ")
					print("11.4. Verif. dos desl. inst. em x:")
					print("---------------------------------------")
					print("                                       ")

					delta_instx=delta_instWkx
					print("delta_instx = {} (cm)".format(round(delta_instx,3)))
					print("---------------------------------------")

					Verif_delta_instx=delta_instx/Delta_inst
					print("Verif_delta_instx = {}".format(round(Verif_delta_instx,3)))
					print("---------------------------------------")

					if Verif_delta_instx>1:
						print("Verif_delta_instx > 1")
						print("---------------------------------------")
						print("Nao atende!")
					else:
						print("Verif_delta_instx <= 1")
						print("---------------------------------------")
						print("Atende!")
					print("---------------------------------------")

					print("                                       ")
					print("12. Verificacao da flecha final:")
					print("---------------------------------------")
					print("                                       ")

					print("12.1. Deslo. fina. max. perm. p. nomr.:")
					print("---------------------------------------")
					print("                                       ")

					Delta_final=L/150
					print("Delta_final = {} (cm)".format(round(Delta_final,3)))
					print("---------------------------------------")

					print("                                       ")
					print("12.2. Deslo. fin. prov. pel. ac. atua.:")
					print("---------------------------------------")
					print("                                       ")

					delta_finalGky=delta_instGky*(1+fi)
					print("delta_finalGky = {} (cm)".format(round(delta_finalGky,3)))
					print("---------------------------------------")

					delta_finalQky=delta_instQky*(1+(fi*psi_2q))
					print("delta_finalQky = {} (cm)".format(round(delta_finalQky,3)))
					print("---------------------------------------")

					delta_finalWkx=delta_instWkx*(1+(fi*psi_2w))
					print("delta_finalWkx = {} (cm)".format(round(delta_finalWkx,3)))
					print("---------------------------------------")

					print("                                       ")
					print("12.3. Verifi. dos desloc. finais. em y:")
					print("---------------------------------------")
					print("                                       ")

					delta_finaly=delta_finalGky+delta_finalQky
					print("delta_finaly = {} (cm)".format(round(delta_finaly,3)))
					print("---------------------------------------")

					Verif_delta_finaly=delta_finaly/Delta_final
					print("Verif_delta_finaly = {}".format(round(Verif_delta_finaly,3)))
					print("---------------------------------------")

					if Verif_delta_finaly>1:
						print("Verif_delta_finaly > 1")
						print("---------------------------------------")
						print("Nao atende!")
					else:
						print("Verif_delta_finaly <= 1")
						print("---------------------------------------")
						print("Atende!")
					print("---------------------------------------")

					print("                                       ")
					print("12.4. Verifi. dos desloc. finais. em x:")
					print("---------------------------------------")
					print("                                       ")

					delta_finalx=delta_finalWkx
					print("delta_finalx = {} (cm)".format(round(delta_finalx,3)))
					print("---------------------------------------")

					Verif_delta_finalx=delta_finalx/Delta_final
					print("Verif_delta_finalx = {}".format(round(Verif_delta_finalx,3)))
					print("---------------------------------------")

					if Verif_delta_finalx>1:
						print("Verif_delta_finalx > 1")
						print("---------------------------------------")
						print("Nao atende!")
					else:
						print("Verif_delta_finalx <= 1")
						print("---------------------------------------")
						print("Atende!")
					print("---------------------------------------")
					print("                                       ")

	if acao==3:
		sys.exit(1)


