#!/usr/bin/env python
# -*- coding: utf-8 -*-

NO_NOTAS = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es" xmlns:og="http://opengraphprotocol.org/schema/">
<head><title>U-Cursos :: DR500A-1 Ajedrez I :: Notas Parciales</title>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<meta name="descripcion" content="Una Herramienta de Apoyo a la Docencia Presencial." />
<link rel="stylesheet" href="https://www.u-cursos.cl/ingenieria/diseno/css/style_v6699" type="text/css" />
<link rel="stylesheet" href="https://www.u-cursos.cl/diseno/css/print_v6699.css" media="print" type="text/css" />
<link rel="shortcut icon" href="https://www.u-cursos.cl/favicon.ico?v4" type="image/x-icon" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/ingenieria/diseno/images/apple-touch-icon-57.png" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/ingenieria/diseno/images/apple-touch-icon-72.png" sizes="72x72"/>
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/ingenieria/diseno/images/apple-touch-icon-114.png" sizes="114x114"/>
<link rel="copyright license" href="https://www.u-cursos.cl/acerca" title="Area de Infotecnologías (ADI), FCFM, U. de Chile." />
<script src="https://www.u-cursos.cl/diseno/js/hash_v6699.js" type="text/javascript"></script>
<script src="https://www.u-cursos.cl/diseno/js/javascript_v6699.js" type="text/javascript"></script><meta property="og:type" content="university" />
<meta property="og:site_name" content="U-Cursos" />
<meta property="og:title" content="Notas Parciales :: DR500A-1 Ajedrez I" />
<meta property="og:url" content="https://www.u-cursos.cl" />
<meta property="og:image" content="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/notas.png" />
<link rel="stylesheet" href="https://www.u-cursos.cl/diseno/css/css_v6699?servicio=notas" type="text/css" /><link rel="alternate" type="application/rss+xml" title="Canales de Mensajes DR500A-1 Ajedrez I" href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/historial/rss20" /><link rel="alternate" type="application/rss+xml" title="DR500A-1 Ajedrez I - Notas Parciales" href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/historial/rss20?servicios=notas" /></head>
<body><a href="https://www.u-cursos.cl"><h1 id="ucursos"><span>U-Cursos :: ingenieria</span></h1></a>

<h2 class="ucursos">DR500A-1 Ajedrez I 2014, Semestre Primavera</h2>

<ul id="servicios_generales">
    <li><a href="https://www.u-cursos.cl/?csrf=dd3f92afab&accion=salir">Salir</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/contacto">Contacto</a></li>
    <li id="buscador">
    <form id="form_buscador" action="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/buscador/">
    <input type="text" name="q" value="Buscar..." onFocus="if(this.value=='Buscar...')this.value='';" onBlur="if(this.value=='')this.value='Buscar...';" />
    <a href="javascript:if($('form_buscador').q.value!='Buscar...')$('form_buscador').submit()"><span>Buscar</span></a>
    </form>
    </li>
</ul>

<style>
body {
    background: white url('https://www.u-cursos.cl/ingenieria/diseno/images/servicios/fondos/notas.png') fixed no-repeat 95% 90%;
}

table{
    background: #fff;
}

td.verde, td.opciones{
    background: #f9f4e8;
}

td.gris{
    background: #f4f4f4;
}


</style>
<div id="izquierda" style="clear:right">

    <div id="usuario" class="caja off">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=usuario">Pablo Pizarro R.</a></h1>
    <ul>
        <li><a href="https://www.u-cursos.cl/inicio"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/pagina_inicio_on.png" title="Mi Inicio" /><span>Mi Inicio</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/mis_canales/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/mis_canales.png" title="Mis Canales" /> <span>Mis Canales</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/datos_usuario.png" title="Mis Datos" /> <span>Mis Datos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/todos_cursos/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/todos_cursos.png" title="Todos Mis Cursos" /> <span>Todos Mis Cursos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/horario/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/horario.png" title="Horario" /> <span>Horario</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/favoritos/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/favoritos.png" title="Mis Estrellas" /> <span>Mis Estrellas</span></a></li>


    </ul>
    </div>


    <div id="cursos" class="caja on">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=cursos">Cursos Actuales</a></h1>
    <ul>
        <li id="curso.115364" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CC3001/2/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CC3001-2 Algoritmos y Estructuras de Datos</span></a>         </li>
        <li id="curso.115983" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CM2004-1 Fisicoquímica</span></a>         </li>
        <li id="curso.115454" class="sel" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>DR500A-1 Ajedrez I</span></a>         </li>
        <li id="curso.114686" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2002-5 Electromagnetismo</span></a>         </li>
        <li id="curso.114695" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2003-9 Métodos Experimentales</span></a>         </li>
        <li id="curso.115024" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/MA2002/4/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>MA2002-4 Cálculo Avanzado y Aplicaciones</span></a>         </li>
    </ul>
    </div>

    <div id="comunidades" class="caja on">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=comunidades">Comunidades</a></h1>
    <ul>
        <li id="curso.57163" class=""><a href="https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMGAMER-1 Comunidad Gamer Beauchef</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/foro/" style="white-space:nowrap">Foro (6)</a></div>        </li>
        <li id="curso.103935" class=""><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMMUSI-1 Música Beauchef</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/foro/" style="white-space:nowrap">Foro (5)</a><br /><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/historial/" style="white-space:nowrap">Historial (1)</a></div>        </li>
        <li id="curso.35017" class=""><a href="https://www.u-cursos.cl/uchile/2009/0/COMVIDA/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMVIDA-1 Comunidad Calidad de Vida Estudiantil</span></a>         </li>
    </ul>
    </div>

    <div id="instituciones" class="caja on">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=instituciones">Instituciones</a></h1>
    <ul>
        <li id="institucion.4" class=""><a href="https://www.u-cursos.cl/uchile/4/"><img src="https://www.u-cursos.cl/medicina/diseno/images/instituciones/uchile.png" alt="Comunidades - Universidad de Chile" title="Comunidades - Universidad de Chile" class="icono" /> <span>Comunidades - Universidad de Chile</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/4/afiches/" style="white-space:nowrap">Afiches (2)</a><br /><a href="https://www.u-cursos.cl/uchile/4/foro_institucion/" style="white-space:nowrap">Foro (>100)</a></div></li>
        <li id="institucion.3000" class=""><a href="https://www.u-cursos.cl/uchile/3000/"><img src="https://www.u-cursos.cl/diseno/images/instituciones/uchile.png" alt="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" title="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Diagnósticos - Facultad de Cs. Físicas y Matemáticas</span></a> </li>
        <li id="institucion.2" class=""><a href="https://www.u-cursos.cl/ingenieria/2/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/instituciones/ingenieria.png" alt="Facultad de Cs. Físicas y Matemáticas" title="Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Facultad de Cs. Físicas y Matemáticas</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/ingenieria/2/foro_institucion/" style="white-space:nowrap">Foro (>100)</a></div></li>
    </ul>
    </div>
</div>

<div id="body">

<ul class="modulos fijos">
    <li><a href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=favorito">
<img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/favorito_add.png" class="icono" title="Para agregarlo a tus favoritos" /><span>Agregar Favorito</span>
</a>
</li>
    <li><a href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=inicio"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/pagina_inicio_add.png" class="icono" /><span>Inicio</span></a>
</li>
    <li><a href="http://manuales.ing.uchile.cl/ucursos/notas/alumno.html" target="_blank"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/ayuda.png" /><span>Ayuda</span></a></li>
</ul>

<ul class="modulos">
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/acta/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/acta.png" alt="Acta" class="icono" /><span>Acta</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/calendario/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/calendario.png" alt="Calendario" class="icono" /><span>Calendario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/correo/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/correo.png" alt="Correo" class="icono" /><span>Correo</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/datos_curso/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/datos_curso.png" alt="Datos del Curso" class="icono" /><span>Datos del Curso</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/encuestas/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/encuestas.png" alt="Encuestas" class="icono" /><span>Encuestas</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/foro/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/foro.png" alt="Foro" class="icono" /><span>Foro</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/historial/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/historial.png" alt="Historial" class="icono" /><span>Historial</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/horario_curso/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/horario_curso.png" alt="Horario" class="icono" /><span>Horario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/integrantes/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/integrantes.png" alt="Integrantes" class="icono" /><span>Integrantes</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/material_alumnos/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/material_alumnos.png" alt="Material Alumnos" class="icono" /><span>Material Alumnos</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/material_docente/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/material_docente.png" alt="Material Docente" class="icono" /><span>Material Docente</span></a></li>
    <li class="servicio sel"><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/notas/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/notas.png" alt="Notas Parciales" class="icono" /><span>Notas Parciales</span></a></li>
</ul>

<ul id="navbar">
    <li><a href="https://www.u-cursos.cl">Inicio</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/instituciones">Instituciones</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/">Facultad de Cs. Físicas y Matemáticas</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/cursos_departamento/?_hook=periodo&periodo=2014.2&departamento=7">Cursos</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/">DR500A-1 Ajedrez I</a></li>
    <li>Notas Parciales</li>
</ul>




<h1 class="modulo">Notas Parciales</h1>
<script type="text/javascript">
function getEstadistica( id ) {
    $('estadisticas').update( '<span class="espera" style="width:150px">Cargando estadísticas...</span>' );
    $('estadisticas').update( quickAjax( 'alumno_detalle?escala=0&id_evaluacion='+id ) );
    $('id_evaluacion').value = id;
    jstriggerTable( $('tabla') );

    $('tabla').select('img.chica').each( function( o ) {
        o.observe( 'click', function( e ) {
            i = e.element();
            i.hasClassName( 'chica' ) ? i.removeClassName( 'chica' ) : i.addClassName( 'chica' );
        } );
    } );
    $('estadisticas').scrollTo();
}

