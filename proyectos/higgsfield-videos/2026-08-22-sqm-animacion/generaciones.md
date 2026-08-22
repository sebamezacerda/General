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
