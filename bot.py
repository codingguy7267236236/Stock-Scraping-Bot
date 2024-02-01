#importing the libraries
import nextcord
from nextcord.ext import commands
#importing from stockdata.py file
from stockdata import *
#importing all the methods and functions from the embeds.py file all represented by *
from embeds import *

#bot token
TOKEN = "YOUR BOT TOKEN"

intents = nextcord.Intents().all()
client=commands.Bot(command_prefix="!",intents=intents)

#testingServer stores the id of the server to test/develop bot in
#this is so that you don't have to wiat for it to register the command each time you run the bot 
#as the API claims it can sometimes take up to an hour to update
testingServer = ["Test server IDs goes here"]

#event called when bot is ready after startup
@client.event
async def on_ready():
  #registering the slash commands so that when bot added to server they will appear
  await client.register_application_commands(stock)
  print("Bot online")


#stock related slash commands
#parent command
#guild ids are the test servers you want this command to work in during development
#dm permission toggles whether the commands will work in dms with the bot
@client.slash_command(name="stock", description="stock commands",
  guild_ids=testingServer,
  dm_permission=False)
async def stock(ctx,type:str=nextcord.SlashOption(name="type",description="the type of card you want to add",choices=["scenario","response"]),txt:str=nextcord.SlashOption(name="value",description="the card value ensure to put _ in a scenario card type")):
  pass

#subcommand for stock
#this sub command allows a user to view a price of any stock
@stock.subcommand(name="price",description="View a stocks current price")
async def price(ctx,ticker:str=nextcord.SlashOption(name="stock-ticker",description="a stocks ticker e.g. Tesla is tsla",required=True)):
  #calling the get stock price command
  stock_price = get_current_price(ticker)
  #creating an embed to display this data so it looks polished and clean
  title = f"{ticker.upper()}'s Stock Price"
  description = f"The current stock price for {ticker.upper()} on the stock market right now, according to Yahoo Finanace."
  #values are the list of lists representing the fields to add to embed
  values = [["Price",f"${stock_price}"]]

  #creating embed
  embed = createEmbed(title,description,values)
  #sending the info back to the channel of the server the user called the command in
  await ctx.send(embed=embed)


#cnadlestick command
@stock.subcommand(name="candlestick",description="View a candlestick for a stock over given period and interval")
async def price(ctx,ticker:str=nextcord.SlashOption(name="stock-ticker",description="a stocks ticker e.g. Tesla is tsla",required=True), 
                period:str=nextcord.SlashOption(name="period",description="the time period to cover e.g. 1d (day) 1M (month)",required=True),
                interval:str=nextcord.SlashOption(name="interval",description="how often candle mapped e.g. 1d (day) 1M (month)",required=True)):
  #tell the user that it is processing the command, setting ephemeral to true so only the user who called the command can see
  await ctx.send("Processing.....",ephemeral=True)

  #creating and getting the candlestick image
  filename = getCandlestick(ticker,period,interval)

  #getting file
  file = nextcord.File(filename)
  await ctx.send(f"{ticker.upper()}'s Candlestick for Period: {period} at an interval of {interval}",file=file)


#codeline to run the bot
client.run(TOKEN)