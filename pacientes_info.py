#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:23:29 2020

@author: necidcanedo
"""
import pandas as pd


def registrar_paciente(paciente, db):
    df=pd.DataFrame(paciente,index=[1])
    df.to_sql('pacientes_info', db, if_exists='append', index=False);
    data = pd.read_sql('SELECT MAX(id) FROM pacientes_info', db)
    return int(data['MAX(id)'][0])
    
def consultar_paciente(cedula, db):
    data = pd.read_sql('SELECT id, nombre, apellido, cedula, celular FROM pacientes_info WHERE cedula="{}"'.format(cedula), db)
    return data.iloc[0].to_dict()

