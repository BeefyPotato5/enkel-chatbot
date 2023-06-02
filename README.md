# enkel-chatbot
hvordan man lager en enkel ChatBot som kan jøre enkel matte og fortelle deg datoen.

dette er en veldig enkel "Chatbot" som ikke egentlig er AI. den kan gjøre enkel matte, det vil si pluss, minus, dele, og gange. den kan også fortelle dato og klokke, det vil si at den kan fortelle datoen veldig nøyaktig som nøyaktig klokkeslett, måned, ukedag, ukenummer, år, osv.

chatboten funker med datetime modulen og python sin innebygde matte funksjon. jeg har også brukt random modulen for noen spørsmål for å få den til å være litt mer opmerksomhetsfangende i motsetning til om den bare svarer nøyaktig samme svar til samme spørsmål

først og fremst trenger du Python lastet ned.
du må importere "datetime" modulen og "random" modulen. disse importeres ved å skrive "import datetime" for datetime modulen, og en linje under skrive "import random" for random modulen

den er stor set bygd opp av input() komandoer og if, elif, og else komandoer for å få den til å svare ulike ting for ulike spørsmål. jeg valgte å bruke denne metoden i stedet for OpenAI sin custom chatbot funksjon, siden jeg fant ut i forbindelse med prosjektet i forige uke av at det koster penger og du trenger å instalere masse ting for å kunne bruke den. og alle andre muligheter var litt vor avanserte og tungvintde.


liste over koder til datetime modulen med eksempler
kode	  forklarng         eksempel

%a	Weekday, short version  	              Wed	
%A	Weekday, full version	                  Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	  3	
%d	Day of month 01-31	                    31	
%b	Month name, short version	              Dec	
%B	Month name, full version	              December	
%m	Month as a number 01-12	                12	
%y	Year, short version, without century	  18	
%Y	Year, full version	                    2018	
%H	Hour 00-23	                            17	
%I	Hour 00-12	                            05	
%p	AM/PM	                                  PM	
%M	Minute 00-59	                          41	
%S	Second 00-59	                          08	
%f	Microsecond 000000-999999	              548513	
%z	UTC offset	                            +0100	
%Z	Timezone	                              CST	
%j	Day number of year 001-366	            365	
%U	Week number, Sunday first day of week, 00-53	52	
%W	Week number, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
