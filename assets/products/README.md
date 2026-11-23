# JPC Product Images Directory (`assets/products/`)

Place verified product images in this folder named `<SKU>.webp`, `<SKU>.jpg`, or `<SKU>.png` (for example: `FESTO-DSBC-32-100-PPVA-N3.webp` or `JPC-4V210-08-24DC.webp`).

When `python3 scripts/import-catalog.py` runs:
1. It checks `assets/products/<SKU>.(webp|jpg|png)` for each of the 500 catalog records.
2. If a verified local image file exists, `media.hasProductPhoto` is set to `true` and `media.imageUrl` points to `assets/products/<SKU>.<ext>`.
3. If no local image is present, it falls back cleanly to the category/series engineering SVG schematic (`media.fallbackSchematicType`), guaranteeing zero broken images.