</script>


<form class="buscar">
<input type="hidden" id="id_evaluacion" name="id_evaluacion" value="0" />
Usar la misma escala para todas las evaluaciones: <select id="escala" name="escala" onchange="this.form.submit()"><option value="0" selected="selected">No</option><option value="1">1.0 - 7.0</option><option value="2">1.00 - 7.00</option><option value="3">1.000 - 7.000</option><option value="4">0% - 100%</option><option value="5">I - MB</option><option value="6">R - D</option><option value="10">1 - 10 ( equivalencia 4.0 = 6 )</option></select></form>

<table class="sortable">
<thead>
<tr>
    <th class="string">Evaluación</th>
    <th class="number strong">Prom.</th>
    <th class="opciones" colspan="2">Opciones</th>
</tr>
</thead>
<tr>
    <td colspan="0">No hay evaluaciones publicadas.</td>
</tr>
</table>
<dl class="leyenda">
    <dt style="width: 10px">*</dt>
    <dd>Los promedios corresponden a la <a target="_blank" href="http://es.wikipedia.org/wiki/Media_aritm%C3%A9tica">media aritmética</a> entre evaluaciones de un mismo tipo y no reflejan las reglas específicas del curso.</dd>
</dl>

<div id="estadisticas"></div>
</div>

<div id="footer">
<ul>
    <li><a href="https://www.u-cursos.cl/dev/paginas/politicas_uso">Políticas de Uso</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/acerca">Acerca de...</a></li>
    <li><a href="https://www.u-cursos.cl/tutoriales/">Tutoriales</a></li>
    <li><a href="https://www.u-cursos.cl/dev/blog/">Blog</a></li>
    <li>Con la tecnología de <a href="http://adi.ing.uchile.cl/" title="�?rea de Infotecnologías - ADI"><img src="https://www.u-cursos.cl/diseno/images/logos/adi.png" alt="�?rea de Infotecnologías - ADI" /></a></li>
    <li class="social">
    <a href="http://twitter.com/ucursos" target="_blank" title="U-Cursos en Twitter" class="file twitter"> &nbsp; </a>
    <a href="http://www.facebook.com/pages/U-Cursos-Chile/147024698734489" target="_blank" title="U-Cursos en Facebook" class="file facebook"> &nbsp; </a>
    </li>
</ul>
</div>

<script type="text/javascript">
Event.onReady( function() {
    ucmsg.init( { server: 'https://static.u-cursos.cl', port: 54321, secure: true }, { id: 'npm4t7o5v149qjkbpog0a64v46', user: '9079e9837b43ce4fc1096a70bf2325fb', avatar: 'av_5385561e94aba.jpg', alias: 'Pablo Pizarro R.' } );
} );
</script>



<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-101878-7']);
_gaq.push(['_setDomainName', 'www.u-cursos.cl']);
_gaq.push(['_trackPageview']);
_gaq.push(['_setCustomVar', 1, 'movil', '0' ]);
</script>
<script type="text/javascript" src="https://www.u-cursos.cl/diseno/js/ga.js"></script>

<script type="text/javascript">
Event.onReady( function() {
    notificacion.init( { server: 'https://static.u-cursos.cl', port: 54322, token: 'npm4t7o5v149qjkbpog0a64v46', url: 'https://www.u-cursos.cl', webkit: true } );
} );
</script>

