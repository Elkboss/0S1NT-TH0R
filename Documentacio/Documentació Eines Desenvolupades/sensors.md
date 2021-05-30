# 🕵️ Sensors {CI} (Tècnica)

La tècnica explicada aquí sorgeix de la necessitat de detectar futurs ciberatacs, investigacions externes dirigides cap a la organització client i altres tipus d’amenaces. 
### 🔍 Que és?
Aquesta tècnica es basa en el desplegament de Honeypots tipus IPLogger integrats en medis d'interès de l’atacant amb l’objectiu que aquest sigui captat pel nostre sistema. 

### 🎯 Objectius?
- Detecció temprana d'amenaces.
- Esdevenir una eina pro-activa.
- Proporcionar indicadors per generar intel·ligència.

### 🧪 Desplegament
Per desplegar la infraestructura necessitarem els següents recursos:
- Determinar els criteris que poden cridar la atenció de l’atacant.
- Capacitat de publicar el honeypot i posicionar-lo correctament.
- Disposar d'un HoneyPot, en el nostre cas utilitzarem (https://grabify.link) (1)
- Monitorització del HoneyPot, per tal de que ens arribi la alerta cada vegada que es detecti un intrús utilitzarem la API de Grabify.

Els criteris que poden despertar l’atenció de l’atacant son tots aquells que contenen informació confidencial, contrasenyes, informació personal, correus i fotografies.

Un recurs molt utilitzat per publicar aquestes infraestructures es Pastebin (2.

### Altre informació rellevant
Es poden incluir hashtags i paraules clau per posicionar millor el Honeypot un cop aquest sigui publicat.

Per obtenir l’enllaç simplement introduirem qualsevol link a la pàgina web de Grabify i automàticament ens mostrarà un menú d’opcions on podrem configurar el nostre Honeypot, permet modificar l’enllaç de forma que no sigui sospitós.

Per publicar el Honeypot utilitzarem Pastebin però es pot publicar en qualsevol altre plataforma que indexi automàticament a Google.


### Bibliografía
- (1) https://grabify.link
- (2) wwww.pastebin.com
