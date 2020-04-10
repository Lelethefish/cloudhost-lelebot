import discord
import random
import asyncio
import traceback
from discord.ext import commands

class authors:
    def __init__(self, balance, xp):
        self.balance = balance
        self.xp = xp

class permissions:
    m2=False
    p_h=False
perm = permissions

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.content.startswith('pls howlesbian'):
            x = list(message.content)
            word=[]
            if len(x) > 14:
                for i in range (len(x)):
                    if i > 13:
                        word.append(x[i])
                x = ''.join(word)
                les_embed = discord.Embed(
                title="Lesbian r8 machine",
                colour=discord.Color.green()
                )
                les_embed.add_field(name=x, value=f' is {random.randint(0, 100)} % lesbian')
                await message.channel.send(embed=les_embed)
            else:
                les_embed = discord.Embed(
                title="Lesbian r8 machine",
                colour=discord.Color.green()
                )
                les_embed.add_field(name='You', value=f'are {random.randint(0, 100)} % lesbian')
                await message.channel.send(embed=les_embed)

        if message.content.startswith('pls howtall'):
            if message.author.id == 636902627921362964 and:
                tall_embed = discord.Embed(
                title="Hight r8 machine",
                colour=discord.Color.gold()
                )
                tall_embed.add_field(name='Lele da boss', value=f'is {random.randint(150, 195)} cm tall!')
                await message.channel.send(embed=tall_embed)
            else:
                x = list(message.content)
                word=[]
                if len(x) > 12:
                    for i in range (len(x)):
                        if i > 11:
                            word.append(x[i])
                    x = ''.join(word)
                    tall_embed = discord.Embed(
                    title="Hight r8 machine",
                    colour=discord.Color.blue()
                    )
                    tall_embed.add_field(name=x, value=f' is {random.randint(50, 210)} cm tall!')
                    await message.channel.send(embed=tall_embed)
                else:
                    tall_embed = discord.Embed(
                    title="Hight r8 machine",
                    colour=discord.Color.blue()
                    )
                    tall_embed.add_field(name='You', value=f'are {random.randint(50, 210)} cm tall!')
                    await message.channel.send(embed=tall_embed)

        if message.content.startswith('pls howiq'):
            if message.author.id == 636902627921362964:
                iq_embed = discord.Embed(
                title="IQ r8 machine",
                colour=discord.Color.gold()
                )
                iq_embed.add_field(name='Lele da boss', value=f'IQ is {random.randint(150, 280)}')
                await message.channel.send(embed=iq_embed)
            else:
                x = list(message.content)
                word=[]
                if len(x) > 10:
                    for i in range (len(x)):
                        if i > 9:
                            word.append(x[i])
                    x = ''.join(word)
                    iq_embed = discord.Embed(
                    title="Hight r8 machine",
                    colour=discord.Color.blue()
                    )
                    iq_embed.add_field(name=x, value=f'IQ is {random.randint(60, 160)}')
                    await message.channel.send(embed=iq_embed)
                else:
                    iq_embed = discord.Embed(
                    title="Hight r8 machine",
                    colour=discord.Color.blue()
                    )
                    iq_embed.add_field(name='Your', value=f'IQ is {random.randint(60, 160)}')
                    await message.channel.send(embed=iq_embed)

        if message.author.id == self.user.id:
            return
        auth=[]
        u=False
        if message.content.startswith('!bj'):
            try:
                for i in range (len(auth)):
                    if message.author.id == auth[i]:
                        balance=auth[i].balance
                        xp=auth[i].xp
                        u=True
                if u == False:
                    u.append(u)
            except:
                u=False
                auth.append(message.author.id)
                auth[len(auth)-1] = authors(2500, 0)
                balance=auth[len(auth)-1].balance
                xp=auth[len(auth)-1].xp
            _cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'ace']
            values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
            dealer_names = ['Jhon', 'Robert', 'Sabastian', 'joseph', 'Matthew', 'Andrew', 'Charles', 'Christopher', 'Kenneth', 'Jeffrey', 'Gary', 'Scott', 'Larry', 'Benjamin', 'Alexander', 'Jack', 'Dennis', 'Oni chan']
            dealer_name = random.choice(dealer_names)
            protips = ["The dealer will always hit if he's card count is under 17", "The dealer accept's your challange", "Consider doubling down", "If you get a blackjack you will earn 150% your bet", "You can only double down if you only have two cards", "The key of not losing is winning", "Use your brain", "Card counting isn't illegal, consider card counting", "Sometimes you just got to risk it", "Good luck", "Remember the dealer always have an advantage over you"]
            round=1
            double_down_=True
            protip=random.choice(protips)
            used = [0]*13
            playercard=[]
            dealer_card=[]
            class cards:
                bet=0
                player_card_count=0
                dealer_card_count=0
                cards_shoe = []
                values_shoe = []
            cards = cards
            while len(cards.cards_shoe) < 312:
                q = random.randint(0, 12)
                if used[q] < 24:
                    cards.cards_shoe.append(_cards[q])
                    cards.values_shoe.append(values[q])
                    used[q] = used[q]+1

            '''@client.event
            async def on_error(event, *args, **kwargs):
                error = args[0]
                error_embed = discord.Embed(
                title="An error acoured",
                colour=discord.Color.red()
                )
                error_embed.add_field(name=f"Error", value=f"{message.author.mention} caused an error ヽ(ಠ_ಠ)ノ", inline=False)
                error_embed.add_field(name=f"Error", value="Game cancled")
                await message.channel.send(embed=error_embed)
                async def on_message(self, message):
                    print(error)'''

            for i in range (2):
                playercard.append(cards.cards_shoe[0])
                cards.player_card_count = cards.player_card_count+cards.values_shoe[0]
                del cards.cards_shoe[0]
                del cards.values_shoe[0]
            for i in range (2):
                dealer_card.append(cards.cards_shoe[0])
                cards.dealer_card_count = cards.dealer_card_count+cards.values_shoe[0]
                del cards.cards_shoe[0]
                del cards.values_shoe[0]
            start_embed = discord.Embed(
            title="Playing Blackjack",
            colour=discord.Color.green()
            )
            start_embed.set_image(url=f"https://cdn.discordapp.com/attachments/696350855078739993/696738978409218048/download_3.jpeg")
            start_embed.add_field(name="Welcome", value=f"`{message.author.mention}`")
            start_embed.add_field(name="Dealer Name", value=f"`{dealer_name}`")
            start_embed.add_field(name="Your balance", value=f'{balance}$')
            start_embed.add_field(name="Your Xp", value=f'{xp}')
            start_embed.add_field(name="Decks", value='6 Decks')
            start_embed.add_field(name="Posible Action", value="hit/stand/double down")
            start_embed.set_footer(text=f"protip: {protip}")
            await message.channel.send(embed=start_embed)

            bet_embed = discord.Embed(
            title=f"Round {round}",
            colour=discord.Color.green()
            )
            bet_embed.add_field(name="number", value='How much do you want to bet')
            await message.channel.send(embed=bet_embed)
            perm.m2=True

            @client.event
            async def on_message(message2):
                if message2.author.id == message.author.id and perm.m2 == True:
                    for i in range (0, balance+1):
                        if str(message2.content) == str(i):
                            cards.bet=int(message2.content)
                    try:
                        if cards.bet < balance and cards.bet > 0:
                            perm.m2=False
                            perm.p_h=True
                            hit_embed = discord.Embed(
                            title=f'Card info (round {round})',
                            colour=discord.Color.green()
                            )
                            hit_embed.add_field(name="Your cards", value=f"{playercard}")
                            hit_embed.add_field(name="Dealer up card", value=f"`{dealer_card[0]}`")
                            hit_embed.add_field(name="Amount of cards left in shoe", value=f'{len(cards.cards_shoe)}')
                            hit_embed.add_field(name="Your bet", value=f'{cards.bet}$')            
                            await message.channel.send(embed=hit_embed)

                            playerhand_embed = discord.Embed(
                            title='Player hand',
                            colour=discord.Color.green()
                            )
                            playerhand_embed.add_field(name="Posible action", value='hit/stand/double down', inline=False)
                            playerhand_embed.add_field(name="hit", value="Draw a card from the shoe", inline=False)
                            playerhand_embed.add_field(name="stand", value='Your happy with your cards', inline=False)
                            playerhand_embed.add_field(name="Double down", value="Double a bet after seeing one's initial cards, with the requirement that one additional card be drawn", inline=False)            
                            await message.channel.send(embed=playerhand_embed)
                            @client.event
                            async def on_message(message3):
                                async def dealer_hand():
                                    dh_embed = discord.Embed(
                                    title=f'Card info (round {round})',
                                    colour=discord.Color.green()
                                    )
                                    dh_embed.add_field(name="Your cards", value=f"{playercard}")
                                    dh_embed.add_field(name="Dealer cards", value=f"`{dealer_card}`")
                                    dh_embed.add_field(name="Amount of cards left in shoe", value=f'{len(cards.cards_shoe)}')
                                    dh_embed.add_field(name="Your bet", value=f'{cards.bet}$')            
                                    await message.channel.send(embed=dh_embed)
                                    while cards.dealer_card_count < 17:
                                        dealer_card.append(cards.cards_shoe[0])
                                        cards.dealer_card_count = cards.dealer_card_count+cards.values_shoe[0]
                                        del cards.cards_shoe[0]
                                        del cards.values_shoe[0]
                                        dh_embed = discord.Embed(
                                        title=f'Card info (round {round})',
                                        colour=discord.Color.green()
                                        )
                                        dh_embed.add_field(name="Your cards", value=f"{playercard}")
                                        dh_embed.add_field(name="Dealer cards", value=f"`{dealer_card}`")
                                        dh_embed.add_field(name="Amount of cards left in shoe", value=f'{len(cards.cards_shoe)}')
                                        dh_embed.add_field(name="Your bet", value=f'{cards.bet}$')            
                                        await message.channel.send(embed=dh_embed)
                                if message3.author.id == message.author.id and perm.p_h == True:
                                    if message3.content.startswith('hit'):
                                        playercard.append(cards.cards_shoe[0])
                                        cards.player_card_count = cards.player_card_count+cards.values_shoe[0]
                                        del cards.cards_shoe[0]
                                        double_down_ == False
                                        hit__embed = discord.Embed(
                                        title=f'Card info (round {round})',
                                        colour=discord.Color.green()
                                        )
                                        hit__embed.add_field(name="Your cards", value=f"{playercard}")
                                        hit__embed.add_field(name="Dealer up card", value=f"`{dealer_card[0]}`")
                                        hit__embed.add_field(name="Amount of cards left in shoe", value=f'{len(cards.cards_shoe)}')
                                        hit__embed.add_field(name="Your bet", value=f'{cards.bet}$')            
                                        await message.channel.send(embed=hit__embed)
                                    if message3.content.startswith('double down') and double_down_ == True :
                                        playercard.append(cards.cards_shoe[0])
                                        cards.player_card_count = cards.player_card_count+cards.values_shoe[0]
                                        del cards.cards_shoe[0]
                                        cards.bet=cards.bet*2
                                        hit__embed = discord.Embed(
                                        title=f'Card info (round {round})',
                                        colour=discord.Color.green()
                                        )
                                        hit__embed.add_field(name="Your cards", value=f"{playercard}")
                                        hit__embed.add_field(name="Dealer up card", value=f"`{dealer_card[0]}`")
                                        hit__embed.add_field(name="Amount of cards left in shoe", value=f'{len(cards.cards_shoe)}')
                                        hit__embed.add_field(name="Your bet", value=f'{cards.bet}$')            
                                        await message.channel.send(embed=hit__embed)
                                        await dealer_hand()
                                    if message3.content.startswith('stand'):
                                        await dealer_hand()
                    except:
                        None
            
client = MyClient()
client.run('Njk2MzUwMDc3NzczNTQ1NDgy.Xonh3w.RP3IfJ8vDAWwct1VDdkfHVpvRBQ')
