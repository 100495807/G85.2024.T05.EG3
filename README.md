# UC3M Travel - Hotel Management EG3

Evolucion del proyecto de gestion hotelera de Ingenieria del Software. Esta entrega reorganiza la solucion con una arquitectura mas modular: atributos validados, clases de dominio, almacenes JSON especializados y pruebas unitarias para verificar comportamiento y patrones de diseno.

## Objetivo

Refactorizar y ampliar el sistema de reservas de hotel para mejorar separacion de responsabilidades, validacion de datos y mantenibilidad del codigo.

El sistema cubre:

- creacion de reservas,
- llegada de huespedes desde fichero JSON,
- generacion de claves de habitacion,
- check-out,
- almacenamiento persistente en JSON,
- deteccion de datos manipulados o inconsistentes.

## Tecnologias

- Python
- JSON
- unittest
- freezegun
- PyBuilder
- Programacion orientada a objetos

## Arquitectura

| Carpeta | Contenido |
| --- | --- |
| `src/main/python/uc3m_travel/attributes/` | Validadores especificos para DNI, tarjeta, fecha, localizador, telefono, tipo de habitacion, etc. |
| `src/main/python/uc3m_travel/storage/` | Stores JSON para reservas, llegadas, check-ins y check-outs. |
| `src/main/python/uc3m_travel/` | Clases principales `HotelManager`, `HotelReservation` y `HotelStay`. |
| `src/unittest/python/` | Pruebas unitarias del sistema y del patron singleton en stores. |

## Funcionalidades Destacadas

- Validacion encapsulada por tipo de atributo.
- Stores JSON reutilizables mediante una clase base.
- Uso de patron singleton en almacenes para evitar estados duplicados.
- Verificacion de integridad entre localizador, reserva y estancia.
- Pruebas automatizadas para flujos y casos limite.

## Como Ejecutar Pruebas

Desde la raiz del proyecto:

```bash
python -m unittest discover src/unittest/python
```

Con PyBuilder:

```bash
pyb
```

## Aprendizajes

- Refactorizar una solucion funcional hacia una arquitectura mas mantenible.
- Separar validaciones en objetos especializados.
- Aplicar patrones como singleton en componentes de almacenamiento.
- Proteger la consistencia de datos persistidos en ficheros JSON.
- Ampliar pruebas para cubrir estructura interna y comportamiento externo.

## Estado

Proyecto academico finalizado. Se conserva como evolucion modular del sistema hotelero desarrollado en EG2.