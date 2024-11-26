# Poly-README

Poly-README ist ein Kommandozeilenwerkzeug, das Ihre README.md-Dateien mithilfe von OpenAI's GPT-4-Modell automatisch in mehrere Sprachen übersetzt.

## Funktionen

- Automatische Übersetzung von README.md-Dateien
- Unterstützung für mehrere Zielsprachen
- Einfache Kommandozeilenschnittstelle
- Beibehaltung der Markdown-Formatierung
- Nutzung von OpenAI's GPT-4 für hochwertige Übersetzungen
- Sichere Verwaltung des API-Schlüssels mit dem Systemschlüsselbund
- Projektbezogene Konfiguration mit YAML
- Fortschrittsanzeige während der Übersetzung
- Unterstützung für benutzerdefinierte Ausgabedateinamenmuster

## Installation

```bash
pip install poly-readme
```

## Voraussetzungen

Bevor Sie Poly-README verwenden können, müssen Sie:

1. Einen OpenAI API-Schlüssel besitzen
2. Entweder:
   - Ihren OpenAI API-Schlüssel als Umgebungsvariable setzen:
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - Oder ihn sicher mittels der CLI installieren:
     ```bash
     poly-readme install
     ```

## Verwendung

### Ersteinrichtung

Konfigurieren Sie Ihre Projekteinstellungen:

```bash
poly-readme setup
```

Dies führt Sie durch:

- Festlegen des Speicherorts der Quell-README-Datei
- Auswahl der Zielsprachen für die Übersetzung
- Konfiguration des Ausgabedateinamensmusters

### Übersetzung

Übersetzen Sie Ihr README entsprechend Ihrer Projektkonfiguration:

```bash
poly-readme translate
```

### Verfügbare Sprachcodes

- `ko`: Koreanisch
- `ja`: Japanisch
- `zh`: Chinesisch (Vereinfacht)
- `es`: Spanisch
- `fr`: Französisch
- `de`: Deutsch
- `it`: Italienisch
- `pt`: Portugiesisch
- `ru`: Russisch
- `ar`: Arabisch
- `vi`: Vietnamesisch

Die übersetzten Dateien werden entsprechend Ihrem konfigurierten Muster gespeichert (Standard: `README_{lang}.md`).

## Befehle

- `poly-readme install` - OpenAI-API-Schlüssel konfigurieren
- `poly-readme setup` - Projekteinstellungen konfigurieren
- `poly-readme translate` - README-Dateien übersetzen
- `poly-readme help [command]` - Hilfsinformationen anzeigen

## Mitwirken

Beiträge sind willkommen! Bitte zögern Sie nicht, einen Pull Request einzureichen.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die LICENSE-Datei für Details.

## Autor

- Chad Lee
- E-Mail: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Danksagungen

- Dieses Tool nutzt das GPT-4-Modell von OpenAI für Übersetzungen.