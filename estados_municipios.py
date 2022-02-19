""" Agregado dos estados e municipios para aplicação """

from pyUFbr.baseuf import ufbr

def retornaEstado():
    estados = ufbr.list_uf
    return estados

def retornaMunicipios(estado):
    municipios = ufbr.list_cidades(estado)
    return municipios
