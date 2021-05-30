# Anàlisi
## Estat de l'art

La globalització d’Internet i el fàcil accés a aquest permeten que qualsevol persona des de qualsevol punt del món tingui al seu abast una quantitat ingent de informació, les tècniques OSINT, i les eines derivades, s’aprofiten d’aquestes característiques i permeten extreure informació d’un objectiu de forma fàcil. 

En referència a les eines per dur a terme investigacions OSINT, actualment n'existeix un ampli espectre que permeten la realització d’investigacions a través de fonts obertes, algunes de pagament i altres no, com és evident les eines que proporcionen una informació més precisa i certera són de pagament, tot i això existeixen alternatives força potents i útils. 

Actualment existeixen moltes eines diferents que presenten solucions molt diverses, segons un article publicat a "derecho de la red" (2) les eines mes utilitzades pels investigadors OSINT son:

1. **Shodan:** Segons el mateix article, shodan es un motor de búsqueda que permet localitzar casi tots els dispositius conectats a Internet. Shodan es un servei que presenta una versió gratuita pero presenta moltes restriccions. Un valor afegit que presenta aquest recurs es que mostra les vulnerabilitats, si les detecta, que presenten els equips localitzats.
2. **TheHarvester:** Harvesters una eina que s'executa a través de la línea de comandes, permet obtenir molta informació a la web d'un objectiu. Aquest programa presenta dues funcionalitats de búsqueda, la pasiva i l'activa. La pasiva no interactua en cap moment amb l'objectiu i solament obtindrà informació dels seus motors de búsqueda. La búsqueda activa te més possibilitats d'obtenir informació de més qualitat ja que aquest actua directament contra l'objectiu i interactua amb ell.

4. **Maltego:** Maltego es un programa d'anàlisi de xarxa que permet l'obtenció d'informació de qualsevol tipus de font. A més a més permet la integració d'altres mòduls que proporcionen informació enriquida. Maltego presenta una llicència de forma gratuita amb certes limitacions, tot i que a la pràctica no es nota tant

5. **Spiderfoot:** Segons la pàgina web de Spiderfoot(3), aquesta és una eina que integra quasi tot el programari i API's que s'utilitzen en OSINT. Defineixen al programa com un Framework que automatitza tot el procés i mostra la informació de forma clara i detallada. Tot i així es destaca que moltes de les API's utilitzades són de pagament o tenen un període de prova.

7. **Intelx.io:** Segons la pàgina web de Intelx.io (4),  aquest recurs es un motor de búsqueda de filtracions, es a dir, aquesta eina proporciona tota la informació relacionada, que s'hagi detectat en filtracions, sobre l'objectiu desitjat. Es destaca que presenta una opció gratuita però amb els resultats extremament limitats.

Es de recalcar la gran quantitat d'eines d'OSINT que actualment es troben per Internet, però no tota la feina la pot fer una màquina o un programa. Segons un informe desclassificat de l’Agència Central d’Intel·ligència(5) les tècniques OSINT presenten dos grans inconvenients:

- Elevada quantitat d’informació i poca capacitat de processar-la per generar intel·ligència. Els cercadors habituals poden arribar a proporcionar milers de resultats i no sempre aquests son acertats fent així molt difícil la tasca de l’analista.

- Credibilitat de la font, com he esmentat abans, tothom pot accedir a Internet i per tant tothom pot publicar informació fent així que la validació d’aquesta sigui difícil. 


El document abans esmentat recalca un dels principals problemes de l'OSINT, la falta d’una eina o un framework que agrupi tot un seguit de recursos que permetin l’obtenció, l’anàlisi i l’emmagatzamatge d’informació.

Actualment aquests problemes es solucionen a través de l'ús de més d'un programa per obtenir, analitzar i processar la informació abans d'elaborar el producte final. Tot hi això, a través de l'experiència adquirida a les pràctiques, he pogut constatar que existeix una tendència molt favorable a l'ús de tècniques d'anàlisi de xarxes per solucionar el problema de l'excés d'informació.

En contra posició no tot allò relacionat amb l'OSINT presenta problemes, segons un treball publicat per la Universitat de la Rioja (6),  l’obtenció d’intel·ligència sempre ha sigut un problema de seguretat operativa i personal per l’agent que la recol·lectava, les tècniques d'OSINT presenten la possibilitat de disminuir considerablement aquest risc i a més a més també presenta els següents avantatges:

- Rendibilitat, amb recursos molt limitats pots accedir a una gran quantitat d’informació.

- Nuls problemes legals, ja que tota la informació és pública no s’està cometent cap delicte a l’accedir a aquesta informació.



## Expectatives d'ús

Totes les eines dissenyades en aquest projecte estan enfocades a ser utilitzades amb l’objectiu de proporcionar un avantatge als cossos de seguretat, forces de l'estat i tota aquella organització que així ho requereixi. 

Les eines també podran ser utilitzades per professionals civils com ara investigadors privats, detectius, analistes d'intel·ligència, departament de recursos humans, asseguradores i tots aquells sectors professionals que requereixin obtenir informació per dur a terme les seves tasques.

Aquest conjunt d’eines, actualment, s’estan utilitzant de forma regular per empreses importants del sector de la ciberseguretat, mostrant la seva aplicació al món laboral i l’ús d’aquestes. 

## Requeriments
Per dur a terme la creació de les eines es necessiten els següents programaris:
- ``Python >= 3.6``
- ``Sublime``
- ``Tokens API Telegram``
- ``Servidor amb SO Linux``


#### Bibliografia
- (1) https://www.cia.gov/readingroom/docs/DOC_0006122548.pdf 
- (2) https://derechodelared.com/herramientas-osint-recopilatorio/
- (3) https://www.spiderfoot.net
- (4) https://intelx.io/about
- (5) https://www.cia.gov/readingroom/docs/DOC_0006122548.pdf
- (6) https://reunir.unir.net/bitstream/handle/123456789/10652/Angulo%20Vidal%2c%20Alcides%20Augusto.pdf?sequence=1&isAllowed=y

