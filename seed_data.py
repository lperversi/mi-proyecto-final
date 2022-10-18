from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")

#1ro importo el modelo, 2do genero el objeto Familiar (con nombre, direcc y pasaporte) y 
#3ro con save lo guardo