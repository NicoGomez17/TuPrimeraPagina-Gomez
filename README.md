# TuPrimeraPagina-Gomez

# Entrega Django - App Prueba (Blog de Viajes)


## Instrucciones para probar la aplicación:

1. **Preparar la BD:** Ejecutar en la terminal:
   - `python manage.py makemigrations`
   - `python manage.py migrate`

2. **Iniciar el servidor:** 
   - `python manage.py runserver`

3. **Orden de prueba sugerido:**
   - **Paso 1:** cargar un autor.
   - **Paso 2:** cargar una categoría (ej: "Playa").
   - **Paso 3:** crear un post (ej: Título: "Viaje a la Costa").
   - **Paso 4:** escribir "Costa" en el cuadro y presionar Buscar. El resultado aparecerá debajo del formulario.