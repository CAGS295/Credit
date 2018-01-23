<!-- page_number: true -->

# Datos de ejemplo: Prestamos en Alemania
* 1000 prestamos
* 20 atributos
	- 7 numéricos
	- 13 categóricos
* Disponibles en la capeta de datos.
	- `german.data`: datos
	- `german.txt`: descripción de los datos

---
# Ejemplos de atributos
* Atributo 1: Estado de cuenta de cheques
	- A11: < 0 Marcos alemánes (DM)
	- A12: entre 0 y 200 DM
	- A13: más de 200 DM
	- A14: no tiene cuenta de cheques
* Atributo 2: Duración en meses
	- Atributo numérico

---
# Ejemplos de atributos
* Atributo 3: Historial de créditos
	- A30: No ha aceptado créditos
	- A31: Todos los créditos han sido pagados completamente.]
	- A32: Créditos existentes, anteriores pagados completamente
	- A33: Retrazos en pagos de créditos anteriores
	- A34: Cuénta en números rojos
* Atributo 5: Importe del crédito
	- Numérico

---
# Resultados de los créditos
* La última columna representa créditos _buenos_ ó _malos_
	- 1 _->_ _bueno_
	- 2 _->_ _malo_

* Matriz de costo
	|resultado  \ predicho | _`bueno`_ | _`malo`_ |
	|-|-|-|
	|_`bueno`_|0|1|
	|_`malo`_|5|0|
    
    - Es peor clasificar un cliente como _bueno_ cuando en realidad es _malo_ que clasificarlo como _malo_ cuano es _bueno_.

---
# Ejercicio
* Hacer visualizaciónes de los datos de créditos alemanes
	- Histogramas para los atributos numéricos
	- Gráficos de pastel/dona para atribútos categóricos

