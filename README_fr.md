# Poly-README

Poly-README est un outil en ligne de commande qui traduit automatiquement vos fichiers README.md en plusieurs langues en utilisant le modèle GPT-4 d'OpenAI.

## Fonctionnalités

- Traduction automatique des fichiers README.md
- Support pour plusieurs langues cibles
- Interface simple en ligne de commande
- Maintien de la mise en forme Markdown
- Utilise GPT-4 d'OpenAI pour des traductions de haute qualité
- Gestion sécurisée des clés API via le trousseau de clés système
- Configuration au niveau du projet utilisant YAML
- Indicateur de progression pendant la traduction
- Support pour des motifs de nom de fichier de sortie personnalisés

## Installation

```bash
pip install poly-readme
```

## Prérequis

Avant d'utiliser Poly-README, vous devez :

1. Avoir une clé API OpenAI
2. Soit :
   - Définir votre clé API OpenAI comme une variable d'environnement :
     ```bash
     export OPENAI_API_KEY='votre-clé-api-ici'
     ```
   - Ou l'installer en toute sécurité via la CLI :
     ```bash
     poly-readme install
     ```

## Utilisation

### Configuration Initiale

Configurez les paramètres de votre projet :

```bash
poly-readme setup
```

Cela vous guidera à travers :

- La configuration de l'emplacement du fichier README source
- La sélection des langues cibles pour la traduction
- La configuration du motif du nom de fichier de sortie

### Traduction

Traduisez votre README selon la configuration de votre projet :

```bash
poly-readme translate
```

### Codes de Langue Disponibles

- `ko`: Coréen
- `ja`: Japonais
- `zh`: Chinois Simplifié
- `es`: Espagnol
- `fr`: Français
- `de`: Allemand
- `it`: Italien
- `pt`: Portugais
- `ru`: Russe
- `ar`: Arabe
- `vi`: Vietnamien

Les fichiers traduits seront enregistrés selon votre motif configuré (par défaut : `README_{lang}.md`).

## Commandes

- `poly-readme install` - Configurer la clé API OpenAI
- `poly-readme setup` - Configurer les paramètres du projet
- `poly-readme translate` - Traduire les fichiers README
- `poly-readme help [command]` - Afficher les informations d'aide

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## Auteur

- Chad Lee
- Email : think.bicycle@gmail.com
- GitHub : [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Remerciements

- Cet outil utilise le modèle GPT-4 d'OpenAI pour les traductions.