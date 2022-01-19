import discord
from discord.ext import commands
import random
import os
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='b.', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"b.help"))
    print(f'I am Big bron')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
      return await ctx.send('Chill! **{}** is still on cooldown for you. Use this command after `{:.2f}` seconds'.format(ctx.command.name, error.retry_after))

@client.event
async def on_member_join(m):
  c = client.get_channel(902208234084003842)
  await c.send(f'<a:pepedance:907192828919185429> <a:pepedance:907192828919185429> <a:pepedance:907192828919185429> {m.mention} Welcome to BeluGANG fans! You are number {len(client.users)}  to join!Top things to do out here:\nStay active in <#924286587410448395>\nCheck out <#902483288315297803> for regular server updates.\nGo to <#924286208392179772> to get some fancy roles.\nEnter giveaways in <#924288466337009704>')

client.remove_command("help")


@client.command()
async def help(ctx):
  e = discord.Embed(title="Commands", description="The prefix is `.`", color=0x0040FF)

  e.add_field(name="General",value="help_1",inline=False,)

  e.add_field(name='Server utilities',value='help_2',inline=False)

  e.add_field(name="Fun",value="help_3",inline=False,)
    
  e.add_field(name="Invite",value="help_4",inline=False,)

  e.add_field(name="Moderation",value="help_5",inline=False)

  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.channel.send(embed=e)

@client.command()
async def help_1(ctx):
  e = discord.Embed(title='General',color=0x0040FF)
  e.add_field(name='help',value='Shows all commands',inline=True)
  e.add_field(name='ping',value='Shows the bot\'s latency',inline=True)
  e.add_field(name='avatar [member]',value='Shows the given user\'s avatar',inline=True)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)

@client.command()
async def help_2(ctx):
  e = discord.Embed(title='Server utilities',color=0x0040FF)
  e.add_field(name='report [member] [reason]',value='Report any Member who attacks you, or violates the rules.\nMisusing this will get you warned!',inline=True)
  e.add_field(name='vote',value='Vote for this server to support the staff',inline=True)
  e.add_field(name='info [member]',value='Shows the member\'s id and top role',inline=True)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)

@client.command()
async def help_3(ctx):
  e = discord.Embed(title='Fun',color=0x0040FF)
  e.add_field(name='rickroll [member]',value='Sends the rickroll lyrics to the given member!\n_credits to SockYeh#0001',inline=True)
  e.add_field(name='8ball [question]',value='Gives a random answer to your question!',inline=True)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)

@client.command()
async def help_4(ctx):
  e = discord.Embed(name='Invitation',color=0x0040FF)
  e.add_field(name='invite_music [member]',value='Gives the invite link to join music voice channel to given member!',inline=True)
  e.add_field(name='invite_lounge [member]',value='Gives the invite link to join Lounge voice channel to given member!',inline=True)
  e.add_field(name='invite_meeting_room [member]',value='Gives the invite link to join meeting room voice channel to given member!',inline=True)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)

@client.command()
async def help_5(ctx):
  e = discord.Embed(name='Moderation',color=0x0040FF)
  e.add_field(name='kick [member] [reason]',value='kicks a member from the server')
  e.add_field(name='yeet [member] [reason]',value='same functionality as kick\n')
  e.add_field(name='ban [member] [reason]',value='Bans the given member reason!\nYou can also use banish')
  e.add_field(name='unban [user with tag]',value='Unbans the member')
  e.add_field(name='mute [member] [reason]',value='Mutes the given member with reason')
  e.add_field(name='unmute [member]',value='Unmutes the given member',)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)

@client.command(aliases=['support'])
@commands.cooldown(1, 100, commands.BucketType.user)
async def vote(ctx):
  e = discord.Embed(title='Vote',description='Vote for the server on top.gg [here](https://top.gg/servers/902208234084003840)\n',color=0x2c36b9)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def suggest(ctx, *, suggestion=None):
    if suggestion == None:
        await ctx.channel.send("Bro define your suggestion")
        return
    chl = await client.fetch_channel(924287520219488316)
    e = discord.Embed(title=f"Suggestion by {ctx.author}",description=suggestion, color=0xFFA500)
    e.add_field(name='Note: It may take time for the moderators to consider the suggestion',value=' ',inline=False)
    e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
    msg = await chl.send(embed=e)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")
    await ctx.channel.send('Suggested! check it out in <#924287520219488316>')

