# Documento de Seguridad y Recomendaciones de IA

**Nombre del estudiante:** Fernando Isla  
**Asignatura:** Programación Back End  
**Evaluación:** Evaluación Sumativa 3  

---

### (a) Prompt utilizado

Le pedí a la IA lo siguiente:

> "Hola, tengo una API hecha en Django REST Framework para un centro médico que guarda datos de pacientes (RUN, nombre, apellido, correo y fecha de nacimiento). Uso MySQL y JWT con SimpleJWT. ¿Qué recomendaciones de seguridad me das para mejorar la API y proteger los endpoints y los datos de entrada? Por favor no pongas contraseñas reales."

---

### (b) Recomendaciones recibidas

La IA me recomendó lo siguiente:
1. No dejar contraseñas de la base de datos ni la SECRET_KEY escritas directamente en el archivo `settings.py`, sino usar variables de entorno con `.env`.
2. Validar bien los datos que ingresan los usuarios en el serializer, en especial el formato del correo y que el RUN tenga un mensaje de error claro si no cumple el formato.
3. Configurar limitación de peticiones (Throttling / Rate Limiting) para evitar que saturen el servidor con muchas peticiones seguidas o intentos de fuerza bruta al pedir tokens.
4. Ajustar los tiempos de expiración de los tokens JWT para que no duren para siempre (darle un tiempo corto al access token y rotar el refresh token).
5. Instalar una lista negra (Blacklist) en la base de datos para guardar cada token usado y bloquearlo.

---

### (c) Cuáles apliqué o descarté y por qué

- **Aplicada 1 (Variables de entorno con .env):** La apliqué porque si subo el código a GitHub o lo comparto, nadie puede ver mi contraseña de MySQL ni la clave secreta de Django.
- **Aplicada 2 (Validar formato del email y mensaje en el RUN):** La apliqué en el `serializers.py`. Agregué una validación con expresión regular para el email para asegurarme de que nadie ingrese correos inválidos, y le puse un mensaje de error claro a la validación del RUN para que el usuario sepa por qué falló si no pone el guión.
- **Aplicada 3 (Throttling / límite de peticiones):** La apliqué en `settings.py` dentro de `REST_FRAMEWORK` para limitar las peticiones por hora/día y proteger la API de sobrecarga.
- **Aplicada 4 (Tiempos de vida del token JWT):** La apliqué configurando `SIMPLE_JWT` en `settings.py` con 30 minutos para el access token y 1 día para el refresh token.
- **Descartada (Lista negra de tokens en BD):** La descarté porque requiere instalar apps adicionales de simplejwt, hacer más migraciones y meter consultas extra a la base de datos cada vez que alguien pide un token. Para el alcance de esta entrega me pareció innecesario y con la rotación de tokens ya queda bastante seguro.

---

### (d) En qué parte del código quedaron

1. **Variables de entorno:** En `islaProject/settings.py` usando `os.getenv` para la base de datos MySQL y la `SECRET_KEY`.
2. **Validación de Email y RUN:** En `fernandoApp/serializers.py`, en los métodos `validate_email` y `validate_run`.
3. **Throttling y permisos:** En `islaProject/settings.py`, dentro del diccionario `REST_FRAMEWORK` con `DEFAULT_THROTTLE_CLASSES` y `DEFAULT_THROTTLE_RATES`.
4. **Tiempos de token JWT:** En `islaProject/settings.py`, dentro del diccionario `SIMPLE_JWT` con `ACCESS_TOKEN_LIFETIME` y `REFRESH_TOKEN_LIFETIME`.
