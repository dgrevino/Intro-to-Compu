#include <iostream>
#include <string>


using namespace std;

// Integrantes del grupo 5: Bonardi, Grevino,  Robles.

/* FUNCION 1 */
/*Verifica si un numero es primo o no.
Dado un entero n, si encuentra solo 2 divisores,en el rango de 
1 a n, devuelve true. De lo contrario, devuelve false.*/

bool esPrimo (int n){ 
	int divisor, sum_div; 
	divisor = 1; 
	sum_div = 0;
	while (divisor <= n){
		if (n%divisor == 0){
			sum_div = sum_div + 1;
		} 
		divisor = divisor + 1;
    }
		    if (sum_div == 2){
			    return true;
	        } else {
		        return false;
	        }
}

////////////////////////////////////////////////////////////

/* FUNCION 2 */
/*Cuenta la CANTIDAD de numeros PRIMOS MENORES O IGUALES a un 
numero dado n.*/

int cantidadPrimosMenoresOIguales (int n){
	int numero, contador_primos;
	numero = 2;
	contador_primos = 0; 
	while (numero <= n){
		if (esPrimo(numero)){
			contador_primos = contador_primos + 1;
		}
		numero = numero + 1;
	}
	return contador_primos; 
}

////////////////////////////////////////////////////////////

/* FUNCION 3 */
/*Cuenta la CANTIDAD de DIVISORES PRIMOS de un 
numero dado n.*/

int cantidadDivisoresPrimos (int n){ 
	int divisor, contador_div_primos;
	divisor = 2;
	contador_div_primos = 0;
	while (divisor <= n){  
		if ((n % divisor)== 0 and esPrimo(divisor)){
		contador_div_primos = contador_div_primos + 1;
		}
		divisor = divisor + 1;
	}	
	return contador_div_primos; 
}

////////////////////////////////////////////////////////////

/* FUNCION 4 */	

/*Busca el IESIMO DIVISOR primo de un numero n*/
/*contp corresponde al contador de divisores primos*/

int iesimoDivisorPrimo (int n, int i){
	int cont_div_primos = 0; 
	int j = 2;
	while (j <= n){
		if (esPrimo(j) and (n % j == 0)){
			cont_div_primos = cont_div_primos + 1;
		}
		if (cont_div_primos == i){
			return j;
		}
		j = j + 1;
	}
	return -1;
}

////////////////////////////////////////////////////////////	
/* FUNCION 5 */
/*Busca la potencia del iesimo divisor primo de un 
numero n en la descomposicion de sus factores primos.*/
/*Notar que si no existe el iesimo divisor primo que se 
pidio, devuelve -1*/


int potenciaIesimoDivisorPrimo(int n, int i){ 
	int div = iesimoDivisorPrimo(n,i);
	int cont_potencia = 0; 
	int contdiv = n; 
	if(div == -1){ 
		return -1;
	}
	else{ 
		while((contdiv%div == 0) and (contdiv >= div)){
			contdiv = contdiv/div;
			cont_potencia = cont_potencia + 1;
		}
    }
	return cont_potencia;	
}



/* FUNCION PRINCIPAL*/

int main(int argc, char* argv[]) {
	string funcion(argv[1]);
/*Evalua la funcion esPrimo con el argumento 2 
y devuelve si o no dependiendo de si es o no primo*/ 
    if(funcion=="esPrimo"){
		if(esPrimo(atoi(argv[2]))){	
			cout << "si" << endl; 
    		}
 	   	else{
    		cout << "no" << endl;
   		}
	}	
/*Notese que en los siguientes condicionales se imprime 
el valor evaluado en la correspondiente funcion*/


    if(funcion=="cantidadPrimosMenoresOIguales"){        
		cout << cantidadPrimosMenoresOIguales(atoi(argv[2])) << endl; 
    }
 

    if(funcion=="cantidadDivisoresPrimos"){
    	cout << cantidadDivisoresPrimos(atoi(argv[2])) << endl; 
    }
   

    if(funcion=="iesimoDivisorPrimo"){
   		if((iesimoDivisorPrimo(atoi(argv[2]) , atoi(argv[3]))==-1)){ 
   			cout << argv[2] << " no tiene " << argv[3] << " divisores primos " << endl;
    	}	
    	else{
    		cout << iesimoDivisorPrimo(atoi(argv[2]) , atoi(argv[3])) << endl;
		} 
    }
   
		
    if(funcion=="potenciaIesimoDivisorPrimo"){ 
   		if(potenciaIesimoDivisorPrimo(atoi(argv[2]) , atoi(argv[3]))==-1){
   			cout << argv[2] << " no tiene " << argv[3] << " divisores primos " << endl;
   		}
   		else{
   			cout << potenciaIesimoDivisorPrimo(atoi(argv[2]) , atoi(argv[3])) << endl;
   		}
    }
}