@client.command(aliases=['info'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def information(ctx,member: discord.Member = None):
  if member != None:
      role = member.top_role
  elif member == None:
      role = ctx.author.top_role
  e = discord.Embed(title=f'{member.name}',description=f'{member.mention}',color=0xa81313)
  e.add_field(name='user id:',value=f'{member.id}')
  e.add_field(name='Top Role',value=f'<@&{role.id}>')
  e.set_thumbnail(url = member.avatar_url)
  e.set_footer(text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",icon_url=ctx.author.avatar_url,)
  await ctx.send(embed=e)

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx,member: discord.Member,*,reason=None):
  channel = client.get_channel(930117260071276554)
  muterole=ctx.guild.get_role(913388693979553862)
  memberrole = ctx.guild.get_role(902215816735498330)
  await member.add_roles(muterole)
  await member.remove_roles(memberrole)
  await ctx.send(member.mention +' was muted!')
  await member.send(f'You have been muted in BeluGANG because of the following reason:\n{reason}')
  await channel.send(f'{member.name}#{member.discriminator} was muted because {reason}')

@client.command(aliases=['yeet'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member: discord.Member):
  channel = client.get_channel(930117260071276554)
  muterole=ctx.guild.get_role(913388693979553862)
  memberrole = ctx.guild.get_role(902215816735498330)
  await member.add_roles(memberrole)
  await member.remove_roles(muterole)
  await ctx.send(member.mention +' was unmuted!')
  await channel.send(f'{member.name}#{member.discriminator} was unmuted ')
  await member.send('You are unmuted in BeluGANG!')

@client.command(aliases=['banish'])
@commands.has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member, *, reason='None'):
  await member.ban(reason=reason)
  await ctx.send('**',member,'** has been banned')

@ban.error
async def ban_error(ctx,error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("dude chill you're not a staff out here")

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx,*,member):
  ban = await ctx.guild.bans()
  member_name,member_disc = member.split('#')

  for ban_entry in ban:
    user = ban_entry.user

    if (user.name,user.discriminator) == (member_name,member_disc):
      await ctx.guild.unban(user)
      await ctx.send(f'{member} is unbanned')

@client.command()
async def report(ctx,member: discord.Member,*,reason='not given'):
  c = client.get_channel(930117260071276554)
  e = discord.Embed(title=f'{ctx.author} has reported {member}',color=0xa81313)
  e.add_field(name='The reason given is:',value=f'{reason}')
  await c.send('<@&902216033773969538>',embed=e)
  await ctx.channel.purge(limit=1)
  await ctx.send('Report has been sent to moderators!')

@client.command()
async def avatar(ctx, user: discord.User = None):
    if user != None:
        ava_url = user.avatar_url
        usr_name = f"{user.name}#{user.discriminator}"
    else:
        ava_url = ctx.author.avatar_url
        usr_name = f"{ctx.author.name}#{ctx.author.discriminator}"
    e = discord.Embed(title=f"{usr_name}'s Avatar", description="", color=0xFFA500)
    e.set_footer(
        text=f"Command requested by {ctx.author} | Bot made by Sheldon Lee Cooper#0787",
        icon_url=ctx.author.avatar_url,
    )
    e.set_image(url=ava_url)
    await ctx.channel.send(embed=e)

@client.command()
async def invite_music(ctx,member: discord.Member):
  await member.send(f'{ctx.author} has invited you to join to listen to music\nhttps://discord.gg/eEkxaNsDWa')
  await ctx.send(f'{member.name} has been invited')

@client.command()
async def invite_meeting_room(ctx,member: discord.Member):
  await member.send(f'{ctx.author} has invited you to the meeting room\nhttps://discord.gg/QFXkKgsUUT')

@client.command()
async def invite_lounge(ctx,member: discord.Member):
  await member.send(f'{ctx.author} has invited you to join the lounge in BeluGANG!\nhttps://discord.gg/3BtbpAbzcU')
  await ctx.send(f'{member.name} has been invited')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member, *, reason='None'):
  await member.kick(reason=reason)
  await ctx.send(f'**{member}** has been kicked!')

@kick.error
async def kick_error(ctx,error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("dude chill you're not a staff out here")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!! my latency is `{round(client.latency * 1000)} ms`')

@client.command()
async def rickroll(ctx, member: discord.Member):
    if member.id == 856769339654930432:
        user = ctx.author
        await user.send(
            'We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you'
        )
        await ctx.channel.send(f"SENT RICKROLL TO `{user.name}`")
    elif member.id == 844244515933913149:
      user = ctx.author
      await user.send('We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you')
      await ctx.channel.send(f"SENT RICKROLL TO `{user.name}`")
    elif member.id == 881122798297296896:
        user = ctx.author
        await user.send(
            'We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you'
        )
        await ctx.channel.send(f"SENT RICKROLl TO {user.name}")
    elif member.id == 692683428478582854:
        user = ctx.author
        await user.send(
            'We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you'
        )
        await ctx.channel.send(f"SENT RICKROL2TO, {user.name}")
    elif member.id == 735393318640287825:
        user = ctx.author
        await user.send(
            'We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you'
        )
        await ctx.channel.send(f"SENT RICKROLL TO {user.name}")
    else:
        user = ctx.author
        await member.send('We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you')
        await ctx.channel.send(f"SENT RICKROLL TO `{member.name}`")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'is certain.', 'It is decidedly so.', 'Without a doubt',
        'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.'
        'Outlook good.', 'Yes.', 'Signs point to yes.', "Don't count on it.", 'My reply is no.',
        'My sources say no.', 'Outlook not so good.', 'Very doubtful.'
    ]
    e = discord.Embed(title='8ball',description='',color=0x0040FF)
    e.add_field(name='Question: ',value=f'{question}',inline=True)
    e.add_field(name='Answer: ',value=f'{random.choice(responses)}',inline=True)
    await ctx.send(embed=e)

@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2,):
  await ctx.channel.purge(limit=amount)


keep_alive()
client.run(os.getenv('token'))
