# Centro de Comando / Command Center

Esta carpeta centraliza la configuración del plano de control para que
la app pueda renderizar un panel de configuraciones desde una fuente única de verdad.
This folder centralizes the control-plane configuration so the app can
render a configuration dashboard from a single source of truth.

## Contenido / Contents

- **master_switch.py**: el interruptor global (kill-switch). / the global kill-switch toggle.
- **endpoints.py**: catálogo de endpoints para exponer en el panel de control. / catalog of endpoints to expose in the control panel.
- **rules_config.py**: primitivas de configuración de reglas. / rule configuration primitives.
- **settings.py**: objeto de nivel superior que agrega todos los datos configurables. / top-level object aggregating all configurable data.

## Próximos pasos / Next steps

- Conectar `CommandCenterSettings` con la capa API para que la UI lea los valores. / Wire `CommandCenterSettings` into the API layer so the UI can read the values.
- Agregar persistencia (base de datos o archivo) si la configuración debe ser mutable. / Add persistence (database or file-backed) if the settings need to be mutable.
