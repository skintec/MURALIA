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
<p>El acero pierde gran parte de su capacidad resistente cuando alcanza temperaturas del orden de los 500&nbsp;°C, algo que en un incendio puede ocurrir en pocos minutos si el perfil está desnudo. Por eso vigas, pilares y cerchas se revisten con <strong>placas de fibrosilicato, morteros proyectados o pinturas intumescentes</strong>, que retardan el calentamiento del acero y mantienen la estabilidad del edificio durante el tiempo exigido.</p>
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
<li>La resistencia al fuego de cada solución se acredita con <strong>ensayos según la norma NCh 935/1</strong>, realizados por laboratorios reconocidos, o mediante las soluciones inscritas en el <strong>Listado Oficial de Comportamiento al Fuego</strong> que publica el Ministerio de Vivienda y Urbanismo (MINVU).</li>
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
<p>Para que los resultados sean comparables, el horno sigue una curva tiempo–temperatura estandarizada (la curva normalizada de la norma ISO 834, que es la base de estos ensayos). Como referencia, la temperatura del horno alcanza aproximadamente:</p>
<table>
<thead><tr><th>Tiempo de ensayo</th><th>Temperatura aproximada del horno</th><th>Clasificación si el elemento cumple</th></tr></thead>
<tbody>
<tr><td>30 minutos</td><td>≈ 840&nbsp;°C</td><td>F-30</td></tr>
<tr><td>60 minutos</td><td>≈ 945&nbsp;°C</td><td>F-60</td></tr>
<tr><td>90 minutos</td><td>≈ 985&nbsp;°C</td><td>F-90</td></tr>
<tr><td>120 minutos</td><td>≈ 1.050&nbsp;°C</td><td>F-120</td></tr>
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
<li>La <strong>masividad o factor de forma</strong> del perfil (relación entre el perímetro expuesto al fuego y su sección): los perfiles delgados se calientan más rápido y necesitan más protección.</li>
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
<p>Es un sistema que cierra la abertura entre la instalación y el elemento constructivo, y que ha sido <strong>ensayado para mantener la misma resistencia al fuego</strong> (F-60, F-120…) que el muro o la losa que atraviesa. Según el caso, combina uno o más de estos materiales:</p>
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
<tr><td><b>Densidad típica</b></td><td>Baja: aprox. 10 a 35 kg/m³</td><td>Media a alta: aprox. 40 a 150 kg/m³ o más</td></tr>
<tr><td><b>Aislación térmica (λ)</b></td><td>Aprox. 0,032 a 0,044 W/m·K</td><td>Aprox. 0,033 a 0,040 W/m·K</td></tr>
<tr><td><b>Temperatura de trabajo</b></td><td>Moderada (bajo los 250&nbsp;°C aprox.)</td><td>Alta: apta para equipos y superficies calientes industriales</td></tr>
<tr><td><b>Comportamiento al fuego</b></td><td>Incombustible (sin revestimiento)</td><td>Incombustible y con alto punto de fusión; se usa en protección pasiva</td></tr>
<tr><td><b>Aislación acústica</b></td><td>Muy buena en tabiques y cielos</td><td>Muy buena; destaca en soluciones acústicas exigentes por su densidad</td></tr>
<tr><td><b>Peso y manipulación</b></td><td>Liviana, fácil de cortar y adaptar</td><td>Más pesada y rígida; paneles con buena estabilidad</td></tr>
<tr><td><b>Costo por m²</b></td><td>Menor</td><td>Mayor</td></tr>
</tbody>
</table>
<p><small>Valores referenciales: las propiedades exactas dependen de cada producto y se indican en su ficha técnica.</small></p>

<h2>Aislación térmica y reglamentación</h2>
<p>Para aislar del frío y del calor, lo que manda es la <strong>resistencia térmica</strong> del aislante, que depende de su espesor y de su conductividad (λ): R = espesor / λ. En Chile es común verla expresada como <strong>R100</strong> (la resistencia térmica multiplicada por 100). Por ejemplo, 50&nbsp;mm de un aislante con λ = 0,042 W/m·K tiene R = 0,050 / 0,042 ≈ 1,19 m²·K/W, es decir, un R100 de aproximadamente 119.</p>
<p>La <strong>reglamentación térmica</strong> (artículo 4.1.10 de la OGUC) fija exigencias de aislación para techumbres, muros, pisos ventilados y ventanas de las viviendas según la <strong>zona térmica</strong> donde se construye. En aislación de viviendas, la lana de vidrio suele ser la opción más conveniente por costo; la lana mineral se prefiere cuando además hay exigencias de fuego o de acústica.</p>

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
    ["¿Qué aísla mejor, la lana de vidrio o la lana de roca?", "Térmicamente, a igual espesor, ambas tienen conductividades similares (aprox. 0,032 a 0,044 W/m·K). La lana de roca destaca en alta temperatura, fuego y acústica por su mayor densidad."],
    ["¿Hacia dónde va el papel kraft de la lana de vidrio?", "Hacia el lado cálido del recinto, normalmente el interior, para que funcione como barrera de vapor y evite condensación dentro del muro o la techumbre."],
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
<p>La capacidad de aislar ruido aéreo se expresa como <strong>índice de reducción acústica</strong> en decibeles (por ejemplo, Rw en dB, o en dB(A) según la norma usada). Mientras mayor el número, mejor aísla. Como referencia, una mejora de unos 10&nbsp;dB se percibe aproximadamente como <strong>la mitad de ruido</strong>.</p>
<table>
<thead><tr><th>Tipo de tabique (referencial)</th><th>Aislación aproximada</th></tr></thead>
<tbody>
<tr><td>Estructura simple, una placa por cara, cavidad vacía</td><td>≈ 33 a 38 dB</td></tr>
<tr><td>Estructura simple, una placa por cara, cavidad con lana</td><td>≈ 40 a 45 dB</td></tr>
<tr><td>Estructura simple, dos placas por cara, cavidad con lana</td><td>≈ 48 a 53 dB</td></tr>
<tr><td>Doble estructura independiente, dos placas por cara, con lana</td><td>≈ 55 a 65 dB</td></tr>
</tbody>
</table>
<p><small>Valores referenciales para orientar el diseño. El valor real de una solución depende de sus componentes exactos y se acredita con ensayo.</small></p>

<h2>Qué exige la normativa en Chile</h2>
<p>La <strong>OGUC</strong> (artículo 4.1.6) establece condiciones acústicas para los elementos que separan unidades de vivienda: los elementos verticales y horizontales deben tener un índice de reducción acústica mínimo de <strong>45 dB(A)</strong>, y las losas y entrepisos deben además limitar el ruido de impacto (nivel máximo de 75 dB). Las soluciones se acreditan con ensayos según las normas chilenas de acústica o mediante el <strong>Listado Oficial de Soluciones Constructivas para Aislamiento Acústico</strong> del MINVU.</p>
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
},
]
