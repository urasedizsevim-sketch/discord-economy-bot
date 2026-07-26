# Real-Time Currency Converter Discord Bot

A reliable and lightweight Discord bot built in Python to convert fiat currencies in real-time using live exchange rate APIs. Designed with native Slash Commands and clear Embed UI output.

![Python](https://img.shields.io/badge/python-v3.10%2B-blue?style=flat-square&logo=python)
![discord.py](https://img.shields.io/badge/discord.py-v2.0%2B-blue?style=flat-square&logo=discord)
![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)

---

## Features

- **Live Exchange Rates:** Fetches real-time financial market rates via Open Exchange Rates API.
- **Modern Slash Commands:** Built using Discord's Application Commands API (`/convert`).
- **Structured Embed UI:** Displays conversion results, direct rates, and inverse rates in a clean layout.
- **Global Currency Support:** Supports USD, EUR, TRY, GBP, JPY, and 150+ fiat currencies.
- **Input Normalization & Error Handling:** Auto-capitalizes currency inputs, maps local aliases (e.g., TL to TRY), and handles invalid currency codes gracefully.

---

## Tech Stack

- **Language:** Python 3
- **Library:** `discord.py` (v2.0+)
- **API:** Open Exchange Rates API (`open.er-api.com`)
- **HTTP Client:** `requests`

---

## Command Usage

| Command | Arguments | Description | Example |
| :--- | :--- | :--- | :--- |
| `/convert` | `amount`, `from_currency`, `to_currency` | Converts an amount between specified currencies in real-time. | `/convert amount:100 from_currency:USD to_currency:EUR` |

---

## Preview

*(Add recorded GIF or screenshot here)*  
`![Bot Preview](./demo.gif)`

---

## Custom Bot Commissions

Looking for a custom Discord bot tailored for your server, community, or business?  
Feel free to reach out for custom development inquiries.

- **Fiverr:** [Your Fiverr Profile Link Here]
- **Discord:** `your_discord_username`