</body>
</html>
"""

CURSO1 = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es" xmlns:og="http://opengraphprotocol.org/schema/">
<head><title>U-Cursos :: FI2003-9 Métodos Experimentales :: Notas Parciales</title>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<meta name="descripcion" content="Una Herramienta de Apoyo a la Docencia Presencial." />
<link rel="stylesheet" href="https://www.u-cursos.cl/ingenieria/diseno/css/style_v6699" type="text/css" />
<link rel="stylesheet" href="https://www.u-cursos.cl/diseno/css/print_v6699.css" media="print" type="text/css" />
<link rel="shortcut icon" href="https://www.u-cursos.cl/favicon.ico?v4" type="image/x-icon" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/ingenieria/diseno/images/apple-touch-icon-57.png" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/ingenieria/diseno/images/apple-touch-icon-72.png" sizes="72x72"/>
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/ingenieria/diseno/images/apple-touch-icon-114.png" sizes="114x114"/>
<link rel="copyright license" href="https://www.u-cursos.cl/acerca" title="�?rea de Infotecnologías (ADI), FCFM, U. de Chile." />
<script src="https://www.u-cursos.cl/diseno/js/hash_v6699.js" type="text/javascript"></script>
<script src="https://www.u-cursos.cl/diseno/js/javascript_v6699.js" type="text/javascript"></script><meta property="og:type" content="university" />
<meta property="og:site_name" content="U-Cursos" />
<meta property="og:title" content="Notas Parciales :: FI2003-9 Métodos Experimentales" />
<meta property="og:url" content="https://www.u-cursos.cl" />
<meta property="og:image" content="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/notas.png" />
<link rel="stylesheet" href="https://www.u-cursos.cl/diseno/css/css_v6699?servicio=notas" type="text/css" /><link rel="alternate" type="application/rss+xml" title="Canales de Mensajes FI2003-9 Métodos Experimentales" href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/historial/rss20" /><link rel="alternate" type="application/rss+xml" title="FI2003-9 Métodos Experimentales - Notas Parciales" href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/historial/rss20?servicios=notas" /></head>
<body><a href="https://www.u-cursos.cl"><h1 id="ucursos"><span>U-Cursos :: ingenieria</span></h1></a>

<h2 class="ucursos">FI2003-9 Métodos Experimentales 2014, Semestre Primavera</h2>

<ul id="servicios_generales">
    <li><a href="https://www.u-cursos.cl/?csrf=dd3f92afab&accion=salir">Salir</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/contacto">Contacto</a></li>
    <li id="buscador">
    <form id="form_buscador" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/buscador/">
    <input type="text" name="q" value="Buscar..." onFocus="if(this.value=='Buscar...')this.value='';" onBlur="if(this.value=='')this.value='Buscar...';" />
    <a href="javascript:if($('form_buscador').q.value!='Buscar...')$('form_buscador').submit()"><span>Buscar</span></a>
    </form>
    </li>
</ul>

<style>
body {
    background: white url('https://www.u-cursos.cl/ingenieria/diseno/images/servicios/fondos/notas.png') fixed no-repeat 95% 90%;
}

table{
    background: #fff;
}

td.verde, td.opciones{
    background: #f9f4e8;
}

td.gris{
    background: #f4f4f4;
}


</style>
<div id="izquierda" style="clear:right">

    <div id="usuario" class="caja off">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=usuario">Pablo Pizarro R.</a></h1>
    <ul>
        <li><a href="https://www.u-cursos.cl/inicio"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/pagina_inicio_on.png" title="Mi Inicio" /><span>Mi Inicio</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/mis_canales/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/mis_canales.png" title="Mis Canales" /> <span>Mis Canales</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/datos_usuario.png" title="Mis Datos" /> <span>Mis Datos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/todos_cursos/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/todos_cursos.png" title="Todos Mis Cursos" /> <span>Todos Mis Cursos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/horario/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/horario.png" title="Horario" /> <span>Horario</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/favoritos/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/favoritos.png" title="Mis Estrellas" /> <span>Mis Estrellas</span></a></li>


    </ul>
    </div>


    <div id="cursos" class="caja on">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=cursos">Cursos Actuales</a></h1>
    <ul>
        <li id="curso.115364" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CC3001/2/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CC3001-2 Algoritmos y Estructuras de Datos</span></a>         </li>
        <li id="curso.115983" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CM2004-1 Fisicoquímica</span></a>         </li>
        <li id="curso.115454" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>DR500A-1 Ajedrez I</span></a>         </li>
        <li id="curso.114686" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2002-5 Electromagnetismo</span></a>         </li>
        <li id="curso.114695" class="sel" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2003-9 Métodos Experimentales</span></a>         </li>
        <li id="curso.115024" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/MA2002/4/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>MA2002-4 Cálculo Avanzado y Aplicaciones</span></a>         </li>
    </ul>
    </div>

    <div id="comunidades" class="caja on">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=comunidades">Comunidades</a></h1>
    <ul>
        <li id="curso.57163" class=""><a href="https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMGAMER-1 Comunidad Gamer Beauchef</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/foro/" style="white-space:nowrap">Foro (6)</a></div>        </li>
        <li id="curso.103935" class=""><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMMUSI-1 Música Beauchef</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/foro/" style="white-space:nowrap">Foro (5)</a><br /><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/historial/" style="white-space:nowrap">Historial (1)</a></div>        </li>
        <li id="curso.35017" class=""><a href="https://www.u-cursos.cl/uchile/2009/0/COMVIDA/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMVIDA-1 Comunidad Calidad de Vida Estudiantil</span></a>         </li>
    </ul>
    </div>

    <div id="instituciones" class="caja on">
    <h1><a class="caja" href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=caja&caja=instituciones">Instituciones</a></h1>
    <ul>
        <li id="institucion.4" class=""><a href="https://www.u-cursos.cl/uchile/4/"><img src="https://www.u-cursos.cl/medicina/diseno/images/instituciones/uchile.png" alt="Comunidades - Universidad de Chile" title="Comunidades - Universidad de Chile" class="icono" /> <span>Comunidades - Universidad de Chile</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/4/afiches/" style="white-space:nowrap">Afiches (2)</a><br /><a href="https://www.u-cursos.cl/uchile/4/foro_institucion/" style="white-space:nowrap">Foro (>100)</a></div></li>
        <li id="institucion.3000" class=""><a href="https://www.u-cursos.cl/uchile/3000/"><img src="https://www.u-cursos.cl/diseno/images/instituciones/uchile.png" alt="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" title="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Diagnósticos - Facultad de Cs. Físicas y Matemáticas</span></a> </li>
        <li id="institucion.2" class=""><a href="https://www.u-cursos.cl/ingenieria/2/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/instituciones/ingenieria.png" alt="Facultad de Cs. Físicas y Matemáticas" title="Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Facultad de Cs. Físicas y Matemáticas</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/ingenieria/2/foro_institucion/" style="white-space:nowrap">Foro (>100)</a></div></li>
    </ul>
    </div>
</div>

<div id="body">

<ul class="modulos fijos">
    <li><a href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=favorito">
<img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/favorito_add.png" class="icono" title="Para agregarlo a tus favoritos" /><span>Agregar Favorito</span>
</a>
</li>
    <li><a href="?csrf=dd3f92afab&accion=mi_ucursos&subaccion=inicio"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/pagina_inicio_add.png" class="icono" /><span>Inicio</span></a>
</li>
    <li><a href="http://manuales.ing.uchile.cl/ucursos/notas/alumno.html" target="_blank"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/ayuda.png" /><span>Ayuda</span></a></li>
</ul>

<ul class="modulos">
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/acta/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/acta.png" alt="Acta" class="icono" /><span>Acta</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/calendario/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/calendario.png" alt="Calendario" class="icono" /><span>Calendario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/correo.png" alt="Correo" class="icono" /><span>Correo</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/datos_curso/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/datos_curso.png" alt="Datos del Curso" class="icono" /><span>Datos del Curso</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/encuestas/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/encuestas.png" alt="Encuestas" class="icono" /><span>Encuestas</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/foro/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/foro.png" alt="Foro" class="icono" /><span>Foro</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/historial/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/historial.png" alt="Historial" class="icono" /><span>Historial</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/horario_curso/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/horario_curso.png" alt="Horario" class="icono" /><span>Horario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/integrantes/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/integrantes.png" alt="Integrantes" class="icono" /><span>Integrantes</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/material_alumnos/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/material_alumnos.png" alt="Material Alumnos" class="icono" /><span>Material Alumnos</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/material_docente/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/material_docente.png" alt="Material Docente" class="icono" /><span>Material Docente</span></a></li>
    <li class="servicio sel"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/notas/"><img src="https://www.u-cursos.cl/ingenieria/diseno/images/servicios/notas.png" alt="Notas Parciales" class="icono" /><span>Notas Parciales</span></a></li>
</ul>

<ul id="navbar">
    <li><a href="https://www.u-cursos.cl">Inicio</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/instituciones">Instituciones</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/">Facultad de Cs. Físicas y Matemáticas</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/cursos_departamento/?_hook=periodo&periodo=2014.2&departamento=13">Cursos</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/">FI2003-9 Métodos Experimentales</a></li>
    <li>Notas Parciales</li>
</ul>




<h1 class="modulo">Notas Parciales</h1>
<script type="text/javascript">
function getEstadistica( id ) {
    $('estadisticas').update( '<span class="espera" style="width:150px">Cargando estadísticas...</span>' );
    $('estadisticas').update( quickAjax( 'alumno_detalle?escala=0&id_evaluacion='+id ) );
    $('id_evaluacion').value = id;
    jstriggerTable( $('tabla') );

    $('tabla').select('img.chica').each( function( o ) {
        o.observe( 'click', function( e ) {
            i = e.element();
            i.hasClassName( 'chica' ) ? i.removeClassName( 'chica' ) : i.addClassName( 'chica' );
        } );
    } );
    $('estadisticas').scrollTo();
}

</script>


<form class="buscar">
<input type="hidden" id="id_evaluacion" name="id_evaluacion" value="0" />
Usar la misma escala para todas las evaluaciones: <select id="escala" name="escala" onchange="this.form.submit()"><option value="0" selected="selected">No</option><option value="1">1.0 - 7.0</option><option value="2">1.00 - 7.00</option><option value="3">1.000 - 7.000</option><option value="4">0% - 100%</option><option value="5">I - MB</option><option value="6">R - D</option><option value="10">1 - 10 ( equivalencia 4.0 = 6 )</option></select></form>

<table class="sortable">
<thead>
<tr>
    <th class="string">Evaluación</th>
    <th class="number">P1</th>
    <th class="number">P2</th>
    <th class="number">P3</th>
    <th class="number strong">Prom.</th>
    <th class="opciones" colspan="2">Opciones</th>
</tr>
</thead>
<tr class="separador">
    <td colspan="0">Controles de Lectura</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 262139 )">Control de lectura 1</a></h1>
        <h2>20 de Agosto</h2>
        <dl id="detalle_262139" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">7.0</span></td>
    <td></td>
    <td><form id="correo_545c53a31b6872.00236601" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control de lectura 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control de lectura 1 donde mi nota fue 7.0 ... " /><a href="javascript:$('correo_545c53a31b6872.00236601').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 264255 )">Control de lectura 2</a></h1>
        <h2>27 de Agosto</h2>
        <dl id="detalle_264255" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">4.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">4.0</span></td>
    <td></td>
    <td><form id="correo_545c53a31b7ad9.90358071" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control de lectura 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control de lectura 2 donde mi nota fue 4.0 ... " /><a href="javascript:$('correo_545c53a31b7ad9.90358071').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 266089 )">Control de lectura 3</a></h1>
        <h2>10 de Septiembre</h2>
        <dl id="detalle_266089" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.6</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">6.6</span></td>
    <td></td>
    <td><form id="correo_545c53a31ba4e4.27947902" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control de lectura 3" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control de lectura 3 donde mi nota fue 6.6 ... " /><a href="javascript:$('correo_545c53a31ba4e4.27947902').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 267867 )">Control de lectura 4</a></h1>
        <h2>24 de Septiembre</h2>
        <dl id="detalle_267867" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">4.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">4.0</span></td>
    <td></td>
    <td><form id="correo_545c53a31bb6a0.09578359" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control de lectura 4" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control de lectura 4 donde mi nota fue 4.0 ... " /><a href="javascript:$('correo_545c53a31bb6a0.09578359').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 270671 )">Control de lectura 5</a></h1>
        <h2>15 de Octubre</h2>
        <dl id="detalle_270671" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">4.5</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">4.5</span></td>
    <td></td>
    <td><form id="correo_545c53a31bc778.39022450" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control de lectura 5" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control de lectura 5 donde mi nota fue 4.5 ... " /><a href="javascript:$('correo_545c53a31bc778.39022450').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 273003 )">Control de lectura 6</a></h1>
        <h2>22 de Octubre</h2>
        <dl id="detalle_273003" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">5.3</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">5.3</span></td>
    <td></td>
    <td><form id="correo_545c53a31bd839.68068977" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control de lectura 6" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control de lectura 6 donde mi nota fue 5.3 ... " /><a href="javascript:$('correo_545c53a31bd839.68068977').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Controles de Lectura'</td>
    <td></td><td></td><td></td>
    <td><span class="">5.2</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
<tr class="separador">
    <td colspan="0">Controles Experimentales</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 265418 )">Control Experimental 1</a></h1>
        <h2>3 de Septiembre</h2>
        <dl id="detalle_265418" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">4.5</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">4.5</span></td>
    <td></td>
    <td><form id="correo_545c53a31bee35.44140169" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control Experimental 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control Experimental 1 donde mi nota fue 4.5 ... " /><a href="javascript:$('correo_545c53a31bee35.44140169').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 271511 )">Control Experimental 2</a></h1>
        <h2>15 de Octubre</h2>
        <dl id="detalle_271511" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.4</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">6.4</span></td>
    <td></td>
    <td><form id="correo_545c53a31bff82.28522199" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control Experimental 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control Experimental 2 donde mi nota fue 6.4 ... " /><a href="javascript:$('correo_545c53a31bff82.28522199').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Controles Experimentales'</td>
    <td></td><td></td><td></td>
    <td><span class="">5.5</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
<tr class="separador">
    <td colspan="0">Ejercicios</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 273532 )">Ejercicio 1</a></h1>
        <dl id="detalle_273532" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">5.0</span></h1>
        <h2>1/3</h2>
    </td>
    <td>
        <h1><span class="reprueba">1.5</span></h1>
        <h2>1/3</h2>
    </td>
    <td>
        <h1><span class="reprueba">1.0</span></h1>
        <h2>1/3</h2>
    </td>
    <td><span class="reprueba">2.5</span></td>
    <td></td>
    <td><form id="correo_545c53a31c0da3.13989880" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 1 donde mi nota fue 2.5 ... " /><a href="javascript:$('correo_545c53a31c0da3.13989880').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 274092 )">Ejercicio 2</a></h1>
        <h2>30 de Octubre</h2>
        <dl id="detalle_274092" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.8</span></h1>
        <h2>1/2</h2>
    </td>
    <td>
        <h1><span class="">4.8</span></h1>
        <h2>1/2</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">5.8</span></td>
    <td></td>
    <td><form id="correo_545c53a31c1f39.63156926" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 2 donde mi nota fue 5.8 ... " /><a href="javascript:$('correo_545c53a31c1f39.63156926').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Ejercicios'</td>
    <td></td><td></td><td></td>
    <td><span class="">4.2</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
<tr class="separador">
    <td colspan="0">Laboratorios</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 268594 )">Informe de Laboratorio 3</a></h1>
        <dl id="detalle_268594" class="detalle">
            <dt>Mensaje Personal:</dt>
            <dd>Observaciones respecto al informe:<br />
La presentación del informe es desordenada. Hacen mal uso del líquido corrector dejando huella del escrito anterior y escribiendo sobre éste. Esto le resta estética al informe. Presentan errores de ortografía.<br />
RESUMEN: Media página. Redundan al escribir "el presente informe presenta". La descripción es muy vaga: "4 montajes distintos para los cuales se realizan análisis de resultados...", debe ser corta pero puntual. Faltaron objetivos referentes a los circuitos RC - RL.<br />
DESCRIPCIÓN: El término Vpp es referido a la amplitud de la onda, para obtener valores de voltaje hay que tener en cuenta que el número de divisiones que barre la onda en el osciloscopio y la escala de medida sobre el canal de interés del mismo osciloscopio. Por lo tanto es incorrecto afirmar que V = 2Vpp.<br />
RESULTADOS, AN�?LISIS Y DISCUSIÓN:  En el caso del multímetro tenían que medir en configuración alterna y continua para el voltaje en CADA SEÑAL (esto estaba señalado en la guía y ustedes lo señalan en la descripción), esto "al parecer" solo lo hicieron para la señal senosoidal, ya que en la tabla de datos de medidas de voltaje alterno para cada tipo de señal incluyen una columna que no está rotulada. Retomando la idea, si los valores medidos en voltaje continuo arrojaban cero a las señales triangular y cuadrada, esto también debe reportarse ya que estaban determinando el rango de validez del dispositivo de medida, este es un rango frecuencial de carácter numérico para cada tipo de señal. Bastaba con haber realizado lo que sugería la guía cuando preguntaba qué tipo de medición arrojaba el multímetro si Vrms, Vpp ó amplitud, es decir, calcular para cada uno habrían descubierto el tipo de medida y el rango de validez del multímetro además de la señal en que es confiable este tipo de medida; con esto justificaban por descarte y demostraban lo argumentado. Ustedes analizan solo con palabras, no es suficiente argumentar "... el multímetro mide Vrms, se puede ver en la tabla 1, 2 y 3..." cuando al analizar no hacen referencia al tipo señal ni el rango frecuencial en que sucede el fenómeno. Cuando discuten afirman que corroboraron .el comportamiento del multímetro en distintos modos de medición y la dependencia entre "V y la frecuencia aplicada dada por la EDO teórica", suena bien y al parecer está bien redactado pero nada de esto está incluido en el informe. <br />
Por otra parte, las mediciones hechas sobre los circuitos de los cuales entregaron gráficos están mal interpretadas y mal dibujadas.  Las  mediciones en las dos configuraciones del circuito RC: circuito con fuente - condensador - resistencia (primera parte) y fuente - resistencia - condensador  (al invertir la polaridad), en la  primera configuración ustedes medían sobre la resistencia, esto lo aclaraba la misma guía, por lo que la señal mostrada era la corriente sobre el condensador. Al invertir la polaridad, la señal mostrada era de carga y descarga del condensador, por lo que al analizar y empalmar las dos señales, lo que en el condensador era la carga, en la resistencia era la descarga ya que la corriente disminuye al cargar el condensador. Lo que corresponde a ustedes, analizan " montaje c la carga  del condensador corresponde a la curva azul creciente y descarga a la curva decreciente"  sin referirse a los gráficos, hay 7, cuál de todos?, así de literal sin más nada.  "En el montaje C al intercambiar la entrada se puede ver que los gráficos de carga y descarga (azul) se intercambian", carga y descarga de quién?. También incluyeron el gráfico al invertir las polaridades del circuito el cual está mal dibujado: para este caso la señal de entrada modula a la señal de medida, la señal reportada por ustedes, la señal medida es más pequeña que la señal que la modula. Las escalas en los ejes de las dos señales no están insertas y no son la misma, en el gráfico de corriente en el condensador, la señal de medida sobrepasa a la señal que modula (entrada del canal 1). Puede ser que la sonda del osciloscopio o en la punta de medida estuviera en 10x o que el generador de señales estaba en la configuración de 50 ohmios y no en alta impedancia (High Z).  Esto demuestra que no se familiarizaron totalmente con los elementos del laboratorio como lo afirmaron.<br />
La medida sobre el circuito así como lo indico: fuente - resistencia - inductancia, muestra la carga y descarga de la inductancia y al invertir la polaridad, se medía sobre la resistencia, es decir, el gráfico se interpreta como la corriente sobre la inductancia. La forma de la señal era muy parecida a la señal de entrada del generador de señales, con la diferencia que los bordes del cuadrado se curvaban muy levemente. Estas señales están mal dibujadas, el efecto es el mismo que señalé anteriormente con la configuración de los equipos. <br />
DISCUSIÓN: Discuten muy vagamente acerca del circuito con inductancia. No discuten del circuito RC ni de la primera práctica que era el cálculo del periodo de la señal triangular.<br />
CONCLUSIONES: Las conclusiones están bien propuestas, pero nada de lo que concluyen lo hicieron en el informe.<br />
Adelante</dd>
        </dl>
    </td>
    <td>
        <h1><span class="reprueba">3.6</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="reprueba">3.6</span></td>
    <td><a href="javascript:toggle( 'detalle_268594' )">Observaciones</a></td>
    <td><form id="correo_545c53a326ee64.95256407" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Informe de Laboratorio 3" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Informe de Laboratorio 3 donde mi nota fue 3.6 ... " /><a href="javascript:$('correo_545c53a326ee64.95256407').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 262166 )">Laboratorio 1</a></h1>
        <h2>20 de Agosto</h2>
        <dl id="detalle_262166" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">5.9</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">5.9</span></td>
    <td></td>
    <td><form id="correo_545c53a3270368.90512655" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Laboratorio 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Laboratorio 1 donde mi nota fue 5.9 ... " /><a href="javascript:$('correo_545c53a3270368.90512655').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 263586 )">Laboratorio 2</a></h1>
        <h2>27 de Agosto</h2>
        <dl id="detalle_263586" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.5</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">6.5</span></td>
    <td></td>
    <td><form id="correo_545c53a3271482.48409903" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Laboratorio 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Laboratorio 2 donde mi nota fue 6.5 ... " /><a href="javascript:$('correo_545c53a3271482.48409903').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 268598 )">Laboratorio 4</a></h1>
        <h2>24 de Septiembre</h2>
        <dl id="detalle_268598" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">6.0</span></td>
    <td></td>
    <td><form id="correo_545c53a3272566.69156584" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Laboratorio 4" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Laboratorio 4 donde mi nota fue 6.0 ... " /><a href="javascript:$('correo_545c53a3272566.69156584').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 270511 )">Laboratorio 5</a></h1>
        <h2>8 de Octubre</h2>
        <dl id="detalle_270511" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">5.5</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">5.5</span></td>
    <td></td>
    <td><form id="correo_545c53a32736f6.72448558" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Laboratorio 5" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Laboratorio 5 donde mi nota fue 5.5 ... " /><a href="javascript:$('correo_545c53a32736f6.72448558').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Laboratorios'</td>
    <td></td><td></td><td></td>
    <td><span class="">5.5</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
</table>
<dl class="leyenda">
    <dt style="width: 10px">*</dt>
    <dd>Los promedios corresponden a la <a target="_blank" href="http://es.wikipedia.org/wiki/Media_aritm%C3%A9tica">media aritmética</a> entre evaluaciones de un mismo tipo y no reflejan las reglas específicas del curso.</dd>
</dl>

<div id="estadisticas"></div>
</div>

<div id="footer">
<ul>
    <li><a href="https://www.u-cursos.cl/dev/paginas/politicas_uso">Políticas de Uso</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/acerca">Acerca de...</a></li>
    <li><a href="https://www.u-cursos.cl/tutoriales/">Tutoriales</a></li>
    <li><a href="https://www.u-cursos.cl/dev/blog/">Blog</a></li>
    <li>Con la tecnología de <a href="http://adi.ing.uchile.cl/" title="�?rea de Infotecnologías - ADI"><img src="https://www.u-cursos.cl/diseno/images/logos/adi.png" alt="�?rea de Infotecnologías - ADI" /></a></li>
    <li class="social">
    <a href="http://twitter.com/ucursos" target="_blank" title="U-Cursos en Twitter" class="file twitter"> &nbsp; </a>
    <a href="http://www.facebook.com/pages/U-Cursos-Chile/147024698734489" target="_blank" title="U-Cursos en Facebook" class="file facebook"> &nbsp; </a>
    </li>
</ul>
</div>

<script type="text/javascript">
Event.onReady( function() {
    ucmsg.init( { server: 'https://static.u-cursos.cl', port: 54321, secure: true }, { id: 'npm4t7o5v149qjkbpog0a64v46', user: '9079e9837b43ce4fc1096a70bf2325fb', avatar: 'av_5385561e94aba.jpg', alias: 'Pablo Pizarro R.' } );
} );
</script>



<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-101878-7']);
_gaq.push(['_setDomainName', 'www.u-cursos.cl']);
_gaq.push(['_trackPageview']);
_gaq.push(['_setCustomVar', 1, 'movil', '0' ]);
</script>
<script type="text/javascript" src="https://www.u-cursos.cl/diseno/js/ga.js"></script>

<script type="text/javascript">
Event.onReady( function() {
    notificacion.init( { server: 'https://static.u-cursos.cl', port: 54322, token: 'npm4t7o5v149qjkbpog0a64v46', url: 'https://www.u-cursos.cl', webkit: true } );
} );
</script>

</body>
</html>
"""

