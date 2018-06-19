# Migración Harvest a Bitbucket
El siguiente proyecto consta de un scripts desarrollado en Python 2.7 para la migración de packages [Harvest](https://www.ca.com/ar/products/ca-harvest-software-change-manager.html) a [Bitbucket Cloud](https://confluence.atlassian.com/get-started-with-bitbucket). 
Para esto, el script descarga todos los últimos 40 paquetes del ambiente **Modelo de desarrollo paralelo**. En caso de querer migrar todos los repositorios, modificar comando batch de la fuenten [listado_fuentes.py](src/listado_fuentes.py)
## HOWTO
* Clonar el repositorio remoto a repositorio local
* Ingresar al repositorio local a traves de la consola
* Ejecutar el siguiente comando
	* ´./test-env.sh migrate_to_bitbucket´