(fin-edu:assets:futures)=
# Futures

**Def.** Contratti standardizzati, con scadenza (obbligo di scambio, non diritto come le **opzioni**), su sottostanti che possono essere indici azionari, materie prime, o altri indici. Possono essere comprati o venduti su un determinato sottostante, avendo una posizione rialzista o ribassista su di esso. Possono quindi essere usati per speculazione o come hedging. Si scambiano in lotti. Esistono contratti che hanno moltiplicatori diversi: ogni punto di indice corrisponde a diversi valori (es. FIB: 5 Euro, miniFIB: 1 Euro, microFIB: 0.20 Euro). Mercati sempre aperti, da luendì a venerdì. **Molto liquidi**.

**Leva.** "Sui futures la leva non si paga, è implicita". **(?)**

**Commisisoni** per ogni lotto. FIB 6.95, mini 3.95, micro: 2.95

**Mark-to-market e tassazione.** Settlement di giornata anche su posizioni multiday: serve la liquidità sul c/c per garantire il settlement monetario a fine giornata. Le tasse vengono pagate in caso di plusvalenza (26%) quando la posizione viene chiusa; è possibile compensazione minus.

**Dati minimi scheda**: ISIN; moltiplicatore: valore di ogni punto (es. FTSE MIB: 5); tick: movimento minimo dell'indice (es. FTSE MIB: 5 punti); valore tick: 5 punti $\times$ moltiplicatore $=$ ogni tick muove il FIB di 25 Euro ;

```{prf:example} Esempio di acquisto FIB

Ordine acquisto/vendita: esempio con **FIB**, con indice a 28500, tick 5, moltiplicatore 5; ordine minimo corrispondente a 142500 Euro; operatività intraday; margine minimo intraday: 2.5%; margine minimo overnight: 7%; margine in Euro: 3662 Euro (quanto si deve avere sul PTF)

**Operatività:** 
- intraday, margine da 2.5 a 6.5% (più margine si mette, più si allontanta lo SL da 1 a 5%)
- multiday, margine maggiore (da 7 a 30%) 
- intraday 1% (Fineco permette di andare a leva 100; SL: posizione chisa con un ribasso del .5%).

```


```{prf:example} Confronto FIB, miniFIB, microFIB

FIB: valore tick: 25 Euro; con indice a 28500. Stima margine 3662 Euro per stima ordine 142500
miniFIB: valore tick: 5 Euro; con indice a 28500. Stima margine 712 Euro per stima ordine 28500
microFIB: valore tick: 1 Euro; con indice a 28500. Stima margine 142 Euro per stima ordine 5700

```

