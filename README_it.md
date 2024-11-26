# Poly-README

Poly-README è uno strumento da riga di comando che traduce automaticamente i tuoi file README.md in più lingue utilizzando il modello GPT-4 di OpenAI.

## Funzionalità

- Traduzione automatica dei file README.md
- Supporto per più lingue di destinazione
- Semplice interfaccia da riga di comando
- Mantiene la formattazione Markdown
- Utilizza il GPT-4 di OpenAI per traduzioni di alta qualità
- Gestione sicura delle chiavi API tramite il portachiavi di sistema
- Configurazione a livello di progetto tramite YAML
- Indicatore di progresso durante la traduzione
- Supporto per modelli di nomi di file di output personalizzati

## Installazione

```bash
pip install poly-readme
```

## Prerequisiti

Prima di utilizzare Poly-README, è necessario:

1. Disporre di una chiave API di OpenAI
2. Effettuare una delle seguenti operazioni:
   - Impostare la chiave API di OpenAI come variabile d'ambiente:
     ```bash
     export OPENAI_API_KEY='la-tua-chiave-api-qui'
     ```
   - Oppure installarla in modo sicuro utilizzando la CLI:
     ```bash
     poly-readme install
     ```

## Utilizzo

### Configurazione Iniziale

Configura le impostazioni del tuo progetto:

```bash
poly-readme setup
```

Questo ti guiderà attraverso:

- Impostazione della posizione del file README di origine
- Selezione delle lingue di destinazione per la traduzione
- Configurazione del modello di nome file di output

### Traduzione

Traduce il tuo README secondo la configurazione del progetto:

```bash
poly-readme translate
```

### Codici Linguistici Disponibili

- `ko`: Coreano
- `ja`: Giapponese
- `zh`: Cinese Semplificato
- `es`: Spagnolo
- `fr`: Francese
- `de`: Tedesco
- `it`: Italiano
- `pt`: Portoghese
- `ru`: Russo
- `ar`: Arabo
- `vi`: Vietnamita

I file tradotti verranno salvati secondo il modello configurato (impostazione predefinita: `README_{lang}.md`).

## Comandi

- `poly-readme install` - Configura la chiave API di OpenAI
- `poly-readme setup` - Configura le impostazioni del progetto
- `poly-readme translate` - Traduce i file README
- `poly-readme help [command]` - Mostra le informazioni di aiuto

## Contributi

I contributi sono benvenuti! Non esitare a inviare una Pull Request.

## Licenza

Questo progetto è sotto licenza MIT - consulta il file LICENSE per i dettagli.

## Autore

- Chad Lee
- Email: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Ringraziamenti

- Questo strumento utilizza il modello GPT-4 di OpenAI per le traduzioni.