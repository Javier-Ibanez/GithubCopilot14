# GithubCopilot14

Calculadora web interactiva con tema naranja.

## Uso en VS Code Online

Esta versión funciona en entornos virtuales sin `DISPLAY` usando un servidor HTTP simple.

### Ejecutar la calculadora web

1. Inicia el servidor local:

```bash
python3 serve.py
```

2. Abre la dirección que se muestra en la terminal, normalmente:

```bash
http://localhost:8000
```

3. Usa los botones para ingresar:
   - números `0` a `9`
   - operadores `+`, `-`, `*`, `/`
   - paréntesis `(` y `)`
   - signo `+/-`
   - `C` para borrar
   - `=` para calcular

4. Después de un resultado, si ingresas un número sin operador, la operación se reinicia automáticamente.

## Funcionalidades añadidas

- Soporte para expresiones con paréntesis.
- Botón `+/-` para cambiar el signo del número activo.
- Manejo de división por cero con mensaje de error.
- Reinicio automático tras resultado cuando se ingresa un nuevo número.
- Soporte de teclado: números, operadores, `Enter`, `Backspace` y `Escape`.

## Archivos importantes

- `web/index.html` — interfaz HTML de la calculadora.
- `web/style.css` — estilo visual naranja.
- `web/script.js` — lógica de botones, validación y evaluación.
- `serve.py` — servidor HTTP simple para servir la app web.
