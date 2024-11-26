# Poly-README

O Poly-README é uma ferramenta de linha de comando que traduz automaticamente seus arquivos README.md para vários idiomas usando o modelo GPT-4 da OpenAI.

## Funcionalidades

- Tradução automática de arquivos README.md
- Suporte para múltiplos idiomas de destino
- Interface simples de linha de comando
- Mantém a formatação markdown
- Utiliza o GPT-4 da OpenAI para traduções de alta qualidade
- Gerenciamento seguro de chave API usando keyring do sistema
- Configuração a nível de projeto usando YAML
- Indicador de progresso durante a tradução
- Suporte para padrões personalizados de nome de arquivo de saída

## Instalação

```bash
pip install poly-readme
```

## Pré-requisitos

Antes de usar o Poly-README, você precisa de:

1. Uma chave API da OpenAI
2. Selecione uma das opções:
   - Configure sua chave API da OpenAI como uma variável de ambiente:
     ```bash
     export OPENAI_API_KEY='sua-chave-api-aqui'
     ```
   - Ou instale-a de forma segura usando o CLI:
     ```bash
     poly-readme install
     ```

## Uso

### Configuração Inicial

Configure as definições do seu projeto:

```bash
poly-readme setup
```

Isso irá guiá-lo sobre:

- Definir a localização do arquivo README de origem
- Selecionar idiomas de destino para tradução
- Configurar o padrão de nome de arquivo de saída

### Tradução

Traduza seu README de acordo com a configuração do seu projeto:

```bash
poly-readme translate
```

### Códigos de Idiomas Disponíveis

- `ko`: Coreano
- `ja`: Japonês
- `zh`: Chinês Simplificado
- `es`: Espanhol
- `fr`: Francês
- `de`: Alemão
- `it`: Italiano
- `pt`: Português
- `ru`: Russo
- `ar`: Árabe
- `vi`: Vietnamita

Os arquivos traduzidos serão salvos de acordo com o padrão configurado (padrão: `README_{lang}.md`).

## Comandos

- `poly-readme install` - Configurar chave API da OpenAI
- `poly-readme setup` - Configurar definições de projeto
- `poly-readme translate` - Traduzir arquivos README
- `poly-readme help [command]` - Mostrar informações de ajuda

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Autor

- Chad Lee
- Email: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Agradecimentos

- Esta ferramenta usa o modelo GPT-4 da OpenAI para traduções.