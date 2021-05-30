# 👀 EyeLocator


### 🔎 Que és?
Eye Locator es una eina dissenyada per facilitar l’extracció d’informació de fonts obertes i optimitzar el resultats en les búsquedes a través de motors de cerca. 
Es un programa que únicament interactua amb APIs públiques i privades. Eyelocator empra diferents API's públiques i privades per cerca informació i rellevant. 

La principal característica important d’aquesta eina es la seva facilitat d’ús, s’executa una ordre a través d’un terminal i immediatament el programa et pregunta per el terme que vols cercar. Immediatament el programari realitzarà les consultes i ens donarà resultats.

###  📝 Quines integracions utilitza?
Nom API | Tipus | Enllaç
--- | --- | ---
PSBDMP | Cercador de Filtracions | *psbdmp.ws*
Wilby | Motor de búsqueda | Wilby.me
Social Searcher   | Buscador de mencions per tot internet del terme introduït.  |   https://www.social-searcher.com
Open Corporates   | Buscador d'empreses nivell internacional   | https://opencorporates.com
Gravatar   | Busca coincidencies amb avatars |   https://es.gravatar.com
Skype Resolver  | Permet localitzar en alguns casos la IP   | https://api.c99.nl/skyperesolver?key=<key>&username=echo123
Protonmail API  | Si Proton existeix i quan es va crear   | https://api.protonmail.ch/
Shodan  |  Busca coincidències a Shodan   | shodan.io
  
### Que em permet?
 El programa permet l’extracció de la informació en format JSON per poder ser integrada a una base de dades tipus no-sql, a més a més, també permet la visualització de les dades de forma clara i precisa.

Eye Locator permet a l’analista cercar informació de forma ràpida i senzilla, amb Eye Locator s’intenta resoldre els problemes d’excés d'informació. 
  
### Requeriments
 - colorama
 - maigret (Actualment deshabilitat dins del codi)
 - json
 - requests
