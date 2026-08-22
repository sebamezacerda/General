# Bitácora de generaciones

## Configuración base (imagen)

**Modelo: `recraft_v4_1`** con `model_type: "utility"`.

Elegido porque es el único del catálogo que acepta **paleta cerrada como parámetro** en vez de
depender de que el prompt convenza al modelo:

```json
{
  "model": "recraft_v4_1",
  "model_type": "utility",
  "aspect_ratio": "16:9",
  "background_color": "#0B0F17",
  "colors": ["#0B0F17", "#151C2B", "#2456D6", "#7DA0F2", "#8A94A6", "#F5F7FA"]
}
```

`utility` está descrito por el proveedor como "cleaner, flatter, front-facing, and predictable"
— que es exactamente el "nada flota / sin sombras / ortográfico" del sistema de Velaria.
`resolution: "1k"` para validación; subir a `"2k"` en las tomas finales.

Las negaciones van dentro del prompt (Recraft no expone negative prompt): cerrar siempre con
`Absolutely no glow, no bloom, no gradient, no rounded corners, no soft shadows, no
reflections, no text, no lettering, no logos.`

## Ronda 1 — frames de validación · 2026-08-22

Tres frames que definen el arte del resto. 1344×768.

| Escena | Toma | job_id | Estado |
|---|---|---|---|
| 5 | 5.1 — la capa Velaria | `5543e2f4-f418-44ce-9f5e-8ca022c7fa11` | generado, sin auditar |
| 8 | 8.1 — dashboard | `3e43218d-d54f-4d7b-a757-d68642509532` | generado, sin auditar |
| 12 | 12.1 — el ecosistema | `a4fb4e65-5e2a-4f6c-8dab-9f9ac0e5e1c4` | generado, sin auditar |

⚠ **No pude inspeccionar estos frames**: la política de red del entorno bloquea el CDN de
Higgsfield (`d8j0ntlcm91z4.cloudfront.net` → 403 en el CONNECT del proxy). Se ven en el widget
del cliente, pero la revisión visual la tiene que hacer una persona.

### Checklist de auditoría (aplicar a cada frame)

- [ ] Fondo exactamente `#0B0F17`, sin viñeta ni degradado.
- [ ] **Un solo** elemento en azul `#2456D6` por frame.
- [ ] Cero glow, cero bloom, cero halo alrededor del azul.
- [ ] Esquinas rectas en todos los planos (0–2px).
- [ ] Sin sombras proyectadas ni sensación de elevación.
- [ ] Sin texto inventado, sin logos, sin iconos con curvas decorativas.
- [ ] Espacio vacío suficiente para los rótulos en post.

## Pendiente

- Ronda 2: el resto de las tomas, una vez aprobado el arte de la ronda 1.
- Escenas 1 y 2 llevan fotografía (faena, puerto, personas) — evaluar si `utility` sirve o si
  conviene otro modelo para esas dos, manteniendo la paleta en post.

## Ronda 2 — validación del motor de video · 2026-08-22

**Motor elegido: `cinematic_studio_video_v2`.** Es el único del catálogo con las cuatro palancas
que este video necesita: `start_image` **+** `end_image` (le doy los dos extremos del movimiento
y solo interpola), `cfg_scale` (adherencia al prompt), `speedramp: "linear"` (el sistema pide
movimientos lineales) y `sound: "off"`.

```json
{
  "model": "cinematic_studio_video_v2",
  "mode": "pro", "duration": 5, "aspect_ratio": "16:9",
  "sound": "off", "genre": "auto", "speedramp": "linear", "cfg_scale": 0.85
}
```

| Prueba | job_id | Estado |
|---|---|---|
| 5.1 — descenso lineal sobre la capa | `00cc868f-628b-4859-8619-3a1818dee471` | generado, **sin auditar** |

Igual que la ronda 1: el CDN está bloqueado por la política de red, así que la revisión visual
la tiene que hacer una persona.

### Presets: rechazar siempre

El servidor sugirió el preset viral **"IN THE DARK"** para este prompt. Se rechazó con
`declined_preset_id`. Los presets imponen un estilo propio — exactamente lo que el sistema de
Velaria prohíbe. **Ningún preset en este proyecto.**

### ⚠ Hallazgo: la resolución del video sigue a la del still

El video salió a **1344×768**, idéntico al still de origen. El modelo no reescala: hereda el
tamaño del `start_image`. Para un máster corporativo en 1080p eso no alcanza.

Dos salidas, y cambian el presupuesto:
- **Stills finales a 2k** (8 créditos c/u contra 1,25 del 1k — 6,4× más caro).
- **`upscale_video`** sobre las tomas aprobadas (costo sin medir todavía).

Recomendación: iterar en 1k, que es barato, y pagar 2k **solo en las tomas ya aprobadas**.

## Costos unitarios reales (medidos, no estimados)

| Ítem | Créditos |
|---|---:|
| Imagen Recraft 1k (1344×768) | 1,25 |
| Imagen Recraft 2k | 8 |
| Video `cinematic_studio_video_v2` pro, 5s | 7,5 |
| Video mismo modelo, std, 5s | 5 |
| Locución `seed_audio`, ~35 palabras | 1,6 |

Los de imagen salen de la diferencia de saldo antes/después; los demás, del preflight
`get_cost`.

## Presupuesto de producción

**8 tomas generativas** (1.1 faena, 1.2 puerto, 2.1 grilla, 2.2 proceso, 3.1 mapa, 5.1 capa,
5.2 los diez, 12.1 ecosistema) — las otras 13 pantallas son HTML y no cuestan créditos.

| Partida | Cálculo | Créditos |
|---|---|---:|
| Stills de iteración (1k) | 8 tomas × 1,25 × 2 intentos | 20 |
| Stills finales (2k) | 8 × 8 | 64 |
| Video pro 5s | 8 × 7,5 × 2,5 intentos | 150 |
| Locución | 424 palabras ≈ 19 cr × 1,5 intentos | 30 |
| **Total estimado** | | **≈ 265** |

Rango razonable: **150** si el arte cierra rápido, **400** si hay mucha iteración. El factor 2,5
en video no es pesimismo: dirigir arte contra un modelo generativo rara vez sale a la primera.

Saldo actual: **1.112 créditos** — sobra holgadamente, del orden de 4× el estimado.

Sin medir todavía: `upscale_video` sobre las tomas aprobadas.
