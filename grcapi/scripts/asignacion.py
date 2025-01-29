from extraccion.models import Registro,Aplicativo,Perfil,Area,Responsable

def encontrarAplicativo(app):
    """
        Retorna el objeto del aplicativo. En caso de no encontrarlo
        lo crea.
    """
    try: 
        return Aplicativo.objects.get(nombre=app)
    except Aplicativo.DoesNotExist:
        obj_app = Aplicativo.objects.create(nombre=app)
        return obj_app
    
def encontarArea(area):
    """
        Retorna el objeto area. En caso de no encontrarlo lo crea.
    """
    try: 
        return Area.objects.get(nombre=area)
    except Area.DoesNotExist:
        obj_area= Area.objects.create(nombre=area)
        return obj_area
    except NameError:
        return None
    
def encontrarPerfil(perfil,area):
    """
        Retorna el objeto perfil. En caso de no encontrarlo lo crea.
    """
    try: 
        return Perfil.objects.get(nombre=perfil)
    
    except Perfil.DoesNotExist:
        # ubicamos el area a la que pertenece
        obj_area = encontarArea(area)
        obj_perfil = Perfil.objects.create(nombre=perfil, area=obj_area)
        return obj_perfil
    
def encontrarResponsable(responsable):
    """
        Retorna el objeto responsable. En caso de no encontrarlo lo crea.
    """
    try: 
        return Responsable.objects.get(nombre=responsable)
    
    except Responsable.DoesNotExist:
        obj_responsable = Perfil.objects.create(nombre=responsable)
        return obj_responsable
    