CURSO2 = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es" xmlns:og="http://opengraphprotocol.org/schema/">
<head><title>U-Cursos :: FI2002-5 Electromagnetismo :: Notas Parciales</title>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<meta name="descripcion" content="Una Herramienta de Apoyo a la Docencia Presencial." />
<script src="https://www.u-cursos.cl/d/js/hash_v6702.js" type="text/javascript"></script>
<script src="https://www.u-cursos.cl/d/js/javascript_v6702.js" type="text/javascript"></script>
<link rel="stylesheet" href="https://www.u-cursos.cl/d/css/style_v6702.css" type="text/css" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/d/images/apple-touch-icon-57.png" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/d/images/apple-touch-icon-72.png" sizes="72x72"/>
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/d/images/apple-touch-icon-114.png" sizes="114x114"/>
<link rel="copyright license" href="https://www.u-cursos.cl/d/acerca" title="Área de Infotecnologías (ADI), FCFM, U. de Chile." />
<link rel="shortcut icon" href="https://www.u-cursos.cl/favicon.ico?v4" type="image/x-icon" /><link rel="stylesheet" href="https://www.u-cursos.cl/d/css/print_v6702.css" media="print" type="text/css" /><link rel="stylesheet" href="https://www.u-cursos.cl/d/css/base_v6702?base=ingenieria" type="text/css" /><meta property="og:type" content="university" />
<meta property="og:site_name" content="U-Cursos" />
<meta property="og:title" content="Notas Parciales :: FI2002-5 Electromagnetismo" />
<meta property="og:url" content="https://www.u-cursos.cl" />
<meta property="og:image" content="https://www.u-cursos.cl/d/images/servicios/notas.png" /><link rel="stylesheet" href="https://www.u-cursos.cl/d/css/css_v6702?servicio=notas" type="text/css" /><link rel="alternate" type="application/rss+xml" title="Canales de Mensajes FI2002-5 Electromagnetismo" href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/historial/rss20" /><link rel="alternate" type="application/rss+xml" title="FI2002-5 Electromagnetismo - Notas Parciales" href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/historial/rss20?servicios=notas" /></head>
<body><a href="https://www.u-cursos.cl"><h1 id="ucursos"><span>U-Cursos :: ingenieria</span></h1></a>

