# -*- coding: utf-8 -*-
"""Artículos del blog de Muralia.

Cada artículo es un diccionario; tools/build_blog.py genera /blog/<slug>.html,
el índice /blog.html, el bloque de artículos del inicio y el sitemap.

Para agregar un artículo: copia uno existente al principio de POSTS, cambia sus
datos y ejecuta  python3 tools/build_blog.py
- slug: palabras clave del rubro, en minúsculas y con guiones (es la URL).
- title: título SEO (pestaña del navegador y Google), idealmente < 60 caracteres.
- h1: título visible del artículo.
- meta: descripción para Google (140-160 caracteres).
- image: foto principal (idealmente 16:9, en img/blog/), con su ancho y alto.
- body: HTML del artículo. Los <h2> arman el índice automáticamente.
  Usa fig(...) para insertar fotos.
- related: slugs de productos (products.json) que se enlazan al final.
- faq: preguntas frecuentes (también se publican como datos estructurados).
"""


def fig(src, alt, caption, w, h):
    return (f'<figure><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">'
            f'<figcaption>{caption}</figcaption></figure>')


POSTS = [
# ---------------------------------------------------------------------------
{
"slug": "reglamentacion-termica-zonas-termicas",
"title": "Reglamentación térmica 2025: zonas térmicas y exigencias",
"h1": "Nueva reglamentación térmica en Chile: zonas térmicas A a la I y qué exige desde noviembre de 2025",
"meta": "Qué cambió con la actualización del artículo 4.1.10 de la OGUC: 9 zonas térmicas (A a I), transmitancias máximas, condensación, infiltraciones y ventilación.",
"kicker": "Aislación térmica y acústica",
"date": "2026-09-27",
"image": ("/img/blog/reglamentacion-termica-zonas-termicas.jpg", 1024, 576),
"image_alt": "Muro exterior de un edificio aislado con paneles de lana mineral alrededor de una ventana",
"excerpt": "Desde el 28 de noviembre de 2025 rige la nueva reglamentación térmica: 9 zonas, más exigencias para techos, muros y pisos, y nuevos requisitos de condensación, infiltraciones y ventilación.",
"related": ["lana-de-vidrio-papel-kraft", "lana-de-vidrio-libre", "lana-mineral", "panel-velo-negro"],
"body": f"""
<p class="lead-p">El <strong>28 de noviembre de 2025</strong> entró en vigor la actualización de la reglamentación térmica, contenida en el <strong>artículo 4.1.10 de la Ordenanza General de Urbanismo y Construcciones (OGUC)</strong>. Fue publicada en el Diario Oficial el 27 de mayo de 2024 mediante el DS N°15 del MINVU, y se aplica a todas las solicitudes de permiso de edificación que ingresan a la Dirección de Obras desde esa fecha.</p>

<h2>¿Qué es la reglamentación térmica?</h2>
<p>Es el conjunto de exigencias mínimas que debe cumplir la <strong>envolvente</strong> de un edificio (techos, muros, pisos, ventanas y puertas) para limitar las pérdidas y ganancias de calor. Según el MINVU, su objetivo es mejorar el comportamiento higrotérmico de las viviendas: más confort interior, menor consumo de energía y menos patologías como hongos y condensación.</p>
<p>La versión anterior regía desde 2007. La actualización aumenta las exigencias y, por primera vez, las extiende más allá de la vivienda.</p>

<h2>¿A qué edificaciones se aplica?</h2>
<ul>
<li>Edificaciones de <strong>uso residencial</strong>.</li>
<li>Establecimientos de <strong>educación</strong> y <strong>salud</strong>, que por primera vez tienen exigencias térmicas mínimas.</li>
<li>En comunas con <strong>Plan de Descontaminación Atmosférica (PDA)</strong>, las viviendas deben cumplir las exigencias del PDA correspondiente.</li>
</ul>

<h2>Las nuevas zonas térmicas: de 7 a 9</h2>
<p>El país pasó de 7 a <strong>9 zonas térmicas, identificadas con letras de la A a la I</strong>. Se definen según la norma <strong>NCh1079:2019</strong> considerando los grados-día de calefacción, la oscilación térmica y la radiación solar, lo que permite reconocer el efecto del mar, los valles y la cordillera.</p>
<table>
<thead><tr><th>Zona</th><th>Localidades representativas (MINVU)</th></tr></thead>
<tbody>
<tr><td>A</td><td>Arica, Iquique, Antofagasta</td></tr>
<tr><td>B</td><td>María Elena, Copiapó, Vallenar</td></tr>
<tr><td>C</td><td>Coquimbo, Valparaíso, Licantén</td></tr>
<tr><td>D</td><td>Santiago, Rancagua, Talca</td></tr>
<tr><td>E</td><td>Constitución, Concepción, Toltén</td></tr>
<tr><td>F</td><td>Chillán, Temuco, Río Bueno</td></tr>
<tr><td>G</td><td>Valdivia, Osorno, Puerto Montt</td></tr>
<tr><td>H</td><td>Putre, Lonquimay, Pucón</td></tr>
<tr><td>I</td><td>Coyhaique, Puerto Natales, Punta Arenas</td></tr>
</tbody>
</table>
<p>La zona no depende solo de la comuna: en la Región Metropolitana, por ejemplo, el límite entre la zona D y la H es la cota de <strong>2.000 metros sobre el nivel del mar</strong>. El MINVU publica los mapas y la tabla de zonas por región, provincia y comuna.</p>

<h2>Qué exige: más aislación y nuevos requisitos</h2>
<h3>Aumentan las exigencias</h3>
<ul>
<li><strong>Techos, muros y pisos ventilados</strong>: menores transmitancias térmicas máximas (valor U) en la mayoría de las zonas.</li>
<li><strong>Ventanas</strong>: porcentaje máximo de superficie vidriada según la orientación y el valor U de la ventana.</li>
</ul>
<h3>Exigencias nuevas</h3>
<ul>
<li>Sobrecimientos y puertas exteriores.</li>
<li><strong>Infiltraciones de aire</strong>: la envolvente debe cumplir una clase máxima de infiltración según la provincia, y puertas y ventanas deben cumplir requisitos de permeabilidad al aire.</li>
<li><strong>Condensación</strong>: se debe verificar que no exista riesgo de condensación superficial ni intersticial en techos, muros y pisos ventilados. El MINVU dispone de una planilla de cálculo para ello.</li>
<li><strong>Ventilación</strong>: las viviendas deben incorporar sistemas de ventilación.</li>
</ul>

<h2>Ejemplo: zona D (Santiago, Rancagua, Talca)</h2>
<p>Según el material técnico del MINVU, en la zona D la transmitancia térmica máxima es:</p>
<table>
<thead><tr><th>Elemento</th><th>U máximo (W/m²K)</th><th>Resistencia térmica mínima equivalente (R = 1/U)</th></tr></thead>
<tbody>
<tr><td>Techo</td><td>0,38</td><td>≈ 2,63 m²K/W (R100 ≈ 263)</td></tr>
<tr><td>Muro</td><td>0,80</td><td>1,25 m²K/W (R100 = 125)</td></tr>
<tr><td>Piso ventilado</td><td>0,60</td><td>≈ 1,67 m²K/W (R100 ≈ 167)</td></tr>
</tbody>
</table>
<p>Como lo explica el propio MINVU: en la zona D, 1&nbsp;m² de muro no puede perder más de 0,80&nbsp;W por cada grado de diferencia de temperatura entre el interior y el exterior.</p>
<div class="callout"><strong>¿Cuánto aislante significa?</strong> Como referencia, la ficha técnica de la lana de vidrio AislanGlass indica un R100 de 235 para el rollo de 100&nbsp;mm y de 282 para el de 120&nbsp;mm. El cálculo real se hace para la solución completa (todas sus capas, resistencias superficiales y puentes térmicos) según la NCh853, o eligiendo una solución del listado oficial.</div>

{fig("/img/productos/lana-de-vidrio-papel-kraft.jpg", "Rollo de lana de vidrio con papel kraft", "Con las nuevas exigencias de condensación, la barrera de vapor (como el papel kraft) debe especificarse e instalarse hacia el lado cálido.", 900, 900)}

<h2>Qué implica para proyectos y obras</h2>
<p>El MINVU resume así las implicancias de la actualización:</p>
<ul>
<li><strong>Mayores espesores de aislante</strong> en techos, muros y pisos ventilados.</li>
<li>Soluciones constructivas adecuadas al clima del lugar, para <strong>evitar condensación</strong>, hongos y moho.</li>
<li>Especificaciones técnicas detalladas de <strong>barreras de humedad y de vapor</strong> y de los aislantes.</li>
<li>Cálculos según la <strong>NCh853:2021</strong> y uso de la planilla de condensación del MINVU.</li>
<li>Mano de obra calificada para instalar barreras y aislación, y autocontrol en obra.</li>
</ul>

<h2>Cómo cumplir paso a paso</h2>
<ol>
<li>Identifica la <strong>zona térmica</strong> de la obra en los mapas y tablas del MINVU (considera la altitud).</li>
<li>Revisa los <strong>valores U máximos</strong> para cada elemento de la envolvente en esa zona.</li>
<li>Define la solución constructiva y el <strong>espesor de aislante</strong> por cálculo o desde el listado oficial.</li>
<li>Verifica el <strong>riesgo de condensación</strong> y especifica la barrera de vapor hacia el lado cálido.</li>
<li>Resuelve <strong>hermeticidad</strong> (infiltraciones) y <strong>ventilación</strong>.</li>
</ol>
<p>¿Tienes que cumplir la nueva reglamentación en tu proyecto? <a href="/contacto.html">Indícanos la zona y el elemento</a> y te ayudamos a definir el aislante y el espesor. También puedes leer <a href="/blog/lana-de-vidrio-vs-lana-mineral.html">lana de vidrio vs lana mineral</a>.</p>
""",
"faq": [
    ["¿Desde cuándo rige la nueva reglamentación térmica?", "Desde el 28 de noviembre de 2025. Fue publicada en el Diario Oficial el 27 de mayo de 2024 (DS N°15 del MINVU, que modifica el artículo 4.1.10 de la OGUC) y se aplica a los permisos de edificación que ingresan a la Dirección de Obras desde esa fecha."],
    ["¿Cuántas zonas térmicas hay en Chile?", "Nueve, identificadas con las letras A a la I, definidas según la NCh1079:2019. Antes eran siete."],
    ["¿En qué zona térmica está Santiago?", "En la zona D, junto con Rancagua y Talca. En la Región Metropolitana, sobre la cota de 2.000 metros sobre el nivel del mar corresponde la zona H."],
],
"sources": [
    ("Nueva Reglamentación Térmica", "Ministerio de Vivienda y Urbanismo (MINVU)", "https://www.minvu.gob.cl/nueva-reglamentacion-termica/"),
    ("Actualización de la reglamentación térmica – Implicancias (DITEC)", "MINVU", "https://www.minvu.gob.cl/wp-content/uploads/2025/11/Actualizacion-RT_DITEC.pdf"),
    ("D.S. N°47 de 1992, Ordenanza General de Urbanismo y Construcciones", "MINVU", "https://www.minvu.gob.cl/elementos-tecnicos/decretos/d-s-n47-1992-ordenanza-general-de-urbanismo-y-construccione/"),
    ("Características técnicas de la lana de vidrio AislanGlass", "Volcán", "https://media.prodalam.cl/material-descarga/60553/60553_20241219122950.pdf"),
],
},
# ---------------------------------------------------------------------------
{
"slug": "yeso-carton-st-rf-rh-diferencias",
"title": "Yeso cartón ST, RF y RH: diferencias y usos",
"h1": "Placas de yeso cartón ST, RF y RH: diferencias, espesores y cuándo usar cada una",
"meta": "Diferencias entre placas de yeso cartón estándar (ST), resistente al fuego (RF) y resistente a la humedad (RH): composición, colores, espesores, pesos y usos.",
"kicker": "Tabiques y cielos",
"date": "2026-09-27",
"image": ("/img/blog/yeso-carton-st-rf-rh-diferencias.jpg", 1024, 576),
"image_alt": "Instalación de placas de yeso cartón en un tabique con aislación",
"excerpt": "Las tres placas se ven parecidas, pero no son intercambiables. Qué las diferencia, cómo reconocerlas y cuál usar en tabiques, cielos, baños y soluciones contra el fuego.",
"related": ["yeso-carton-estandar", "yeso-carton-resistente-al-fuego", "yeso-carton-resistente-a-la-humedad", "yeso-carton-resistente-al-impacto", "yeso-carton-con-atenuacion-acustica"],
"body": f"""
<p class="lead-p">La placa de yeso cartón es la base de la construcción en seco: tabiques, cielos, revestimientos de muros y protección de estructuras. En obra se habla de placas <strong>ST, RF y RH</strong>, y elegir la correcta es clave para la durabilidad y la seguridad del recinto.</p>

<h2>¿Qué es una placa de yeso cartón?</h2>
<p>Es una placa con un <strong>alma de yeso</strong>, que incorpora fibra de vidrio y otros componentes, revestida por ambas caras con papel de alta resistencia. Se atornilla a estructuras de acero galvanizado o madera. En Chile, las placas se rigen por las normas <strong>NCh146/1 y NCh146/2</strong>, que la ficha técnica de Knauf declara cumplir.</p>

<h2>Los tres tipos básicos</h2>
<h3>ST – Estándar</h3>
<p>Para <strong>recintos interiores secos</strong>. En la ficha de Knauf, la placa estándar lleva papel beige en la cara vista y crema en la oculta.</p>
<h3>RH – Resistente a la humedad</h3>
<p>Incorpora <strong>aditivos especiales</strong> que mejoran su comportamiento frente a la humedad. Se usa en <strong>baños, cocinas</strong> y recintos húmedos, pero no en superficies expuestas a agua directa. Se reconoce por su papel <strong>verde</strong>.</p>
<h3>RF – Resistente al fuego</h3>
<p>Tiene <strong>mayor cantidad de fibra de vidrio</strong> en el alma (0,2% de su peso, según Knauf), lo que mejora su comportamiento frente al fuego. Está pensada para recintos con altos requerimientos de protección contra incendios. Se reconoce por su papel <strong>rosa</strong>.</p>
<div class="callout">Los colores pueden variar entre fabricantes: confírmalos siempre en la ficha técnica y en el rotulado de la placa.</div>

<h2>Espesores, medidas y pesos</h2>
<p>Datos de la hoja técnica de placas Knauf (ancho 1.200&nbsp;mm; largos de 2.400 a 3.000&nbsp;mm):</p>
<table>
<thead><tr><th>Placa</th><th>Espesor (mm)</th><th>Peso (kg/m²)</th><th>Uso</th></tr></thead>
<tbody>
<tr><td>ST</td><td>8</td><td>6,1</td><td>Cielos</td></tr>
<tr><td>ST</td><td>10</td><td>6,9</td><td>Cielos y tabiques</td></tr>
<tr><td>ST</td><td>12,5</td><td>8,2</td><td>Tabiques y revestimientos</td></tr>
<tr><td>ST</td><td>15</td><td>10,9</td><td>Tabiques</td></tr>
<tr><td>RH</td><td>12,5 / 15</td><td>9,9 / 11,0</td><td>Baños y cocinas</td></tr>
<tr><td>RF</td><td>12,5 / 15</td><td>10,0 / 12,0</td><td>Soluciones con resistencia al fuego</td></tr>
</tbody>
</table>
<p>Las placas se fabrican con <strong>borde rebajado</strong> (para juntas invisibles con cinta y masilla), biselado o recto, según el tipo.</p>

{fig("/img/productos/yeso-carton-resistente-al-fuego.jpg", "Planchas de yeso cartón resistente al fuego", "Las placas RF se usan en tabiques y cielos que deben cumplir una resistencia al fuego.", 900, 598)}

<h2>¿Una placa RF basta para lograr resistencia al fuego?</h2>
<p>No por sí sola. La resistencia al fuego (F-30, F-60, F-120…) corresponde a la <strong>solución completa</strong>: número y tipo de placas, estructura, aislante y tratamiento de juntas. El <strong>Listado Oficial de Comportamiento al Fuego</strong> del MINVU incluye, por ejemplo, tabiques de estructura de acero con <strong>doble placa RF de 15&nbsp;mm</strong>. Lo explicamos en <a href="/blog/resistencia-al-fuego-f30-f60-f120.html">qué significa F-30, F-60 y F-120</a>.</p>

<h2>Otras placas especiales</h2>
<ul>
<li><strong>Resistente al impacto</strong>: para pasillos, colegios y recintos de alto tráfico.</li>
<li><strong>Con atenuación acústica</strong>: placas perforadas para cielos que controlan la reverberación.</li>
<li><strong>Con blindaje radiológico</strong>: para salas de rayos X.</li>
</ul>

<h2>Recomendaciones de instalación y almacenaje</h2>
<ul>
<li><strong>Almacena</strong> las placas en posición horizontal, sobre una superficie nivelada, bajo techo y protegidas de la humedad, apoyadas en fajas de unos 100&nbsp;mm separadas como máximo 500&nbsp;mm (Knauf, según NCh146/1).</li>
<li><strong>Trasládalas</strong> entre dos personas, en posición vertical y tomadas por los cantos.</li>
<li><strong>Atornilla</strong> aproximadamente cada 25&nbsp;cm en tabiques y cada 17&nbsp;cm en cielos, según la recomendación de Knauf.</li>
<li>Usa la placa correcta para cada recinto: RH en zonas húmedas y RF donde el proyecto exige resistencia al fuego.</li>
</ul>
<p>¿Necesitas cotizar placas para tu obra? <a href="/contacto.html">Envíanos las cantidades y espesores</a>.</p>
""",
"faq": [
    ["¿Qué diferencia hay entre yeso cartón ST, RF y RH?", "La ST es la placa estándar para interiores secos. La RH tiene aditivos para recintos húmedos como baños y cocinas. La RF tiene más fibra de vidrio en el alma para mejorar su comportamiento frente al fuego y se usa en soluciones con resistencia al fuego."],
    ["¿De qué color es el yeso cartón RF y el RH?", "En la ficha técnica de Knauf, la placa RF tiene papel rosa y la RH papel verde en la cara vista. Los colores pueden variar entre fabricantes, así que conviene confirmarlos en la ficha y el rotulado."],
    ["¿Se puede usar yeso cartón RH en una ducha?", "No en superficies expuestas a agua directa. La placa RH está pensada para recintos húmedos como baños y cocinas, pero no para recibir agua de forma directa."],
],
"sources": [
    ("Hoja técnica Knauf Placas de yeso-cartón (04/2019)", "Knauf", "https://neufert-cdn.archdaily.net/uploads/product_file/file/53202/Ficha_T%C3%A9cnica_Placas_de_yeso-cart%C3%B3n_Knauf.pdf"),
    ("Listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción, ED17-2025", "MINVU", "https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf"),
],
},
# ---------------------------------------------------------------------------
{
"slug": "placa-de-fibrosilicato",
"title": "Placa de fibrosilicato: qué es, usos y ventajas",
"h1": "Placa de fibrosilicato: qué es, para qué sirve y en qué se diferencia del yeso cartón",
"meta": "Qué es la placa de fibrosilicato (silicato de calcio), sus propiedades frente al fuego y la humedad, usos en protección pasiva y diferencias con el yeso cartón.",
"kicker": "Protección pasiva contra incendios",
"date": "2026-09-27",
"image": ("/img/blog/placa-de-fibrosilicato.jpg", 900, 506),
"image_alt": "Canto de una placa de fibrosilicato resistente al fuego",
"excerpt": "Una placa incombustible que resiste la humedad y se puede usar en interior y exterior. Qué es, sus propiedades técnicas y dónde conviene frente al yeso cartón.",
"related": ["placa-fibrosilicato", "pasta-para-juntas", "yeso-carton-resistente-al-fuego", "lana-mineral"],
"body": f"""
<p class="lead-p">La placa de fibrosilicato es una de las soluciones más usadas en <strong>protección pasiva contra incendios</strong>. Es incombustible, resiste la humedad y el impacto, y sirve tanto en interior como en exterior. Aquí revisamos sus propiedades con los datos de la ficha técnica de <strong>PROMATECT®-H</strong>, de Promat.</p>

<h2>¿Qué es una placa de fibrosilicato?</h2>
<p>Es una placa de <strong>silicato de calcio</strong> de gran formato. La ficha de Promat la describe como <strong>incombustible, autoportante, monolítica y estable dimensionalmente</strong>, de alta resistencia mecánica y apta para uso interior y exterior.</p>
<p>Es <strong>imputrescible y resistente a la humedad</strong>: según el fabricante, no se deteriora en lugares de alta humedad y, si absorbe agua, puede disminuir levemente su resistencia mecánica, que recupera al secarse.</p>

<h2>Propiedades técnicas (PROMATECT®-H)</h2>
<table>
<thead><tr><th>Propiedad</th><th>Valor aproximado</th></tr></thead>
<tbody>
<tr><td>Reacción al fuego</td><td>A1 (incombustible) según UNE-EN 13501-1</td></tr>
<tr><td>Densidad</td><td>870 kg/m³</td></tr>
<tr><td>Conductividad térmica λ</td><td>0,175 W/m·K</td></tr>
<tr><td>Resistencia a la difusión de vapor μ</td><td>20</td></tr>
<tr><td>Contenido de humedad</td><td>5 a 10%</td></tr>
<tr><td>Resistencia a flexión (longitudinal)</td><td>7,6 N/mm²</td></tr>
<tr><td>Resistencia a compresión</td><td>9,3 N/mm²</td></tr>
<tr><td>Formato estándar</td><td>1.220 × 2.440 mm</td></tr>
</tbody>
</table>
<p>Como referencia de peso, la ficha (edición Perú, 2022) indica aproximadamente 11,7&nbsp;kg/m² para la placa de 12&nbsp;mm y 14,6&nbsp;kg/m² para la de 15&nbsp;mm.</p>

<h2>¿Para qué se usa?</h2>
<p>Según Promat, la placa forma parte de sistemas de protección contra incendios como:</p>
<ul>
<li><strong>Particiones cortafuego</strong> interiores y exteriores (tabiques tipo sándwich).</li>
<li><strong>Cielos</strong> descolgados y autoportantes resistentes al fuego.</li>
<li><strong>Encajonamiento de servicios</strong>: bandejas portacables y tuberías.</li>
<li><strong>Protección de estructuras metálicas</strong>, tipo membrana o encajonada. Ver <a href="/blog/resistencia-al-fuego-f30-f60-f120.html">resistencia al fuego</a>.</li>
<li><strong>Compartimentación en fachadas</strong> y protección de equipos industriales.</li>
</ul>

<h2>Fibrosilicato vs. yeso cartón RF</h2>
<table>
<thead><tr><th>Aspecto</th><th>Fibrosilicato (PROMATECT®-H)</th><th>Yeso cartón RF</th></tr></thead>
<tbody>
<tr><td>Material</td><td>Silicato de calcio, sin papel</td><td>Alma de yeso con fibra de vidrio, revestida en papel</td></tr>
<tr><td>Humedad</td><td>Imputrescible y resistente a la humedad</td><td>Para recintos interiores; existen placas RH para zonas húmedas</td></tr>
<tr><td>Uso exterior</td><td>Sí, con tratamiento impermeabilizante</td><td>Interior</td></tr>
<tr><td>Peso (placa de 12–12,5 mm)</td><td>≈ 11,7 kg/m²</td><td>≈ 10,0 kg/m² (Knauf RF 12,5 mm)</td></tr>
<tr><td>Uso típico</td><td>Shafts, estructuras, zonas húmedas o expuestas, industria</td><td>Tabiques y cielos interiores de edificios</td></tr>
</tbody>
</table>
<p>No compiten entre sí: se eligen según la exigencia de fuego, la humedad, el impacto y la ubicación del elemento. En ambos casos, la <strong>resistencia al fuego la da el sistema completo</strong>, que en Chile debe acreditarse según la OGUC (ensayo NCh 935/1 o Listado Oficial del MINVU).</p>

{fig("/img/productos/pasta-para-juntas.jpg", "Pasta para juntas de placas de fibrosilicato", "Las juntas y cabezas de tornillos se tratan con la pasta de juntas del sistema.", 900, 599)}

<h2>Recomendaciones de instalación</h2>
<ul>
<li><strong>Corte</strong>: con sierra circular manual o de mesa con aspiración; para cortes curvos, sierra de calar.</li>
<li><strong>Fijación</strong>: tornillos autorroscantes de doble filete y cabeza cónica, o grapas con grapadora neumática industrial.</li>
<li><strong>Juntas</strong>: tratar juntas y cabezas de tornillos con la pasta de juntas del sistema.</li>
<li><strong>Terminación</strong>: admite pintura, aplicando antes una impregnación tapaporos. En exterior requiere tratamiento impermeabilizante.</li>
<li><strong>Seguridad</strong>: al cortar, no respirar el polvo. Usar aspiración, gafas de seguridad y protección respiratoria si la ventilación es insuficiente.</li>
</ul>
<p>¿Evaluando fibrosilicato para tu proyecto? <a href="/contacto.html">Cuéntanos el elemento y la resistencia exigida</a>.</p>
""",
"faq": [
    ["¿Qué es la placa de fibrosilicato?", "Es una placa de silicato de calcio, incombustible (clase A1), resistente a la humedad y de alta resistencia mecánica, que se usa en sistemas de protección pasiva contra incendios en interior y exterior."],
    ["¿La placa de fibrosilicato se puede usar en exterior?", "Sí. Según la ficha técnica de Promat, PROMATECT®-H es apta para interior y exterior; en exterior requiere un tratamiento impermeabilizante."],
    ["¿Qué diferencia hay entre fibrosilicato y yeso cartón?", "El fibrosilicato es silicato de calcio sin papel, imputrescible y apto para exterior; el yeso cartón tiene alma de yeso revestida en papel y se usa en interiores. La elección depende de la exigencia de fuego, la humedad y la ubicación."],
],
"sources": [
    ("Ficha técnica PROMATECT®-H, placa de fibrosilicato (agosto 2022)", "Promat", "https://media.promat.com/pi642769/original/901159562/ft_promatect-h_promat_agosto_2022_v0_peru.pdf"),
    ("Hoja técnica Knauf Placas de yeso-cartón (04/2019)", "Knauf", "https://neufert-cdn.archdaily.net/uploads/product_file/file/53202/Ficha_T%C3%A9cnica_Placas_de_yeso-cart%C3%B3n_Knauf.pdf"),
    ("Listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción, ED17-2025", "MINVU", "https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf"),
],
},
# ---------------------------------------------------------------------------
{
"slug": "aislacion-termica-de-galpones",
"title": "Aislación térmica de galpones: techo y muros",
"h1": "Aislación térmica de galpones: cómo aislar techos y muros metálicos y evitar la condensación",
"meta": "Cómo aislar térmicamente un galpón: lana de vidrio con polipropileno, foil o papel kraft, espesores y R100, control de condensación y recomendaciones de instalación.",
"kicker": "Aislación térmica y acústica",
"date": "2026-09-27",
"image": ("/img/blog/aislacion-termica-de-galpones.jpg", 1024, 576),
"image_alt": "Interior de una nave industrial con estructura de techumbre metálica",
"excerpt": "Las cubiertas metálicas se calientan en verano, se enfrían en invierno y generan condensación. Qué aislante usar en un galpón, con qué revestimiento y cuánto espesor.",
"related": ["lana-de-vidrio", "lana-de-vidrio-papel-kraft", "lana-de-vidrio-libre", "panel-velo-negro"],
"body": f"""
<p class="lead-p">Un galpón con cubierta y muros de planchas metálicas sin aislar es <strong>caluroso en verano, frío en invierno</strong> y propenso a la <strong>condensación</strong>, que termina goteando sobre personas, productos o maquinaria. Aislar la envolvente resuelve los tres problemas y mejora las condiciones de trabajo.</p>

<h2>¿Por qué aislar un galpón?</h2>
<ul>
<li><strong>Confort térmico</strong>: la plancha metálica transmite rápidamente el calor del sol y el frío nocturno.</li>
<li><strong>Condensación</strong>: cuando el aire interior, más cálido y húmedo, toca la plancha fría, el vapor se condensa y gotea.</li>
<li><strong>Ahorro de energía</strong> si el recinto se calefacciona o climatiza.</li>
<li><strong>Acústica</strong>: la lana reduce la reverberación interior y el ruido de la lluvia sobre la cubierta.</li>
</ul>

<h2>El aislante más usado: lana de vidrio en rollo</h2>
<p>La lana de vidrio es liviana, flexible y se entrega en rollos largos que cubren grandes superficies con pocas uniones. Según la ficha técnica de AislanGlass (Volcán), es un producto de uso habitacional e industrial, indicado para techumbres y muros de <strong>galpones y talleres industriales</strong>. Además:</p>
<ul>
<li>Es <strong>incombustible</strong> (ensayos de no combustibilidad y ASTM E-84 informados en su ficha).</li>
<li>Es químicamente inerte, <strong>imputrescible</strong>, no se asienta con el tiempo y no es atacada por plagas.</li>
<li>Cumple la norma <strong>NCh 1071</strong>, según el fabricante.</li>
</ul>

<h2>Qué revestimiento elegir</h2>
<table>
<thead><tr><th>Revestimiento</th><th>Para qué sirve</th><th>Uso en galpones</th></tr></thead>
<tbody>
<tr><td><b>Polipropileno blanco</b></td><td>Terminación a la vista, alta reflectancia lumínica</td><td>Galpones industriales, talleres y salas de secado con la aislación a la vista</td></tr>
<tr><td><b>Foil de aluminio</b></td><td>Barrera de vapor, soporte mecánico y terminación reflectante</td><td>Galpones industriales y recubrimiento de ductos de aire acondicionado</td></tr>
<tr><td><b>Papel kraft</b></td><td>Barrera de vapor y soporte mecánico</td><td>Cuando la aislación queda oculta tras un revestimiento</td></tr>
<tr><td><b>Libre</b></td><td>Sin revestimiento</td><td>Rellenos de muros o cielos con otra barrera de vapor</td></tr>
</tbody>
</table>
<p>Los usos indicados corresponden a los descritos en la ficha técnica de AislanGlass.</p>

{fig("/img/productos/lana-de-vidrio.jpg", "Rollo de lana de vidrio con polipropileno blanco", "La lana de vidrio con polipropileno blanco queda a la vista y aporta luminosidad al interior del galpón.", 900, 900)}

<h2>¿Qué espesor necesito?</h2>
<p>La capacidad aislante se mide con el <strong>R100</strong> (resistencia térmica × 100, en m²K/W). Estos son los valores de la ficha técnica de AislanGlass para rollos de lana de vidrio:</p>
<table>
<thead><tr><th>Espesor</th><th>R100</th></tr></thead>
<tbody>
<tr><td>40 mm</td><td>94</td></tr>
<tr><td>50 mm</td><td>122</td></tr>
<tr><td>80 mm</td><td>188</td></tr>
<tr><td>100 mm</td><td>235</td></tr>
<tr><td>120 mm</td><td>282</td></tr>
<tr><td>160 mm</td><td>376</td></tr>
</tbody>
</table>
<p>La <a href="/blog/reglamentacion-termica-zonas-termicas.html">reglamentación térmica</a> se aplica a viviendas y a establecimientos de educación y salud. En galpones industriales no es obligatoria, pero sirve como referencia: más espesor implica menos pérdidas, y el espesor conveniente depende del clima, del uso y de si el recinto se climatiza.</p>

<h2>Cómo evitar la condensación</h2>
<ul>
<li>Instala una <strong>barrera de vapor en la cara caliente</strong> del aislante (normalmente hacia el interior). La ficha de AislanGlass lo indica para el papel kraft: el papel enfrenta el ambiente de mayor temperatura.</li>
<li>Asegura la <strong>continuidad</strong>: traslapa y sella las uniones del revestimiento; cada abertura deja pasar vapor.</li>
<li>Evita <strong>puentes térmicos</strong>: la lana debe cubrir toda la superficie, sin espacios entre paños.</li>
<li>Ventila el recinto cuando hay fuentes de humedad (procesos, secado, personas).</li>
<li>Protege los rollos de la lluvia durante la obra: la ficha recomienda almacenarlos bajo techo.</li>
</ul>

<h2>Consejos de instalación</h2>
<ul>
<li>Instala la lana <strong>sin comprimirla</strong>: si pierde espesor, pierde capacidad aislante.</li>
<li>Deja el revestimiento (polipropileno o foil) hacia el interior del galpón.</li>
<li>Usa elementos de protección: guantes, mascarilla, lentes con protección lateral y manga larga, como recomienda el fabricante.</li>
</ul>
<p>¿Vas a aislar un galpón? <a href="/contacto.html">Envíanos la superficie y la ubicación</a> y te recomendamos el producto y el espesor.</p>
""",
"faq": [
    ["¿Qué aislante se usa en galpones?", "Lo más habitual es lana de vidrio en rollo con revestimiento de polipropileno blanco o foil de aluminio, que queda a la vista, funciona como barrera de vapor y refleja la luz."],
    ["¿Cómo se evita la condensación en un galpón?", "Con aislación continua bajo la cubierta y una barrera de vapor en la cara caliente (hacia el interior), con uniones traslapadas y selladas, y ventilando el recinto cuando hay fuentes de humedad."],
    ["¿Qué espesor de lana de vidrio necesita un galpón?", "Depende del clima, del uso y de si se climatiza. Como referencia, según la ficha de AislanGlass, un rollo de 50 mm tiene R100 = 122 y uno de 80 mm tiene R100 = 188."],
],
"sources": [
    ("Características técnicas de la lana de vidrio AislanGlass", "Volcán", "https://media.prodalam.cl/material-descarga/60553/60553_20241219122950.pdf"),
    ("Nueva Reglamentación Térmica", "MINVU", "https://www.minvu.gob.cl/nueva-reglamentacion-termica/"),
    ("Actualización de la reglamentación térmica – Implicancias (DITEC)", "MINVU", "https://www.minvu.gob.cl/wp-content/uploads/2025/11/Actualizacion-RT_DITEC.pdf"),
],
},
# ---------------------------------------------------------------------------
{
"slug": "aislacion-termica-industrial",
"title": "Aislación térmica industrial de cañerías y equipos",
"h1": "Aislación térmica industrial: cómo aislar cañerías, calderas y equipos para ahorrar energía",
"meta": "Aislación térmica industrial: cuánta energía pierde una cañería sin aislar, qué superficies aislar, lana mineral para alta temperatura y buenas prácticas de mantención.",
"kicker": "Aislación térmica y acústica",
"date": "2026-09-27",
"image": ("/img/blog/aislacion-termica-industrial.jpg", 1024, 576),
"image_alt": "Sala de máquinas con cañerías y equipos aislados y revestidos en aluminio",
"excerpt": "Una cañería de vapor sin aislar pierde energía las 24 horas. Cuánto se pierde, qué superficies aislar y cómo elegir la aislación para temperaturas industriales.",
"related": ["frazada-lana-mineral", "colchoneta-lana-mineral", "lana-mineral", "fibra-ceramica"],
"body": f"""
<p class="lead-p">En plantas industriales, mineras, de celulosa o centrales térmicas, las cañerías de vapor, las calderas y los equipos calientes <strong>pierden energía todo el tiempo</strong> si no están aislados. Según el Departamento de Energía de Estados Unidos (DOE), la aislación reduce típicamente esas pérdidas en torno al <strong>90%</strong>.</p>

<h2>Cuánta energía pierde una cañería sin aislar</h2>
<p>El DOE publica una tabla de pérdidas de calor en líneas de vapor sin aislar. La convertimos a unidades métricas (vatios por metro lineal de cañería, operando todo el año):</p>
<table>
<thead><tr><th>Diámetro</th><th>Vapor a 15 psig (≈ 1 bar)</th><th>Vapor a 150 psig (≈ 10 bar)</th></tr></thead>
<tbody>
<tr><td>1"</td><td>≈ 154 W/m</td><td>≈ 313 W/m</td></tr>
<tr><td>2"</td><td>≈ 258 W/m</td><td>≈ 527 W/m</td></tr>
<tr><td>4"</td><td>≈ 455 W/m</td><td>≈ 933 W/m</td></tr>
<tr><td>8"</td><td>≈ 812 W/m</td><td>≈ 1.690 W/m</td></tr>
</tbody>
</table>
<p><small>Conversión de los valores del DOE (MMBtu/año por cada 100 pies), para tubería de acero horizontal, aire a 24&nbsp;°C, sin viento y 8.760 horas de operación al año.</small></p>
<p>Por ejemplo, 100&nbsp;m de cañería de 2" con vapor a unos 10&nbsp;bar sin aislar pierden del orden de <strong>53&nbsp;kW de forma continua</strong>, que la caldera tiene que reponer quemando combustible.</p>

<h2>Qué superficies aislar</h2>
<ul>
<li>El DOE recomienda aislar <strong>toda superficie sobre 120&nbsp;°F (unos 49&nbsp;°C)</strong>: superficies de calderas, cañerías de vapor y de retorno de condensado, y sus fittings.</li>
<li><strong>Válvulas, flanges y trampas de vapor</strong> también pierden calor: según el DOE, una válvula de compuerta de 6" puede tener más de 6 pies² (≈ 0,56&nbsp;m²) de superficie. Para ellas existen <strong>chaquetas aislantes removibles</strong>.</li>
</ul>

<h2>Lana mineral para alta temperatura</h2>
<p>Para cañerías y equipos calientes se usan <strong>frazadas de lana mineral con malla</strong>, que se amarran a superficies curvas, y colchonetas o paneles para superficies planas. Como referencia, la ficha técnica de la frazada ROCKWOOL ProRox WM 960ES informa:</p>
<table>
<thead><tr><th>Propiedad</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Temperatura máxima de servicio</td><td>660&nbsp;°C</td></tr>
<tr><td>Reacción al fuego</td><td>Euroclase A1 (incombustible)</td></tr>
<tr><td>Densidad</td><td>100 kg/m³</td></tr>
<tr><td>Conductividad térmica λ a 50 / 300 / 500&nbsp;°C</td><td>0,041 / 0,083 / 0,146 W/m·K</td></tr>
</tbody>
</table>
<div class="callout"><strong>Ojo:</strong> la conductividad térmica <em>aumenta con la temperatura</em>. Por eso el espesor se calcula para la temperatura real de operación y no con el λ a temperatura ambiente. El DOE recomienda la herramienta gratuita 3E Plus, de la asociación norteamericana de fabricantes de aislación (NAIMA), para determinar el espesor óptimo.</div>

{fig("/img/productos/frazada-lana-mineral.jpg", "Frazada de lana mineral con malla", "La frazada de lana mineral con malla se adapta a cañerías y equipos de gran diámetro.", 900, 900)}

<h2>Humedad y corrosión bajo aislamiento</h2>
<p>La aislación mojada pierde capacidad y puede favorecer la <strong>corrosión bajo aislamiento</strong> (CUI, por su sigla en inglés). Por eso:</p>
<ul>
<li>El DOE indica <strong>reparar o reemplazar de inmediato</strong> la aislación dañada o húmeda, y eliminar antes las fuentes de humedad: válvulas con fugas, filtraciones de cañerías o equipos cercanos.</li>
<li>En instalaciones a la intemperie se usan lanas con ligantes <strong>hidrorrepelentes</strong> y un <strong>revestimiento exterior</strong> que proteja del agua y de daños mecánicos.</li>
<li>Es común que la aislación se retire durante una reparación y <strong>no se reponga</strong>: inclúyela en los procedimientos de mantención.</li>
</ul>

<h2>Cómo estimar el ahorro</h2>
<p>El DOE propone este cálculo:</p>
<p><strong>Ahorro anual = 0,90 × pérdida de calor anual × costo del combustible ÷ eficiencia de la caldera</strong></p>
<p>El 0,90 corresponde al 90% de reducción que logra la aislación. Con la pérdida de la tabla, el precio de tu combustible y la eficiencia de tu caldera (el ejemplo del DOE usa 80%), puedes estimar el retorno de la inversión.</p>

<h2>Paso a paso</h2>
<ol>
<li>Haz un <strong>catastro</strong> de cañerías, válvulas y equipos sin aislar o con aislación dañada.</li>
<li>Registra diámetros, largos y temperaturas de operación.</li>
<li>Define el material según la <strong>temperatura</strong> y el ambiente (interior o intemperie).</li>
<li>Calcula el <strong>espesor</strong> para la temperatura de operación.</li>
<li>Protege con <strong>revestimiento</strong> y agrega chaquetas removibles en válvulas y fittings.</li>
</ol>
<p>¿Necesitas aislar cañerías o equipos? <a href="/contacto.html">Envíanos diámetros, largos y temperaturas</a> y cotizamos frazadas, colchonetas o paneles de lana mineral.</p>
""",
"faq": [
    ["¿Cuánto ahorra aislar una cañería de vapor?", "Según el Departamento de Energía de EE.UU., la aislación reduce típicamente las pérdidas de energía en torno al 90%. Por ejemplo, 100 m de cañería de 2 pulgadas con vapor a unos 10 bar pierden del orden de 53 kW sin aislación."],
    ["¿Qué superficies se deben aislar en una planta?", "El DOE recomienda aislar toda superficie sobre 120 °F (unos 49 °C): calderas, cañerías de vapor y condensado, fittings, válvulas y trampas, usando chaquetas removibles donde se requiere acceso."],
    ["¿Qué aislante se usa para cañerías de alta temperatura?", "Lana mineral (lana de roca) en frazadas con malla, colchonetas o paneles. Por ejemplo, la frazada ROCKWOOL ProRox WM 960ES informa una temperatura máxima de servicio de 660 °C."],
],
"sources": [
    ("Insulate Steam Distribution and Condensate Return Lines – Steam Tip Sheet #2", "U.S. Department of Energy (DOE)", "https://www.energy.gov/sites/prod/files/2014/05/f16/steam2_insulate.pdf"),
    ("ProRox WM 960ES – Product data sheet", "ROCKWOOL Technical Insulation", "https://rti.rockwool.com/siteassets/tools--documentation/products-industrial/product-data-sheets/english/rw-ti-pds-prorox-wm-960-en.pdf"),
],
},
# ---------------------------------------------------------------------------
{
"slug": "proteccion-pasiva-contra-incendios",
"title": "Protección pasiva contra incendios: qué es y cómo funciona",
"h1": "Protección pasiva contra incendios: qué es, cómo funciona y qué exige la normativa en Chile",
"meta": "Qué es la protección pasiva contra incendios, cómo se diferencia de la activa, sus sistemas (compartimentación, protección de estructuras y sellos) y la normativa chilena.",
"kicker": "Protección pasiva contra incendios",
"date": "2026-09-27",
"image": ("/img/blog/proteccion-pasiva-contra-incendios.jpg", 960, 540),
"image_alt": "Construcción envuelta en llamas durante un incendio nocturno",
"excerpt": "La parte de la seguridad contra incendios que no se ve: muros, placas, sellos y revestimientos que contienen el fuego y el humo el tiempo necesario para evacuar y combatirlo.",
"related": ["placa-fibrosilicato", "yeso-carton-resistente-al-fuego", "masilla-cortafuego", "cinta-intumescente", "lana-mineral"],
"body": f"""
<p class="lead-p">Cuando se habla de seguridad contra incendios, lo primero que viene a la mente son los extintores, los rociadores o las alarmas. Pero gran parte de la seguridad de un edificio depende de elementos que no se ven y que no necesitan activarse: los muros, losas, placas, sellos y revestimientos que <strong>impiden que el fuego y el humo se propaguen</strong>. Eso es la protección pasiva contra incendios.</p>

<h2>¿Qué es la protección pasiva contra incendios?</h2>
<p>La protección pasiva contra incendios (PPCI) es el conjunto de soluciones constructivas que forman parte del propio edificio y que, sin intervención humana ni equipos que se activen, <strong>resisten el fuego durante un tiempo determinado</strong>. Su objetivo es ganar minutos: tiempo para que las personas evacúen de forma segura, para que llegue bomberos y para que la estructura no colapse.</p>
<p>Esa capacidad se mide como <strong>resistencia al fuego</strong> y en Chile se expresa con la letra F seguida de los minutos que el elemento resiste en un ensayo normalizado: F-30, F-60, F-120, etc. Lo explicamos en detalle en <a href="/blog/resistencia-al-fuego-f30-f60-f120.html">qué significa F-30, F-60 y F-120</a>.</p>

<h2>Protección pasiva vs. protección activa</h2>
<p>Ambas son complementarias y la normativa exige las dos según el tipo de edificio. La diferencia está en cómo actúan:</p>
<table>
<thead><tr><th>Aspecto</th><th>Protección pasiva</th><th>Protección activa</th></tr></thead>
<tbody>
<tr><td><b>Cómo actúa</b></td><td>Está siempre presente; contiene el fuego por las propiedades de sus materiales</td><td>Se activa ante un incendio (de forma automática o manual)</td></tr>
<tr><td><b>Ejemplos</b></td><td>Muros y tabiques cortafuego, revestimiento de estructuras, sellos de pasadas, puertas cortafuego</td><td>Rociadores (sprinklers), detectores, alarmas, extintores, red húmeda</td></tr>
<tr><td><b>Objetivo</b></td><td>Compartimentar, proteger la estructura y dar tiempo</td><td>Detectar, avisar y extinguir</td></tr>
<tr><td><b>Mantención</b></td><td>Baja, pero se debe cuidar que nadie la perfore o modifique</td><td>Periódica, con revisiones y pruebas de funcionamiento</td></tr>
</tbody>
</table>

<h2>Los tres objetivos de la protección pasiva</h2>
<h3>1. Compartimentar</h3>
<p>Consiste en dividir el edificio en <strong>sectores de incendio</strong>: recintos cerrados por muros, losas y puertas con resistencia al fuego, de modo que un incendio quede confinado donde se originó. Las cajas de escalera, los shafts, las salas eléctricas y los muros entre unidades son ejemplos típicos. Un sector de incendio solo funciona si <em>todo</em> su perímetro tiene la resistencia exigida, incluidos cielos, puertas y cada perforación.</p>
<h3>2. Proteger la estructura</h3>
<p>El acero pierde capacidad resistente a medida que se calienta, y un perfil desnudo expuesto a un incendio se calienta rápido: mientras más delgado es (mayor <em>masividad</em>), antes llega a su temperatura crítica. Por eso vigas, pilares y cerchas se revisten con <strong>placas de fibrosilicato, morteros proyectados o pinturas intumescentes</strong>, que retardan el calentamiento del acero y mantienen la estabilidad del edificio durante el tiempo exigido.</p>
<h3>3. Sellar pasadas y juntas</h3>
<p>Cada cañería, ducto o bandeja de cables que atraviesa un muro cortafuego abre un camino al fuego y al humo. Los <strong>sellos cortafuego</strong> (masillas intumescentes, collarines, cintas y rellenos de lana mineral) devuelven al muro su resistencia original. Es uno de los puntos más olvidados en obra; le dedicamos un artículo completo: <a href="/blog/sellos-cortafuego-pasadas-de-instalaciones.html">cómo sellar pasadas de instalaciones</a>.</p>

{fig("/img/productos/placa-fibrosilicato.jpg", "Placa de fibrosilicato resistente al fuego", "Las placas de fibrosilicato se usan tanto en muros y cielos cortafuego como para revestir estructuras metálicas.", 900, 601)}

<h2>Materiales y sistemas más usados</h2>
<ul>
<li><strong>Placas de fibrosilicato</strong> (como Promatect®): placas rígidas e incombustibles para tabiques, cielos, shafts y revestimiento de estructuras. Resisten además la humedad y el impacto.</li>
<li><strong>Yeso cartón resistente al fuego (RF)</strong>: placas de yeso con aditivos y fibras que mejoran su comportamiento frente al fuego; habituales en tabiques y cielos de edificios.</li>
<li><strong>Lana mineral (lana de roca)</strong>: incombustible y de alto punto de fusión; se usa como relleno de tabiques cortafuego y como respaldo en sellos. Ver <a href="/blog/lana-de-vidrio-vs-lana-mineral.html">diferencias con la lana de vidrio</a>.</li>
<li><strong>Sellos intumescentes</strong>: masillas, cintas y collarines que se expanden con el calor y cierran los huecos que dejan las instalaciones.</li>
<li><strong>Pinturas intumescentes y morteros proyectados</strong>: protegen perfiles de acero cuando se requiere mantener la estructura a la vista o recubrir formas complejas.</li>
<li><strong>Puertas y compuertas cortafuego</strong>: cierran los vanos de los sectores de incendio y deben estar certificadas junto a su marco y quincallería.</li>
</ul>

<h2>Qué exige la normativa en Chile</h2>
<p>La base es la <strong>Ordenanza General de Urbanismo y Construcciones (OGUC)</strong>, que en su Título 4, Capítulo 3, establece las condiciones de seguridad contra incendio. En términos generales:</p>
<ul>
<li>Los edificios se clasifican según su <strong>destino, superficie, número de pisos y carga de ocupación</strong>, y según esa clasificación se exige una resistencia al fuego mínima para cada elemento: muros cortafuego, muros de caja de escalera, elementos soportantes verticales y horizontales, muros divisorios entre unidades, entre otros.</li>
<li>La resistencia al fuego de cada solución se acredita con <strong>ensayos según la norma NCh 935/1</strong>, realizados por laboratorios reconocidos, o mediante las soluciones inscritas en el <strong>Listado Oficial de Comportamiento al Fuego</strong> que publica el Ministerio de Vivienda y Urbanismo (MINVU). Las puertas se ensayan según la NCh 935/2 y los sellos de penetraciones según la NCh 935/3.</li>
<li>La solución ensayada es un <strong>sistema completo</strong>: tipo y espesor de placas, estructura, aislante, fijaciones y tratamiento de juntas. Cambiar un componente sin respaldo técnico puede invalidar la resistencia declarada.</li>
</ul>
<div class="callout">Las exigencias concretas dependen de cada proyecto. El arquitecto y el calculista definen la resistencia requerida para cada elemento; nuestro rol es ayudarte a elegir un sistema ensayado que la cumpla.</div>

<h2>Errores frecuentes en obra</h2>
<ul>
<li>Perforar un muro cortafuego para pasar instalaciones y cerrarlo con espuma de poliuretano común, que <strong>no es cortafuego</strong>.</li>
<li>Reemplazar las placas especificadas por otras "equivalentes" sin ensayo que lo respalde.</li>
<li>Dejar la unión entre el muro y la losa superior sin sellar: el fuego y el humo pasan por esa junta.</li>
<li>Proteger la estructura con un espesor menor al que exige la masividad del perfil.</li>
<li>No dejar registro (fotos, fichas técnicas) de los sellos y revestimientos una vez tapados.</li>
</ul>

<h2>Cómo elegir el sistema correcto</h2>
<ol>
<li>Identifica la <strong>resistencia exigida</strong> (F-30, F-60, F-120…) para cada elemento según el proyecto.</li>
<li>Define el <strong>tipo de elemento</strong>: tabique, cielo, shaft, protección de acero, sello de pasada.</li>
<li>Considera las condiciones del recinto: humedad, impactos, exterior o interior, terminación.</li>
<li>Elige un <strong>sistema ensayado</strong> y sigue su ficha técnica al pie de la letra.</li>
</ol>
<p>Si tienes planos o especificaciones, <a href="/contacto.html">envíanoslos</a> y te recomendamos el sistema y las cantidades para cotizar.</p>
""",
"faq": [
    ["¿Qué es la protección pasiva contra incendios?", "Es el conjunto de soluciones constructivas (muros, placas, revestimientos, sellos y puertas cortafuego) que forman parte del edificio y resisten el fuego durante un tiempo determinado sin necesidad de activarse, para compartimentar el incendio, proteger la estructura y dar tiempo a la evacuación."],
    ["¿Cuál es la diferencia entre protección pasiva y activa contra incendios?", "La pasiva está siempre presente y contiene el fuego por las propiedades de sus materiales (muros cortafuego, sellos, revestimientos). La activa se pone en marcha ante un incendio para detectarlo, avisar o extinguirlo (rociadores, detectores, extintores)."],
    ["¿Qué norma regula la protección contra incendios en Chile?", "La Ordenanza General de Urbanismo y Construcciones (OGUC), Título 4, Capítulo 3. La resistencia al fuego se acredita con ensayos según NCh 935/1 o con soluciones del Listado Oficial de Comportamiento al Fuego del MINVU."],
],
"sources": [
    ('D.S. N°47 de 1992, Ordenanza General de Urbanismo y Construcciones', 'MINVU', 'https://www.minvu.gob.cl/elementos-tecnicos/decretos/d-s-n47-1992-ordenanza-general-de-urbanismo-y-construccione/'),
    ('Listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción, ED17-2025', 'MINVU', 'https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf'),
],
},
# ---------------------------------------------------------------------------
{
"slug": "resistencia-al-fuego-f30-f60-f120",
"title": "Resistencia al fuego F-30, F-60, F-120: qué significa",
"h1": "Resistencia al fuego F-30, F-60 y F-120: qué significa y cómo se certifica en Chile",
"meta": "Qué significa la resistencia al fuego F-30, F-60, F-90 y F-120, cómo se ensaya según NCh 935/1, qué criterios se evalúan y cómo elegir una solución certificada.",
"kicker": "Protección pasiva contra incendios",
"date": "2026-09-27",
"image": ("/img/blog/resistencia-al-fuego-f30-f60-f120.jpg", 1024, 576),
"image_alt": "Estructura de vigas y pilares de acero de un edificio en construcción",
"excerpt": "La letra F y un número aparecen en planos y especificaciones técnicas. Te explicamos qué mide, cómo se ensaya y por qué una solución solo vale si se construye tal como fue ensayada.",
"related": ["placa-fibrosilicato", "yeso-carton-resistente-al-fuego", "lana-mineral", "pasta-para-juntas"],
"body": f"""
<p class="lead-p">En planos y especificaciones técnicas es común ver indicaciones como <strong>"tabique F-60"</strong> o <strong>"protección de estructura F-120"</strong>. Esa letra y ese número definen cuánto tiempo debe resistir un elemento frente a un incendio. Entenderlos bien evita comprar materiales que no cumplen o, peor, construir soluciones que no protegen.</p>

<h2>¿Qué significa la F en la resistencia al fuego?</h2>
<p>En Chile, la resistencia al fuego se expresa con la letra <strong>F seguida de un número que indica minutos</strong>. Un elemento F-60 es capaz de mantener su función durante al menos 60 minutos en un ensayo de fuego normalizado. La clasificación se obtiene según la norma <strong>NCh 935/1</strong>, que define el método de ensayo de resistencia al fuego para elementos de construcción.</p>
<p>Las clases habituales son F-15, F-30, F-60, F-90, F-120, F-150, F-180 y F-240. Mientras mayor el número, más exigente la solución.</p>

<h2>Qué se evalúa en el ensayo</h2>
<p>Durante el ensayo, una cara del elemento se expone al fuego en un horno y se verifica que siga cumpliendo, a lo largo del tiempo, los criterios que correspondan a su función:</p>
<ul>
<li><strong>Capacidad de soporte (estabilidad):</strong> el elemento no colapsa ni se deforma más allá de lo admisible mientras sostiene su carga. Aplica a muros soportantes, vigas, pilares y losas.</li>
<li><strong>Estanqueidad a las llamas y gases calientes:</strong> no aparecen grietas ni aberturas por las que pasen llamas o gases capaces de inflamar la cara no expuesta.</li>
<li><strong>Aislación térmica:</strong> la cara no expuesta no supera un aumento de temperatura límite (en el enfoque habitual de estas normas, del orden de 140&nbsp;°C en promedio y 180&nbsp;°C en cualquier punto), para que no inicie un incendio al otro lado.</li>
</ul>
<p>La resistencia al fuego es el tiempo durante el cual se cumplen <em>todos</em> los criterios exigidos; el primero que falla determina la clasificación.</p>

<h2>La curva de fuego normalizada</h2>
<p>Para que los resultados sean comparables, el horno sigue una curva tiempo–temperatura estandarizada: la curva normalizada de la norma <strong>ISO 834-1</strong>, T = 345·log<sub>10</sub>(8t + 1) + T<sub>0</sub>, donde t son los minutos y T<sub>0</sub> la temperatura inicial (unos 20&nbsp;°C). Con esa fórmula, la temperatura del horno alcanza aproximadamente:</p>
<table>
<thead><tr><th>Tiempo de ensayo</th><th>Temperatura aproximada del horno</th><th>Clasificación si el elemento cumple</th></tr></thead>
<tbody>
<tr><td>30 minutos</td><td>≈ 842&nbsp;°C</td><td>F-30</td></tr>
<tr><td>60 minutos</td><td>≈ 945&nbsp;°C</td><td>F-60</td></tr>
<tr><td>90 minutos</td><td>≈ 1.006&nbsp;°C</td><td>F-90</td></tr>
<tr><td>120 minutos</td><td>≈ 1.049&nbsp;°C</td><td>F-120</td></tr>
</tbody>
</table>

<h2>¿Qué resistencia exige la normativa?</h2>
<p>La <strong>OGUC</strong> (Título 4, Capítulo 3) clasifica los edificios según su destino, superficie edificada, número de pisos y carga de ocupación, y para cada tipo establece la resistencia al fuego mínima de sus elementos: muros cortafuego, muros de cajas de escalera, elementos soportantes verticales y horizontales, muros divisorios entre unidades, escaleras y techumbres, entre otros.</p>
<p>No existe una única respuesta: un mismo tabique puede requerir F-30 en una vivienda y F-120 como muro cortafuego de un edificio. La exigencia de cada elemento la define el proyecto de arquitectura.</p>

<h2>Cómo se acredita la resistencia al fuego</h2>
<p>Hay dos caminos habituales:</p>
<ol>
<li><strong>Listado Oficial de Comportamiento al Fuego</strong> del MINVU: reúne soluciones constructivas ya ensayadas, con su descripción y clasificación. Es la referencia más usada en proyectos.</li>
<li><strong>Informe de ensayo</strong> de un laboratorio reconocido, emitido para una solución específica de un fabricante.</li>
</ol>
<div class="callout"><strong>Clave:</strong> la clasificación F corresponde a la solución <em>completa</em> tal como fue ensayada: tipo y número de placas, espesores, estructura, aislante, distancia entre fijaciones y tratamiento de juntas. Si en obra se cambia uno de esos componentes, la clasificación deja de estar respaldada.</div>

{fig("/img/productos/yeso-carton-resistente-al-fuego.jpg", "Planchas de yeso cartón resistente al fuego", "Las placas RF y de fibrosilicato forman parte de muchas soluciones ensayadas de tabiques y cielos.", 900, 598)}

<h2>Protección de estructuras metálicas</h2>
<p>En el caso del acero, la exigencia se traduce en mantener el perfil por debajo de su temperatura crítica durante el tiempo requerido. El espesor de protección necesario depende de:</p>
<ul>
<li>La <strong>resistencia exigida</strong> (F-30, F-60, F-120…).</li>
<li>La <strong>masividad o factor de forma</strong> del perfil (relación entre la superficie expuesta al fuego y su sección): los perfiles delgados se calientan más rápido y necesitan más protección. Para pinturas intumescentes, el Listado Oficial del MINVU entrega tablas de espesores según la masividad.</li>
<li>El sistema elegido: placas de fibrosilicato en cajón, morteros proyectados o pinturas intumescentes, cada uno con sus propias tablas de espesores según ensayo.</li>
</ul>

<h2>Recomendaciones para especificar y comprar</h2>
<ul>
<li>Pide siempre la <strong>ficha técnica y el respaldo de ensayo</strong> o la referencia del Listado Oficial de la solución.</li>
<li>Verifica que las placas, el aislante y los accesorios (tornillos, masillas, cintas) sean los del sistema ensayado.</li>
<li>Considera los detalles: encuentros con losas, pasadas de instalaciones y juntas de dilatación también deben mantener la F.</li>
<li>Deja registro fotográfico de la instalación antes de cerrar cielos y shafts.</li>
</ul>
<p>¿Necesitas cumplir una F específica? <a href="/contacto.html">Cuéntanos el elemento y la resistencia exigida</a> y te recomendamos una solución.</p>
""",
"faq": [
    ["¿Qué significa F-60 en resistencia al fuego?", "Que el elemento mantiene sus funciones (capacidad de soporte, estanqueidad a llamas y gases y aislación térmica, según corresponda) durante al menos 60 minutos en un ensayo de fuego normalizado según NCh 935/1."],
    ["¿Qué diferencia hay entre F-30, F-60 y F-120?", "Los minutos de resistencia en el ensayo: 30, 60 o 120. Una clase mayor requiere soluciones más robustas, por ejemplo más capas de placas o mayor espesor de protección."],
    ["¿Dónde se revisa si una solución constructiva es F-60?", "En el Listado Oficial de Comportamiento al Fuego del MINVU o en el informe de ensayo de un laboratorio reconocido. La clasificación solo es válida si la solución se construye tal como fue ensayada."],
],
"sources": [
    ('D.S. N°47 de 1992, Ordenanza General de Urbanismo y Construcciones', 'MINVU', 'https://www.minvu.gob.cl/elementos-tecnicos/decretos/d-s-n47-1992-ordenanza-general-de-urbanismo-y-construccione/'),
    ('Listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción, ED17-2025', 'MINVU', 'https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf'),
    ('ISO 834-1: Fire-resistance tests — Elements of building construction — Part 1: General requirements', 'ISO', 'https://www.iso.org/standard/83943.html'),
],
},
# ---------------------------------------------------------------------------
{
"slug": "sellos-cortafuego-pasadas-de-instalaciones",
"title": "Sellos cortafuego: cómo sellar pasadas de instalaciones",
"h1": "Sellos cortafuego: cómo sellar pasadas de cañerías, ductos y cables en muros y losas",
"meta": "Qué es un sello cortafuego, qué tipo usar en cada pasada (cables, tuberías metálicas y plásticas, ductos, juntas) y cómo instalarlo para mantener la resistencia al fuego del muro.",
"kicker": "Protección pasiva contra incendios",
"date": "2026-09-27",
"image": ("/img/blog/sellos-cortafuego-pasadas-de-instalaciones.jpg", 1070, 602),
"image_alt": "Tubos de masilla cortafuego Promaseal para sellar pasadas de instalaciones",
"excerpt": "Un muro cortafuego pierde su resistencia en la primera perforación mal sellada. Qué sello usar en cada pasada y cómo instalarlo correctamente.",
"related": ["masilla-cortafuego", "cinta-intumescente", "lana-mineral", "fibra-ceramica"],
"body": f"""
<p class="lead-p">Un muro o una losa cortafuego pueden estar perfectamente construidos y, aun así, fallar por un detalle: la <strong>perforación por donde pasa una cañería, un ducto o una bandeja de cables</strong>. Los sellos cortafuego existen para cerrar esos huecos y devolverle al elemento la resistencia al fuego que tenía antes de ser perforado.</p>

<h2>Por qué las pasadas son el punto débil</h2>
<p>En un edificio, los muros y losas que separan sectores de incendio son atravesados por decenas de instalaciones: agua, alcantarillado, electricidad, datos, climatización, gas. Cada una deja un espacio anular alrededor, y muchas de ellas, como los tubos plásticos o los cables, <strong>se queman o se ablandan</strong> con el fuego, dejando un hueco abierto. Por ahí pasan llamas, gases calientes y, sobre todo, humo, que es la principal causa de víctimas en un incendio.</p>

<h2>¿Qué es un sello cortafuego?</h2>
<p>Es un sistema que cierra la abertura entre la instalación y el elemento constructivo, y que ha sido <strong>ensayado para mantener la misma resistencia al fuego</strong> (F-60, F-120…) que el muro o la losa que atraviesa. En Chile, los sistemas de sello de penetraciones se ensayan según la norma <strong>NCh 935/3</strong>, y el Listado Oficial de Comportamiento al Fuego del MINVU tiene un capítulo dedicado a ellos. Según el caso, combina uno o más de estos materiales:</p>
<ul>
<li><strong>Masillas intumescentes</strong>: se expanden con el calor y rellenan el espacio que deja un material que se consume.</li>
<li><strong>Masillas de silicona cortafuego</strong>: elásticas, adecuadas para juntas con movimiento y pasadas metálicas.</li>
<li><strong>Collarines y cintas intumescentes</strong>: se colocan alrededor de tubos plásticos; al expandirse, estrangulan el tubo que se ablanda y cierran el paso.</li>
<li><strong>Lana mineral de alta densidad</strong> y <strong>fibra cerámica</strong>: relleno incombustible que actúa como respaldo de las masillas.</li>
<li><strong>Morteros y placas cortafuego</strong>: para aberturas grandes o con muchas instalaciones juntas.</li>
</ul>

<h2>Qué sello usar en cada tipo de pasada</h2>
<table>
<thead><tr><th>Pasada</th><th>Solución habitual</th><th>Qué cuidar</th></tr></thead>
<tbody>
<tr><td>Cables sueltos o en bandeja</td><td>Masilla intumescente con respaldo de lana mineral; en aberturas grandes, mortero o placas con masilla</td><td>Rellenar también los espacios entre cables</td></tr>
<tr><td>Tuberías metálicas (cobre, acero)</td><td>Relleno de lana mineral + masilla cortafuego en ambas caras</td><td>El metal conduce calor: algunas soluciones exigen aislar un tramo del tubo</td></tr>
<tr><td>Tuberías plásticas (PVC, PP, PE)</td><td>Collarín o cinta intumescente alrededor del tubo + masilla</td><td>El intumescente debe tener volumen suficiente para cerrar todo el diámetro</td></tr>
<tr><td>Ductos de climatización</td><td>Relleno perimetral con lana mineral y masilla; compuerta cortafuego cuando corresponde</td><td>La compuerta es parte de la protección activa y requiere mantención</td></tr>
<tr><td>Juntas lineales (muro–losa, dilatación)</td><td>Respaldo de lana mineral comprimida + masilla elástica cortafuego</td><td>La masilla debe admitir el movimiento de la junta</td></tr>
</tbody>
</table>
<p>Cada fabricante define en su ficha técnica los diámetros máximos, profundidades de masilla, densidad del relleno y resistencia alcanzada para cada configuración. <strong>La solución vale para la configuración ensayada</strong>.</p>

{fig("/img/cinta-intumescente.jpg", "Cinta intumescente para sellos cortafuego", "Las cintas intumescentes se expanden con el calor y cierran el paso que deja un tubo plástico al ablandarse.", 550, 650)}

<h2>Paso a paso: cómo instalar un sello con masilla</h2>
<ol>
<li><strong>Limpia la abertura</strong>: sin polvo, grasa ni restos sueltos. La masilla necesita buena adherencia.</li>
<li><strong>Revisa el tamaño del espacio anular</strong>: debe estar dentro de lo que permite el sistema. Si la perforación es demasiado grande, primero redúcela con mortero o placa.</li>
<li><strong>Coloca el relleno de lana mineral</strong> comprimida, dejando la profundidad indicada para la masilla.</li>
<li><strong>Aplica la masilla</strong> con el espesor que exige la ficha técnica, presionando para que no queden vacíos, y alisa la superficie.</li>
<li><strong>Repite por la otra cara</strong> si el sistema lo requiere (es habitual en muros).</li>
<li><strong>Identifica y registra</strong>: etiqueta el sello y guarda foto, ubicación y producto usado. Facilita las inspecciones y las futuras intervenciones.</li>
</ol>

<h2>Errores comunes</h2>
<ul>
<li><strong>Usar espuma de poliuretano común</strong>: se quema y alimenta el fuego. Solo las espumas certificadas como cortafuego sirven, y en las configuraciones ensayadas.</li>
<li>Rellenar con materiales al azar (yeso, lana de vidrio, restos de placa) sin un sistema ensayado.</li>
<li>Sellar solo por una cara cuando la solución exige ambas.</li>
<li>Mezclar productos de distintos sistemas o fabricantes.</li>
<li>Olvidar las pasadas nuevas: cada vez que alguien perfora un muro cortafuego para una instalación adicional, el sello debe rehacerse.</li>
</ul>

<h2>Inspección y mantención</h2>
<p>Los sellos no requieren mantención periódica como un extintor, pero sí <strong>control</strong>: después de cada remodelación, cambio de instalaciones o trabajos en shafts, revisa que no se hayan retirado o dañado. Un catastro con fotos y ubicación de cada sello hace mucho más simple esta revisión.</p>
<p>¿Tienes que sellar pasadas en tu obra? <a href="/contacto.html">Indícanos el tipo de instalación, los diámetros y la resistencia exigida</a> y te recomendamos el sistema.</p>
""",
"faq": [
    ["¿Qué es un sello cortafuego?", "Es un sistema de masillas, cintas o collarines intumescentes y rellenos incombustibles que cierra la abertura por donde una instalación atraviesa un muro o losa, manteniendo la resistencia al fuego del elemento."],
    ["¿Sirve la espuma de poliuretano para sellar pasadas cortafuego?", "No. La espuma de poliuretano común es combustible. Solo sirven productos certificados como cortafuego, usados en la configuración ensayada."],
    ["¿Cómo se sella una tubería de PVC que atraviesa un muro cortafuego?", "Con un collarín o cinta intumescente alrededor del tubo, que al calentarse se expande y cierra el hueco que deja el plástico al ablandarse, complementado con masilla según el sistema del fabricante."],
],
"sources": [
    ('Listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción, ED17-2025', 'MINVU', 'https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf'),
    ('D.S. N°47 de 1992, Ordenanza General de Urbanismo y Construcciones', 'MINVU', 'https://www.minvu.gob.cl/elementos-tecnicos/decretos/d-s-n47-1992-ordenanza-general-de-urbanismo-y-construccione/'),
],
},
# ---------------------------------------------------------------------------
{
"slug": "lana-de-vidrio-vs-lana-mineral",
"title": "Lana de vidrio vs lana mineral: diferencias y usos",
"h1": "Lana de vidrio vs lana mineral: diferencias, ventajas y cuándo usar cada una",
"meta": "Diferencias entre lana de vidrio y lana mineral (lana de roca): densidad, aislación térmica y acústica, resistencia a temperatura, usos y cómo elegir según tu obra.",
"kicker": "Aislación térmica y acústica",
"date": "2026-09-27",
"image": ("/img/blog/lana-de-vidrio-vs-lana-mineral.jpg", 1200, 675),
"image_alt": "Rollo de lana de vidrio junto a un panel de lana mineral",
"excerpt": "Ambas son aislantes incombustibles y muy usados en construcción, pero no son intercambiables. Comparamos sus propiedades y te decimos cuál conviene en cada caso.",
"related": ["lana-de-vidrio-libre", "lana-de-vidrio-papel-kraft", "lana-de-vidrio", "lana-mineral", "frazada-lana-mineral", "panel-velo-negro"],
"body": f"""
<p class="lead-p">La lana de vidrio y la lana mineral (también llamada <strong>lana de roca</strong>) son los aislantes más usados en la construcción en Chile. Ambas son fibras minerales, ambas aíslan del frío, del calor y del ruido, y ninguna es combustible. Sin embargo, tienen diferencias importantes de densidad, temperatura de trabajo y precio que definen dónde conviene cada una.</p>

<h2>¿Qué es la lana de vidrio?</h2>
<p>Se fabrica fundiendo arena de sílice y vidrio reciclado, que luego se transforma en fibras finas aglomeradas con un ligante. El resultado es un material <strong>liviano, flexible y económico</strong>, que se comercializa principalmente en rollos y paneles, libre o con revestimientos como papel kraft, polipropileno o velo negro.</p>

<h2>¿Qué es la lana mineral o lana de roca?</h2>
<p>Se obtiene fundiendo rocas volcánicas, principalmente <strong>basalto</strong>, a muy alta temperatura. Sus fibras forman un material <strong>más denso y con un punto de fusión mucho más alto</strong> que el de la lana de vidrio. Se vende en paneles rígidos, colchonetas y frazadas con malla, en distintas densidades.</p>

<h2>Comparación lado a lado</h2>
<table>
<thead><tr><th>Aspecto</th><th>Lana de vidrio</th><th>Lana mineral (roca)</th></tr></thead>
<tbody>
<tr><td><b>Materia prima</b></td><td>Arena de sílice y vidrio reciclado</td><td>Roca volcánica (basalto)</td></tr>
<tr><td><b>Densidad típica</b></td><td>Baja: ej. rollos AislanGlass de 9,8 a 50,5 kg/m³</td><td>Mayor: ej. ProRox WM 960ES 100 kg/m³; paneles de 80 a 140 kg/m³</td></tr>
<tr><td><b>Aislación térmica (λ)</b></td><td>Ej. AislanGlass: 0,038 a 0,043 W/m·K según densidad</td><td>Ej. ProRox WM 960ES: 0,041 W/m·K a 50&nbsp;°C (aumenta con la temperatura)</td></tr>
<tr><td><b>Temperatura de trabajo</b></td><td>Edificación: techumbres, muros, tabiques y galpones</td><td>Alta: ej. ProRox WM 960ES hasta 660&nbsp;°C, para equipos y cañerías industriales</td></tr>
<tr><td><b>Comportamiento al fuego</b></td><td>Incombustible (ej. AislanGlass, ensayos NCh 1914 y ASTM E-84)</td><td>Incombustible, Euroclase A1; se usa en protección pasiva</td></tr>
<tr><td><b>Aislación acústica</b></td><td>Muy buena en tabiques y cielos</td><td>Muy buena; destaca en soluciones acústicas exigentes por su densidad</td></tr>
<tr><td><b>Peso y manipulación</b></td><td>Liviana, fácil de cortar y adaptar</td><td>Más pesada y rígida; paneles con buena estabilidad</td></tr>
<tr><td><b>Costo por m²</b></td><td>Menor</td><td>Mayor</td></tr>
</tbody>
</table>
<p><small>Valores de ejemplo tomados de las fichas técnicas citadas en Fuentes; cada producto declara los suyos.</small></p>

<h2>Aislación térmica y reglamentación</h2>
<p>Para aislar del frío y del calor, lo que manda es la <strong>resistencia térmica</strong> del aislante, que depende de su espesor y de su conductividad (λ): R = espesor / λ. En Chile es común verla expresada como <strong>R100</strong> (la resistencia térmica multiplicada por 100). Por ejemplo, 50&nbsp;mm de un aislante con λ = 0,042 W/m·K tiene R = 0,050 / 0,042 ≈ 1,19 m²·K/W, es decir, un R100 de aproximadamente 119. Como referencia, la ficha de AislanGlass declara R100 = 122 para su rollo de 50&nbsp;mm y 188 para el de 80&nbsp;mm.</p>
<p>La <strong>reglamentación térmica</strong> (artículo 4.1.10 de la OGUC), actualizada desde el 28 de noviembre de 2025, fija exigencias para techos, muros, pisos ventilados y ventanas según <strong>9 zonas térmicas (A a la I)</strong>. Lo explicamos en <a href="/blog/reglamentacion-termica-zonas-termicas.html">la nueva reglamentación térmica</a>. En aislación de viviendas, la lana de vidrio suele ser la opción más conveniente por costo; la lana mineral se prefiere cuando además hay exigencias de fuego o de acústica.</p>

{fig("/img/productos/lana-de-vidrio-papel-kraft.jpg", "Rollo de lana de vidrio con papel kraft", "El papel kraft actúa como barrera de vapor y se instala hacia el lado cálido del recinto.", 900, 900)}

<h2>Cuándo usar lana de vidrio</h2>
<ul>
<li>Aislación de <strong>entretechos, cielos y muros perimetrales</strong> de viviendas.</li>
<li>Relleno acústico de <strong>tabiques</strong> de yeso cartón o fibrocemento.</li>
<li><strong>Cubiertas y muros de galpones</strong>, con revestimiento de polipropileno blanco a la vista.</li>
<li>Fachadas ventiladas y cielos acústicos, en paneles con velo negro.</li>
</ul>

<h2>Cuándo usar lana mineral</h2>
<ul>
<li><strong>Aislación industrial</strong>: cañerías, calderas, estanques y equipos que trabajan a alta temperatura (frazadas con malla y colchonetas).</li>
<li><strong>Protección pasiva contra incendios</strong>: relleno de tabiques cortafuego y respaldo de sellos. Ver <a href="/blog/proteccion-pasiva-contra-incendios.html">qué es la protección pasiva</a>.</li>
<li>Soluciones <strong>acústicas exigentes</strong>: salas de máquinas, estudios, muros entre unidades.</li>
<li>Aplicaciones donde se necesita un panel <strong>rígido y denso</strong>, por ejemplo en fachadas.</li>
</ul>

<h2>Revestimientos y formatos</h2>
<ul>
<li><strong>Libre</strong>: sin revestimiento, para rellenar cavidades.</li>
<li><strong>Papel kraft</strong>: incorpora barrera de vapor; se instala hacia el interior (lado cálido).</li>
<li><strong>Polipropileno blanco</strong>: terminación a la vista y reflectante en galpones.</li>
<li><strong>Velo negro</strong>: para quedar detrás de revestimientos con juntas abiertas o cielos perforados.</li>
<li><strong>Malla metálica</strong> (frazadas de lana mineral): permite amarrarla a superficies curvas.</li>
</ul>

<h2>Consejos de instalación</h2>
<ul>
<li><strong>No comprimas</strong> la lana: pierde espesor y, con ello, capacidad aislante.</li>
<li>Asegura <strong>continuidad</strong>: sin espacios entre paños ni en los encuentros con la estructura.</li>
<li>Instala la barrera de vapor hacia el lado correcto para evitar condensación.</li>
<li>Usa elementos de protección: guantes, manga larga, antiparras y mascarilla.</li>
</ul>
<p>¿No sabes cuál conviene en tu proyecto? <a href="/contacto.html">Cuéntanos el uso y la zona</a> y te recomendamos el aislante y el espesor.</p>
""",
"faq": [
    ["¿Cuál es la diferencia entre lana de vidrio y lana mineral?", "La lana de vidrio se hace con arena y vidrio reciclado; es más liviana y económica. La lana mineral o de roca se hace con basalto; es más densa, soporta temperaturas mucho más altas y se prefiere en industria, protección contra fuego y acústica exigente."],
    ["¿Qué aísla mejor, la lana de vidrio o la lana de roca?", "A temperatura ambiente tienen conductividades térmicas similares: por ejemplo, la lana de vidrio AislanGlass declara 0,038 a 0,043 W/m·K según densidad y la frazada de lana de roca ProRox WM 960ES 0,041 W/m·K a 50 °C. La lana de roca destaca en alta temperatura, fuego y acústica por su mayor densidad."],
    ["¿Hacia dónde va el papel kraft de la lana de vidrio?", "Hacia el lado cálido del recinto, normalmente el interior, para que funcione como barrera de vapor y evite condensación dentro del muro o la techumbre."],
],
"sources": [
    ('Características técnicas de la lana de vidrio AislanGlass', 'Volcán', 'https://media.prodalam.cl/material-descarga/60553/60553_20241219122950.pdf'),
    ('ProRox WM 960ES – Product data sheet', 'ROCKWOOL Technical Insulation', 'https://rti.rockwool.com/siteassets/tools--documentation/products-industrial/product-data-sheets/english/rw-ti-pds-prorox-wm-960-en.pdf'),
    ('Nueva Reglamentación Térmica', 'MINVU', 'https://www.minvu.gob.cl/nueva-reglamentacion-termica/'),
],
},
# ---------------------------------------------------------------------------
{
"slug": "aislacion-acustica-de-tabiques",
"title": "Aislación acústica de tabiques: cómo reducir el ruido",
"h1": "Aislación acústica de tabiques: cómo reducir el ruido entre recintos",
"meta": "Cómo mejorar la aislación acústica de un tabique: índice Rw, principio masa-resorte-masa, lana en la cavidad, doble placa, banda elastoacústica y exigencias de la OGUC.",
"kicker": "Aislación térmica y acústica",
"date": "2026-09-27",
"image": ("/img/blog/aislacion-acustica-de-tabiques.jpg", 1024, 576),
"image_alt": "Recinto con muros y cielo aislados acústicamente con paneles de lana mineral",
"excerpt": "Un tabique acústico no depende solo de la placa: la lana en la cavidad, la estructura, los encuentros y los sellos hacen la diferencia. Te explicamos cómo lograrlo.",
"related": ["banda-elastoacustica", "lana-de-vidrio-libre", "lana-mineral", "yeso-carton-estandar", "panel-velo-negro"],
"body": f"""
<p class="lead-p">El ruido entre departamentos, oficinas, salas de clases o habitaciones de hotel es una de las quejas más frecuentes de los usuarios. La buena noticia es que un tabique liviano bien diseñado puede <strong>aislar tanto o más que un muro macizo</strong>, siempre que se respeten algunos principios y se cuiden los detalles de instalación.</p>

<h2>Aislación acústica vs. acondicionamiento acústico</h2>
<p>Son dos cosas distintas y se confunden a menudo:</p>
<ul>
<li><strong>Aislación acústica</strong>: impedir que el sonido pase de un recinto a otro. Es el tema de este artículo.</li>
<li><strong>Acondicionamiento acústico</strong>: controlar cómo suena un recinto por dentro (eco, reverberación), con cielos y paneles absorbentes, como las placas perforadas con lana detrás.</li>
</ul>

<h2>Cómo viaja el ruido</h2>
<ul>
<li><strong>Ruido aéreo</strong>: voces, música, televisión. Se transmite por el aire y hace vibrar el tabique.</li>
<li><strong>Ruido de impacto</strong>: pasos, golpes, arrastre de muebles. Se transmite por la estructura, sobre todo a través de losas.</li>
<li><strong>Transmisión por flancos</strong>: el sonido rodea el tabique a través de losas, muros laterales, cielos o ductos comunes. Por eso un tabique excelente puede rendir poco si sus encuentros no están resueltos.</li>
</ul>

<h2>Cómo se mide: el índice de reducción acústica</h2>
<p>La capacidad de aislar ruido aéreo se expresa como <strong>índice de reducción acústica</strong> en decibeles. En laboratorio se informa como <strong>Rw</strong>; según el listado oficial del MINVU, al sumar el término de corrección C (Rw + C) el resultado es equivalente a dB(A), la unidad de la exigencia de la OGUC. Mientras mayor el número, mejor aísla.</p>
<p>Estos son valores ensayados del <strong>Listado Oficial de Soluciones Constructivas para Aislamiento Acústico</strong> del MINVU:</p>
<table>
<thead><tr><th>Tabique ensayado</th><th>Rw</th><th>Rw + C (≈ dB(A))</th></tr></thead>
<tbody>
<tr><td>Pino 45×45 mm, una placa de yeso cartón ST 10 mm por cara, <b>cavidad vacía</b></td><td>33 dB</td><td>31</td></tr>
<tr><td>El mismo tabique con <b>lana de vidrio</b> de 50 mm (11 kg/m³) en la cavidad</td><td>39 dB</td><td>36</td></tr>
<tr><td><b>Doble estructura</b> de acero separada 10 mm, <b>dos placas por cara</b> (ER 15 mm + RF 12,5 mm) y dos capas de lana de vidrio de 50 mm</td><td>53 dB</td><td>52</td></tr>
</tbody>
</table>
<p>Solo agregar lana a la cavidad sube el tabique simple en 6 dB. La solución de doble estructura y doble placa supera con holgura los 45 dB(A) que exige la OGUC entre viviendas.</p>

<h2>Qué exige la normativa en Chile</h2>
<p>La <strong>OGUC</strong> (artículo 4.1.6) establece condiciones acústicas para los elementos que separan unidades de vivienda: los elementos verticales y horizontales deben tener un índice de reducción acústica mínimo de <strong>45 dB(A)</strong>, y las losas y entrepisos deben además limitar el ruido de impacto (nivel máximo de 75 dB). Para acreditar el cumplimiento, las soluciones especificadas deben corresponder a una del <strong>Listado Oficial de Soluciones Constructivas para Aislamiento Acústico</strong> del MINVU o contar con un informe de ensayo.</p>
<p>Para oficinas, hoteles, colegios o salud, los estándares suelen venir en las especificaciones técnicas del proyecto y pueden ser más exigentes.</p>

<h2>El principio masa – resorte – masa</h2>
<p>Un tabique liviano aísla bien porque funciona como un sistema de <strong>dos hojas (las placas) separadas por una cámara con material absorbente (la lana)</strong>. Cada hoja vibra por separado y la lana amortigua la energía dentro de la cavidad. De ahí salen las tres palancas para mejorar un tabique:</p>
<ol>
<li><strong>Más masa</strong>: placas más pesadas o doble placa por cara.</li>
<li><strong>Más desacople</strong>: que las dos caras toquen lo menos posible la misma estructura.</li>
<li><strong>Más absorción</strong>: cavidad rellena con lana de vidrio o lana mineral.</li>
</ol>

{fig("/img/banda-elastoacustica.jpg", "Rollos de banda elastoacústica autoadhesiva", "La banda elastoacústica se coloca bajo las soleras y montantes perimetrales para cortar la transmisión de vibraciones.", 1000, 750)}

<h2>Claves para un tabique acústico que funcione</h2>
<ul>
<li><strong>Rellena toda la cavidad</strong> con lana, sin comprimirla ni dejar espacios. Ver <a href="/blog/lana-de-vidrio-vs-lana-mineral.html">lana de vidrio vs lana mineral</a>.</li>
<li><strong>Usa doble placa</strong> por cara cuando se requiera más aislación, trabando las juntas de la primera y segunda capa.</li>
<li><strong>Desacopla la estructura</strong> del perímetro con <strong>banda elastoacústica</strong> bajo soleras y montantes de borde.</li>
<li><strong>Sella el perímetro</strong> con sellante acústico elástico: una rendija de pocos milímetros puede anular varios decibeles.</li>
<li><strong>No enfrentes cajas eléctricas</strong> espalda con espalda en ambas caras; desfásalas y séllalas.</li>
<li><strong>Lleva el tabique hasta la losa</strong>, no solo hasta el cielo falso: si el entretecho es común, el ruido pasa por arriba.</li>
<li>Resuelve los <strong>flancos</strong>: ductos, cielos continuos y pisos flotantes comunes a ambos recintos.</li>
<li>Considera <strong>la puerta</strong>: en muchos casos es el elemento más débil del conjunto.</li>
</ul>

<h2>Errores comunes</h2>
<ul>
<li>Pensar que basta con agregar lana: sin masa ni sellos, la mejora es limitada.</li>
<li>Dejar la lana a media altura o "a trozos".</li>
<li>Perforar el tabique para instalaciones y no sellar las pasadas.</li>
<li>Usar espuma de poliuretano como sello acústico: es rígida y transmite vibraciones.</li>
</ul>
<p>¿Tienes un proyecto con exigencias acústicas? <a href="/contacto.html">Envíanos el requerimiento</a> y te ayudamos a definir la solución y los materiales.</p>
""",
"faq": [
    ["¿Cómo mejorar la aislación acústica de un tabique?", "Rellenando la cavidad con lana de vidrio o lana mineral, aumentando la masa con doble placa por cara, desacoplando la estructura con banda elastoacústica y sellando el perímetro, las cajas eléctricas y las pasadas."],
    ["¿Qué aislación acústica exige la OGUC entre viviendas?", "El artículo 4.1.6 de la OGUC exige un índice de reducción acústica mínimo de 45 dB(A) para los elementos que separan unidades de vivienda, además de limitar el ruido de impacto en losas y entrepisos."],
    ["¿Qué es la banda elastoacústica?", "Una banda autoadhesiva que se instala entre la estructura del tabique y los muros, losas o cielos, para cortar la transmisión de vibraciones y mejorar la aislación acústica."],
],
"sources": [
    ('Listado Oficial de Soluciones Constructivas para Aislamiento Acústico, E13-2024', 'MINVU', 'https://www.minvu.gob.cl/wp-content/uploads/2024/06/LISTADO-OFICIAL-VIGENTE-LOSCAA-2024.pdf'),
    ('D.S. N°47 de 1992, Ordenanza General de Urbanismo y Construcciones', 'MINVU', 'https://www.minvu.gob.cl/elementos-tecnicos/decretos/d-s-n47-1992-ordenanza-general-de-urbanismo-y-construccione/'),
],
},
]
