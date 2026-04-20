#!/usr/bin/env bash
#
# Build Astro puis upload vers Infomaniak via FTP.
# Credentials lus depuis .env.deploy (gitignored).
#
# Usage: ./deploy.sh [--clean]
#   --clean : forcer clean build (supprime dist/ avant)

set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" == "--clean" ]]; then
    echo "🧹 Clean dist/"
    rm -rf dist
fi

echo "🛠  Building Astro…"
npm run build

echo ""
echo "🚀 Uploading to Infomaniak…"
python3 scripts/ftp_upload.py

echo ""
echo "✅ Done. https://cmadevops.de/"
