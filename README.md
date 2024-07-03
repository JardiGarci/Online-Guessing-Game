### Reporte de Desarrollo del Juego de Adivinanzas en Red

#### Introducción

El objetivo de este proyecto fue desarrollar un juego de adivinanzas en red utilizando sockets en Python. El juego consiste en un servidor que selecciona una palabra al azar y la envía a los clientes. Los clientes intentan adivinar la palabra enviando sus intentos al servidor, que proporciona pistas y lleva un registro de las puntuaciones de los jugadores. El juego continúa hasta que un jugador adivine la palabra correcta.

#### Desarrollo del Proyecto

##### 1. Configuración del Entorno
Para desarrollar esta solución, se utilizó Python 3, aprovechando las bibliotecas `socket` y `threading` para la comunicación en red y la gestión de múltiples clientes, respectivamente.

##### 2. Implementación del Servidor

El código del servidor se encarga de:

- Seleccionar una palabra al azar de una lista predefinida.
- Esperar conexiones de clientes.
- Recibir intentos de los clientes.
- Proporcionar pistas basadas en los intentos.
- Mantener un registro de las puntuaciones de los jugadores.


##### 3. Implementación del Cliente

El código del cliente se encarga de:

- Conectarse al servidor.
- Enviar intentos de adivinanza.
- Recibir pistas y resultados del servidor.


#### Ejecución y Evidencia

##### Ejecución del Servidor
![Servidor en Ejecución](path/to/server_screenshot.png)

##### Ejecución del Cliente
![Cliente en Ejecución](path/to/client_screenshot.png)

#### Conclusiones

El juego de adivinanzas en red se implementó con éxito utilizando sockets en Python. La estructura modular del código permite manejar múltiples clientes de manera concurrente, proporcionando una experiencia de juego fluida. Este proyecto no solo refuerza el conocimiento en programación de redes, sino que también demuestra el uso efectivo de las bibliotecas `socket` y `threading` para desarrollar aplicaciones interactivas.

#### Código en GitHub
El código completo del proyecto puede ser revisado en el siguiente enlace de GitHub:
[Repositorio GitHub](https://github.com/JardiGarci/Proped-utico-de-Programaci-n/tree/main)

#### Referencias

- Comer, D. E. (2000). *Internetworking with TCP/IP Volume One* (4th ed.). Prentice Hall.
- Stevens, W. R., Fenner, B., & Rudoff, A. M. (2004). *UNIX Network Programming Volume 1: The Sockets Networking API* (3rd ed.). Addison-Wesley.

Estos textos proporcionan una comprensión profunda de la programación de redes y la API de sockets en el contexto de UNIX, que es aplicable a la programación de sockets en Python.

---

¿Necesitas ayuda adicional con la elaboración del reporte o algún otro aspecto del proyecto?
