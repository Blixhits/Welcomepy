import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="+")

@client.event
async def on_ready():
  print("Online")
  
  @client.event
  async def on_member_join(member):
    channel = client.get_channel(1043219927353536512)
    embed=discord.Embed(title=f"Welcome {member.name}",description="Welcome to Warriors For God\n Thank you for being here!",color=0x9208ea)
    embed.set_thumnail(url=member.avatar_url)
    embed.set_footer(text="Created by Blix#8288")
    
    await channel.send(embed=embed)
    
    @client.command(pass_context=True)
    async def hello(ctx):
      await ctx.send(f"Hello {ctx.author.mention}")
      
      client.run("MTA0MTY5MDY4Nzk4NjQ3NTA5OQ.Gjwx0g.Vn80GsigftNFeTeW88NH3q-8t05AaAZYcEaeWA")
