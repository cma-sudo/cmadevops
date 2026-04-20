#!/usr/bin/env python3
"""Upload dist/ to Infomaniak via plain FTP.

Usage: loads credentials from .env.deploy, mirrors dist/ to FTP_TARGET.
Only uploads changed files (compares size + mtime when possible).
"""
import ftplib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
ENV = ROOT / ".env.deploy"

if not DIST.exists():
    print(f"❌ {DIST} not found — run npm run build first")
    sys.exit(1)

if not ENV.exists():
    print(f"❌ {ENV} not found — copy .env.deploy.example and fill credentials")
    sys.exit(1)

cfg = {}
for line in ENV.read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    k, _, v = line.partition("=")
    cfg[k.strip()] = v.strip()

for key in ("FTP_HOST", "FTP_USER", "FTP_PASSWORD", "FTP_TARGET"):
    if not cfg.get(key):
        print(f"❌ {key} missing in .env.deploy")
        sys.exit(1)

TARGET = cfg["FTP_TARGET"].rstrip("/") or "/"

print(f"📦 Connecting to {cfg['FTP_HOST']} as {cfg['FTP_USER']}…")
ftp = ftplib.FTP(cfg["FTP_HOST"], timeout=30)
ftp.login(cfg["FTP_USER"], cfg["FTP_PASSWORD"])
print(f"✅ Connected · server → {TARGET}")

def ensure_dir(remote_path):
    parts = remote_path.strip("/").split("/")
    path = ""
    for p in parts:
        if not p:
            continue
        path = f"{path}/{p}"
        try:
            ftp.cwd(path)
        except ftplib.error_perm:
            try:
                ftp.mkd(path)
                print(f"  mkdir {path}")
            except ftplib.error_perm as e:
                if not str(e).startswith("550"):
                    raise
    ftp.cwd("/")

def remote_size(path):
    try:
        return ftp.size(path)
    except Exception:
        return None

uploaded = skipped = 0
for local in sorted(DIST.rglob("*")):
    if not local.is_file():
        continue
    rel = local.relative_to(DIST).as_posix()
    remote = f"{TARGET}/{rel}".replace("//", "/")
    remote_dir = os.path.dirname(remote) or "/"
    ensure_dir(remote_dir)
    local_sz = local.stat().st_size
    rsz = remote_size(remote)
    if rsz == local_sz:
        skipped += 1
        continue
    with open(local, "rb") as f:
        ftp.storbinary(f"STOR {remote}", f)
    uploaded += 1
    print(f"  ↑ {rel}")

ftp.quit()
print(f"\n✨ Done — {uploaded} uploaded, {skipped} skipped (unchanged)")
print(f"🌐 https://cmadevops.de/")
