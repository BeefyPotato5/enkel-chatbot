# enkel-chatbot
hvordan man lager en enkel ChatBot som kan jøre enkel matte og fortelle deg datoen.

dette er en veldig enkel "Chatbot" som ikke egentlig er AI. den kan gjøre enkel matte, det vil si pluss, minus, dele, og gange. den kan også fortelle dato og klokke, det vil si at den kan fortelle datoen veldig nøyaktig som nøyaktig klokkeslett, måned, ukedag, ukenummer, år, osv.

chatboten funker med datetime modulen og python sin innebygde matte funksjon. jeg har også brukt random modulen for noen spørsmål for å få den til å være litt mer opmerksomhetsfangende i motsetning til om den bare svarer nøyaktig samme svar til samme spørsmål

først og fremst trenger du Python lastet ned.
du må importere "datetime" modulen og "random" modulen. disse importeres ved å skrive "import datetime" for datetime modulen, og en linje under skrive "import random" for random modulen

den er stor set bygd opp av input() komandoer og if, elif, og else komandoer for å få den til å svare ulike ting for ulike spørsmål. jeg valgte å bruke denne metoden i stedet for OpenAI sin custom chatbot funksjon, siden jeg fant ut i forbindelse med prosjektet i forige uke av at det koster penger og du trenger å instalere masse ting for å kunne bruke den. og alle andre muligheter var litt vor avanserte og tungvintde.
