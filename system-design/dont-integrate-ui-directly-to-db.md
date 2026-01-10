### Why to keep UI and DB layer seperate?

The below points explain why DB layer and UI layer should be different:
* Sanity testing is not done, as the UI directly sends request to DB
* The approach is not very optimized and can take longer time
* This exposes your database to a lot of vulnerability, SQL Injection becomes easy.
* Tight coupling of UI-DB, can cause issues during version upgrade or during database migrations.