<h2 class="ucursos">FI2002-5 Electromagnetismo 2014, Semestre Primavera</h2>

<ul id="servicios_generales">
    <li><a href="https://www.u-cursos.cl/?csrf=e92081661f&accion=salir">Salir</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/contacto">Contacto</a></li>
    <li id="buscador">
    <form id="form_buscador" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/buscador/">
    <input type="text" name="q" value="Buscar..." onFocus="if(this.value=='Buscar...')this.value='';" onBlur="if(this.value=='')this.value='Buscar...';" />
    <a href="javascript:if($('form_buscador').q.value!='Buscar...')$('form_buscador').submit()"><span>Buscar</span></a>
    </form>
    </li>
</ul>

<style>
h2.ucursos {
   background-image: url( 'https://www.u-cursos.cl/d/images/bases/ingenieria.png' );
}

body {
    background: white url('https://www.u-cursos.cl/d/images/servicios/fondos/notas.png') fixed no-repeat 95% 90%;
}

table{
    background: #fff;
}

td.verde, td.opciones{
    background: #f9f4e8;
}

td.gris{
    background: #f4f4f4;
}


</style>

<div id="izquierda" style="clear:right">

    <div id="usuario" class=" off">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=usuario">Pablo Pizarro R.</a></h1>
    <ul>
        <li><a href="https://www.u-cursos.cl/inicio"><img src="https://www.u-cursos.cl/d/images/servicios/pagina_inicio_on.png" title="Mi Inicio" /> <span>Mi Inicio</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/mis_canales/"><img src="https://www.u-cursos.cl/d/images/servicios/mis_canales.png" title="Mis Canales" /> <span>Mis Canales</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/"><img src="https://www.u-cursos.cl/d/images/servicios/datos_usuario.png" title="Mis Datos" /> <span>Mis Datos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/todos_cursos/"><img src="https://www.u-cursos.cl/d/images/servicios/todos_cursos.png" title="Todos Mis Cursos" /> <span>Todos Mis Cursos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/horario/"><img src="https://www.u-cursos.cl/d/images/servicios/horario.png" title="Horario" /> <span>Horario</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/favoritos/"><img src="https://www.u-cursos.cl/d/images/servicios/favoritos.png" title="Mis Estrellas" /> <span>Mis Estrellas</span></a></li>


    </ul>
    </div>


    <div id="cursos" class="caja on">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=cursos">Cursos Actuales</a></h1>
    <ul>
        <li id="curso.115364" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CC3001/2/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CC3001-2 Algoritmos y Estructuras de Datos</span></a>         </li>
        <li id="curso.115983" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CM2004-1 Fisicoquímica</span></a>         </li>
        <li id="curso.115454" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>DR500A-1 Ajedrez I</span></a>         </li>
        <li id="curso.114686" class="sel" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2002-5 Electromagnetismo</span></a>         </li>
        <li id="curso.114695" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2003-9 Métodos Experimentales</span></a>         </li>
        <li id="curso.115024" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/MA2002/4/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>MA2002-4 Cálculo Avanzado y Aplicaciones</span></a>         </li>
    </ul>
    </div>

    <div id="comunidades" class="caja on">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=comunidades">Comunidades</a></h1>
    <ul>
        <li id="curso.57163" class=""><a href="https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMGAMER-1 Comunidad Gamer Beauchef</span></a>         </li>
        <li id="curso.103935" class=""><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMMUSI-1 Música Beauchef</span></a>         </li>
        <li id="curso.35017" class=""><a href="https://www.u-cursos.cl/uchile/2009/0/COMVIDA/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMVIDA-1 Comunidad Calidad de Vida Estudiantil</span></a>         </li>
    </ul>
    </div>

    <div id="instituciones" class="caja on">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=instituciones">Instituciones</a></h1>
    <ul>
        <li id="institucion.4" class=""><a href="https://www.u-cursos.cl/uchile/4/"><img src="https://www.u-cursos.cl/d/images/instituciones/uchile.png" alt="Comunidades - Universidad de Chile" title="Comunidades - Universidad de Chile" class="icono" /> <span>Comunidades - Universidad de Chile</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/4/foro_institucion/" style="white-space:nowrap">Foro (3)</a></div></li>
        <li id="institucion.3000" class=""><a href="https://www.u-cursos.cl/uchile/3000/"><img src="https://www.u-cursos.cl/d/images/instituciones/uchile.png" alt="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" title="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Diagnósticos - Facultad de Cs. Físicas y Matemáticas</span></a> </li>
        <li id="institucion.2" class=""><a href="https://www.u-cursos.cl/ingenieria/2/"><img src="https://www.u-cursos.cl/d/images/instituciones/ingenieria.png" alt="Facultad de Cs. Físicas y Matemáticas" title="Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Facultad de Cs. Físicas y Matemáticas</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/ingenieria/2/foro_institucion/" style="white-space:nowrap">Foro (2)</a></div></li>
    </ul>
    </div>
</div>

<div id="body">

<ul class="modulos fijos">
    <li><a href="?csrf=e92081661f&accion=mi_ucursos&subaccion=favorito">
<img src="https://www.u-cursos.cl/d/images/servicios/favorito_add.png" class="icono" title="Para agregarlo a tus favoritos" /><span>Agregar Favorito</span>
</a>
</li>
    <li><a href="?csrf=e92081661f&accion=mi_ucursos&subaccion=inicio"><img src="https://www.u-cursos.cl/d/images/servicios/pagina_inicio_add.png" class="icono" /><span>Inicio</span></a>
</li>
    <li><a href="http://manuales.ing.uchile.cl/ucursos/notas/alumno.html" target="_blank"><img src="https://www.u-cursos.cl/d/images/servicios/ayuda.png" /><span>Ayuda</span></a></li>
</ul>

<ul class="modulos">
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/acta/"><img src="https://www.u-cursos.cl/d/images/servicios/acta.png" alt="Acta" class="icono" /><span>Acta</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/calendario/"><img src="https://www.u-cursos.cl/d/images/servicios/calendario.png" alt="Calendario" class="icono" /><span>Calendario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/"><img src="https://www.u-cursos.cl/d/images/servicios/correo.png" alt="Correo" class="icono" /><span>Correo</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/datos_curso/"><img src="https://www.u-cursos.cl/d/images/servicios/datos_curso.png" alt="Datos del Curso" class="icono" /><span>Datos del Curso</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/encuestas/"><img src="https://www.u-cursos.cl/d/images/servicios/encuestas.png" alt="Encuestas" class="icono" /><span>Encuestas</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/enlaces/"><img src="https://www.u-cursos.cl/d/images/servicios/enlaces.png" alt="Enlaces" class="icono" /><span>Enlaces</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/foro/"><img src="https://www.u-cursos.cl/d/images/servicios/foro.png" alt="Foro" class="icono" /><span>Foro</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/historial/"><img src="https://www.u-cursos.cl/d/images/servicios/historial.png" alt="Historial" class="icono" /><span>Historial</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/horario_curso/"><img src="https://www.u-cursos.cl/d/images/servicios/horario_curso.png" alt="Horario" class="icono" /><span>Horario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/integrantes/"><img src="https://www.u-cursos.cl/d/images/servicios/integrantes.png" alt="Integrantes" class="icono" /><span>Integrantes</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/material_alumnos/"><img src="https://www.u-cursos.cl/d/images/servicios/material_alumnos.png" alt="Material Alumnos" class="icono" /><span>Material Alumnos</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/material_docente/"><img src="https://www.u-cursos.cl/d/images/servicios/material_docente.png" alt="Material Docente" class="icono" /><span>Material Docente</span></a></li>
    <li class="servicio sel"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/notas/"><img src="https://www.u-cursos.cl/d/images/servicios/notas.png" alt="Notas Parciales" class="icono" /><span>Notas Parciales</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/votaciones/"><img src="https://www.u-cursos.cl/d/images/servicios/votaciones.png" alt="Votaciones" class="icono" /><span>Votaciones</span></a></li>
