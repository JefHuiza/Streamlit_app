
import streamlit as st
import pandas as pd

# Estilo personalizado para el título
titulo_style = """
<style>
    .titulo {
        font-family: "Arial", sans-serif;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
</style>
"""

# Mostrar el título con estilo personalizado
st.markdown(titulo_style, unsafe_allow_html=True)
st.markdown('<p class="titulo">Casos Positivos del Covid-2019</p>', unsafe_allow_html=True)



import streamlit as st
from PIL import Image


# Ruta de la imagen del logo
ruta_logo = "nombre_del_logo.png"  # Reemplaza "nombre_del_logo.png" con el nombre de tu archivo de imagen

# Establecer el tamaño de la columna
st.sidebar.image(ruta_logo, use_column_width=True)


# Cargar y mostrar la segunda imagen debajo del logo
image = Image.open('i.png')
st.sidebar.image(image, use_column_width=True)






# Generar tres espacios en blanco
espacios = "<br>" * 1

# Mostrar los tres espacios en blanco
st.markdown(espacios, unsafe_allow_html=True)


# Subtítulo
st.subheader("Integrantes:")

# Lista de integrantes
integrantes = ["○ Elmer Taipe Llamoca",
               "○ Cristian Nelson Lima Huamani",
               "○ Miguel Angel Sanchez Rosario",
               "○ Jefferson Huiza Quispe"]

# Mostrar la lista de integrantes
for integrante in integrantes:
    st.write(integrante)

import streamlit as st

# Generar tres espacios en blanco
espacios = "<br>" * 2

# Mostrar los tres espacios en blanco
st.markdown(espacios, unsafe_allow_html=True)

import streamlit as st

# Texto en formato formal
texto_formal = """
En esta página se presenta el registro diario de casos positivos de COVID-19 confirmados mediante pruebas y que presentan síntomas. Cada registro corresponde a una persona, y se recopilan datos como el sexo, la edad y la ubicación geográfica, incluso a nivel de distrito.

La Directiva Sanitaria para la vigilancia epidemiológica del Coronavirus en el Perú establece las directrices y procedimientos para la identificación de casos positivos. Para obtener más información detallada, puedes consultar el siguiente enlace:

[https://www.gob.pe/institucion/minsa/normas-legales/1322786-905-2020-minsa](https://www.gob.pe/institucion/minsa/normas-legales/1322786-905-2020-minsa)

Es importante tener en cuenta que, a partir del 2 de junio de 2020, los casos detectados mediante pruebas rápidas no incluyen los resultados de las instituciones privadas que realizan tamizajes a los trabajadores de empresas en el contexto de la reactivación económica. Esto se debe a que el objetivo de estos tamizajes no es identificar nuevos casos en personas sospechosas.

La fuente de esta información es el Instituto Nacional de Salud y el Centro Nacional de Epidemiología, Prevención y Control de Enfermedades del Ministerio de Salud (MINSA).
"""

# Establecer el estilo del texto centrado
texto_centrado = """
<style>
    .center-text {
        text-align: center;
    }
</style>
"""

# Mostrar el texto centrado en formato formal
st.markdown(texto_centrado + texto_formal, unsafe_allow_html=True)




import pandas as pd
import streamlit as st

# Ruta del archivo CSV
csv_path = 'positivos_covid.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(csv_path, delimiter=';')

import streamlit as st
import streamlit as st

st.write("\n**Escoge un departamento, una provincia y un distrito para filtrar los datos que se tienen. Sea paciente**.\n")

import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('positivos_covid.csv', delimiter=';')

# Crear selectores desplegables para departamento, provincia y distrito
departamentos = df['DEPARTAMENTO'].unique()
departamento_seleccionado = st.selectbox('Selecciona un departamento:', departamentos)

provincias = df[df['DEPARTAMENTO'] == departamento_seleccionado]['PROVINCIA'].unique()
provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)

distritos = df[(df['DEPARTAMENTO'] == departamento_seleccionado) & (df['PROVINCIA'] == provincia_seleccionada)]['DISTRITO'].unique()
distrito_seleccionado = st.selectbox('Selecciona un distrito:', distritos)


# Mostrar el número de personas registradas en las condiciones seleccionadas
num_personas = len(filtered_data)
st.write('Número de personas contagiadas:', num_personas)


import streamlit as st

st.write(" \n**A continuacion, se muestran los casos de contagio de acuerdo al sexo de las personas mediante un grafico:**\n")




