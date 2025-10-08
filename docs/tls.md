TLS
===

This page explains how to use TLS with the ORM when connecting to ClickHouse over HTTPS, including mutual TLS (mTLS).

Requirements
------------

- Use an HTTPS `db_url` (e.g. `https://host:8443/`).
- Provide server CA bundle and optional client certificate/private key if required by your ClickHouse deployment.

Configuration Options
---------------------

You can configure TLS in two ways:

1. Constructor arguments
2. URL query parameters

Constructor Arguments
---------------------

- `verify_ssl_cert` (bool): Verify server certificate (default: `True`).
- `ca_cert` (str): Path to CA bundle file to verify the server certificate.
- `client_cert` (str): Path to client certificate file (PEM) used for mTLS.
- `client_key` (str): Path to client private key file (PEM) used for mTLS.

Example:

```python
from infi.clickhouse_orm import Database

db = Database(
    'analytics',
    db_url='https://clickhouse.example.com:8443/',
    username='user',
    password='pass',
    ca_cert='/etc/ssl/certs/ca-bundle.pem',
    client_cert='/etc/certs/client.crt',
    client_key='/etc/certs/client.key',
)
```

URL Query Parameters
--------------------

TLS options can be supplied as query parameters on `db_url`. If both URL params and constructor args are provided, URL params are applied as defaults and constructor args take precedence, except for `verify_ssl_cert` which is overridden by the URL if present.

Supported parameters:

- `verify_ssl_cert` (bool-like): `true|false|1|0|yes|no|on|off`
- `ca_cert` (string): Filesystem path to CA bundle
- `client_cert` (string): Filesystem path to client certificate (PEM)
- `client_key` (string): Filesystem path to client private key (PEM)

Examples:

```python
# Only verify with custom CA bundle
db = Database('analytics', db_url='https://host:8443/?ca_cert=/etc/ssl/certs/ca.pem')

# Disable verification (not recommended)
db = Database('analytics', db_url='https://host:8443/?verify_ssl_cert=false')

# mTLS using URL params
db = Database(
    'analytics',
    db_url=(
        'https://host:8443/?ca_cert=/etc/ssl/certs/ca.pem'
        '&client_cert=/etc/certs/client.crt'
        '&client_key=/etc/certs/client.key'
    ),
)
```

Notes
-----

- Paths must be accessible to the running process.
- If both `client_cert` and `client_key` are provided, they are passed as a tuple to the HTTP client.
- If only `client_cert` is provided, it is passed as a single PEM file that contains both certificate and key.
- When `ca_cert` is set, it overrides the boolean `verify_ssl_cert` and is used as the verification bundle.

Troubleshooting
---------------

- Certificate verification failures usually indicate an incorrect `ca_cert` path or a missing intermediate CA in the bundle.
- For mTLS handshake failures, ensure `client_cert` and `client_key` are a matching pair and in PEM format.

