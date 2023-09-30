#python export aco_ab2()
# -*- coding: utf-8 -*-
import sys
import math

# Desenvolvido por Gilson Carvalho - Maceio - 2023

aco=1
aco=1
while aco==1:
	print("---------------------------------------")
	print("---------- ESTRUTURAS DE ACO ----------")
	print("---------------------------------------")
	print("---------------- AB2 ------------------")
	print("---------------------------------------")
	print("--- Desenvolvido por GILSON CARVALHO --")
	print("                                       ")
	print("Selecione o exercicio: ")
	print("[1] FLEXAO SIMPLES PERFIL SOLDADO")
	print("[2] FLEXAO COMPOSTA PERFIL SOLDADO")
	print("[3] SAIR")
	acao2=int(input())

	if acao2==1:
		print("                                       ")
		print("---------------------------------------")
		print("---- FLEXAO SIMPLES PERFIL SOLDADO ----")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")

		print("                                       ")
		print("Carregamento e Coeficientes")
		print("---------------------------------------")

		#-----------------------------------------------------------------
		'''
		g0=1.5
		g1=7.5
		q=10
		P=30
		Ygg0=1.25
		Ygg1=1.4
		Yqq=1.5
		psi_1q=0.6
		psi_2q=0.4
		Yqp=1.5
		psi_1p=0.6
		psi_2p=0.4
		l=8
		lb=4
		a=4
		d=500
		bf=250
		tf=9.5
		tw=6.3
		Cb=1
		fy=25
		fr=0.3*fy
		E=20000
		G=7700
		'''

		#-------------------------------------------------------------

		print("Insira o g0 (kN/m): ")
		g0=float(input())
		print(g0)
		print("---------------------------------------")

		print("Insira o g1 (kN/m): ")
		g1=float(input())
		print(g1)
		print("---------------------------------------")

		print("Insira o q (kN/m): ")
		q=float(input())
		print(q)
		print("---------------------------------------")

		print("Insira o P (kN): ")
		P=float(input())
		print(P)
		print("---------------------------------------")

		print("Insira o Ygg0: ")
		Ygg0=float(input())
		print(Ygg0)
		print("---------------------------------------")

		print("Insira o Ygg1: ")
		Ygg1=float(input())
		print(Ygg1)
		print("---------------------------------------")

		print("Insira o Yqq: ")
		Yqq=float(input())
		print(Yqq)
		print("---------------------------------------")

		print("Insira o psi_1q: ")
		psi_1q=float(input())
		print(psi_1q)
		print("---------------------------------------")

		print("Insira o psi_2q: ")
		psi_2q=float(input())
		print(psi_2q)
		print("---------------------------------------")

		print("Insira o Yqp: ")
		Yqp=float(input())
		print(Yqp)
		print("---------------------------------------")

		print("Insira o psi_1p: ")
		psi_1p=float(input())
		print(psi_1p)
		print("---------------------------------------")

		print("Insira o psi_2p: ")
		psi_2p=float(input())
		print(psi_2p)
		print("---------------------------------------")

		print("                                       ")
		print("Comprimentos de flambagem")
		print("---------------------------------------")

		print("Insira o L (m): ")
		l=float(input())
		print(l)
		print("---------------------------------------")

		print("Insira o Lb (m): ")
		lb=float(input())
		print(lb)
		print("---------------------------------------")

		print("Insira o a (m): ")
		a=float(input())
		print(a)
		print("---------------------------------------")
		
		print("                                       ")
		print("Secao transversal e coeficientes")
		print("---------------------------------------")

		print("Insira o d (mm): ")
		d=float(input())
		print(d)
		print("---------------------------------------")

		print("Insira o bf (mm): ")
		bf=float(input())
		print(bf)
		print("---------------------------------------")

		print("Insira o tf (mm): ")
		tf=float(input())
		print(tf)
		print("---------------------------------------")

		print("Insira o tw (mm): ")
		tw=float(input())
		print(tw)
		print("---------------------------------------")

		print("Insira o Cb: ")
		Cb=float(input())
		print(Cb)
		print("---------------------------------------")

		print("                                       ")
		print("Propriedades do aco")
		print("---------------------------------------")

		print("Insira o fy (kN/cm2): ")
		fy=float(input())
		print(fy)
		print("---------------------------------------")
		fr=0.3*fy

		print("Insira o E (kN/cm2): ")
		E=float(input())
		print(E)
		print("---------------------------------------")

		print("Insira o G (kN/cm2): ")
		G=float(input())
		print(G)
		print("                                       ")


		print("---------------------------------------")
		print("[1] Resolucao - Parte 1 (1/6)")
		print("[2] SAIR")
		r11=int(input())

		if(r11==2):
			sys.exit(1)
		if(r11==1):

			print("                                       ")
			print("---------------------------------------")
			print("1. Dados do problema:")
			print("---------------------------------------")
			print("                                       ")
			print("Carregamento e Coeficientes")
			print("---------------------------------------")

			print("g0 = {} (kN/m)".format(g0))
			print("---------------------------------------")

			print("g1 = {} (kN/m)".format(g1))
			print("---------------------------------------")

			print("q = {} (kN/m)".format(q))
			print("---------------------------------------")

			print("P = {} (kN)".format(P))
			print("---------------------------------------")

			print("Ygg0 = {}".format(Ygg0))
			print("---------------------------------------")

			print("Ygg1 = {}".format(Ygg1))
			print("---------------------------------------")

			print("Yqq = {}".format(Yqq))
			print("---------------------------------------")

			print("psi_1q = {}".format(psi_1q))
			print("---------------------------------------")

			print("psi_2q = {}".format(psi_2q))
			print("---------------------------------------")

			print("Yqp = {}".format(Yqp))
			print("---------------------------------------")

			print("psi_1p = {}".format(psi_1p))
			print("---------------------------------------")

			print("psi_2p = {}".format(psi_2p))
			print("---------------------------------------")

			print("                                       ")
			print("Comprimentos de flambagem")
			print("---------------------------------------")

			print("L = {} (m)".format(l))
			print("---------------------------------------")

			print("Lb = {} (m)".format(lb))
			print("---------------------------------------")

			print("a = {} (m)".format(a))
			print("---------------------------------------")

			print("                                       ")
			print("Secao transversal e coeficientes")
			print("---------------------------------------")

			print("d = {} (mm)".format(d))
			print("---------------------------------------")

			print("bf = {} (mm)".format(bf))
			print("---------------------------------------")

			print("tf = {} (mm)".format(tf))
			print("---------------------------------------")

			print("tw = {} (mm)".format(tw))
			print("---------------------------------------")

			print("Cb = {}".format(Cb))
			print("---------------------------------------")

			print("                                       ")
			print("Propriedades do aco")
			print("---------------------------------------")

			print("fy = {} (kN/cm2)".format(fy))
			print("---------------------------------------")

			print("fr = {} (kN/cm2)".format(round(fr,3)))
			print("---------------------------------------")

			print("E = {} (kN/cm2)".format(E))
			print("---------------------------------------")

			print("G = {} (kN/cm2)".format(G))
			print("---------------------------------------")

			print("[1] Resolucao - Parte 2 (2/6)")
			print("[2] SAIR")
			r12=int(input())

			if(r12==2):
				sys.exit(1)
			if(r12==1):

				print("                                       ")
				print("---------------------------------------")
				print("2. Propri. geometri. da secao transv.:")
				print("---------------------------------------")
				print("                                       ")
		
				hw = d - 2 * tf
				print("hw = {} (mm)".format(round(hw,3)))
				print("---------------------------------------")

				Ag=(2*bf*tf+hw*tw)
				print("Ag = {} (cm2)".format(round(Ag/100,3)))
				print("---------------------------------------")

				Ix=((bf*tf**3)/12)+((tw*hw**3)/12)+2*bf*tf*((tf/2)+(hw/2))**2
				print("Ix = {} (cm4)".format(round(Ix/10000,3)))
				print("---------------------------------------")

				Iy=(2*tf*bf**3/12)+(hw*tw**3/12)
				print("Iy = {} (cm4)".format(round(Iy/10000),3))
				print("---------------------------------------")

				Wx=Ix*2/d
				print("Wx = {} (cm3)".format(round(Wx/1000,3)))
				print("---------------------------------------")

				Wy=Iy*2/bf
				print("Wy = {} (cm3)".format(round(Wy/1000,3)))
				print("---------------------------------------")

				rx=(Ix/Ag)**(1/2)
				print("rx = {} (cm)".format(round(rx/10,3)))
				print("---------------------------------------")

				ry=(Iy/Ag)**(1/2)
				print("ry = {} (cm)".format(round(ry/10,3)))
				print("---------------------------------------")

				Zx=(bf*tf*(d-tf))+(tw/4)*(d-2*tf)**2
				print("Zx = {} (cm3)".format(round(Zx/1000,3)))
				print("---------------------------------------")

				Zy=((bf**2)*tf/2)+(1/4)*(d-2*tf)*tw**2
				print("Zy = {} (cm3)".format(round(Zy/1000,3)))
				print("---------------------------------------")

				J=(1/3)*(2*bf*(tf**3)+hw*(tw**3))
				print("J = {} (cm4)".format(round(J/10000,3)))
				print("---------------------------------------")

				Cw=(((d-tf)**2)*Iy)/4
				print("Cw = {} (cm6)".format("{:.2e}".format(Cw/1000000)))
				print("---------------------------------------")

				x0=0
				y0=0
				r0=((rx**2)+(ry**2)+(x0**2)+(y0**2))**(1/2)
				print("r0 = {} (cm)".format(round(r0/10,3)))
				print("---------------------------------------")

				print("                                       ")
				print("[1] Resolucao - Parte 3 (3/6)")
				print("[2] SAIR")
				r13=int(input())

				if(r13==2):
					sys.exit(1)
				if(r13==1):

					print("                                       ")
					print("---------------------------------------")
					print("3. Esforcos de projeto:")
					print("---------------------------------------")
					print("                                       ")

					qd=Ygg0*g0+Ygg1*g1+Yqq*q
					print("qd = {} (kN/m)".format(qd))
					print("---------------------------------------")

					Pd=Yqp*P
					print("Pd = {} (kN)".format(Pd))
					print("---------------------------------------")

					MxSd=((qd*l**2)/8)+(Pd*l/4)
					print("MxSd = {} (kN.cm)".format(round(MxSd*100,3)))
					print("---------------------------------------")

					VySd=((qd*l)/2)+Pd/2
					print("VySd = {} (kN)".format(round(VySd,3)))
					print("---------------------------------------")

					print("                                       ")
					print("[1] Resolucao - Parte 4 (4/6)")
					print("[2] SAIR")
					r14=int(input())

					if(r14==2):
						sys.exit(1)
					if(r14==1):

						print("                                       ")
						print("---------------------------------------")
						print("4. Veri. do mome. flet. em rela. a x:")
						print("---------------------------------------")
						print("                                       ")

						print("4.1. Plastific. total da secao Transv.:")
						print("---------------------------------------")
						print("                                       ")

						Mpl=Zx*fy
						print("Mpl = {} (kN.cm)".format(round(Mpl/1000,3)))
						print("---------------------------------------")
						MxRdy=Mpl/1.1
						print("MxRdy = {} (kN.cm)".format(round(MxRdy/1000,3)))

						print("                                       ")
						print("---------------------------------------")
						print("4.2. Instabilidade local da mesa (FLM):")
						print("---------------------------------------")
						print("                                       ")

						Lamb_m=bf/(2*tf)
						print("Lamb_m = {}".format(round(Lamb_m,3)))
						print("---------------------------------------")
						if (4/((hw/tw)**(1/2)))>0.76:
							kc=0.76
							print("kc = {}".format(kc))
						else:
							if (4/((hw/tw)**(1/2)))<0.35:
								kc=0.35
								print("kc = {}".format(kc))
							else:
								kc=(4/((hw/tw)**(1/2)))
								print("kc = {}".format(round(kc,3)))
						print("---------------------------------------")
						Lamb_pm=0.38*(E/fy)**(1/2)
						print("Lamb_pm = {}".format(round(Lamb_pm,3)))
						print("---------------------------------------")
						Lamb_rm=0.95*(E/((fy-fr)/kc))**(1/2)
						print("Lamb_rm = {}".format(round(Lamb_rm,3)))
						print("---------------------------------------")
						MrFLM=(fy-fr)*Wx
						print("MrFLM = {} (kN/cm)".format(round(MrFLM/1000,3)))
						print("---------------------------------------")
						Mcrm=(0.9*E*kc*Wx)/(Lamb_m**2)
						print("Mcrm = {} (kN/cm)".format(round(Mcrm/1000,3)))
						print("---------------------------------------")
						Mrm=(fy-fr)*Wx
						print("Mrm = {} (kN/cm)".format(round(Mrm/1000,3)))
						print("---------------------------------------")
						if(Lamb_m<=Lamb_pm):
							print("Lamb_m <= Lamb_pm")
							print("---------------------------------------")
							print("Nao ha possibilidade de FLM!")
						else:
							if(Lamb_m>Lamb_rm):
								print("Lamb_m > Lamb_rm")
								print("---------------------------------------")
								print("Ha possibilidade de FLM em regime inelastico!")
							else:
								print("Ha possibilidade de FLM em regime inelastico!")
						print("---------------------------------------")
						if (Lamb_m<=Lamb_pm):
							MxRdFLM=Mpl/1.1
							print("Lamb_m <= Lamb_pm")
							print("---------------------------------------")
							print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLM/1000,3)))
						else:
							if (Lamb_m>Lamb_rm):
								MxRdFLM=Mcrm/1.1
								print("Lamb_m > Lamb_rm")
								print("---------------------------------------")
								print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLM/1000,3)))
							else:
								MxRdFLM=(Cb/1.1)*(Mpl-(Mpl-Mrm)*((Lamb_m-Lamb_pm)/(Lamb_rm-Lamb_pm)))
								print("Lamb_m <= Lamb_rm")
								print("---------------------------------------")
								print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLM/1000,3)))

						print("                                       ")
						print("---------------------------------------")
						print("4.3. Instabilidade local da alma (FLA):")
						print("---------------------------------------")
						print("                                       ")

						Lamb_w=hw/tw
						print("Lamb_w = {}".format(round(Lamb_w,3)))
						print("---------------------------------------")
						Lamb_pw=3.76*(E/fy)**(1/2)
						print("Lamb_pw = {}".format(round(Lamb_pw,3)))
						print("---------------------------------------")
						Lamb_rw=5.7*(E/fy)**(1/2)
						print("Lamb_rw = {}".format(round(Lamb_rw,3)))
						print("---------------------------------------")

						if (Lamb_w<=Lamb_pw):
							print("Lamb_w <= Lamb_pw")
							print("---------------------------------------")
							print("Nao ha possibilidade de FLA!")
						else:
							if (Lamb_w>Lamb_rw):
								print("Lamb_w > Lamb_rw")
								print("---------------------------------------")
								print("Atencao: viga de alma esbelta! Consultar a norma!")
							else:
								print("Lamb_w <= Lamb_rw")
								print("---------------------------------------")
								print("Ha possibilidade de FLA em regime inelastico!")

						print("---------------------------------------")
						Mrw=fy*Wx
						print("Mrw = {} (kN.cm)".format(round(Mrw/1000,3)))
						print("---------------------------------------")
						if (Lamb_w<=Lamb_pw):
							MxRdFLA=Mpl/1.1
							print("Lamb_w <= Lamb_pw")
							print("---------------------------------------")
							print("MxRdFLA = {} (kN.cm)".format(round(MxRdFLA/1000,3)))
						else:
							if (Lamb_w>Lamb_rw):
								MxRdFLA=0
								print("Lamb_w > Lamb_rw")
								print("---------------------------------------")
								print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLA/1000,3)))
							else:
								MxRdFLA=(Cb/1.1)*(Mpl-(Mpl-Mrw)*((Lamb_w-Lamb_pw)/(Lamb_rw-Lamb_pw)))
								print("Lamb_w <= Lamb_rw")
								print("---------------------------------------")
								print("MxRdFLA = {} (kN.cm)".format(round(MxRdFLA/1000,3)))

						print("                                       ")
						print("---------------------------------------")
						print("4.4. Insta. lateral com torcao (FLT):")
						print("---------------------------------------")
						print("                                       ")

						Lamb_b=(lb/ry)*1000
						print("Lamb_b = {}".format(round(Lamb_b,3)))
						print("---------------------------------------")

						Lamb_pb=1.76*(E/fy)**(1/2)
						print("Lamb_pb = {}".format(round(Lamb_pb,3)))
						print("---------------------------------------")

						Beta_1=((fy-fr)*Wx)/(E*J)
						print("Beta_1 = {} (m-1)".format(round(Beta_1*1000,3)))
						print("---------------------------------------")


						Lamb_rb=((1.38*((Iy*J)**(1/2)))/(ry*J*Beta_1))*((1+(((27*Cw*(Beta_1**2))/Iy)**(1/2)))**(1/2))
						print("Lamb_rb = {}".format(round(Lamb_rb,3)))
						print("---------------------------------------")

						if (Lamb_b<=Lamb_pb):
							print("Lamb_b <= Lamb_pb")
							print("---------------------------------------")
							print("Nao ha possibilidade de FLT!")
						else:
							if (Lamb_b>Lamb_rb):
								print("Lamb_b > Lamb_rb")
								print("---------------------------------------")
								print("Ha possibilidade de FLT em regime elastico!")
							else:
								print("Lamb_b <= Lamb_rb")
								print("---------------------------------------")
								print("Ha possibilidade de FLT em regime inelastico!")
						print("---------------------------------------")


						Mcrb=((Cb*math.pi*E*Iy)/(lb**2))*(((Cw/Iy)*(1+(0.039*J*(lb**2)/Cw)))**(1/2))
						print("Mcrb= = {} (kN.cm)".format(round(Mcrb/1000000000,3)))
						print("---------------------------------------")

						Mrb=(fy-fr)*Wx
						print("Mrb = {} (kN.cm)".format(round(Mrb/1000,3)))
						print("---------------------------------------")


						if (Lamb_b>Lamb_rb):
							MxRdFLT=Mcrb/1.1
							print("Lamb_b > Lamb_rb")
							print("---------------------------------------")
							print("MxRdFLT = {} (kN.cm)".format(round(MxRdFLT/1000,3)))
						else:
							if (Lamb_b<=Lamb_pb):
								MxRdFLT=Mpl/1.1
								print("Lamb_b <= Lamb_pb")
								print("---------------------------------------")
								print("MxRdFLT = {} (kN.cm)".format(round(MxRdFLT/1000,3)))
							else:
								MxRdFLT=(Cb/1.1)*(Mpl-(Mpl-Mrb)*((Lamb_b-Lamb_pb)/(Lamb_rb-Lamb_pb)))
								print("Lamb_b > Lamb_pb")
								print("---------------------------------------")
								print("MxRdFLT = {} (kN.cm)".format(round(MxRdFLT/1000,3)))

						print("                                       ")
						print("---------------------------------------")
						print("4.5. Verif. do Mome. Flet. Resi. em X:")
						print("---------------------------------------")
						print("                                       ")


						Mx1=[[round(MxRdy/100000,2)],[round(MxRdFLM/100000,2)],[round(MxRdFLA/100000,2)],[round(MxRdFLT/100000,2)]]
						Mx=[[MxRdy],[MxRdFLM],[MxRdFLA],[MxRdFLT]]
						menor = Mx[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
						for linha in Mx:
							for elemento in linha:
								if elemento < menor:
									menor = elemento
						MxRd=menor
						print("Mx = {} (kN.m)".format(Mx1))
						print("---------------------------------------")
						print("MxRd = {} (kN.cm)".format(round(MxRd/1000,3)))
						print("---------------------------------------")
						print("MxSd = {} (kN.cm)".format(MxSd*100))
						print("---------------------------------------")
						print("MxSd/MxRd = ",round(((MxSd*100)/(MxRd/1000)),3))
						print("---------------------------------------")

						if ((MxSd/MxRd)>1):
							print("MxSd / MxRd > 1")
							print("---------------------------------------")
							print("Nao atende!")
						else:
							print("MxSd / MxRd <= 1")
							print("---------------------------------------")
							print("Atende!")

						print("---------------------------------------")

						print("[1] Resolucao - Parte 5 (5/6)")
						print("[2] SAIR")
						r15=int(input())

						if(r15==2):
							sys.exit(1)
						if(r15==1):

							print("                                       ")
							print("---------------------------------------")
							print("5. Verif. do Esfor. Cort. Resist. em Y:")
							print("---------------------------------------")
							print("                                       ")

							print("a/hw = {}".format(round((a/hw)*1000,3)))
							print("---------------------------------------")

							if ((a/hw)*1000>3):
								kv=5
								print("a / hw > 3")
								print("---------------------------------------")
								print("kv = {}".format(kv))
							else:
								kv=5+(5/((a/hw)*1000)**2)
								print("a / hw <= 3")
								print("---------------------------------------")
								print("kv = {}".format(round(kv,3)))
							print("---------------------------------------")

							Lamb_wv=hw/tw
							print("Lamb_wv = {}".format(round(Lamb_wv,3)))
							print("---------------------------------------")

							Lamb_pv=1.1*(kv*E/fy)**(1/2)
							print("Lamb_pv = {}".format(round(Lamb_pv,3)))
							print("---------------------------------------")

							Lamb_rv=1.37*(kv*E/fy)**(1/2)
							print("Lamb_rv = {}".format(round(Lamb_rv,3)))
							print("---------------------------------------")

							if (Lamb_wv<=Lamb_pv):
								print("Lamb_wv <= Lamb_pv")
								print("---------------------------------------")
								print("Forma de colapso: escoamento da alma por cisalhamento!")
							else:
								if (Lamb_wv>Lamb_rv):
									print("Lamb_wv > Lamb_rv")
									print("---------------------------------------")
									print("Forma de colapso: flambagem elastica da alma por cisalhamento!")
								else:
									print("Lamb_wv <= Lamb_rv")
									print("---------------------------------------")
									print("Forma de colapso: flambagem inelastica da alma por cisalhamento!")
							print("---------------------------------------")

							Aw=d*tw
							print("Aw = {} (cm2)".format(round(Aw/100,3)))
							print("---------------------------------------")

							Vpl=0.6*Aw*fy
							print("Vpl = {} (kN)".format(round(Vpl/100,3)))
							print("---------------------------------------")

							if (Lamb_wv<=Lamb_pv):
								VyRd=Vpl/1.1
								print("Lamb_wv <= Lamb_pv")
								print("---------------------------------------")
								print("VyRd = {} (kN)".format(round(VyRd/100,3)))
							else:
								if (Lamb_wv>Lamb_rv):
									VyRd=(1/1.1)*1.24*((Lamb_pv/Lamb_wv)**2)*Vpl
									print("Lamb_wv > Lamb_rv")
									print("---------------------------------------")
									print("VyRd = {} (kN)".format(round(VyRd/100,3)))
								else:
									VyRd=(1/1.1)*(Lamb_pv/Lamb_wv)*Vpl
									print("Lamb_wv <= Lamb_rv")
									print("---------------------------------------")
									print("VyRd = {} (kN)".format(round(VyRd/100,3)))
							print("---------------------------------------")

							print("VySd = {} (kN)".format(round(VySd,3)))
							print("---------------------------------------")

							print("VySd/VyRd = {}".format(round((VySd/VyRd)*100,3)))
							print("---------------------------------------")
							
							if ((VySd/VyRd)*100>1):
								print("VySd / VyRd > 1")
								print("---------------------------------------")
								print("Não atende!")
							else:
								print("VySd / VyRd <= 1")
								print("---------------------------------------")
								print("Atende!")

							print("---------------------------------------")

							print("[1] Resolucao - Parte 6 (6/6)")
							print("[2] SAIR")
							r16=int(input())

							if(r16==2):
								sys.exit(1)
							if(r16==1):

								print("                                       ")
								print("---------------------------------------")
								print("6. Verif. do desl. em rela. ao eixo Y:")
								print("---------------------------------------")
								print("                                       ")

								print("6.1. Desloca. limi. permit. pela norma:")
								print("---------------------------------------")
								print("                                       ")

								delta1_y=l/350
								print("delta1_y = {} (cm)".format(round(delta1_y*100,3)))

								print("                                       ")
								print("---------------------------------------")
								print("6.2. Desloca. provoc. pelos carregame.:")
								print("---------------------------------------")
								print("                                       ")

								delta_g0=(5*g0*l**4)/(384*E*Ix)
								print("delta_g0 = {} (cm)".format(round(delta_g0*1e10,3)))
								print("---------------------------------------")

								delta_g1=(5*g1*l**4)/(384*E*Ix)
								print("delta_g1 = {} (cm)".format(round(delta_g1*1e10,3)))
								print("---------------------------------------")
								delta_q=(5*q*l**4)/(384*E*Ix)
								print("delta_q = {} (cm)".format(round(delta_q*1e10,3)))
								print("---------------------------------------")
								delta_p=(P*l**3)/(48*E*Ix)
								print("delta_p = {} (cm)".format(round(delta_p*1e10,3)))
								
								print("---------------------------------------")
								print("                                       ")
								print("Combinacao 1")
								print("---------------------------------------")

								delta_y1=delta_g0+delta_g1+psi_1q*delta_q+psi_2p*delta_p
								print("delta_y1 = {} (cm)".format(round(delta_y1*1e10,3)))

								print("---------------------------------------")
								print("                                       ")
								print("Combinacao 2")
								print("---------------------------------------")

								delta_y2=delta_g0+delta_g1+psi_1p*delta_p+psi_2q*delta_q
								print("delta_y2 = {} (cm)".format(round(delta_y2*1e10,3)))

								print("---------------------------------------")
								print("                                       ")
								print("Deslocamento maximo")
								print("---------------------------------------")

								if (delta_y1>delta_y2):
									delta_y=delta_y1
									print("delta_y1 > delta_y2")
									print("---------------------------------------")
									print("delta_y = delta_y1 = {} (cm)".format(round(delta_y*1e10,3)))
								else:
									delta_y=delta_y2
									print("delta_y1 <= delta_y2")
									print("---------------------------------------")
									print("delta_y = delta_y2 = {} (cm)".format(round(delta_y*1e10,3)))
								print("---------------------------------------")
								print("delta_y = {} (cm)".format(round(delta_y*1e10,3)))
								print("---------------------------------------")
								print("delta1_y = {} (cm)".format(round(delta1_y*100,3)))

								print("---------------------------------------")
								print("                                       ")
								print("Verificacao do deslocamento maximo")
								print("---------------------------------------")

								print("delta_y / delta1_y = {}".format(round((delta_y/delta1_y)*1e8,3)))
								print("---------------------------------------")

								if((delta_y/delta1_y)>1):
									print("delta_y / delta1_y > 1")
									print("---------------------------------------")
									print("Nao atende!")
								else:
									print("delta_y / delta1_y <= 1")
									print("---------------------------------------")
									print("Atende!")
								print("---------------------------------------")
								print("                                       ")

	if acao2==2:
		print("                                       ")
		print("---------------------------------------")
		print("---- FLEXAO COMPOSTA PERFIL SOLDADO ---")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")

		print("                                       ")
		print("Informacoes preliminares")
		print("---------------------------------------")

		
		'''
		L=10
		H=4.5
		N1=270
		N2=410
		M1=120
		M2=85
		M3=100
		M4=60

		NtSd=N1
		MxSd1=M1
		NcSd=N2
		MxSd2=M3

		kxLx=H
		kyLy=H
		kzLz=0.7*H
		Lb=H

		d=250
		bf=250
		tf=12.5
		tw=8
		Cb=1
		fy=25
		fr=0.3*fy
		E=20000
		G=7700

		'''

		#-------------------------------------------------------------

		print("Insira o L (m): ")
		L=float(input())
		print(L)
		print("---------------------------------------")

		print("Insira o H (m): ")
		H=float(input())
		print(H)
		print("---------------------------------------")

		print("Insira o N1 (kN): ")
		N1=float(input())
		print(N1)
		print("---------------------------------------")

		print("Insira o N2 (kN): ")
		N2=float(input())
		print(N2)
		print("---------------------------------------")

		print("Insira o M1 (kN.m): ")
		M1=float(input())
		print(M1)
		print("---------------------------------------")

		print("Insira o M2 (kN.m): ")
		M2=float(input())
		print(M2)
		print("---------------------------------------")

		print("Insira o M3 (kN.m): ")
		M3=float(input())
		print(M3)
		print("---------------------------------------")

		print("Insira o M4 (kN.m): ")
		M4=float(input())
		print(M4)
		print("---------------------------------------")

		print("                                       ")
		print("Secao transversal e coeficientes")
		print("---------------------------------------")

		print("Insira o d (mm): ")
		d=float(input())
		print(d)
		print("---------------------------------------")

		print("Insira o bf (mm): ")
		bf=float(input())
		print(bf)
		print("---------------------------------------")

		print("Insira o tf (mm): ")
		tf=float(input())
		print(tf)
		print("---------------------------------------")

		print("Insira o tw (mm): ")
		tw=float(input())
		print(tw)
		print("---------------------------------------")

		print("Insira o Cb: ")
		Cb=float(input())
		print(Cb)
		print("---------------------------------------")

		print("                                       ")
		print("Propriedades do aco")
		print("---------------------------------------")

		print("Insira o fy (kN/cm2): ")
		fy=float(input())
		print(fy)
		print("---------------------------------------")

		print("Insira o E (kN/cm2): ")
		E=float(input())
		print(E)
		print("---------------------------------------")

		print("Insira o G (kN/cm2): ")
		G=float(input())
		print(G)
		

		print("---------------------------------------")
		print("                                       ")
		print("[1] Resolucao - Parte 1 (1/4)")
		print("[2] SAIR")
		r21=int(input())

		if(r21==2):
			sys.exit(1)
		if(r21==1):
		

			print("                                       ")
			print("---------------------------------------")
			print("1. Dados do problema:")
			print("---------------------------------------")
			print("                                       ")

			print("Informacoes preliminares")
			print("---------------------------------------")

			print("L = {} (m)".format(L))
			print("---------------------------------------")

			print("H = {} (m)".format(H))
			print("---------------------------------------")

			print("N1 = {} (kN)".format(N1))
			print("---------------------------------------")

			print("N2 = {} (kN)".format(N2))
			print("---------------------------------------")

			print("M1 = {} (kN.m)".format(M1))
			print("---------------------------------------")

			print("M2 = {} (kN.m)".format(M2))
			print("---------------------------------------")

			print("M3 = {} (kN.m)".format(M3))
			print("---------------------------------------")

			print("M4 = {} (kN.m)".format(M4))
			print("---------------------------------------")
			print("                                       ")

			print("Esforcos solicitantes")
			print("---------------------------------------")

			NtSd=N1
			print("NtSd = {} (kN)".format(NtSd))
			print("---------------------------------------")

			MxSd1=M1
			print("MxSd1 = {} (kN.m)".format(MxSd1))
			print("---------------------------------------")

			NcSd=N2
			print("NcSd = {} (kN)".format(NcSd))
			print("---------------------------------------")

			MxSd2=M3
			print("MxSd2 = {} (kN.m)".format(MxSd2))
			print("---------------------------------------")
			print("                                       ")

			print("Comprimentos de flambagem")
			print("---------------------------------------")

			kxLx=100*H
			print("kxLx = {} (cm)".format(round(kxLx,3)))
			print("---------------------------------------")

			kyLy=100*H
			print("kyLy = {} (cm)".format(round(kyLy,3)))
			print("---------------------------------------")

			kzLz=0.7*100*H
			print("kzLz = {} (cm)".format(round(kzLz,3)))
			print("---------------------------------------")

			Lb=100*H
			print("Lb = {} (cm)".format(round(Lb,3)))
			print("---------------------------------------")
			print("                                       ")

			print("Secao transversal e coeficientes")
			print("---------------------------------------")

			print("d = {} (mm)".format(d))
			print("---------------------------------------")

			print("bf = {} (mm)".format(bf))
			print("---------------------------------------")

			print("tf = {} (mm)".format(tf))
			print("---------------------------------------")

			print("tw = {} (mm)".format(tw))
			print("---------------------------------------")

			print("Cb = {}".format(Cb))
			print("---------------------------------------")
			print("                                       ")

			print("Propriedades do aco")
			print("---------------------------------------")

			print("fy = {} (kN/cm2)".format(fy))
			print("---------------------------------------")

			print("E = {} (kN/cm2)".format(E))
			print("---------------------------------------")

			print("G = {} (kN/cm2)".format(G))
			print("---------------------------------------")

			fr=0.3*fy
			print("fr = {} (kN/cm2)".format(round(fr,3)))

			print("                                       ")
			print("---------------------------------------")
			print("2. Proprie. geomet. da secao transv.:")
			print("---------------------------------------")
			print("                                       ")

			hw=d-2*tf
			print("hw = {} (mm)".format(round(hw,3)))
			print("---------------------------------------")

			Ag=2*bf*tf+hw*tw
			print("Ag = {} (cm2)".format(round(Ag/100,3)))
			print("---------------------------------------")

			Ix=((bf*tf**3)/12)+((tw*hw**3)/12)+2*bf*tf*(((tf/2)+(hw/2))**2)
			print("Ix = {} (cm4)".format(round(Ix/10000,3)))
			print("---------------------------------------")

			Iy=2*((tf*bf**3)/12)+((hw*tw**3)/12)
			print("Iy = {} (cm4)".format(round(Iy/10000,3)))
			print("---------------------------------------")

			Wx=Ix*(2/d)
			print("Wx = {} (cm3)".format(round(Wx/1000,3)))
			print("---------------------------------------")

			Wy=Iy*(2/bf)
			print("Wy = {} (cm3)".format(round(Wy/1000,3)))
			print("---------------------------------------")

			rx=(Ix/Ag)**(1/2)
			print("rx = {} (cm)".format(round(rx/10,3)))
			print("---------------------------------------")

			ry=(Iy/Ag)**(1/2)
			print("ry = {} (cm)".format(round(ry/10,3)))
			print("---------------------------------------")

			Zx=bf*tf*(d-tf)+(tw/4)*((d-2*tf)**2)
			print("Zx = {} (cm3)".format(round(Zx/1000,3)))
			print("---------------------------------------")

			Zy=(((bf**2)*tf)/2)+(1/4)*(d-2*tf)*(tw**2)
			print("Zy = {} (cm3)".format(round(Zy/1000,3)))
			print("---------------------------------------")

			J=(1/3)*(2*bf*(tf**3)+hw*(tw**3))
			print("J = {} (cm4)".format(round(J/10000,3)))
			print("---------------------------------------")

			Cw=(((d-tf)**2)*Iy)/4
			print("Cw = {:.3e} (cm6)".format(Cw/1000000))
			print("---------------------------------------")

			x0=0
			y0=0
			r0=((rx**2)+(ry**2)+(x0**2)+(y0**2))**(1/2)
			print("r0 = {} (cm)".format(round(r0/10,3)))

			print("                                       ")
			print("---------------------------------------")
			print("3. Verificacao dos esforcos de tracao:")
			print("---------------------------------------")
			print("                                       ")

			NtRd=((Ag*fy)/1.1)/100
			print("NtRd = {} (kN)".format(round(NtRd,3)))
			print("---------------------------------------")

			print("NtSd = {} (kN)".format(round(NtSd,3)))
			print("---------------------------------------")

			print("NtSd / NtRd = {}".format(round(NtSd/NtRd,3)))
			print("---------------------------------------")

			if (NtSd/NtRd)>1:
				print("(NtSd/NtRd) > 1")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("(NtSd/NtRd) <= 1")
				print("---------------------------------------")
				print("Atende!")

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
				print("4. Verifica. do esforco de compresssao:")
				print("---------------------------------------")
				print("                                       ")

				print("4.1. Estabilidade local:")
				print("---------------------------------------")
				print("                                       ")

				print("Mesas")
				print("---------------------------------------")

				Lamb_m=bf/(2*tf)
				print("Lamb_m = {}".format(round(Lamb_m,3)))
				print("---------------------------------------")

				kc1=4/((hw/tw)**(1/2))
				print("kc1 = {}".format(round(kc1,3)))
				print("---------------------------------------")

				if kc1>0.76:
					kc=0.76
					print("kc = {}".format(round(kc,3)))
					print("---------------------------------------")
				else:
					if kc1<0.35:
						kc=0.35
						print("kc = {}".format(round(kc,3)))
						print("---------------------------------------")
					else:
						kc=kc1
						print("kc = kc1")
						print("---------------------------------------")
						print("kc = {}".format(round(kc,3)))
						print("---------------------------------------")

				Lamb_pm=0.64*((E/(fy/kc))**(1/2))
				print("Lamb_pm = {}".format(round(Lamb_pm,3)))
				print("---------------------------------------")

				Lamb_rm=1.17*((E/(fy/kc))**(1/2))
				print("Lamb_rm = {}".format(round(Lamb_rm,3)))
				print("---------------------------------------")

				if Lamb_m>Lamb_rm:
					Qs=(0.9*E*kc)/(fy*(Lamb_m**2))
					print("Qs = {}".format(round(Qs,3)))
					print("---------------------------------------")
				else:
					if Lamb_m<=Lamb_pm:
						Qs=1
						print("Qs = {}".format(round(Qs,3)))
						print("---------------------------------------")
					else:
						Qs=1.415-(0.65*Lamb_m*((fy/(kc*E))**(1/2)))
						print("Qs = {}".format(round(Qs,3)))
						print("---------------------------------------")

				print("                                       ")
				print("Alma")
				print("---------------------------------------")

				Lamb_w=hw/tw
				print("Lamb_w = {}".format(round(Lamb_w,3)))
				print("---------------------------------------")

				Lamb_pw=1.49*((E/fy)**(1/2))
				print("Lamb_pw = {}".format(round(Lamb_pw,3)))
				print("---------------------------------------")

				Ca=0.34
				print("Ca = {}".format(Ca))
				print("---------------------------------------")

				sigma=fy
				print("sigma = fy")
				print("---------------------------------------")
				print("sigma = {} (kN/cm2)".format(sigma))
				print("---------------------------------------")

				bef1=1.92*tw*(((E/sigma)*(1-(Ca/Lamb_w)*((E/sigma)**(1/2))))**(1/2))
				print("bef1 = {} (cm)".format(round(bef1/10,3)))
				print("---------------------------------------")

				print("hw = {} (cm)".format(round(hw/10,3)))
				print("---------------------------------------")

				if bef1>hw:
					bef=hw
					print("bef = {} (cm)".format(round(bef/10,3)))
					print("---------------------------------------")
				else:
					bef=bef1
					print("bef = {} (cm)".format(round(bef/10,3)))
					print("---------------------------------------")

				Aef=Ag-(hw-bef)*tw
				print("Aef = {} (cm2)".format(round(Aef/100,3)))
				print("---------------------------------------")

				if Lamb_w>Lamb_pw:
					Qa=1
					print("Qa = {}".format(Qa))
					print("---------------------------------------")
				else:
					Qa=Aef/Ag
					print("Qa = {}".format(round(Qa,3)))
					print("---------------------------------------")

				print("                                       ")
				print("Coeficiente Q")
				print("---------------------------------------")

				Q=Qs*Qa
				print("Q = {}".format(round(Q,3)))

				print("                                       ")
				print("---------------------------------------")
				print("4.2. Estabilidade global:")
				print("---------------------------------------")
				print("                                       ")

				Nex=(((math.pi**2)*E*Ix)/(kxLx**2))/10000
				print("Nex = {} (kN)".format(round(Nex,3)))
				print("---------------------------------------")

				Ney=(((math.pi**2)*E*Iy)/(kyLy**2))/10000
				print("Ney = {} (kN)".format(round(Ney,3)))
				print("---------------------------------------")

				Nez=(1/((r0/10)**2))*((((math.pi**2)*E*(Cw/1000000))/((kzLz)**2))+((J/10000)*G))
				print("Nez = {} (kN)".format(round(Nez,3)))
				print("---------------------------------------")

				NeI=[[int(Nex)],[int(Ney)],[int(Nez)]]
				NeI1=[[Nex],[Ney],[Nez]]
				menor = NeI1[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
				for linha in NeI1:
					for elemento in linha:
						if elemento < menor:
							menor = elemento
				Ne=menor
				print("NeI = {} (kN)".format(NeI))
				print("---------------------------------------")
				
				print("Ne = {} (kN)".format(round(Ne,3)))
				print("---------------------------------------")

				Lamb_0=(((Q*Ag*fy)/Ne)**(1/2))/10
				print("Lamb_0 = {}".format(round(Lamb_0,3)))
				print("---------------------------------------")

				if Lamb_0>1.5:
					X=(0.877/(Lamb_0**2))
					print("Lamb_0 > 1.5")
					print("---------------------------------------")
					print("X = {}".format(round(X,3)))
				else:
					X=0.658**(Lamb_0**2)
					print("Lamb_0 <= 1.5")
					print("---------------------------------------")
					print("X = {}".format(round(X,3)))

				print("                                       ")
				print("---------------------------------------")
				print("4.3. Verificacao do esforco resistente:")
				print("---------------------------------------")
				print("                                       ")

				NcRd=((Q*X*Ag*fy)/1.1)/100
				print("NcRd = {} (kN)".format(round(NcRd,3)))
				print("---------------------------------------")

				print("NcSd = {} (kN)".format(round(NcSd,3)))
				print("---------------------------------------")

				print("NcSd / NcRd = {}".format(round(NcSd/NcRd,3)))
				print("---------------------------------------")

				if (NcSd/NcRd)>1:
					print("(NcSd/NcRd) > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("(NcSd/NcRd) <= 1")
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
					print("4.4. Verificacao da esbeltez maxima:")
					print("---------------------------------------")
					print("                                       ")

					Lamb_x=(kxLx/rx)*10
					print("Lamb_x = {}".format(round(Lamb_x,3)))
					print("---------------------------------------")

					Lamb_y=(kyLy/ry)*10
					print("Lamb_y = {}".format(round(Lamb_y,3)))
					print("---------------------------------------")

					if Lamb_x>Lamb_y:
						Lamb_max=Lamb_x
						print("Lamb_x > Lamb_y")
						print("---------------------------------------")
						print("Lamb_max = {}".format(round(Lamb_max,3)))
					else:
						Lamb_max=Lamb_y
						print("Lamb_x <= Lamb_y")
						print("---------------------------------------")
						print("Lamb_max = {}".format(round(Lamb_max,3)))

					Lamb_lim=200
					print("---------------------------------------")
					print("Lamb_lim = {}".format(round(Lamb_lim,3)))
					print("---------------------------------------")

					if Lamb_max>Lamb_lim:
						print("Lamb_max > Lamb_lim")
						print("---------------------------------------")
						print("Nao atende!")
					else:
						print("Lamb_max <= Lamb_lim")
						print("---------------------------------------")
						print("Atende!")
					
					print("                                       ")
					print("---------------------------------------")
					print("5. Verif. do momen. flet. em rela. a x:")
					print("---------------------------------------")
					print("                                       ")

					print("5.1. Plastif. total da secao Transv.:")
					print("---------------------------------------")
					print("                                       ")

					Mpl=(Zx*fy)/1000
					print("Mpl = {} (kN.cm)".format(round(Mpl,3)))
					print("---------------------------------------")

					MxRdy=Mpl/1.1
					print("MxRdy = {} (kN.cm)".format(round(MxRdy,3)))

					print("                                       ")
					print("---------------------------------------")
					print("5.2. Instabilidade local da mesa (FLM):")
					print("---------------------------------------")
					print("                                       ")

					Lamb_m=bf/(2*tf)
					print("Lamb_m = {}".format(round(Lamb_m,3)))
					print("---------------------------------------")

					Lamb_pm=0.38*((E/fy)**(1/2))
					print("Lamb_pm = {}".format(round(Lamb_pm,3)))
					print("---------------------------------------")

					Lamb_rm=0.95*((E/((fy-fr)/kc))**(1/2))
					print("Lamb_rm = {}".format(round(Lamb_rm,3)))
					print("---------------------------------------")

					MrFLM=((fy-fr)*Wx)/1000
					print("MrFLM = {} (kN.cm)".format(round(MrFLM,3)))
					print("---------------------------------------")

					Mcrm=((0.9*E*kc*Wx)/(Lamb_m**2))/1000
					print("Mcrm = {:.3e} (kN.cm)".format(round(Mcrm,3)))
					print("---------------------------------------")

					Mrm=((fy-fr)*Wx)/1000
					print("Mrm = {} (kN.cm)".format(round(Mrm,3)))
					print("---------------------------------------")

					if Lamb_m<=Lamb_pm:
						MxRdFLM=Mpl/1.1
						print("Lamb_m <= Lamb_pm")
						print("---------------------------------------")
						print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLM,3)))
					else:
						if Lamb_m>Lamb_rm:
							MxRdFLM=Mcrm/1.1
							print("Lamb_m > Lamb_rm")
							print("---------------------------------------")
							print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLM,3)))
						else:
							MxRdFLM=(Cb/1.1)*(Mpl-(Mpl-Mrm)*((Lamb_m-Lamb_pm)/(Lamb_rm-Lamb_pm)))
							print("Lamb_m <= Lamb_rm")
							print("---------------------------------------")
							print("MxRdFLM = {} (kN.cm)".format(round(MxRdFLM,3)))

					print("                                       ")
					print("---------------------------------------")
					print("5.3. Instabilidade local da alma (FLA):")
					print("---------------------------------------")
					print("                                       ")

					Lamb_w=hw/tw
					print("Lamb_w = {}".format(round(Lamb_w,3)))
					print("---------------------------------------")

					Lamb_pw=3.76*((E/fy)**(1/2))
					print("Lamb_pw = {}".format(round(Lamb_pw,3)))
					print("---------------------------------------")

					Lamb_rw=5.7*((E/fy)**(1/2))
					print("Lamb_rw = {}".format(round(Lamb_rw,3)))
					print("---------------------------------------")

					Mrw=(fy*Wx)/1000
					print("Mrw = {} (kN.cm)".format(round(Mrw,3)))
					print("---------------------------------------")

					if Lamb_w<=Lamb_pw:
						MxRdFLA=Mpl/1.1
						print("Lamb_w <= Lamb_pw")
						print("---------------------------------------")
						print("MxRdFLA = {} (kN.cm)".format(round(MxRdFLA,3)))
					else:
						if Lamb_w>Lamb_rw:
							MxRdFLA=0
							print("Lamb_w > Lamb_rw")
							print("---------------------------------------")
							print("MxRdFLA = {} (kN.cm)".format(round(MxRdFLA,3)))
						else:
							MxRdFLA=(Cb/1.1)*(Mpl-(Mpl-Mrw)*((Lamb_w-Lamb_pw)/(Lamb_rw-Lamb_pw)))
							print("Lamb_w <= Lamb_rw")
							print("---------------------------------------")
							print("MxRdFLA = {} (kN.cm)".format(round(MxRdFLA,3)))

					print("                                       ")
					print("---------------------------------------")
					print("5.4. Instab. lateral com torcao (FLT):")
					print("---------------------------------------")
					print("                                       ")

					Lamb_b=(Lb/ry)*10
					print("Lamb_b = {}".format(round(Lamb_b,3)))
					print("---------------------------------------")

					Lamb_pb=1.76*((E/fy)**(1/2))
					print("Lamb_pb = {}".format(round(Lamb_pb,3)))
					print("---------------------------------------")

					Beta_1=((fy-fr)*(Wx/1000))/(E*(J/10000))
					print("Beta_1 = {} (1/m)".format(round(Beta_1*100,3)))
					print("---------------------------------------")

					Lamb_rb=((1.38*(((Iy/10000)*(J/10000))**(1/2)))/((ry/10)*(J/10000)*Beta_1))*((1+(((27*(Cw/1000000)*(Beta_1**2))/(Iy/10000))**(1/2)))**(1/2))
					print("Lamb_rb = {}".format(round(Lamb_rb,3)))
					print("---------------------------------------")

					Mcrb=((Cb*math.pi*E*(Iy/10000))/(Lb**2))*((((Cw/1000000)/(Iy/10000))*(1+0.039*(((J/10000)*(Lb**2))/(Cw/1000000))))**(1/2))
					print("Mcrb = {}".format(round(Mcrb,3)))
					print("---------------------------------------")

					Mrb=((fy-fr)*Wx)/1000
					print("Mrb = {} (kN.cm)".format(round(Mrb,3)))
					print("---------------------------------------")

					if Lamb_b>Lamb_rb:
						MxRdFLT=Mcrm/1.1
						print("Lamb_b > Lamb_rb")
						print("---------------------------------------")
						print("MxRdFLT = {} (kN.cm)".format(round(MxRdFLT,3)))

					else:
						if Lamb_b<=Lamb_pb:
							MxRdFLT=Mpl/1.1
							print("Lamb_b <= Lamb_pb")
							print("---------------------------------------")
							print("MxRdFLT = {} (kN.cm)".format(round(MxRdFLT,3)))
						else:
							MxRdFLT=(Cb/1.1)*(Mpl-(Mpl-Mrb)*((Lamb_b-Lamb_pb)/(Lamb_rb-Lamb_pb)))
							print("Lamb_b > Lamb_pb")
							print("---------------------------------------")
							print("MxRdFLT = {} (kN.cm)".format(round(MxRdFLT,3)))

					print("---------------------------------------")
					print("                                       ")
					print("[1] Resolucao - Parte 4 (4/4)")
					print("[2] SAIR")
					r24=int(input())

					if(r24==2):
						sys.exit(1)
					if(r24==1):

						print("                                       ")
						print("---------------------------------------")
						print("5.5. Veri. do Mome. Flet. resist. em x:")
						print("---------------------------------------")
						print("                                       ")

						Mx=[[int(MxRdy/100)],[int(MxRdFLM/100)],[int(MxRdFLA/100)],[int(MxRdFLT/100)]]
						Mx1=[[MxRdy],[MxRdFLM],[MxRdFLA],[MxRdFLT]]
						menor = Mx1[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
						for linha in Mx1:
							for elemento in linha:
								if elemento < menor:
									menor = elemento
						MxRd=menor
						print("Mx = {}(kN.m)".format(Mx))
						print("---------------------------------------")
						
						print("MxRd = {} (kN.cm)".format(round(MxRd,3)))
						print("---------------------------------------")

						MxSdI=[[int(MxSd1)],[int(MxSd2)]]
						MxSdI1=[[MxSd1],[MxSd2]]
						menor = MxSdI1[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
						for linha in MxSdI1:
							for elemento in linha:
								if elemento < menor:
									menor = elemento
						MxSd=(menor)*100
						print("MxSdI = {} (kN.m)".format(MxSdI))
						print("---------------------------------------")
						
						print("MxSd = {} (kN.cm)".format(round(MxSd,3)))
						print("---------------------------------------")

						print("MxSd / MxRd = {}".format(round(MxSd/MxRd,3)))
						print("---------------------------------------")

						if (MxSd/MxRd)>1:
							print("MxSd / MxRd > 1")
							print("---------------------------------------")
							print("Nao atende!")
						else:
							print("MxSd / MxRd <= 1")
							print("---------------------------------------")
							print("Atende!")

						print("                                       ")
						print("---------------------------------------")
						print("6. Verificacao da flexao composta:")
						print("---------------------------------------")
						print("                                       ")

						print("6.1. Pilar sob flexotracao:")
						print("---------------------------------------")
						print("                                       ")

						print("NtSd = {} (kN)".format(round(NtSd,3)))
						print("---------------------------------------")

						print("NtRd = {} (kN)".format(round(NtRd,3)))
						print("---------------------------------------")

						MxSd1=MxSd1*100
						print("MxSd1 = {} (kN.cm)".format(round(MxSd1,3)))
						print("---------------------------------------")

						print("MxRd = {} (kN.cm)".format(round(MxRd,3)))
						print("---------------------------------------")

						print("NtSd / NtRd = {}".format(round(NtSd/NtRd,3)))
						print("---------------------------------------")

						if (NtSd/NtRd)>=0.2:
							print("(NtSd / NtRd) >= 0.2")
							Eq1=(NtSd/NtRd)+((8/9)*(MxSd1/MxRd))
							print("---------------------------------------")
							print("Eq1 = {}".format(round(Eq1,3)))
						else:
							Eq1=(NtSd/(2*NtRd))+(MxSd1/MxRd)
							print("(NtSd / NtRd) >= 0.2")
							print("---------------------------------------")
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

						print("                                       ")
						print("---------------------------------------")
						print("6.2. Pilar sob flexocompressao:")
						print("---------------------------------------")
						print("                                       ")

						print("NcSd = {} (kN)".format(round(NcSd,3)))
						print("---------------------------------------")

						print("NcRd = {} (kN)".format(round(NcRd,3)))
						print("---------------------------------------")

						MxSd2=MxSd2*100
						print("MxSd2 = {} (kN.cm)".format(round(MxSd2,3)))
						print("---------------------------------------")

						print("MxRd = {} (kN.cm)".format(round(MxRd,3)))
						print("---------------------------------------")

						print("NcSd / NcRd = {}".format(round(NcSd/NcRd,3)))
						print("---------------------------------------")

						if (NcSd/NcRd)>=0.2:
							print("(NcSd / NcRd) >= 0.2")
							Eq2=(NcSd/NcRd)+((8/9)*(MxSd2/MxRd))
							print("---------------------------------------")
							print("Eq2 = {}".format(round(Eq2,3)))
						else:
							Eq2=(NcSd/(2*NcRd))+(MxSd/MxRd)
							print("(NcSd / NcRd) >= 0.2")
							print("---------------------------------------")
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

	if acao2==3:
		sys.exit(1)

#end