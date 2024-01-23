Algoritmo HuevosALaCopa
	Definir to Como Real
	Definir t Como Real
	Definir M Como Entero
	Escribir 'ingrese la temperatura original del huevo'
	Leer to
	Escribir '1. huevo pequeño '
	Escribir '2. huevo grande'
	Leer M
	Si M==1 Entonces
		M <- 47
	SiNo
		M <- 67
	FinSi
	t <- (((M^(2/3))*((3.7*(1.038^(1/3)))))/((0.0054*(PI^2))*(((4*PI)/3)^(2/3))))*ln((0.76)*((to-100)/(70-100)))
	Escribir 'el huevo se demorara ', redon(t), ' segndos en estar preparado a la copa'
FinAlgoritmo
