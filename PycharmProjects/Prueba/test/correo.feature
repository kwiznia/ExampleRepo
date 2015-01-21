@correo

Feature: Correo Gmail

Scenario Outline: Abrir el correo satisfactoriamente  
Given Un usuario y una contrasena registrados
When Introduzco credenciales validos 
Then Estare en la pagina principal y el boton redactar es <c>

Examples: 
|c|
|"REDACTAR"|