import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource

# Filtrar los datos por departamento, provincia y distrito
datos_filtrados = df[(df['DEPARTAMENTO'] == departamento_seleccionado) &
                     (df['PROVINCIA'] == provincia_seleccionada) &
                     (df['DISTRITO'] == distrito_seleccionado)]

# Contar los registros por sexo
registros_por_sexo = datos_filtrados['SEXO'].value_counts().reset_index()
registros_por_sexo.columns = ['Sexo', 'Número de registros']

# Crear el gráfico de barras con colores personalizados
p = figure(x_range=registros_por_sexo['Sexo'], plot_height=400, plot_width=600,
           title='Número de Registros por Sexo', toolbar_location=None, tools='')

p.vbar(x='Sexo', top='Número de registros', width=0.9, source=ColumnDataSource(registros_por_sexo),
       line_color='black', fill_color=['#FF5733', '#C70039'])  # Colores personalizados

p.xgrid.grid_line_color = None
p.y_range.start = 0

# Mostrar el gráfico utilizando Bokeh
show(p)




st.write(" \n**En este apartado, se muestran los casos de contagio de acuerdo a la edad de las personas en una tabla de distribucion:**\n")

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource

# Filtrar los datos por departamento, provincia y distrito
datos_filtrados = df[(df['DEPARTAMENTO'] == departamento_seleccionado) &
                     (df['PROVINCIA'] == provincia_seleccionada) &
                     (df['DISTRITO'] == distrito_seleccionado)]

# Contar los registros por edad
registros_por_edad = datos_filtrados['EDAD'].value_counts().reset_index()
registros_por_edad.columns = ['Edad', 'Número de registros']

# Crear el gráfico de barras
p = figure(x_range=list(map(str, registros_por_edad['Edad'])), plot_height=400, plot_width=600,
           title='Número de Registros por Edad', toolbar_location=None, tools='')

p.vbar(x='Edad', top='Número de registros', width=0.9, source=ColumnDataSource(registros_por_edad))

p.xgrid.grid_line_color = None
p.y_range.start = 0

# Mostrar el gráfico utilizando Bokeh
show(p)


st.write(" \n**Con respecto al tipo de pruebas que se realizaron, se tienen las siguientes estadisticas:**\n")


import pandas as pd
import seaborn as sns
import streamlit as st

# Cargar los datos del archivo CSV
df = pd.read_csv('positivos_covid.csv', delimiter=';')

# Filtrar los datos por departamento, provincia y distrito
datos_filtrados = df[(df['DEPARTAMENTO'] == departamento_seleccionado) &
                     (df['PROVINCIA'] == provincia_seleccionada) &
                     (df['DISTRITO'] == distrito_seleccionado)]

# Contar los registros por método de diagnóstico
registros_por_metodo = datos_filtrados['METODODX'].value_counts().reset_index()
registros_por_metodo.columns = ['Método de Diagnóstico', 'Número de Registros']

# Crear el gráfico de barras utilizando seaborn
sns.barplot(x='Método de Diagnóstico', y='Número de Registros', data=registros_por_metodo)

# Configurar el título y etiquetas de los ejes
plt.title('Número de Registros por Método de Diagnóstico')
plt.xlabel('Método de Diagnóstico')
plt.ylabel('Número de Registros')

# Mostrar el gráfico
st.pyplot()


import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Crear el DataFrame con los datos de la leyenda
leyenda_data = pd.DataFrame({
    'MétodoDX': ['PC', 'PCR', 'Ag'],
    'Descripción': ['Pruebas Rápidas', 'Reacción en Cadena de Polimerasa', 'Prueba de Antígenos']
})

# Estilo personalizado para la tabla
estilo = """
<style>
    .tabla-leyenda {
        color: white;
        background-color: #FF4F40;
        padding: 10px;
    }
    .tabla-leyenda th {
        background-color: #FF220C;
        padding: 10px;
    }
    .tabla-leyenda td {
        background-color: #318CE7;
        padding: 10px;
    }
</style>
"""

# Mostrar la tabla con estilo personalizado
components.html(estilo, height=0)
st.markdown('<div class="tabla-leyenda"> </div>', unsafe_allow_html=True)
st.table(leyenda_data)


# Cargar el archivo CSV con delimitador ","
df = pd.read_csv('positivos_covid.csv', delimiter=',')

# Imprimir los nombres de las columnas
columnas = df.columns.tolist()
print(columnas)

