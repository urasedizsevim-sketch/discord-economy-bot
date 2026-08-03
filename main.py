import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

MY_GUILD_ID = 123456789012345678 #replace with your Guild ID


@bot.event
async def on_ready():
    guild = discord.Object(id=MY_GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    synced = await bot.tree.sync(guild=guild)
    print(f"Converter Bot is ready! Synced {len(synced)} slash command(s).")


@bot.tree.command(name="convert", description="Converts live currency exchange rates.")
async def convert_slash(
    interaction: discord.Interaction,
    amount: float,
    from_currency: str,
    to_currency: str
):
    await interaction.response.defer()

    from_currency = from_currency.upper().replace("TL", "TRY")
    to_currency = to_currency.upper().replace("TL", "TRY")

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    try:
        response = requests.get(url).json()

        if response.get("result") == "success":
            rates = response["rates"]

            if to_currency in rates:
                rate = rates[to_currency]
                result = amount * rate
                reverse_rate = 1 / rate if rate != 0 else 0

                # --- EMBED CARD ---
                embed = discord.Embed(
                    title="Currency Converter",
                    description=f"**{amount:,.2f} {from_currency}** ➔ **{result:,.2f} {to_currency}**",
                    color=discord.Color.green()
                )

                # Detail Fields
                embed.add_field(name="Amount", value=f"`{amount:,.2f} {from_currency}`", inline=True)
                embed.add_field(name="Result", value=f"`{result:,.2f} {to_currency}`", inline=True)
                embed.add_field(name="Exchange Rate", value=f"`1 {from_currency} = {rate:.4f} {to_currency}`", inline=False)

                embed.set_footer(
                    text=f"Inverse Rate: 1 {to_currency} = {reverse_rate:.4f} {from_currency} • Live API Data"
                )

                await interaction.followup.send(embed=embed)
            else:
                await interaction.followup.send(
                    f"Invalid target currency: `{to_currency}`. (e.g., USD, TRY, EUR, GBP)",
                    ephemeral=True
                )
        else:
            await interaction.followup.send(f"Invalid source currency: `{from_currency}`.", ephemeral=True)

    except Exception as e:
        await interaction.followup.send(f"An error occurred while fetching exchange rates: {e}", ephemeral=True)
bot.run("YOUR_BOT_TOKEN_HERE")
