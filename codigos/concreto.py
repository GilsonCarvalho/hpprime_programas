import sys
import math

# Desenvolvido por Gilson Carvalho - Maceió - 2023
# Ainda falta comparar resultados com resolução feitas
# Falta adicionar os calculos de Vsd1 e Vsd2, no momento o scrip só realiza calculos com 1 Vsd

print("---------------------------------------")
print("---------------------------------------")
print("------- ESTRUTURAS DE CONCRETO 1 ------")
print("---------------------------------------")
print("---------------------------------------")
print("                                       ")

concreto=1
while concreto==1:
	print("Selecione a avaliacao bimestral: ")
	print("[1] (Icom) Resis. a compr. media na idade t")
	print("[2] Modu. de elast. p/ menos de 28 dias")
	print("[3] AB2.1")
	print("[4] AB2.2")
	print("[5] SAIR")
	acao=int(input())
	while (acao!=1 and acao!=2 and acao!=3 and acao!=4 and acao!=5):
		print("Escolha apenas um numero entre 1 e 5:")
		print("Selecione a avaliacao bimestral: ")
		print("[1] (Icom) Resis. a compr. media na idade t")
		print("[2] Modu. de elast. p/ menos de 28 dias")
		print("[3] AB2.1")
		print("[4] AB2.2")
		print("[5] SAIR")
		acao=int(input())
	if acao==1:
		print("                                       ")
		print("---------------------------------------")
		print("---------------------------------------")
		print("---- RESISTENCIA A COMPRESSAO MEDIA ---")
		print("-------------- NA IDADE T -------------")
		print("---------------------------------------")
		print("-------------- CAPITULO 1 -------------")
		print("---------------------------------------")
		print("---------------------------------------")
		print("                                       ")

		print("Insira o t (dia): ")
		t=float(input())
		print(t)
		print("---------------------------------------")

		print("Selecione o s: ")
		print("[1] Cimento CP V - ARI ")
		print("[2] Cimento CP I e II ")
		print("[3] Cimento CP III e IV ")
		print("[4] Inserir o s ")
		s=float(input())
		if s==1:
			s=0.2
		if s==2:
			s=0.25
		if s==3:
			s=0.38
		if s==4:
			print("Insira o s: ")
			s=float(input())
		print(s)
		print("---------------------------------------")

		print("Insira o fck (MPa): ")
		fck=float(input())
		print(fck)
		print("---------------------------------------")


		fcm_t=fcm*(math.e)**(s*(1-((28/(t/1))**(1/2))))
		print("fcm_t = {} (MPa)".format(round(fcm_t,3)))
		print("---------------------------------------")

	if acao==2:
		print("                                       ")
		print("---------------------------------------")
		print("---------------------------------------")
		print("----- MODULO DE ELASTICIDADE PARA  ----")
		print("----------- MENOS DE 28 DIAS ----------")
		print("---------------------------------------")
		print("-------------- CAPITULO 1 -------------")
		print("---------------------------------------")
		print("---------------------------------------")
		print("                                       ")

		print("Insira o fck (MPa): ")
		fck=float(input())
		print(fck)
		print("---------------------------------------")

		print("Selecione o alfa_E: ")
		print("[1] Basalto e diabasio ")
		print("[2] Granito e gnaisse ")
		print("[3] Calcario ")
		print("[4] Arenito ")
		print("[5] Inserir o alfa_E ")
		alfa_E=float(input())
		if alfa_E==1:
			alfa_E=0.2
		if alfa_E==2:
			alfa_E=0.25
		if alfa_E==3:
			alfa_E=0.38
		if alfa_E==4:
			print("Insira o alfa_E: ")
			alfa_E=float(input())
		print(s)
		print("---------------------------------------")


	if acao==3:
		print("                                       ")
		print("---------------------------------------")
		print("---------------------------------------")
		print("--- DIMENSIONAMENTO A FORCA CORTANTE --")
		print("---------------------------------------")
		print("-------------- CAPITULO 4 -------------")
		print("---------------------------------------")
		print("---------------------------------------")
		print("                                       ")

		print("Selecione o modelo: ")
		print("[1] Modelo de calculo I  ")
		print("[2] Modelo de calculo II ")

		modelo=int(input())
		if modelo==2:

			'''print("Insira o fck (Mpa): ")
			fck=float(input())
			print(fck)
			print("---------------------------------------")

			print("Insira o fywd (Mpa): ")
			fywd=float(input())
			print(fywd)
			print("---------------------------------------")

			print("Insira o fywk (Mpa): ")
			fywk=float(input())
			print(fywk)
			print("---------------------------------------")

			print("Insira o bw (cm): ")
			bw=float(input())
			print(bw)
			print("---------------------------------------")

			print("Insira o d (cm): ")
			d=float(input())
			print(d)
			print("---------------------------------------")

			print("Insira o c (cm): ")
			c=float(input())
			print(c)
			print("---------------------------------------")

			print("Insira o bitola do estribo (cm): ")
			bit=float(input())
			print(bit)
			print("---------------------------------------")

			print("Insira o teta (grau): ")
			teta=float(input())
			print(teta)
			print("---------------------------------------")

			print("Insira o alfa (grau): ")
			alfa=float(input())
			print(alfa)
			print("---------------------------------------")

			print("Insira Vsd (kN): ")
			Vsd1=float(input())
			print(Vsd1)
			print("---------------------------------------")'''

			fck=30
			bw=22
			d=74
			teta=37.5
			alfa=90
			Vsd=468
			fywd=43.5
			fywk=60
			c=3.5
			bit=0.8
			

			print("                                       ")
			print("---------------------------------------")
			print("---------------------------------------")
			print("--------- MODELO DE CALCULO II --------")
			print("---------------------------------------")
			print("---------------------------------------")
			print("                                       ")
			print("---------------------------------------")
			print("-*-*-*-*-*-*-*-RESOLUCAO-*-*-*-*-*-*-*")
			print("---------------------------------------")
			print("                                       ")
			print("---------------------------------------")
			print("1. Verificacao das bielas comprimidas:")
			print("---------------------------------------")
			print("                                       ")

			print("fck = {} (kN/cm2)".format(round(fck/10,3)))
			print("---------------------------------------")

			fcd=(fck/10)/1.4
			print("fcd = {} (kN/cm2)".format(round(fcd,3)))
			print("---------------------------------------")

			print("Vsd = {} (kN)".format(round(Vsd,3)))
			print("---------------------------------------")

			print("d = {} (cm)".format(round(d,3)))
			print("---------------------------------------")

			alfa_v2=1-(fck/250)
			print("alfa_v2 = {}".format(round(alfa_v2,3)))
			print("---------------------------------------")

			teta=teta*(math.pi/180)
			alfa=alfa*(math.pi/180)

			VRd2=0.54*alfa_v2*fcd*bw*d*((math.tan(alfa)**(-1))+(math.tan(teta)**(-1)))*(math.sin(teta)**2)
			print("VRd2 = {} (kN)".format(round(VRd2,3)))
			print("---------------------------------------")

			if (VRd2>Vsd):
				print("VRd2 > Vsd")
				print("---------------------------------------")
				print("As bielas nao serao esmagadas")
			else:
				print("VRd2 < Vsd")
				print("---------------------------------------")
				print("As bielas serao esmagadas")

			print("                                       ")
			print("---------------------------------------")
			print("2. Dimensi. das armaduras transversais:")
			print("---------------------------------------")
			print("                                       ")

			if (fck<=50):
				fctm=0.3*((fck**2)**(1/3))
				print("fctm = {} (Mpa)".format(round(fctm,3)))
			else:
				fctm=2.12*math.log(1+0.11*fck)
				print("fctm = {} (Mpa)".format(round(fctm,3)))
			print("---------------------------------------")

			fctk_inf=0.7*fctm
			print("fctk_inf = {} (Mpa)".format(round(fctk_inf,3)))
			print("---------------------------------------")

			fctd=fctk_inf/1.4
			print("fctd = {} (Mpa)".format(round(fctd,3)))
			print("---------------------------------------")

			Vc0=0.6*(fctd/10)*bw*d
			print("Vc0 = {} (kN)".format(round(Vc0,3)))
			print("---------------------------------------")

			if Vc0 < Vsd and Vsd < VRd2:
				print("Vc0 < Vsd < VRd2")
				print("---------------------------------------")

				Vc=Vc0*(VRd2-Vsd)/(VRd2-Vc0)
				print("Vc = {} (kN)".format(round(Vc,3)))
				print("---------------------------------------")

				print("Vc1 = Vc = {} (kN)".format(round(Vc,3)))
				print("---------------------------------------")
			else:
				print("Atencao!")
				print("Vc0 < Vsd < VRd2 (FALSO)")

			Vsw=Vsd-Vc
			print("Vsw = {} (kN)".format(round(Vsw,3)))
			print("---------------------------------------")

			Asw_s=Vsw/(0.9*d*fywd*((math.tan(alfa)**(-1))+(math.tan(teta)**(-1)))*math.sin(alfa))
			print("(Asw/s) = {} (cm2/cm)".format(round(Asw_s,3)))
			print("---------------------------------------")

			Asw_smin=0.2*(fctm/fywk)*bw*math.sin(alfa)
			print("(Asw/s)min = {} (cm2/cm)".format(round(Asw_smin/10,3)))
			print("---------------------------------------")

			Asw=(2*math.pi*(bit)**2)/4
			print("Asw = {} (cm2)".format(round(Asw,3)))
			print("---------------------------------------")

			s=Asw/Asw_s
			print("s = {} (cm)".format(round(s,3)))


			print("                                       ")
			print("---------------------------------------")
			print("3. Verific. espacamento longitudinal:")
			print("---------------------------------------")
			print("                                       ")


			print("0.67 * VRd2 = {} (kN)".format(round(0.67*VRd2,3)))
			print("---------------------------------------")

			if (Vsd<=(0.67*VRd2)):
				print("Vsd <= 0.67 * VRd2")
				print("---------------------------------------")
				smax=0.6*d
				print("smax = {} <= 30 (cm)".format(round(smax,3)))
				if smax>=30:
					smax=30
					print("---------------------------------------")
					print("Portanto o novo smax = {} (cm)".format(round(smax,3)))
				if(s>=smax):
					print("---------------------------------------")
					s=smax
					print("s>=smax")
					print("Portanto o s adotado sera {}".format(round(smax,3)))

			else:
				print("Vsd > 0.67 * VRd2")
				print("---------------------------------------")
				smax=0.3*d
				print("smax = {} <= 20 (cm)".format(round(smax,3)))
				if (smax>=20):
					smax=20
					print("---------------------------------------")
					print("Portanto o novo smax = {} (cm)".format(round(smax,3)))
				if(s>=smax):
					print("---------------------------------------")
					s=smax
					print("s>=smax")
					print("Portanto o s adotado sera {}".format(round(smax,3)))

			print("                                       ")
			print("---------------------------------------")
			print("4. Verific. espacamento transversal:")
			print("---------------------------------------")
			print("                                       ")

			print("0.2 * VRd2 = {} (kN)".format(round(0.2*VRd2,3)))
			print("---------------------------------------")

			st=bw-(2*c)-(2*bit/2)
			print("st = {} (cm)".format(round(st,3)))
			print("---------------------------------------")

			if (Vsd<=(0.2*VRd2)):
				print("Vsd <= 0.2 * VRd2")
				print("---------------------------------------")
				stmax=d
				print("smax = {} <= 80 (cm)".format(round(stmax,3)))
				if stmax>=80:
					stmax=80
					print("---------------------------------------")
					print("Portanto o novo stmax = {} (cm)".format(round(stmax,3)))
				if(st>=stmax):
					print("---------------------------------------")
					st=stmax
					print("st>=stmax")
					print("Portanto o st adotado sera {}".format(round(stmax,3)))

			else:
				print("Vsd > 0.2 * VRd2")
				print("---------------------------------------")
				stmax=0.6*d
				print("smax = {} <= 35 (cm)".format(round(stmax,3)))
				if(stmax>=35):
					stmax=35
					print("---------------------------------------")
					print("Portanto o novo stmax = {} (cm)".format(round(stmax,3)))
				if(st>=stmax):
					print("---------------------------------------")
					st=stmax
					print("st>=stmax")
					print("Portanto o st adotado sera {}".format(round(stmax,3)))

			print("                                       ")
			print("---------------------------------------")
			print("5. Esquematizacao dos balancos:")
			print("---------------------------------------")
			print("                                       ")

			print("Bitola {} c.{}".format(bit,round(s,2)))

			print("                                       ")
			print("---------------------------------------")
			print("6. Esquematizacao do vao:")
			print("---------------------------------------")
			print("                                       ")

			Vsw_min=0.9*d*Asw_smin*(fywd/10)*((math.tan(alfa)**(-1))+((math.tan(teta))**(-1)))*math.sin(alfa)
			print("Vsw_min = {} (kN)".format(round(Vsw_min,3)))
			print("---------------------------------------")

			Vsd_min=Vsw_min+Vc
			print("Vsd_min = {} (kN)".format(round(Vsd_min,3)))
			print("---------------------------------------")




			#end