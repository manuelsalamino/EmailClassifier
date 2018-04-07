Come primo passo scaricare il dataset:
 - vai su http://qwone.com/~jason/20Newsgroups/
 - scendi nella sezione 'Data'
 - scarica il secondo dataset 20news-bydate.tar.gz - 20 Newsgroups sorted by date

Dopodich�:
 - prendere la cartella scaricata
 - decomprimerla
 - mettere le due cartelle che si ottengono all'interno di una nuova cartella chiamata 'dataset' e
   posizionare quest'ultima cartella dove si hanno i file .py del programma da eseguire.

In questo modo i percorsi presenti nel codice del programma saranno validi.

I test sono stati eseguiti su questo dataset, � quindi necessaria la sua presenza.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

COME OTTENERE RISULTATI DESCRITTI
Per ottenere i risultati descritti nella relazione eseguire il modulo Exec.py nel seguente modo:

1) Scegliere la cartella del dataset che si vuole prendere come positiva

2) Impostare il percorso della cartella scelta all'interno del dataset, stando attenti a mettere nella
   variabile "trainPath" il percorso relativo alla cartella contenuta nella cartella del train ed in
   "testPath" il percorso relativo alla cartella del test

IMPORTANTE: fare attenzione che entrambi i percorsi, nel train e nel test, indichino una cartella con
            lo stesso nome (cio� email sullo stesso argomento)

3) Fare lo stesso procedimento anche per le righe di codice successive, in cui di fatto si eseguono
   le stesse operazioni per� cambiando la scelta della cartella scelta come positiva.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

COME LEGGERE L'OUTPUT
Una volta mandato in esecuzione il programma ci saranno delle stampe per aggiornare l'utente sulle
operazioni in atto, per esempio "calculating Bernoulli Matrix..." oppure "calculating hyperplane...".
Una volta eseguite tutte le operazioni e stampato a video che sono terminate viene stampato, sempre a
video, un resoconto del test effettuato, che � costituito dal nome delle cartelle e dal numero di email
calcolato come positive e negative al suo interno.
Al termine del risultato verr� stampato anche il tempo di esecuzione dell'intera operazione, in secondi.

Dopodich� verranno fatte le stesse operazioni prendendo altre classi come positiv e a video si avranno
le stesse stampe, con naturalmente il resoconto ed il tempo di esecuzione relativo a quest'ultimo test
test.


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

TEMPI DI ESECUZIONE (su computer con le seguenti caratteristiche: Intel Core i3-5005U 2.0GHz, RAM 4GB)


- primo test (classe positiva "alt.atheism")     17 minuti circa

- secondo test (classe positiva "rec.motorcycles")     17 minuti circa

- terzo test (classe positiva "sci.electronics")     16 minuti circa


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

RIFERIMENTI:

L'implementazione dell'algoritmo per le curve ROC � stato preso dal seguente indirizzo:
https://datamize.wordpress.com/2015/01/24/how-to-plot-a-roc-curve-in-scikit-learn/

L'implementazione della funzione per trovare l'iperpiano di separazione ha trovato riferimenti qu�:
http://scikit-learn.org/0.18/auto_examples/svm/plot_separating_hyperplane.html


In entrambi i casi il codice trovato pu� aver subito della variazioni o essere stato preso in parte
per motivi di necessit� ed adattamento al problema da risolvere nello specifico caso trattato.