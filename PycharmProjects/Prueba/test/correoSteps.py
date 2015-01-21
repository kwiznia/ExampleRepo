__author__ = 'kwiznia'
from lettuce import *
import correo

class correoSteps():

    correo = correo()

    @step("^Un usuario y una contrasena registrados$")

    @step("^Introduzco credenciales validos$")
    def yo_introduzco(self):
        print("Todo en orden")


    @step("^Estare en la pagina principal y el boton redactar es \"([^\"]*)\"$")
    def estare_en(self, boton):
        assert correo.get_boton() == boton
        return ("El resultado esperado era" + correo.get_boton() + "y fue :" + boton)