</ul>

<ul id="navbar">
    <li><a href="https://www.u-cursos.cl">Inicio</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/instituciones">Instituciones</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/">Facultad de Cs. Físicas y Matemáticas</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/cursos_departamento/?_hook=periodo&periodo=2014.2&departamento=13">Cursos</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/">FI2002-5 Electromagnetismo</a></li>
    <li>Notas Parciales</li>
</ul>




<h1 class="modulo">Notas Parciales</h1>
<script type="text/javascript">
function getEstadistica( id ) {
    $('estadisticas').update( '<span class="espera" style="width:150px">Cargando estadísticas...</span>' );
    $('estadisticas').update( quickAjax( 'alumno_detalle?escala=0&id_evaluacion='+id ) );
    $('id_evaluacion').value = id;
    jstriggerTable( $('tabla') );

    $('tabla').select('img.chica').each( function( o ) {
        o.observe( 'click', function( e ) {
            i = e.element();
            i.hasClassName( 'chica' ) ? i.removeClassName( 'chica' ) : i.addClassName( 'chica' );
        } );
    } );
    $('estadisticas').scrollTo();
}

</script>


<form class="buscar">
<input type="hidden" id="id_evaluacion" name="id_evaluacion" value="0" />
Usar la misma escala para todas las evaluaciones: <select id="escala" name="escala" onchange="this.form.submit()"><option value="0" selected="selected">No</option><option value="1">1.0 - 7.0</option><option value="2">1.00 - 7.00</option><option value="3">1.000 - 7.000</option><option value="4">0% - 100%</option><option value="5">I - MB</option><option value="6">R - D</option><option value="10">1 - 10 ( equivalencia 4.0 = 6 )</option></select></form>

<table class="sortable">
<thead>
<tr>
    <th class="string">Evaluación</th>
    <th class="number">P1</th>
    <th class="number">P2</th>
    <th class="number">P3</th>
    <th class="number strong">Prom.</th>
    <th class="opciones" colspan="2">Opciones</th>
</tr>
</thead>
<tr class="separador">
    <td colspan="0">Controles</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 266188 )">Control 1</a></h1>
        <dl id="detalle_266188" class="detalle">
            <dt>Observación General:</dt>
            <dd>MEJOR(PROMEDIO(pregunta_1,pregunta_2,pregunta_3),((2/5)*pregunta_1+(1/5)*pregunta_2+(2/5)*pregunta_3))</dd>
            <dt>Mensaje Personal:</dt>
            <dd>MEJOR(PROMEDIO(7.0,7.0,7.0),((2/5)*7.0+(1/5)*7.0+(2/5)*7.0))</dd>
        </dl>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">7.0</span></td>
    <td><a href="javascript:toggle( 'detalle_266188' )">Observaciones</a></td>
    <td><form id="correo_545db4ae3c8074.58598518" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control 1 donde mi nota fue 7.0 ... " /><a href="javascript:$('correo_545db4ae3c8074.58598518').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 270948 )">Control 2</a></h1>
        <h2>9 de Octubre</h2>
        <dl id="detalle_270948" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.0</span></h1>
        <h2>1/3</h2>
    </td>
    <td>
        <h1><span class="">6.0</span></h1>
        <h2>1/3</h2>
    </td>
    <td>
        <h1><span class="reprueba">3.2</span></h1>
        <h2>1/3</h2>
    </td>
    <td><span class="">5.1</span></td>
    <td></td>
    <td><form id="correo_545db4ae3c8c70.78867063" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control 2 donde mi nota fue 5.1 ... " /><a href="javascript:$('correo_545db4ae3c8c70.78867063').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Controles'</td>
    <td></td><td></td><td></td>
    <td><span class="">6.1</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
<tr class="separador">
    <td colspan="0">Ejercicios</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 260348 )">Ejercicio 1</a></h1>
        <h2>8 de Agosto</h2>
        <dl id="detalle_260348" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">5.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">5.0</span></td>
    <td></td>
    <td><form id="correo_545db4ae3ca6f8.34482968" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 1 donde mi nota fue 5.0 ... " /><a href="javascript:$('correo_545db4ae3ca6f8.34482968').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 263992 )">Ejercicio 2</a></h1>
        <h2>22 de Agosto</h2>
        <dl id="detalle_263992" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">5.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">5.0</span></td>
    <td></td>
    <td><form id="correo_545db4ae3cb118.42016842" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 2 donde mi nota fue 5.0 ... " /><a href="javascript:$('correo_545db4ae3cb118.42016842').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 266850 )">Ejercicio 3</a></h1>
        <h2>5 de Septiembre</h2>
        <dl id="detalle_266850" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">4.7</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">4.7</span></td>
    <td></td>
    <td><form id="correo_545db4ae3cbb81.12379115" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 3" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 3 donde mi nota fue 4.7 ... " /><a href="javascript:$('correo_545db4ae3cbb81.12379115').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 266373 )">Ejercicio 4</a></h1>
        <h2>12 de Septiembre</h2>
        <dl id="detalle_266373" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">7.0</span></td>
    <td></td>
    <td><form id="correo_545db4ae3cc672.33534917" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 4" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 4 donde mi nota fue 7.0 ... " /><a href="javascript:$('correo_545db4ae3cc672.33534917').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 273568 )">Ejercicio 6</a></h1>
        <h2>17 de Octubre</h2>
        <dl id="detalle_273568" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="reprueba">3.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="reprueba">3.0</span></td>
    <td></td>
    <td><form id="correo_545db4ae3cd070.40822521" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 6" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 6 donde mi nota fue 3.0 ... " /><a href="javascript:$('correo_545db4ae3cd070.40822521').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 273567 )">Ejercicio 7 </a></h1>
        <h2>24 de Octubre</h2>
        <dl id="detalle_273567" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="reprueba">3.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="reprueba">3.0</span></td>
    <td></td>
    <td><form id="correo_545db4ae3cda79.70864681" action="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 7 " /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 7  donde mi nota fue 3.0 ... " /><a href="javascript:$('correo_545db4ae3cda79.70864681').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Ejercicios'</td>
    <td></td><td></td><td></td>
    <td><span class="">4.6</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
</table>
<dl class="leyenda">
    <dt style="width: 10px">*</dt>
    <dd>Los promedios corresponden a la <a target="_blank" href="http://es.wikipedia.org/wiki/Media_aritm%C3%A9tica">media aritmética</a> entre evaluaciones de un mismo tipo y no reflejan las reglas específicas del curso.</dd>
</dl>

<div id="estadisticas"></div>
</div>

<div id="footer">
<ul>
    <li><a href="https://www.u-cursos.cl/dev/paginas/politicas_uso">Políticas de Uso</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/acerca">Acerca de...</a></li>
    <li><a href="https://www.u-cursos.cl/tutoriales/">Tutoriales</a></li>
    <li><a href="https://www.u-cursos.cl/dev/blog/">Blog</a></li>
    <li>Con la tecnología de <a href="http://adi.ing.uchile.cl/" title="Área de Infotecnologías - ADI"><img src="https://www.u-cursos.cl/d/images/logos/adi.png" alt="Área de Infotecnologías - ADI" /></a></li>
    <li class="social">
    <a href="http://twitter.com/ucursos" target="_blank" title="U-Cursos en Twitter" class="file twitter"> &nbsp; </a>
    <a href="http://www.facebook.com/pages/U-Cursos-Chile/147024698734489" target="_blank" title="U-Cursos en Facebook" class="file facebook"> &nbsp; </a>
    </li>
</ul>
</div>

<script type="text/javascript">
Event.onReady( function() {
    ucmsg.init( { server: 'https://static.u-cursos.cl', port: 54321, secure: true }, { id: '4emk4fo00de4tmud48bhi3bna1', user: '9079e9837b43ce4fc1096a70bf2325fb', avatar: 'av_5385561e94aba.jpg', alias: 'Pablo Pizarro R.' } );
} );
</script>



<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-101878-7']);
_gaq.push(['_setDomainName', 'www.u-cursos.cl']);
_gaq.push(['_trackPageview']);
_gaq.push(['_setCustomVar', 1, 'movil', '0' ]);
</script>
<script type="text/javascript" src="https://www.u-cursos.cl/d/js/ga.js"></script>

<script type="text/javascript">
Event.onReady( function() {
    notificacion.init( { server: 'https://static.u-cursos.cl', port: 54322, token: '4emk4fo00de4tmud48bhi3bna1', url: 'https://www.u-cursos.cl', webkit: true } );
} );
</script>

