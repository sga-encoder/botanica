# Script para crear entorno virtual, activarlo e instalar dependencias en PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
