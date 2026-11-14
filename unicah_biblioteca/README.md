# Biblioteca UNICAH - Módulo Odoo

## Datos del Estudiante
**Nombre:** José Isaías Lagos Rodríguez
**Número de Cuenta:** 0703199402245
**Universidad:** UNICAH
**Materia:** Programación de Negocios
**Año:** 2026

## Descripción del Proyecto
Módulo de Odoo para gestionar los préstamos de libros de la Biblioteca UNICAH.
Resuelve el problema del control manual en cuadernos y Excel, donde se perdían libros y no se sabía quién tenía cada libro ni cuándo vencía.

Lo usaría el bibliotecario para registrar préstamos y el estudiante para consultar su historial.

## ¿Por qué en Odoo?
Porque Odoo ya tiene Contactos (`res.partner`) y Productos (`product.product`). Se heredan y no se crea todo de cero. Se aprovecha la seguridad, usuarios e interfaz de Odoo. Todo queda en un solo sistema.

## Requisitos Cumplidos
- [x] Modelo nuevo con más de 5 campos: `unicah.prestamo`
- [x] Campo Many2one: `estudiante_id` -> `res.partner` y `libro_id` -> `product.product`
- [x] Campo calculado: `dias_prestamo` = `fecha_devolucion` - `fecha_prestamo`
- [x] Permisos en `ir.model.access.csv`
- [x] Vistas de lista y formulario, una acción y un menú
- [x] Herencia de modelo: `res.partner` con `carnet_unicah`, `carrera`
- [x] Herencia de vista: `base.view_partner_form`
- [x] Validación / Regla de negocio: Fecha devolución no puede ser menor que préstamo y máximo 14 días

## Diseño - Modelo `unicah.prestamo`
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| name | Char | Nombre del libro |
| estudiante_id | Many2one | Estudiante que presta |
| libro_id | Many2one | Libro del catálogo |
| fecha_prestamo | Date | Fecha de préstamo |
| fecha_devolucion | Date | Fecha de devolución |
| dias_prestamo | Integer Calculado | Días de préstamo |
| estado | Selection | Prestado / Devuelto / Vencido |

## Reglas de Negocio
1. La fecha de devolución no puede ser antes que la fecha de préstamo.
2. El préstamo no puede superar 14 días, según reglamento de Biblioteca UNICAH.

## Estructura del Módulo