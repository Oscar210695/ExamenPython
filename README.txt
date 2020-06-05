Creado Por Oscar Arias Velázquez

Aplicación para para realizar el flujo de compras de
mercancía para la empresa Ilusiones S.A. de C.V. generando las ordenes de compras para cada
almacén de acuerdo al archivo Orden de Compras y realizando la recepción de la mercancía para
cada almacén de acuerdo al archivo Recepción de Mercancía.

Pestaña Almacenes: Se listan los almacenes disponibles donde se les puede, actualizar(haciendo click sobre el nombre), 
  borrar, añadir uno nuevo o incluso consultar el inventario del mismo.
Pestaña Cargar Orden de compra: Se hacen validaciones para certificarse que el archivo cumple con los requisitos para ser
  cargado y de la misma se valida que se llene el campo de de Clave donde esta debe ser única y debe cumplir con una expresión regular
  (solo números y/o letras), al igual que el archivo solo debe ser de tipo Excel, siendo estos dos obligatorios.
Pestaña ordenes: Se listan todas las ordenes generadas identificadas por su clave única, donde a cada uno se le pude cargar un Excel 
  (en caso de que no haya sido previamente cargado) donde es validado para certificarse que el archivo cumple con los requisitos y a
  su ves si todo es correcto genera el inventario del mismo.
Inventario General: Se listan todos los productos con su respectivo IMEI, nombre del producto y FOLIO con el que fue entregado, la 
   tabla se encuentra paginada a 10 registros.
   
**En el caso de que los productos en los archivos no existieran se cargan automaticamente
**Las cargas de archivos pueden demorar de acuerdo al tamaño del archivo
**LA interacción con el modelo de la base de datos esta en una API REST de Django

URL Heroku: https://ilusiones-web.herokuapp.com/
URL´s API:
  https://ilusiones-web.herokuapp.com/api/almacen
  https://ilusiones-web.herokuapp.com/api/prod
  https://ilusiones-web.herokuapp.com/api/orden
  https://ilusiones-web.herokuapp.com/api/ordenIn
  https://ilusiones-web.herokuapp.com/api/recep
  https://ilusiones-web.herokuapp.com/api/inven
  https://ilusiones-web.herokuapp.com/api/invAlm

  
