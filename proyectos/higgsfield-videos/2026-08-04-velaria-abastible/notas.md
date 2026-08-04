# Animación VELARIA → Abastible

- Para qué negocio: VELARIA (venta del servicio a Abastible)
- Objetivo del video: que un cliente corporativo NO experto en IA entienda en ~60-90s
  qué hace VELARIA y vea con claridad el **antes** (cada persona usando IA por su
  cuenta, superficialmente, sin colaboración) y el **después** (equipo trabajando con
  IA de forma colaborativa y metódica, con resultados medibles).
- Plataforma/formato: 16:9 horizontal (reunión comercial / envío por correo). Pendiente confirmar.
- Referencias / inspiración:
  - Video de referencia del cliente: https://www.youtube.com/watch?v=AfTU_796XaM
    (análisis escena-a-escena en Higgsfield, id `7595ca4e-41de-4e44-9d79-f673546dc3e3`)
  - Tendencia 2025-26 en explainers de empresas de IA: motion graphics minimalista,
    gradientes sutiles, transiciones suaves de UI, look premium/confiable.
  - Estilo visual: debe salir del repo VELARIA y/o de las propuestas HTML
    (Abastible y SQM). PENDIENTE: acceso a esos documentos.
- Motor/flujo en Higgsfield: workflow `faceless-channel-video`, tipo **Explainer**,
  modo **Animated** (bloques de 10s), estilo propuesto **Editorial Motion Graphics**
  (el recomendado para Explainer y el que mejor calza con el look de empresas de IA).
  Voz en off en español. Pipeline: style anchor → asset roster → guion por bloques →
  generación por lotes → VO → ensamblado → upscale Topaz → entrega.
- Estado: en progreso

## Bloqueos / pendientes (para Sebastián)
1. **Repo VELARIA**: no existe `sebamezacerda/velaria` o la app de GitHub de Claude
   no tiene acceso. Falta owner/nombre exacto del repo, o copiar los docs clave a
   `proyectos/velaria/` de este repo.
2. **Propuestas HTML (Abastible y SQM)**: son archivos locales del PC de Sebastián,
   ilegibles desde el entorno remoto. Gmail requiere reautorización (token expirado).
   Opciones: subirlas a este repo, reautorizar Gmail, o pegar el contenido en el chat.
3. Confirmar duración (propuesta: 60-90s), aspecto (propuesta: 16:9) y narración
   (propuesta: voz en off en español).

## Bitácora
- 2026-08-04: Setup del proyecto. Workflow Explainer de Higgsfield estudiado completo.
  Análisis del video de referencia lanzado en Higgsfield. Guion v1 (con supuestos
  marcados) en `guion-v1.md`. Bloqueado en: contenido real de VELARIA y propuestas.
