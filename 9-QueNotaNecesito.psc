Algoritmo QueNotaNecesito
	Definir c1 Como Real
	Definir c2 Como Real
	Definir nl Como Real
	Definir nc Como Real
	Definir c3 Como Real
	Escribir 'ingrese la nota del primer certamen'
	Leer c1
	Escribir 'ingrese la nota del segundo certamen'
	Leer c2
	Escribir 'ingrese la nota del laboratorio'
	Leer nl
	nc <- (60-nl*0.3)/0.7
	c3 <- 3*nc-c1-c2
	Escribir 'necesita obtener ', c3, ' en el tercer certamen para aprovar con 60'
FinAlgoritmo
