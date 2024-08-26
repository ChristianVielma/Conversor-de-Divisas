### Crear el entorno virtual
´´´python
python -m venv .venv
´´´
#### Activamos el entorno virtual
´´´shellp
.\env\Scripts\activate
source .env/bin/activat 
´´´

#### Instalar Flask
´´´python 
pip install flask
´´´
#### mostrar paquetes instalados 
´´´python
pip freeze
pip freeze > paquetes.txt

#### En caso de recrear el proyecto
´´´
pip install -r paquetes.txt
´´´
#### traer cambios de repositorio
´´´
git pull

