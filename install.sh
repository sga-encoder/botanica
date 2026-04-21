#!/bin/bash
# Script para crear entorno virtual, activarlo e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
