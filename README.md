# Gnist 2022 - Hittegods

## Set up

```bash
# Install dependencies
make install

# Run migrations
make migrate

# Create user
make createsuperuser

# Start server
make start
```

## Backups

### Windows

[Windows Scheduling](https://www.esri.com/arcgis-blog/products/product/analytics/scheduling-a-python-script-or-model-to-run-at-a-prescribed-time/)

### Linux - Crontab

```bash
crontab -e
# */10 * * * * /path/to/script
```
