# Unified Async LLM Client

## Características

- Cliente asíncrono (`async/await`)
- Streaming de respuestas
- Validación de datos con Pydantic
- Clase base abstracta para unificar la interfaz de los proveedores
- Implementación de clientes para distintos proveedores (Gemini y DeepSeek a traves de OpenRouter)

## Estructura del proyecto

```
.
├── clients/
│   ├── base.py
│   ├── gemini_client.py
│   └── openrouter_client.py
├── schemas.py
├── main.py
├── .env.example
└── config.py
```

## Instalación

1. Clonar el repositorio.

2. Instalar las dependencias:

```bash
pip install google-genai openai pydantic
```

3. Crear un archivo `.env` a partir de `.env.example` y completar las API Keys correspondientes.

## Variables de entorno

Ejemplo:

```env
OPENAI_API_KEY=tu_api_key
ANTHROPIC_API_KEY=tu_api_key
```

## Ejecutar

```bash
python main.py
```

El programa realiza una consulta de ejemplo utilizando:

- Generación normal
- Generación en streaming

## Tecnologías utilizadas

- Python 3.13.14
- Pydantic
- Gemini SDK
- OpenRouter SDK
