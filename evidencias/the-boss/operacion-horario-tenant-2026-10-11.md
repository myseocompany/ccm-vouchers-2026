# Horario cargado en el tenant — The Boss

- **Fecha:** 2026-10-11.
- **Tenant:** The Boss (`01a12179-0c6e-70d2-9694-d11125bc3295`), zona `America/Bogota`.
- **Fuente:** caracterización diligenciada (martes–jueves 6–10 p. m.; viernes–domingo 5–10 p. m.) y mensaje de bienvenida actual del negocio: «Hola bienvenidos a the boss burger. En un momento te atenderemos. Los días Lunes no tenemos Servicio».
- **Cargado en `tenants.business_hours` (SSH, verificado por lectura):**
  - Lunes: cerrado (`enabled: false`).
  - Martes, miércoles, jueves: 18:00–22:00.
  - Viernes, sábado, domingo: 17:00–22:00.
- **No configurado:** festivos (`respect_holidays` false, `holiday_hours` vacío); no hay información del cliente sobre festivos.
- **Alcance:** horario general del tenant, no por sede. No acredita que el negocio esté abierto en tiempo real.
