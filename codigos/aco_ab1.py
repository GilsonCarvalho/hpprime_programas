#python export aco_ab1()
# -*- coding: utf-8 -*-
import sys
import math

# Desenvolvido por Gilson Carvalho - Maceio - 2023

aco=1
while aco==1:
	print("---------------------------------------")
	print("---------- ESTRUTURAS DE ACO ----------")
	print("---------------------------------------")
	print("---------------- AB1 ------------------")
	print("---------------------------------------")
	print("--- Desenvolvido por GILSON CARVALHO ---")
	print("                                       ")
	print("Selecione o exercicio: ")
	print("[1] PROPRIEDADES GEOMETRICAS")
	print("[2] TRACAO SIMPLES PERFIL 2L")
	print("[3] COMPRESSAO SIMPLES PERFIL SOLDADO")
	print("[4] COMPRESSAO SIMPLES PERFIL 2L")
	print("[5] SAIR")
	acao1=int(input())
	
	if acao1==1:
		print("                                       ")
		print("---------------------------------------")
		print("------- PROPRIEDADES GEOMETRICAS ------")
		print("---------------------------------------")
		print("---------SECAO TRANSVERSAL EM I--------")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")
		print("                                       ")

		d=float(input("Insira o d (mm): "))
		print(d)

		print("---------------------------------------")
		bf=float(input("Insira o bf (mm): "))
		print(bf)

		print("---------------------------------------")
		tf=float(input("Insira o tf (mm): "))
		print(tf)

		print("---------------------------------------")
		tw=float(input("Insira o tw (mm): "))
		print(tw)
		
		'''
		d=350
		bf=350
		tf=12.5
		tw=8
		'''
		print("---------------------------------------")
		print("                                       ")
		print("1. Dimensoes da secao transversal:")
		print("---------------------------------------")
		print("d = {} (mm)".format(d))
		print("---------------------------------------")
		print("bf = {} (mm)".format(bf))
		print("---------------------------------------")
		print("tf = {} (mm)".format(tf))
		print("---------------------------------------")
		print("tw = {} (mm)".format(tw))
		print("---------------------------------------")
		print("                                       ")
		print("2. Propri. geome. da secao transv.:")
		print("---------------------------------------")

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
		print("---------------------------------------")
		print("                                       ")

	if acao1==2:
		print("                                       ")
		print("---------------------------------------")
		print("--- VERIFICAÇÃO DE TIRANTE EM PERFIL --")
		print("---------------------------------------")
		print("------ 2L SUPORTANDO VIGA DE PISO -----")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")
		print("                                       ")
		print("Dados da cantoneira simples")
		print("---------------------------------------")

		b1L=float(input("Insira o b1L (mm): "))
		print(b1L)
		print("---------------------------------------")

		t1L=float(input("Insira o t1L (mm): "))
		print(t1L)
		print("---------------------------------------")

		xg1L=float(input("Insira o xg1L (cm): "))
		print(xg1L)
		print("---------------------------------------")

		Ag1L=float(input("Insira o Ag1L (cm2): "))
		print(Ag1L)
		print("---------------------------------------")

		Ix1L=float(input("Insira o Ix1L (cm4): "))
		print(Ix1L)
		print("---------------------------------------")

		Iy1L=float(input("Insira o Iy1L (cm4): "))
		print(Iy1L)
		print("---------------------------------------")

		rz1L=float(input("Insira o rz1L (cm): "))
		print(rz1L)

		print("---------------------------------------")
		print("                                       ")
		print("Dados da estrutura")
		print("---------------------------------------")

		L=float(input("Insira o L (m): "))
		print(L)
		print("---------------------------------------")

		H=float(input("Insira o H (m): "))
		print(H)
		print("---------------------------------------")

		npresilhas=float(input("Insira o npresilhas: "))
		print(npresilhas)

		print("---------------------------------------")
		print("                                       ")
		print("Dados da ligacao")
		print("---------------------------------------")

		dp=float(input("Insira o dp (mm): "))
		print(dp)
		print("---------------------------------------")

		tch=float(input("Insira o tch (mm): "))
		print(tch)

		print("---------------------------------------")
		print("                                       ")
		print("Dados do aco")
		print("---------------------------------------")

		fy=float(input("Insira o fy (kN/cm2): "))
		print(fy)
		print("---------------------------------------")

		fu=float(input("Insira o fu (kN/cm2): "))
		print(fu)

		print("---------------------------------------")
		print("                                       ")
		print("Dados do carreg. e dos fato. de ponder.")
		print("---------------------------------------")

		g0=float(input("Insira o g0 (kN/m): "))
		print(g0)
		print("---------------------------------------")

		gama_g0=float(input("Insira o gama_g0: "))
		print(gama_g0)
		print("---------------------------------------")

		g1=float(input("Insira o g1 (kN/m): "))
		print(g1)
		print("---------------------------------------")

		gama_g1=float(input("Insira o gama_g1: "))
		print(gama_g1)
		print("---------------------------------------")

		q=float(input("Insira o q (kN/m): "))
		print(q)
		print("---------------------------------------")

		gama_qq=float(input("Insira o gama_qq: "))
		print(gama_qq)
		print("---------------------------------------")

		p=float(input("Insira o p (kN): "))
		print(p)
		print("---------------------------------------")

		gama_gp=float(input("Insira o gama_gp: "))
		print(gama_gp)
		print("---------------------------------------")

		fator=float(input("Insira o fator: "))
		print(fator)
		
		'''
		b1L=76
		t1L=6.35
		xg1L=2.05
		Ag1L=8.72
		Ix1L=45.7
		Iy1L=45.7
		rz1L=1.5
		L=8
		H=3.5
		npresilhas=2
		dp=19
		tch=8
		fy=25
		fu=40
		g0=10
		gama_g0=1.25
		g1=5
		gama_g1=1.25
		q=20
		gama_qq=1.5
		p=25
		gama_gp=1.25
		fator=1.33
		'''

		print("                                       ")
		print("---------------------------------------")
		print("1. Dados do problema:")
		print("---------------------------------------")
		print("                                       ")
		print("Dados da cantoneira simples")
		print("---------------------------------------")
		print("b1L = {} (mm)".format(b1L))
		print("---------------------------------------")
		print("t1L = {} (mm)".format(t1L))
		print("---------------------------------------")
		print("xg1L = {} (cm)".format(xg1L))
		print("---------------------------------------")
		print("Ag1L = {} (cm2)".format(Ag1L))
		print("---------------------------------------")
		print("Ix1L = {} (cm4)".format(Ix1L))
		print("---------------------------------------")
		print("Iy1L = {} (cm4)".format(Iy1L))
		print("---------------------------------------")
		print("rz1L = {} (cm)".format(rz1L))
		print("---------------------------------------")
		print("                                       ")
		print("Dados da estrutura")
		print("---------------------------------------")
		print("L = {} (m)".format(L))
		print("---------------------------------------")
		print("H = {} (m)".format(H))
		print("---------------------------------------")
		print("npresilhas = {}".format(npresilhas))
		print("---------------------------------------")
		print("                                       ")
		print("Dados da ligacao")
		print("---------------------------------------")
		print("dp = {} (mm)".format(dp))
		print("---------------------------------------")
		Lc=6*dp
		print("Lc = {} (mm)".format(Lc))
		print("---------------------------------------")
		print("tch = {} (mm)".format(tch))
		print("---------------------------------------")
		print("                                       ")
		print("Dados do aco")
		print("---------------------------------------")
		print("fy = {} (kN/cm2)".format(fy))
		print("---------------------------------------")
		print("fu = {} (kN/cm2)".format(fu))
		print("---------------------------------------")
		print("                                       ")
		print("Dados do carreg. e dos fato. de ponder.")
		print("---------------------------------------")
		print("g0 = {} (kN/m)".format(g0))
		print("---------------------------------------")
		print("gama_g0 = {}".format(gama_g0))
		print("---------------------------------------")
		print("g1 = {} (kN/m)".format(g1))
		print("---------------------------------------")
		print("gama_g1 = {}".format(gama_g1))
		print("---------------------------------------")
		print("q = {} (kN/m)".format(q))
		print("---------------------------------------")
		print("gama_qq = {}".format(gama_qq))
		print("---------------------------------------")
		print("p = {} (kN)".format(p))
		print("---------------------------------------")
		print("gama_gp = {}".format(gama_gp))
		print("---------------------------------------")
		print("fator = {}".format(fator))

		print("---------------------------------------")
		print("[1] Resolucao - Parte 2 (2/2)")
		print("[2] SAIR")
		r22=int(input())

		if(r22==2):
			sys.exit(1)
		if(r22==1):

			print("                                       ")
			print("---------------------------------------")
			print("2. Propri. geome. do perfil 2L:")
			print("---------------------------------------")
			print("                                       ")

			Ag2L=2*Ag1L
			print("Ag2L = {} (cm2)".format(round(Ag2L,3)))
			print("---------------------------------------")

			Ix2L=2*Ix1L
			print("Ix2L = {} (cm4)".format(round(Ix2L,3)))
			print("---------------------------------------")

			e=xg1L+(tch/10/2)
			print("e = {} (cm)".format(round(e,3)))
			print("---------------------------------------")

			Iy2L=2*(Iy1L+Ag1L*(e**2))
			print("Iy2L = {} (cm4)".format(round(Iy2L,3)))
			print("---------------------------------------")

			rx2L=(Ix2L/Ag2L)**(1/2)
			print("rx2L = {} (cm)".format(round(rx2L,3)))
			print("---------------------------------------")

			ry2L=(Iy2L/Ag2L)**(1/2)
			print("ry2L = {} (cm)".format(round(ry2L,3)))

			print("                                       ")
			print("---------------------------------------")
			print("3. Esforco solicitante de projeto:")
			print("---------------------------------------")
			print("                                       ")

			NtSd=((gama_g0*g0+gama_g1*g1+gama_qq*fator*q)*L/2)+(gama_gp*p)
			print("NtSd = {} (kN)".format(round(NtSd,3)))

			print("                                       ")
			print("---------------------------------------")
			print("4. Esforco resistente de projeto:")
			print("---------------------------------------")
			print("                                       ")
			print("4.1. Escoamento da secao bruta:")
			print("---------------------------------------")
			print("                                       ")

			NtyRd=(Ag2L*fy)/1.1
			print("NtyRd = {} (kN)".format(round(NtyRd,3)))

			print("                                       ")
			print("4.2. Ruptura da secao liquida efetiva:")
			print("---------------------------------------")
			print("                                       ")

			df=dp+1.5+2
			print("df = {} (cm)".format(round(df/10,3)))
			print("---------------------------------------")

			An=Ag2L-(1*df/10*(t1L/10)*2)
			print("An = {} (cm2)".format(round(An,3)))
			print("---------------------------------------")

			ec=xg1L
			print("ec = {} (cm)".format(round(ec,3)))
			print("---------------------------------------")

			if (1-((ec*10)/Lc))<0.6:
				Ct=0
				print("Ct = {}".format(Ct))
			else:
				Ct=(1-((ec*10)/Lc))
				print("Ct = {}".format(round(Ct,3)))
			print("---------------------------------------")

			NtuRd=(Ct*An*fu)/1.35
			print("NtuRd = {} (kN)".format(round(NtuRd,3)))
			print("---------------------------------------")

			print("                                       ")
			print("4.3. Esforco resistente:")
			print("---------------------------------------")
			print("                                       ")

			if NtyRd<NtuRd:
				NtRd=NtyRd
				print("NtRd = {} (kN)".format(round(NtRd,3)))
			else:
				NtRd=NtuRd
				print("NtRd = {} (kN)".format(round(NtRd,3)))
			print("---------------------------------------")

			print("                                       ")
			print("5. Verific. da condicao de seguranca:")
			print("---------------------------------------")
			print("                                       ")

			print("NtSd / NtRd = {}".format(round(NtSd/NtRd,3)))
			print("---------------------------------------")

			if NtSd>NtRd:
				print("NtSd > NtRd")
				print("---------------------------------------")
				print("Nao atende!")
			else:
				print("NtSd <= NtRd")
				print("---------------------------------------")
				print("Atende!")

			print("---------------------------------------")
			print("                                       ")
			print("6. Verificacao da esbeltez:")
			print("---------------------------------------")
			print("                                       ")

			print("6.1. Esbel. lim. defin. em norm.:")
			print("---------------------------------------")
			print("                                       ")

			Lamb_lim=300
			print("Lamb_lim = {}".format(Lamb_lim))
			print("---------------------------------------")

			print("                                       ")
			print("6.2. Esbeltez do perfil composto (2L):")
			print("---------------------------------------")
			print("                                       ")

			r2L=[[round(rx2L,3)],[round(ry2L,3)]]
			print("r2L = {} (cm)".format(r2L))
			print("---------------------------------------")

			menor = r2L[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
			for linha in r2L:
				for elemento in linha:
					if elemento < menor:
						menor = elemento
			rmin2L=menor
			print("rmin2L = {} (cm)".format(rmin2L))
			print("---------------------------------------")

			Lamb_max2L=(H/rmin2L)*100
			print("Lamb_max2L = {}".format(round(Lamb_max2L,3)))
			print("---------------------------------------")

			if (Lamb_max2L<=Lamb_lim):
				print("Atende!")
			else:
				print("Não atende!")

			print("---------------------------------------")
			print("                                       ")
			print("6.3. Esbeltez do perfil isolado (1L):")
			print("---------------------------------------")
			print("                                       ")

			Lamb_max1L=((H/3)/(rz1L))*100
			print("Lamb_max1L = {}".format(round(Lamb_max1L,3)))
			print("---------------------------------------")

			if (Lamb_max1L<=Lamb_lim):
				print("Atende!")
			else:
				print("Não atende!")
			print("---------------------------------------")
			print("                                       ")

	if acao1==3:
		print("                                       ")
		print("---------------------------------------")
		print("---- VERIFICACAO DE PERFIL SOLDADO ----")
		print("---------------------------------------")
		print("---- SUBMETIDO A COMPRESSAO SIMPLES ---")
		print("---------------------------------------")
		print("                                       ")

		
		print("DADOS INICIAIS")
		print("---------------------------------------")
		print("                                       ")

		print("Dimesoes")
		print("---------------------------------------")

		H1=float(input("Insira o H1 (m): "))
		print(H1)
		print("---------------------------------------")

		L1=float(input("Insira o L1 (m): "))
		print(L1)
		print("---------------------------------------")

		L2=float(input("Insira o L2 (m): "))
		print(L2)
		print("---------------------------------------")
		
		print("                                       ")
		print("Esforcos solicitantes")
		print("---------------------------------------")

		NcSd=float(input("Insira o NcSd (kN): "))
		print(NcSd)
		print("---------------------------------------")

		print("                                       ")
		print("Secao transversal")
		print("---------------------------------------")

		d=float(input("Insira o d (mm): "))
		print(d)
		print("---------------------------------------")

		bf=float(input("Insira o bf (mm): "))
		print(bf)
		print("---------------------------------------")

		tf=float(input("Insira o tf (mm): "))
		print(tf)
		print("---------------------------------------")

		tw=float(input("Insira o tw (mm): "))
		print(tw)
		print("---------------------------------------")

		print("                                       ")
		print("Propriedades do aco")
		print("---------------------------------------")

		fy=float(input("Insira o fy (kN/cm2): "))
		print(fy)
		print("---------------------------------------")

		E=float(input("Insira o E (kN/cm2): "))
		print(E)
		print("---------------------------------------")

		G=float(input("Insira o G (kN/cm2): "))
		print(G)
		
		'''
		H1=4
		L1=8
		L2=6
		NcSd=2000
		fy=34.5
		E=20000
		G=7700
		d=350
		bf=350
		tf=12.5
		tw=8
		'''


		print("                                       ")
		print("---------------------------------------")
		print("1. Dados do problema:")
		print("---------------------------------------")
		print("                                       ")

		print("Esforcos solicitantes")
		print("---------------------------------------")
		print("NcSd = {} (kN)".format(NcSd))
		print("---------------------------------------")

		print("                                       ")
		print("Comprimentos de flambagem")
		print("---------------------------------------")

		kxLx=2*H1
		print("kxLx = {} (cm)".format(round(kxLx*100,3)))
		print("---------------------------------------")

		kyLy=H1
		print("kyLy = {} (cm)".format(round(kyLy*100,3)))
		print("---------------------------------------")

		kzLz=0.7*(2*H1)
		print("kzLz = {} (cm)".format(round(kzLz*100,3)))
		print("---------------------------------------")

		print("                                       ")
		print("Secao transversal")
		print("---------------------------------------")

		print("d = {} (mm)".format(d))
		print("---------------------------------------")
		print("bf = {} (mm)".format(bf))
		print("---------------------------------------")
		print("tf = {} (mm)".format(tf))
		print("---------------------------------------")
		print("tw = {} (mm)".format(tw))
		print("---------------------------------------")

		print("                                       ")
		print("Propriedades do aco")
		print("---------------------------------------")

		print("fy = {} (kN)".format(fy))
		print("---------------------------------------")
		print("E = {} (kN)".format(E))
		print("---------------------------------------")
		print("G = {} (kN)".format(G))

		print("                                       ")
		print("---------------------------------------")
		print("2. Propri. geometri. da secao transv.:")
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

		print("---------------------------------------")
		print("[1] Resolucao - Parte 2 (2/3)")
		print("[2] SAIR")
		r32=int(input())

		if(r32==2):
			sys.exit(1)
		if(r32==1):

			print("                                       ")
			print("---------------------------------------")
			print("3. Verificacao do esforco de compressao:")
			print("---------------------------------------")
			print("                                       ")

			print("---------------------------------------")
			print("3.1. Estabilidade local:")
			print("---------------------------------------")
			print("                                       ")

			print("Mesa")
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

			print("---------------------------------------")
			print("[1] Resolucao - Parte 3 (3/3)")
			print("[2] SAIR")
			r33=int(input())

			if(r33==2):
				sys.exit(1)
			if(r33==1):

				print("                                       ")
				print("---------------------------------------")
				print("3.2. Estabilidade global:")
				print("---------------------------------------")
				print("                                       ")

				Nex=((math.pi**2)*E*Ix)/(kxLx**2)
				print("Nex = {} (kN)".format(round(Nex/100000000,3)))
				print("---------------------------------------")

				Ney=((math.pi**2)*E*Iy)/(kyLy**2)
				print("Ney = {} (kN)".format(round(Ney/100000000,3)))
				print("---------------------------------------")

				Nez=(1/((r0/10)**2))*((((math.pi**2)*E*(Cw/1000000))/((kzLz*100)**2))+((J/10000)*G))
				print("Nez = {} (kN)".format(round(Nez,3)))
				print("---------------------------------------")

				NeI=[[round(Nex/100000000,2)],[round(Ney/100000000,2)],[round(Nez,2)]]
				NeI1=[[Nex],[Ney],[Nez]]
				menor = NeI[0][0]  # Suponha que o primeiro elemento é o menor inicialmente
				for linha in NeI:
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
				print("3.3. Verificacao do esforco resistente:")
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

				print("                                       ")
				print("---------------------------------------")
				print("3.4. Verificacao da esbeltez maxima:")
				print("---------------------------------------")
				print("                                       ")

				Lamb_x=(kxLx/rx)*1000
				print("Lamb_x = {}".format(round(Lamb_x,3)))
				print("---------------------------------------")

				Lamb_y=(kyLy/ry)*1000
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
				print("---------------------------------------")
				print("                                       ")

	if acao1==4:
		print("                                       ")
		print("---------------------------------------")
		print("----- COMPRESSAO SIMPLES PERFIL 2L ----")
		print("---------------------------------------")
		print("                                       ")

		print("DADOS INICIAIS")
		print("---------------------------------------")

		print("                                       ")
		print("Acoes atuantes e coeficientes adotados")
		print("---------------------------------------")

		
		print("Insira o G0 (kN/m2): ")
		G0=float(input())
		print(G0)
		print("---------------------------------------")

		print("Insira o gama_g0: ")
		gama_g0=float(input())
		print(gama_g0)
		print("---------------------------------------")

		print("Insira o G1 (kN/m2): ")
		G1=float(input())
		print(G1)
		print("---------------------------------------")

		print("Insira o gama_g1: ")
		gama_g1=float(input())
		print(gama_g1)
		print("---------------------------------------")

		print("Insira o Q (kN/m2): ")
		Q=float(input())
		print(Q)
		print("---------------------------------------")

		print("Insira o gama_q: ")
		gama_q=float(input())
		print(gama_q)
		print("---------------------------------------")

		print("                                       ")
		print("Secao transversal - 1L")
		print("---------------------------------------")

		print("Insira o b1L (mm): ")
		b1L=float(input())
		print(b1L)
		print("---------------------------------------")

		print("Insira o t1L (mm): ")
		t1L=float(input())
		print(t1L)
		print("---------------------------------------")

		print("Insira o Ag1L (cm2): ")
		Ag1L=float(input())
		print(Ag1L)
		print("---------------------------------------")

		print("Insira o Ix1L (cm4): ")
		Ix1L=float(input())
		print(Ix1L)
		print("---------------------------------------")

		print("Insira o Iy1L (cm4): ")
		Iy1L=float(input())
		print(Iy1L)
		print("---------------------------------------")

		print("Insira o xg1L (cm): ")
		xg1L=float(input())
		print(xg1L)
		print("---------------------------------------")

		print("Insira o yg1L (cm): ")
		yg1L=float(input())
		print(yg1L)
		print("---------------------------------------")

		print("Insira o rz1L (cm): ")
		rz1L=float(input())
		print(rz1L)
		print("---------------------------------------")

		print("Insira o J1L (cm4): ")
		J1L=float(input())
		print(J1L)
		print("---------------------------------------")

		print("Insira o tch (mm): ")
		tch=float(input())
		print(tch)
		print("---------------------------------------")

		print("                                       ")
		print("Dados da estrutura")
		print("---------------------------------------")

		print("Insira o a (m): ")
		a=float(input())
		print(a)
		print("---------------------------------------")

		print("Insira o b (m): ")
		b=float(input())
		print(b)
		print("---------------------------------------")

		print("Insira o c (m): ")
		c=float(input())
		print(c)
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
		'''

		G0=0.25
		gama_g0=1.25
		G1=0.5
		gama_g1=1.35
		Q=3
		gama_q=1.5
		b1L=88.9
		t1L=7.94
		Ag1L=13.5
		Ix1L=102
		Iy1L=102
		xg1L=2.52
		yg1L=2.52
		rz1L=1.75
		J1L=2.83
		tch=8
		a=1.5
		b=1.25
		c=4
		kxLx=a
		kyLy=2*a
		kzLz=a
		fy=25
		E=20000
		G=7700
		'''

		print("                                       ")
		print("---------------------------------------")
		print("1. Dados do problema:")
		print("---------------------------------------")
		print("                                       ")

		print("Acoes atuantes e coeficientes adotados")
		print("---------------------------------------")

		print("G0 = {} (kN/m2)".format(G0))
		print("---------------------------------------")

		print("G1 = {} (kN/m2)".format(G1))
		print("---------------------------------------")

		print("Q = {} (kN/m2)".format(Q))
		print("---------------------------------------")

		print("gama_g0 = {}".format(gama_g0))
		print("---------------------------------------")

		print("gama_g1 = {}".format(gama_g1))
		print("---------------------------------------")

		print("gama_q = {}".format(gama_q))
		print("---------------------------------------")

		print("                                       ")
		print("Comprimentos de flambagem")
		print("---------------------------------------")

		kxLx=a*100
		print("kxLx = {} (cm)".format(round(kxLx,3)))
		print("---------------------------------------")

		kyLy=a*2*100
		print("kyLy = {} (cm)".format(round(kyLy,3)))
		print("---------------------------------------")

		kzLz=a*100
		print("kzLz = {} (cm)".format(round(kzLz,3)))
		print("---------------------------------------")

		print("                                       ")
		print("Secao transversal - 1L")
		print("---------------------------------------")

		print("b1L = {} (mm)".format(b1L))
		print("---------------------------------------")

		t1L=t1L/10
		print("t1L = {} (mm)".format(t1L))
		print("---------------------------------------")

		print("Ag1L = {} (cm2)".format(Ag1L))
		print("---------------------------------------")

		print("Ix1L = {} (cm4)".format(Ix1L))
		print("---------------------------------------")

		print("Iy1L = {} (cm4)".format(Iy1L))
		print("---------------------------------------")

		print("xg1L = {} (cm)".format(xg1L))
		print("---------------------------------------")

		print("yg1L = {} (cm)".format(yg1L))
		print("---------------------------------------")

		print("rz1L = {} (cm)".format(rz1L))
		print("---------------------------------------")

		print("J1L = {} (cm4)".format(J1L))
		print("---------------------------------------")

		tch=tch/10
		print("tch = {} (mm)".format(tch))
		print("---------------------------------------")

		print("                                       ")
		print("Dados da estrutura")
		print("---------------------------------------")

		print("a = {} (m)".format(a))
		print("---------------------------------------")

		print("b = {} (m)".format(b))
		print("---------------------------------------")

		print("c = {} (m)".format(c))
		print("---------------------------------------")

		print("                                       ")
		print("Propriedades do aco")
		print("---------------------------------------")

		print("fy = {} (kN/cm2)".format(fy))
		print("---------------------------------------")

		print("E = {} (kN/cm2)".format(E))
		print("---------------------------------------")

		print("G = {} (kN/cm2)".format(G))

		print("                                       ")
		print("---------------------------------------")
		print("2. Esf. de comp. no banzo sup. proj.:")
		print("---------------------------------------")
		print("                                       ")

		Qd=gama_g0*G0+gama_g1*G1+gama_q*Q
		print("Qd = {} (kN/m2)".format(round(Qd,3)))
		print("---------------------------------------")

		Pd=Qd*(a*c)
		print("Pd = {} (kN)".format(round(Pd,3)))
		print("---------------------------------------")

		NcSd=(8*Pd*a)/b
		print("NcSd = {} (kN)".format(round(NcSd,3)))

		print("                                       ")
		print("---------------------------------------")
		print("3. Propri. geometri. da secao transv.:")
		print("---------------------------------------")
		print("                                       ")

		Ag2L=2*Ag1L
		print("Ag2L = {} (cm2)".format(round(Ag2L,3)))
		print("---------------------------------------")

		Ix2L=2*Ix1L
		print("Ix2L = {} (cm4)".format(round(Ix2L,3)))
		print("---------------------------------------")

		e=xg1L+(tch/2)
		print("e = {} (cm)".format(round(e,3)))
		print("---------------------------------------")

		Iy2L=2*(Iy1L+Ag1L*(e**2))
		print("Iy2L = {} (cm4)".format(round(Iy2L,3)))
		print("---------------------------------------")

		rx2L=(Ix2L/Ag2L)**(1/2)
		print("rx2L = {} (cm)".format(round(rx2L,3)))
		print("---------------------------------------")

		ry2L=(Iy2L/Ag2L)**(1/2)
		print("ry2L = {} (cm)".format(round(ry2L,3)))
		print("---------------------------------------")

		J2L=2*J1L
		print("J2L = {} (cm4)".format(round(J2L,3)))
		print("---------------------------------------")

		x02L=0
		print("x02L = {} (cm)".format(round(x02L,3)))
		print("---------------------------------------")

		y02L=yg1L-(t1L/2)
		print("y02L = {} (cm)".format(round(y02L,3)))
		print("---------------------------------------")

		r02L=((rx2L**2)+(ry2L**2)+(x02L**2)+(y02L**2))**(1/2)
		print("r02L = {} (cm)".format(round(r02L,3)))
		print("---------------------------------------")

		Cw2L=0
		print("Cw2L = {} (cm6)".format(round(Cw2L,3)))

		print("---------------------------------------")
		print("[1] Resolucao - Parte 2 (2/3)")
		print("[2] SAIR")
		r42=int(input())

		if(r42==2):
			sys.exit(1)
		if(r42==1):
		
			print("                                       ")
			print("---------------------------------------")
			print("4. Estabilidade local:")
			print("---------------------------------------")
			print("                                       ")

			print("Mesas")
			print("---------------------------------------")

			Lamb_m=(b1L/t1L)/10
			print("Lamb_m = {}".format(round(Lamb_m,3)))
			print("---------------------------------------")

			Lamb_pm=0.45*((E/fy)**(1/2))
			print("Lamb_pm = {}".format(round(Lamb_pm,3)))
			print("---------------------------------------")

			Lamb_rm=0.91*((E/fy)**(1/2))
			print("Lamb_rm = {}".format(round(Lamb_rm,3)))
			print("---------------------------------------")

			if Lamb_m<=Lamb_pm:
				Qs=1
				print("Lamb_m <= Lamb_pm")
				print("---------------------------------------")
				print("Qs = {}".format(Qs))
			else:
				if Lamb_m>Lamb_rm:
					Qs=((0.53*E)/(fy*(Lamb_m**2)))
					print("Lamb_m > Lamb_rm")
					print("---------------------------------------")
					print("Qs = {}".format(round(Qs,3)))
				else:
					Qs=1.34-(0.76*Lamb_m*((fy/E)**(1/2)))
					print("Lamb_m <= Lamb_rm")
					print("---------------------------------------")
					print("Qs = {}".format(round(Qs,3)))
			print("---------------------------------------")

			if Lamb_m<=Lamb_pm:
				print("Lamb_m <= Lamb_pm")
				print("---------------------------------------")
				print("Nao ha possibilidade de flambagem local na mesa do perfil")
			else:
				if Lamb_m>Lamb_rm:
					print("Lamb_m > Lamb_rm")
					print("---------------------------------------")
					print("Ha possibilidade de flambagem local elastica na mesa do perfil")
				else:
					print("Ha possibilidade de flambagem local inelastica na mesa do perfil")
			print("---------------------------------------")

			print("Coeficiente Q")
			print("---------------------------------------")

			Q=Qs
			print("Q = Qs")
			print("---------------------------------------")
			print("Q = {}".format(round(Q,3)))

			print("                                       ")
			print("---------------------------------------")
			print("5. Estabilidade global (Param. X):")
			print("---------------------------------------")
			print("                                       ")

			Nex=((math.pi**2)*E*Ix2L)/(kxLx**2)
			print("Nex = {} (kN)".format(round(Nex,3)))
			print("---------------------------------------")

			Ney=((math.pi**2)*E*Iy2L)/(kyLy**2)
			print("Ney = {} (kN)".format(round(Ney,3)))
			print("---------------------------------------")

			Nez=(1/(r02L**2))*((((math.pi**2)*E*Cw2L)/(kzLz**2))+(G*J2L))
			print("Nez = {} (kN)".format(round(Nez,3)))
			print("---------------------------------------")

			Neyz=((Ney+Nez)/(2*(1-((y02L/r02L)**2))))*(1-((1-((4*Ney*Nez*(1-((y02L/r02L)**2)))/((Ney+Nez)**2)))**(1/2)))
			print("Neyz = {} (kN)".format(round(Neyz,3)))
			print("---------------------------------------")

			if Nex>Neyz:
				Ne=Neyz
				print("Nex > Neyz")
				print("---------------------------------------")
				print("Ne = {} (kN)".format(round(Ne,3)))
			else:
				Ne=Nex
				print("Nex M = Nex")
				print("---------------------------------------")
				print("Ne = {} (kN)".format(round(Ne,3)))
			print("---------------------------------------")

			Lamb_0=((Q*Ag2L*fy)/Ne)**(1/2)
			print("Lamb_0 = {}".format(round(Lamb_0,3)))
			print("---------------------------------------")

			if Lamb_0>1.5:
				X=0.877/(Lamb_0**2)
				print("Lamb_0 > 1.5")
				print("---------------------------------------")
				print("X = {}".format(round(X,3)))
			else:
				X=0.658**(Lamb_0**2)
				print("Lamb_0 <= 1.5")
				print("---------------------------------------")
				print("X = {}".format(round(X,3)))

			print("---------------------------------------")
			print("[1] Resolucao - Parte 3 (3/3)")
			print("[2] SAIR")
			r43=int(input())

			if(r43==2):
				sys.exit(1)
			if(r43==1):

				print("                                       ")
				print("---------------------------------------")
				print("5.1. Determ. e verif. do esf. resist.:")
				print("---------------------------------------")
				print("                                       ")

				NcRd=(Q*X*Ag2L*fy)/1.1
				print("NcRd = {} (kN)".format(round(NcRd,3)))
				print("---------------------------------------")

				print("NcSd = {} (kN)".format(round(NcSd,3)))
				print("---------------------------------------")

				print("NcSd / NtRd = {}".format(round(NcSd/NcRd,3)))
				print("---------------------------------------")

				if (NcSd/NcRd)>1:
					print("NcSd / NcRd > 1")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("NcSd / NcRd <= 1")
					print("---------------------------------------")
					print("Atende!")

				print("                                       ")
				print("---------------------------------------")
				print("6. Verificacao da esbeltez maxima:")
				print("---------------------------------------")
				print("                                       ")

				print("6.1. Esb. lim. def. em nor. ele. comp.:")
				print("---------------------------------------")
				print("                                       ")

				Lamb_lim=200
				print("Lamb_lim = {}".format(Lamb_lim))

				print("                                       ")
				print("---------------------------------------")
				print("6.2. Verif. da esbel. max. do perf. 2L:")
				print("---------------------------------------")
				print("                                       ")

				Lamb_x2L=(kxLx/rx2L)
				print("Lamb_x2L = {}".format(round(Lamb_x2L,3)))
				print("---------------------------------------")

				Lamb_y2L=(kyLy/ry2L)
				print("Lamb_y2L = {}".format(round(Lamb_y2L,3)))
				print("---------------------------------------")

				if Lamb_x2L>Lamb_y2L:
					Lamb_max2L=Lamb_x2L
					print("Lamb_x2L > Lamb_y2L")
					print("---------------------------------------")
					print("Lamb_max2L = {}".format(round(Lamb_max2L,3)))
				else:
					Lamb_max2L=Lamb_y2L
					print("Lamb_x2L <= Lamb_y2L")
					print("---------------------------------------")
					print("Lamb_max2L = {}".format(round(Lamb_max2L,3)))
				print("---------------------------------------")

				if Lamb_max2L>Lamb_lim:
					print("Lamb_max2L > Lamb_lim")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Lamb_max2L <= Lamb_lim")
					print("---------------------------------------")
					print("Atende!")

				print("                                       ")
				print("---------------------------------------")
				print("6.3. Verif. da esbel. max. do perf. 1L:")
				print("---------------------------------------")
				print("                                       ")

				Lamb_lim1L=(1/2)*Lamb_max2L
				print("Lamb_lim1L = {}".format(round(Lamb_lim1L,3)))
				print("---------------------------------------")

				Lamb_max1L=(a/rz1L)*100
				print("Lamb_max1L = {}".format(round(Lamb_max1L,3)))
				print("---------------------------------------")

				if Lamb_max1L>Lamb_lim1L:
					print("Lamb_max1L > Lamb_lim1L")
					print("---------------------------------------")
					print("Nao atende!")
				else:
					print("Lamb_max1L <= Lamb_lim1L")
					print("---------------------------------------")
					print("Atende!")
				print("---------------------------------------")

				print("                                       ")
				print("---------------------------------------")
				print("6.4. Quant. min. nece. de chap. espac. ")
				print("     (presilhas) entre os nós:")
				print("---------------------------------------")
				print("                                       ")

				L1Lmax=((1/2)*Lamb_max2L*rz1L)/100
				print("L1Lmax = {} (m)".format(round(L1Lmax,3)))
				print("---------------------------------------")

				print("a = {} (m)".format(round(a,3)))
				print("---------------------------------------")

				if L1Lmax<=a:
					print("L1Lmax <= a")
					print("---------------------------------------")
					print("Ha necessidade de chapas espacadoras (presilhas) entre os nos!")
				else:
					print("L1Lmax > a")
					print("---------------------------------------")
					print("Nao ha necessidade de chapas espacadoras (presilhas) entre os nos!")
				print("---------------------------------------")

				npresilhas=int(a/L1Lmax)
				print("npresilhas = {}".format(npresilhas))
				print("---------------------------------------")
				print("                                       ")

	if acao1==5:
		sys.exit(1)