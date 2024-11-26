# Poly-README

Poly-README es una herramienta de línea de comandos que traduce automáticamente tus archivos README.md a múltiples idiomas usando el modelo GPT-4 de OpenAI.

## Características

- Traducción automática de archivos README.md
- Soporte para múltiples idiomas de destino
- Interfaz de línea de comandos sencilla
- Mantiene el formato markdown
- Utiliza GPT-4 de OpenAI para traducciones de alta calidad
- Gestión segura de la clave API usando el sistema de llavero
- Configuración a nivel de proyecto usando YAML
- Indicador de progreso durante la traducción
- Soporte para patrones personalizados de nombres de archivo de salida

## Instalación

```bash
pip install poly-readme
```

## Prerrequisitos

Antes de usar Poly-README, necesitas:

1. Tener una clave de API de OpenAI
2. Ya sea:
   - Configurar tu clave de API de OpenAI como una variable de entorno:
     ```bash
     export OPENAI_API_KEY='tu-clave-api-aquí'
     ```
   - O instalarla de forma segura usando la CLI:
     ```bash
     poly-readme install
     ```

## Uso

### Configuración Inicial

Configura los ajustes de tu proyecto:

```bash
poly-readme setup
```

Esto te guiará a través de:

- Configurar la ubicación del archivo fuente README
- Seleccionar idiomas de destino para la traducción
- Configurar el patrón de nombre de archivo de salida

### Traducción

Traduce tu README de acuerdo a la configuración de tu proyecto:

```bash
poly-readme translate
```

### Códigos de Idioma Disponibles

- `ko`: Coreano
- `ja`: Japonés
- `zh`: Chino Simplificado
- `es`: Español
- `fr`: Francés
- `de`: Alemán
- `it`: Italiano
- `pt`: Portugués
- `ru`: Ruso
- `ar`: Árabe
- `vi`: Vietnamita

Los archivos traducidos se guardarán de acuerdo al patrón configurado (por defecto: `README_{lang}.md`).

## Comandos

- `poly-readme install` - Configurar la clave de API de OpenAI
- `poly-readme setup` - Configurar ajustes del proyecto
- `poly-readme translate` - Traducir archivos README
- `poly-readme help [command]` - Mostrar información de ayuda

## Contribuciones

¡Las contribuciones son bienvenidas! No dudes en enviar un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Autor

- Chad Lee
- Correo electrónico: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Agradecimientos

- Esta herramienta utiliza el modelo GPT-4 de OpenAI para traducciones.