<h1>Lista de Tareas - Aplicación Web</h1>

<p>Este proyecto es una aplicación web de lista de tareas desarrollada con Python y Flask. Permite gestionar tareas pendientes, completarlas, eliminarlas y exportar/importar las tareas a través de archivos JSON. Además, cuenta con una interfaz gráfica sencilla utilizando HTML y CSS.</p>

<h2>Funcionalidades</h2>
<ul>
  <li><strong>Crear tareas</strong>: Añadir nuevas tareas con un título y una descripción.</li>
  <li><strong>Modificar tareas</strong>: Marcar tareas como completadas.</li>
  <li><strong>Eliminar tareas</strong>: Eliminar tareas de la lista.</li>
  <li><strong>Exportar e Importar tareas</strong>: Exportar la lista de tareas a formato JSON o importar nuevas tareas desde un archivo JSON.</li>
  <li><strong>Interfaz gráfica</strong>: Una sencilla interfaz de usuario desarrollada con HTML y CSS.</li>
</ul>

<h2>Requisitos</h2>
<p>Para ejecutar este proyecto, necesitas tener Python 3.x instalado en tu sistema.</p>
<ul>
  <li><a href="https://pypi.org/project/Flask/" target="_blank">Flask</a> (para la aplicación web)</li>
</ul>

<p>Puedes instalar Flask usando <code>pip</code>:</p>

<pre><code>pip install flask</code></pre>

<h2>Instalación</h2>
<ol>
  <li>Clona el repositorio en tu máquina local:
    <pre><code>git clone https://github.com/Brahiam12/Proyecto-TO-DO-LIST.git</code></pre>
  </li>
  <li>Accede al directorio del proyecto:
    <pre><code>cd  ProyectoTO-DO </code></pre>
  </li>
  <li>Instala las dependencias necesarias:
    <pre><code>pip install -r requirements.txt</code></pre>
    (Si no tienes el archivo <code>requirements.txt</code>, puedes crear uno con el siguiente contenido):
    <pre><code>flask==2.3.0</code></pre>
  </li>
</ol>

<h2>Uso</h2>
<ol>
  <li><strong>Iniciar el servidor</strong>: Una vez que hayas instalado las dependencias, ejecuta el siguiente comando para iniciar la aplicación web:
    <pre><code>python app.py</code></pre>
  </li>
  <li>Abre tu navegador web y visita la dirección <code>http://127.0.0.1:5000/</code> para ver la aplicación en acción.</li>
</ol>

<h2>Estructura del Proyecto</h2>
<p>El proyecto tiene la siguiente estructura:</p>

<pre><code>
project/
├── app.py        # Código principal de la aplicación
├── static/       # Archivos CSS, JS e imágenes
│   ├── style.css
├── templates/    # Archivos HTML
│   ├── index.html
└── tareas.json    # Almacenamiento de datos en formato JSON
</code></pre>

<ul>
  <li><strong>app.py</strong>: Archivo principal que contiene la lógica de la aplicación Flask.</li>
  <li><strong>static/style.css</strong>: Estilos para la interfaz de usuario.</li>
  <li><strong>templates/index.html</strong>: Plantilla HTML que muestra la lista de tareas y permite la interacción.</li>
  <li><strong>tasks.json</strong>: Archivo que guarda las tareas en formato JSON.</li>
</ul>

<h2>Rutas disponibles</h2>
<ul>
  <li><strong>GET /</strong>: Muestra la lista de tareas.</li>
  <li><strong>POST /add</strong>: Añade una nueva tarea.</li>
  <li><strong>POST /complete/&lt;int:task_id&gt;</strong>: Marca una tarea como completada.</li>
  <li><strong>POST /delete/&lt;int:task_id&gt;</strong>: Elimina una tarea.</li>
  <li><strong>GET /export</strong>: Exporta las tareas en formato JSON.</li>
  <li><strong>POST /import</strong>: Importa tareas desde un archivo JSON.</li>
</ul>

<h2>Contribuciones</h2>
<p>Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio y enviar un pull request. Asegúrate de seguir las mejores prácticas de codificación y de añadir pruebas cuando sea necesario.</p>

<h2>Licencia</h2>
<p>Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo <a href="LICENSE">LICENSE</a>.</p>
