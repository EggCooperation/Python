from typing import Any, Callable


def validar_entrada(etiqueta: str, acciones: tuple[Callable, ...]) -> None | str:
    while True:
        entrada_validada: Any = False
        try:
            entrada: Any = input(etiqueta)
        except KeyboardInterrupt:
            return None
        for acción in acciones:
            entrada_validada = acción(entrada)
            if not entrada_validada:
                break
            else:
                entrada = entrada_validada
        if not entrada_validada:
            continue
        else:
            return entrada


def crear_estructura_datos(datos: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    id_datos: int = 0
    datos_validados: dict[int, dict[str, Any]] = {}
    for elemento in datos:
        for clave, valor in elemento.items():
            if clave == "id":
                id_datos = valor
                datos_validados[id_datos] = {}
            else:
                datos_validados[id_datos].update({clave: valor})
    return datos_validados


def entrada(formulario:  dict[str, dict[str, Any]]) -> dict[int, Any] | None:
    datos: list[dict] = []
    formulario_validado = False
    for clave_formulario, valor in formulario.items():
        etiqueta = valor['etiqueta']
        acciones = valor['acciones']
        entrada_validada: Any = validar_entrada(etiqueta, acciones)
        if not entrada_validada:
            print("\n❌ Formulario no válido")
            formulario_validado = False
            break
        else:
            formulario_validado = True
            datos.append({clave_formulario: entrada_validada})
    if not formulario_validado:
        return None
    else:
        datos_estructurados = crear_estructura_datos(datos)
        return datos_estructurados
