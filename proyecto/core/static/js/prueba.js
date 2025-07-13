if ('webkitSpeechRecognition' in window) {
    var recognition = new webkitSpeechRecognition();

    recognition.onresult = function(event) {
        var resultado = event.results[0][0].transcript;
        if (resultado.toLowerCase() === 'iniciar') {
            //   URL para iniciar y redirige al usuario a navegacion2
            var navegacionLink = document.getElementById('navegacion-link');
            var href = navegacionLink.getAttribute('href');
            window.location.href = href;
        } else if (resultado.toLowerCase() === 'continuar') {
            //  URL para continuar y redirige al usuario a navegacion
            var navegacionLink = document.getElementById('navegacion-link2');
            var href = navegacionLink.getAttribute('href');
            window.location.href = href;
        }
    };

    recognition.start();
} else {
    alert('Tu navegador no es compatible con el reconocimiento de voz.');
}



// Función para leer un mensaje por voz
function leerMensajePorVoz(mensaje) {
    // Verificar si el navegador es compatible con la síntesis de voz
    if ('speechSynthesis' in window) {
        var synthesis = window.speechSynthesis;
        var speechMsg = new SpeechSynthesisUtterance(mensaje);

        // Configurar opciones de la voz
        speechMsg.lang = 'es-ES'; // Configura el idioma 

        // Leer el mensaje por voz
        synthesis.speak(speechMsg);
    } else {
        alert('Tu navegador no es compatible con la síntesis de voz.');
    }
}

window.onload = function() {
    // Comprobar si la URL actual corresponde a la página específica donde se desea leer el mensaje
    if (window.location.pathname.indexOf("/navegacion2") !== -1) {
        // leer por voz en la página específica
        var mensaje = "¡Bienvenido a la página de navegación! Aquí, tú estás al mando. Puedes pausar la navegación diciendo simplemente 'pausar la navegación'. Cuando estés listo para continuar, solo necesitas decir 'continuar la navegación'. Si prefieres dar por concluida la navegación, utiliza 'terminar la navegación'. ¿Necesitas más detalles sobre tu viaje? Solo pide 'información'. ¡Disfruta de tu experiencia!";
        // Llamar a la función para leer el mensaje por voz
        leerMensajePorVoz(mensaje);
    } else if (window.location.pathname.indexOf("/navegacion") !== -1) {
         // leer por voz en la página específica
        var otroMensaje = "¡Bienvenido a nuestra página de tutoriales! Estamos encantados de ayudarte a través de comandos de voz para que tengas la mejor experiencia posible. Aquí te presentamos algunos comandos clave que puedes utilizar:Para regresar a la página de inicio, simplemente di 'volver a inicio'.Si deseas iniciar la navegación, usa el comando 'iniciar'.Para pausar la navegación en cualquier momento, di 'pausar la navegación'. Para finalizar la navegación, solo menciona 'terminar la navegación'.Si quieres continuar la navegación, utiliza 'continuar navegación'.Si necesitas información adicional, simplemente di 'información'.Para retroceder a la página de tutoriales, utiliza 'volver a navegación'.";
        leerMensajePorVoz(otroMensaje);
    } else if (window.location.pathname.indexOf("/iniciousuario") !== -1) {
         // leer por voz en la página específica
        var mensajeNavegacion2= "Estamos desarrollando un dispositivo especialmente diseñado para ayudarle en sus desplazamientos hacia lugares específicos. Este dispositivo utiliza la tecnología GPS para proporcionarle indicaciones precisas sobre la ruta que debes seguir. Además, se complementa con unos auriculares que le guiarán detalladamente y le alertarán sobre posibles riesgos en el camino, lo que le permitirá desplazarte de manera más segura y autónoma. Además de estas funciones principales, el dispositivo también se conecta a una aplicación web que tus familiares o cuidadores pueden usar para supervisar en tiempo real el progreso durante el viaje. Esta aplicación almacena información sobre los lugares que visita con frecuencia y evalúa posibles riesgos en la ruta. Con estos datos, el sistema selecciona automáticamente la ruta más segura para ti, lo que optimiza tu seguridad y autonomía en sus desplazamientos. diga continuar para poder ir a la siguiente página";
        leerMensajePorVoz(mensajeNavegacion2);
    } else {
        // Si ninguna de las condiciones anteriores se cumple, se muestra un mensaje genérico
        var mensajeGenerico = "Estás en una página diferente.";
        leerMensajePorVoz(mensajeGenerico);
    }
};


// Función para configurar el reconocimiento de voz
// Función para configurar el reconocimiento de voz
function configurarReconocimientoDeVoz() {
    if ('webkitSpeechRecognition' in window) {
        var recognition = new webkitSpeechRecognition();

        recognition.onresult = function(event) {
            var resultado = event.results[0][0].transcript;
            if (resultado.toLowerCase() === 'iniciar') {
                // URL para iniciar y redirige al usuario a navegacion2
                var navegacionLink = document.getElementById('navegacion-link');
                var href = navegacionLink.getAttribute('href');
                window.location.href = href;
            } else if (resultado.toLowerCase() === 'continuar') {
                // URL para continuar y redirige al usuario a navegacion
                var navegacionLink = document.getElementById('navegacion-link2');
                var href = navegacionLink.getAttribute('href');
                window.location.href = href;
            } else if (resultado.toLowerCase() === 'volver a inicio') {
                // URL para volver al inicio y redirige al usuario
                var navegacionLink = document.getElementById('navegacion-link3');
                var href = navegacionLink.getAttribute('href');
                window.location.href = href;
            } else if (resultado.toLowerCase() === 'volver a navegación') {
                // URL para volver al inicio y redirige al usuario
                var navegacionLink = document.getElementById('navegacion-link4');
                var href = navegacionLink.getAttribute('href');
                window.location.href = href;
            } else if (resultado.toLowerCase() === 'pausar la navegación') {
                // Respuesta al comando "pausar el sistema"
                leerMensajePorVoz(' la navegación se ha pausado'); // Responde "Listo"
                // No se realiza ninguna otra acción aquí para no detener la grabación de voz
            }
            else if (resultado.toLowerCase() === 'continuar la navegación') {
                // Respuesta al comando "pausar el sistema"
                leerMensajePorVoz(' Hemos retomado la navegación '); // Responde "Listo"
                // No se realiza ninguna otra acción aquí para no detener la grabación de voz
            }
            else if (resultado.toLowerCase() === 'terminar la navegación') {
                // Respuesta al comando "pausar el sistema"
                leerMensajePorVoz(' La navegacion a finalizado '); // Responde "Listo"
                // No se realizaninguna otra acción aquí para no detener la grabación de voz
            } else if (resultado.toLowerCase() === 'información') {
                // Respuesta al comando "pausar el sistema"
                leerMensajePorVoz('Mostrando informacion '); // Responde "Listo"
                //No se realizaninguna otra acción aquí para no detener la grabación de voz
            }

            // Reinicia el reconocimiento después de un comando
            recognition.start();
        };

        recognition.onend = function() {
            // Reinicia el reconocimiento si se detiene
            recognition.start();
        };

        recognition.start();
    } else {
        alert('Tu navegador no es compatible con el reconocimiento de voz.');
    }
}

// Llama a la función de configuración del reconocimiento de voz
configurarReconocimientoDeVoz();