</body>
</html>
"""

CURSO3 = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es" xmlns:og="http://opengraphprotocol.org/schema/">
<head><title>U-Cursos :: CM2004-1 Fisicoquímica :: Notas Parciales</title>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<meta name="descripcion" content="Una Herramienta de Apoyo a la Docencia Presencial." />
<script src="https://www.u-cursos.cl/d/js/hash_v6702.js" type="text/javascript"></script>
<script src="https://www.u-cursos.cl/d/js/javascript_v6702.js" type="text/javascript"></script>
<link rel="stylesheet" href="https://www.u-cursos.cl/d/css/style_v6702.css" type="text/css" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/d/images/apple-touch-icon-57.png" />
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/d/images/apple-touch-icon-72.png" sizes="72x72"/>
<link rel="apple-touch-icon" href="https://www.u-cursos.cl/d/images/apple-touch-icon-114.png" sizes="114x114"/>
<link rel="copyright license" href="https://www.u-cursos.cl/d/acerca" title="Área de Infotecnologías (ADI), FCFM, U. de Chile." />
<link rel="shortcut icon" href="https://www.u-cursos.cl/favicon.ico?v4" type="image/x-icon" /><link rel="stylesheet" href="https://www.u-cursos.cl/d/css/print_v6702.css" media="print" type="text/css" /><link rel="stylesheet" href="https://www.u-cursos.cl/d/css/base_v6702?base=ingenieria" type="text/css" /><meta property="og:type" content="university" />
<meta property="og:site_name" content="U-Cursos" />
<meta property="og:title" content="Notas Parciales :: CM2004-1 Fisicoquímica" />
<meta property="og:url" content="https://www.u-cursos.cl" />
<meta property="og:image" content="https://www.u-cursos.cl/d/images/servicios/notas.png" /><link rel="stylesheet" href="https://www.u-cursos.cl/d/css/css_v6702?servicio=notas" type="text/css" /><link rel="alternate" type="application/rss+xml" title="Canales de Mensajes CM2004-1 Fisicoquímica" href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/historial/rss20" /><link rel="alternate" type="application/rss+xml" title="CM2004-1 Fisicoquímica - Notas Parciales" href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/historial/rss20?servicios=notas" /></head>
<body><a href="https://www.u-cursos.cl"><h1 id="ucursos"><span>U-Cursos :: ingenieria</span></h1></a>

<h2 class="ucursos">CM2004-1 Fisicoquímica 2014, Semestre Primavera</h2>

<ul id="servicios_generales">
    <li><a href="https://www.u-cursos.cl/?csrf=e92081661f&accion=salir">Salir</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/contacto">Contacto</a></li>
    <li id="buscador">
    <form id="form_buscador" action="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/buscador/">
    <input type="text" name="q" value="Buscar..." onFocus="if(this.value=='Buscar...')this.value='';" onBlur="if(this.value=='')this.value='Buscar...';" />
    <a href="javascript:if($('form_buscador').q.value!='Buscar...')$('form_buscador').submit()"><span>Buscar</span></a>
    </form>
    </li>
</ul>

<style>
h2.ucursos {
   background-image: url( 'https://www.u-cursos.cl/d/images/bases/ingenieria.png' );
}

body {
    background: white url('https://www.u-cursos.cl/d/images/servicios/fondos/notas.png') fixed no-repeat 95% 90%;
}

table{
    background: #fff;
}

td.verde, td.opciones{
    background: #f9f4e8;
}

td.gris{
    background: #f4f4f4;
}


</style>

<div id="izquierda" style="clear:right">

    <div id="usuario" class=" off">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=usuario">Pablo Pizarro R.</a></h1>
    <ul>
        <li><a href="https://www.u-cursos.cl/inicio"><img src="https://www.u-cursos.cl/d/images/servicios/pagina_inicio_on.png" title="Mi Inicio" /> <span>Mi Inicio</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/mis_canales/"><img src="https://www.u-cursos.cl/d/images/servicios/mis_canales.png" title="Mis Canales" /> <span>Mis Canales</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/"><img src="https://www.u-cursos.cl/d/images/servicios/datos_usuario.png" title="Mis Datos" /> <span>Mis Datos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/todos_cursos/"><img src="https://www.u-cursos.cl/d/images/servicios/todos_cursos.png" title="Todos Mis Cursos" /> <span>Todos Mis Cursos</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/horario/"><img src="https://www.u-cursos.cl/d/images/servicios/horario.png" title="Horario" /> <span>Horario</span></a></li>

        <li class=""><a href="https://www.u-cursos.cl/usuario/9079e9837b43ce4fc1096a70bf2325fb/favoritos/"><img src="https://www.u-cursos.cl/d/images/servicios/favoritos.png" title="Mis Estrellas" /> <span>Mis Estrellas</span></a></li>


    </ul>
    </div>


    <div id="cursos" class="caja on">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=cursos">Cursos Actuales</a></h1>
    <ul>
        <li id="curso.115364" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CC3001/2/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CC3001-2 Algoritmos y Estructuras de Datos</span></a>         </li>
        <li id="curso.115983" class="sel" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>CM2004-1 Fisicoquímica</span></a>         </li>
        <li id="curso.115454" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/DR500A/1/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>DR500A-1 Ajedrez I</span></a>         </li>
        <li id="curso.114686" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2002/5/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2002-5 Electromagnetismo</span></a>         </li>
        <li id="curso.114695" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/FI2003/9/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>FI2003-9 Métodos Experimentales</span></a>         </li>
        <li id="curso.115024" class="" style="vertical-align: bottom"><a href="https://www.u-cursos.cl/ingenieria/2014/2/MA2002/4/"><div title="Alumno" class="sprite_cargos cargos_alumno"></div> <span>MA2002-4 Cálculo Avanzado y Aplicaciones</span></a>         </li>
    </ul>
    </div>

    <div id="comunidades" class="caja on">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=comunidades">Comunidades</a></h1>
    <ul>
        <li id="curso.57163" class=""><a href="https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMGAMER-1 Comunidad Gamer Beauchef</span></a>         </li>
        <li id="curso.103935" class=""><a href="https://www.u-cursos.cl/uchile/2013/0/COMMUSI/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMMUSI-1 Música Beauchef</span></a>         </li>
        <li id="curso.35017" class=""><a href="https://www.u-cursos.cl/uchile/2009/0/COMVIDA/1/"><div title="Miembro de Comunidad" class="sprite_cargos cargos_miembro_de_comunidad"></div> <span>COMVIDA-1 Comunidad Calidad de Vida Estudiantil</span></a>         </li>
    </ul>
    </div>

    <div id="instituciones" class="caja on">
    <h1><a class="caja" href="?csrf=e92081661f&accion=mi_ucursos&subaccion=caja&caja=instituciones">Instituciones</a></h1>
    <ul>
        <li id="institucion.4" class=""><a href="https://www.u-cursos.cl/uchile/4/"><img src="https://www.u-cursos.cl/d/images/instituciones/uchile.png" alt="Comunidades - Universidad de Chile" title="Comunidades - Universidad de Chile" class="icono" /> <span>Comunidades - Universidad de Chile</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/uchile/4/foro_institucion/" style="white-space:nowrap">Foro (3)</a></div></li>
        <li id="institucion.3000" class=""><a href="https://www.u-cursos.cl/uchile/3000/"><img src="https://www.u-cursos.cl/d/images/instituciones/uchile.png" alt="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" title="Diagnósticos - Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Diagnósticos - Facultad de Cs. Físicas y Matemáticas</span></a> </li>
        <li id="institucion.2" class=""><a href="https://www.u-cursos.cl/ingenieria/2/"><img src="https://www.u-cursos.cl/d/images/instituciones/ingenieria.png" alt="Facultad de Cs. Físicas y Matemáticas" title="Facultad de Cs. Físicas y Matemáticas" class="icono" /> <span>Facultad de Cs. Físicas y Matemáticas</span></a> <div class="nuevo"><a href="https://www.u-cursos.cl/ingenieria/2/foro_institucion/" style="white-space:nowrap">Foro (2)</a></div></li>
    </ul>
    </div>
</div>

<div id="body">

<ul class="modulos fijos">
    <li><a href="?csrf=e92081661f&accion=mi_ucursos&subaccion=favorito">
<img src="https://www.u-cursos.cl/d/images/servicios/favorito_add.png" class="icono" title="Para agregarlo a tus favoritos" /><span>Agregar Favorito</span>
</a>
</li>
    <li><a href="?csrf=e92081661f&accion=mi_ucursos&subaccion=inicio"><img src="https://www.u-cursos.cl/d/images/servicios/pagina_inicio_add.png" class="icono" /><span>Inicio</span></a>
</li>
    <li><a href="http://manuales.ing.uchile.cl/ucursos/notas/alumno.html" target="_blank"><img src="https://www.u-cursos.cl/d/images/servicios/ayuda.png" /><span>Ayuda</span></a></li>
</ul>

<ul class="modulos">
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/acta/"><img src="https://www.u-cursos.cl/d/images/servicios/acta.png" alt="Acta" class="icono" /><span>Acta</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/calendario/"><img src="https://www.u-cursos.cl/d/images/servicios/calendario.png" alt="Calendario" class="icono" /><span>Calendario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/correo/"><img src="https://www.u-cursos.cl/d/images/servicios/correo.png" alt="Correo" class="icono" /><span>Correo</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/datos_curso/"><img src="https://www.u-cursos.cl/d/images/servicios/datos_curso.png" alt="Datos del Curso" class="icono" /><span>Datos del Curso</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/encuestas/"><img src="https://www.u-cursos.cl/d/images/servicios/encuestas.png" alt="Encuestas" class="icono" /><span>Encuestas</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/foro/"><img src="https://www.u-cursos.cl/d/images/servicios/foro.png" alt="Foro" class="icono" /><span>Foro</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/historial/"><img src="https://www.u-cursos.cl/d/images/servicios/historial.png" alt="Historial" class="icono" /><span>Historial</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/horario_curso/"><img src="https://www.u-cursos.cl/d/images/servicios/horario_curso.png" alt="Horario" class="icono" /><span>Horario</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/integrantes/"><img src="https://www.u-cursos.cl/d/images/servicios/integrantes.png" alt="Integrantes" class="icono" /><span>Integrantes</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/material_alumnos/"><img src="https://www.u-cursos.cl/d/images/servicios/material_alumnos.png" alt="Material Alumnos" class="icono" /><span>Material Alumnos</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/material_docente/"><img src="https://www.u-cursos.cl/d/images/servicios/material_docente.png" alt="Material Docente" class="icono" /><span>Material Docente</span></a></li>
    <li class="servicio sel"><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/notas/"><img src="https://www.u-cursos.cl/d/images/servicios/notas.png" alt="Notas Parciales" class="icono" /><span>Notas Parciales</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/novedades/"><img src="https://www.u-cursos.cl/d/images/servicios/novedades.png" alt="Novedades" class="icono" /><span>Novedades</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/tareas/"><img src="https://www.u-cursos.cl/d/images/servicios/tareas.png" alt="Tareas" class="icono" /><span>Tareas</span></a></li>
    <li class="servicio "><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/votaciones/"><img src="https://www.u-cursos.cl/d/images/servicios/votaciones.png" alt="Votaciones" class="icono" /><span>Votaciones</span></a></li>
</ul>

<ul id="navbar">
    <li><a href="https://www.u-cursos.cl">Inicio</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/instituciones">Instituciones</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/">Facultad de Cs. Físicas y Matemáticas</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2/cursos_departamento/?_hook=periodo&periodo=2014.2&departamento=306">Cursos</a></li>
    <li><a href="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/">CM2004-1 Fisicoquímica</a></li>
    <li>Notas Parciales</li>
</ul>




<h1 class="modulo">Notas Parciales</h1>
<script type="text/javascript">
function getEstadistica( id ) {
    $('estadisticas').update( '<span class="espera" style="width:150px">Cargando estadísticas...</span>' );
    $('estadisticas').update( quickAjax( 'alumno_detalle?escala=0&id_evaluacion='+id ) );
    $('id_evaluacion').value = id;
    jstriggerTable( $('tabla') );

    $('tabla').select('img.chica').each( function( o ) {
        o.observe( 'click', function( e ) {
            i = e.element();
            i.hasClassName( 'chica' ) ? i.removeClassName( 'chica' ) : i.addClassName( 'chica' );
        } );
    } );
    $('estadisticas').scrollTo();
}

</script>


<form class="buscar">
<input type="hidden" id="id_evaluacion" name="id_evaluacion" value="0" />
Usar la misma escala para todas las evaluaciones: <select id="escala" name="escala" onchange="this.form.submit()"><option value="0" selected="selected">No</option><option value="1">1.0 - 7.0</option><option value="2">1.00 - 7.00</option><option value="3">1.000 - 7.000</option><option value="4">0% - 100%</option><option value="5">I - MB</option><option value="6">R - D</option><option value="10">1 - 10 ( equivalencia 4.0 = 6 )</option></select></form>

<table class="sortable">
<thead>
<tr>
    <th class="string">Evaluación</th>
    <th class="number">P1</th>
    <th class="number">P2</th>
    <th class="number">P3</th>
    <th class="number">P4</th>
    <th class="number strong">Prom.</th>
    <th class="opciones" colspan="2">Opciones</th>
</tr>
</thead>
<tr class="separador">
    <td colspan="0"></td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 274047 )">Control 2</a></h1>
        <dl id="detalle_274047" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>1/4</h2>
    </td>
    <td>
        <h1><span class="reprueba">1.5</span></h1>
        <h2>1/4</h2>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>1/4</h2>
    </td>
    <td>
        <h1><span class="reprueba">1.4</span></h1>
        <h2>1/4</h2>
    </td>
    <td><span class="">4.2</span></td>
    <td></td>
    <td><form id="correo_545db92e20bd54.02853791" action="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control 2 donde mi nota fue 4.2 ... " /><a href="javascript:$('correo_545db92e20bd54.02853791').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tr class="separador">
    <td colspan="0">Control</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 264864 )">Control 1</a></h1>
        <h2>4 de Septiembre</h2>
        <dl id="detalle_264864" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.8</span></h1>
        <h2>25%</h2>
    </td>
    <td>
        <h1><span class="">6.2</span></h1>
        <h2>25%</h2>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>25%</h2>
    </td>
    <td>
        <h1><span class="">5.2</span></h1>
        <h2>25%</h2>
    </td>
    <td><span class="">6.3</span></td>
    <td></td>
    <td><form id="correo_545db92e20ca60.18497694" action="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Control 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Control 1 donde mi nota fue 6.3 ... " /><a href="javascript:$('correo_545db92e20ca60.18497694').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tr class="separador">
    <td colspan="0">Ejercicios</td>
</tr>
<tbody>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 263727 )">Ejercicio 2</a></h1>
        <dl id="detalle_263727" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">6.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">6.0</span></td>
    <td></td>
    <td><form id="correo_545db92e20def7.51917985" action="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 2" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 2 donde mi nota fue 6.0 ... " /><a href="javascript:$('correo_545db92e20def7.51917985').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 266901 )">Ejercicio 4</a></h1>
        <dl id="detalle_266901" class="detalle">
            <dt>Observación General:</dt>
            <dd>Este es el &uacute;ltimo ejercicio que tuvieron.</dd>
        </dl>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">7.0</span></td>
    <td><a href="javascript:toggle( 'detalle_266901' )">Observaciones</a></td>
    <td><form id="correo_545db92e20f313.57575304" action="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 4" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 4 donde mi nota fue 7.0 ... " /><a href="javascript:$('correo_545db92e20f313.57575304').submit()">Consultar</a></form></td>


</tr>
<tr class="">
    <td>
        <h1><a href="javascript:getEstadistica( 264442 )">Ejercicio 1</a></h1>
        <h2>30 de Agosto</h2>
        <dl id="detalle_264442" class="detalle">
        </dl>
    </td>
    <td>
        <h1><span class="">7.0</span></h1>
        <h2>100%</h2>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td>
        <h1><span class=""></span></h1>
    </td>
    <td><span class="">7.0</span></td>
    <td></td>
    <td><form id="correo_545db92e20fdb5.03331662" action="https://www.u-cursos.cl/ingenieria/2014/2/CM2004/1/correo/" method="post"><input type="hidden" name="tema" value="Consulta sobre Ejercicio 1" /><input type="hidden" name="mensaje_correo" value="Profesor,

En la evaluación Ejercicio 1 donde mi nota fue 7.0 ... " /><a href="javascript:$('correo_545db92e20fdb5.03331662').submit()">Consultar</a></form></td>


</tr>
</tbody>
<tbody>
<tr class="foot">
    <td>Promedio 'Ejercicios'</td>
    <td></td><td></td><td></td><td></td>
    <td><span class="">6.7</span> <sup>*</sup></td>
    <td colspan="2"></td>
</tr>
</tbody>
</table>
<dl class="leyenda">
    <dt style="width: 10px">*</dt>
    <dd>Los promedios corresponden a la <a target="_blank" href="http://es.wikipedia.org/wiki/Media_aritm%C3%A9tica">media aritmética</a> entre evaluaciones de un mismo tipo y no reflejan las reglas específicas del curso.</dd>
</dl>

<div id="estadisticas"></div>
</div>

<div id="footer">
<ul>
    <li><a href="https://www.u-cursos.cl/dev/paginas/politicas_uso">Políticas de Uso</a></li>
    <li><a href="https://www.u-cursos.cl/dev/paginas/acerca">Acerca de...</a></li>
    <li><a href="https://www.u-cursos.cl/tutoriales/">Tutoriales</a></li>
    <li><a href="https://www.u-cursos.cl/dev/blog/">Blog</a></li>
    <li>Con la tecnología de <a href="http://adi.ing.uchile.cl/" title="Área de Infotecnologías - ADI"><img src="https://www.u-cursos.cl/d/images/logos/adi.png" alt="Área de Infotecnologías - ADI" /></a></li>
    <li class="social">
    <a href="http://twitter.com/ucursos" target="_blank" title="U-Cursos en Twitter" class="file twitter"> &nbsp; </a>
    <a href="http://www.facebook.com/pages/U-Cursos-Chile/147024698734489" target="_blank" title="U-Cursos en Facebook" class="file facebook"> &nbsp; </a>
    </li>
</ul>
</div>

<script type="text/javascript">
Event.onReady( function() {
    ucmsg.init( { server: 'https://static.u-cursos.cl', port: 54321, secure: true }, { id: '4emk4fo00de4tmud48bhi3bna1', user: '9079e9837b43ce4fc1096a70bf2325fb', avatar: 'av_5385561e94aba.jpg', alias: 'Pablo Pizarro R.' } );
} );
</script>



<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-101878-7']);
_gaq.push(['_setDomainName', 'www.u-cursos.cl']);
_gaq.push(['_trackPageview']);
_gaq.push(['_setCustomVar', 1, 'movil', '0' ]);
</script>
<script type="text/javascript" src="https://www.u-cursos.cl/d/js/ga.js"></script>

<script type="text/javascript">
Event.onReady( function() {
    notificacion.init( { server: 'https://static.u-cursos.cl', port: 54322, token: '4emk4fo00de4tmud48bhi3bna1', url: 'https://www.u-cursos.cl', webkit: true } );
} );
</script>

</body>
</html>

"""