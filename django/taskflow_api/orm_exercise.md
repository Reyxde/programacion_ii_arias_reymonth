>>> control_vuelos.objects.all()
<QuerySet [<control_vuelos: 01>]>

>>> control_vuelos.objects.create(
... id_vuelo= "02"
... )
<control_vuelos: 02>
>>> p = control_vuelos(id_vuelo="03", destino="URG")
>>> p.save()

>>> control_vuelos.objects.all()
<QuerySet [<control_vuelos: 01>, <control_vuelos: 02>, <control_vuelos: 03>]>
>>> 
KeyboardInterrupt
>>> 
>>> control_vuelos.objects.get(id_vuelo="01")
<control_vuelos: 01>
>>> 

