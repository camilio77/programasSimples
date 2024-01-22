Algoritmo HoraFutura
	Definir ho Como Real
	Definir des Como Real
	Definir ht Como Real
	Definir m Como Cadena
	Escribir 'ingrese la hora actual'
	Leer ho
	Escribir 'ingrese el numero de horas'
	Leer des
	ht <- (ho+des)
	Si (ht>12) Entonces
		m <- 'pm'
		ht <- ht-12
	SiNo
		m <- 'am'
	FinSi
	Escribir 'dentro de ', des, ' horas el reloj marcara las ', ht, m
FinAlgoritmo
