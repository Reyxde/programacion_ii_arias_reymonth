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
>>> control_vuelos.objects.get(id_vuelo="01")
<control_vuelos: 01>
>>> 

control_vuelos.objects.get(id_vuelo="No existe")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/Rey/Documents/programacion_ii_arias_reymonth/django/taskflow_api/venv/lib/python3.14/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/Rey/Documents/programacion_ii_arias_reymonth/django/taskflow_api/venv/lib/python3.14/site-packages/django/db/models/query.py", line 722, in get
    raise self.model.DoesNotExist(
        "%s matching query does not exist." % self.model._meta.object_name
    )
tasks.models.control_vuelos.DoesNotExist: control_vuelos matching query does not exist.

>>> control_vuelos.objects.get(destino__icontains="a")
<control_vuelos: 02>
