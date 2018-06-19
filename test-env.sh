#!/usr/bin/env bash

NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)

function red() {
  echo -e "$RED$*$NORMAL"
}

function green() {
  echo -e "$GREEN$*$NORMAL"
}

function yellow() {
  echo -e "$YELLOW$*$NORMAL"
}

case "$1" in
  migrate_to_bitbucket)
    cd src
    green "CAPTURANDO LISTADO PARA BAJADA DE FUENTES"
    python listado_fuentes.py
    green "LIMPIANDO ARCHIVO DE LISTADO"
    python limpiar_listado.py
    green "BAJANDO FUENTES"
    python bajar_fuentes.py
    green "PUSHEANDO REPOSITORIOS"
    python push_packages.py
    ;;
  migrate_to_harvest)
    
    ;;
esac