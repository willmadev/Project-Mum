import discord
import os
import random
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
      

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'mom':
            await message.channel.send('HAHAHAHA YOUR MOM HAS A MASSIVE WILLY')
        if message.content =='ping':
            await message.channel.send('PING PONG MOTHERFUCKER')
        if message.content =='a'or 'e'or'1'or'i'or'o'or'u':
            if message.content =='mama':
                momlist=["Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.","Yo mama's so fat, when she skips a meal, the stock market drops.","Yo mama's so fat, it took me two buses and a train to get to her good side.","Yo mama's so fat, when she goes camping, the bears hide their food.","Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said 'concentrate.'","Yo mama's so stupid when they said it was chilly outside, she grabbed a bowl.","Yo mama's so stupid, she put lipstick on her forehead to make up her mind.","Yo mama's so stupid, when they said, 'Order in the court', she asked for fries and a shake.","Yo mama's so stupid, she got locked in the grocery store and starved to death.","Yo mama's so stupid, when I said, 'Drinks on the house', she got a ladder.","Yo mama's so poor, the ducks throw bread at her.","Yo mama's so classless, she's a Marxist utopia.","Yo mama so dumb, she went to the eye doctor to get an iPhone.","Yo mama's so short, you can see her feet on her driver's license."]
                await message.channel.send(random.choice(momlist))
            if random.randint(0, 10)==9:
                momlist=["Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.","Yo mama's so fat, when she skips a meal, the stock market drops.","Yo mama's so fat, it took me two buses and a train to get to her good side.","Yo mama's so fat, when she goes camping, the bears hide their food.","Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said 'concentrate.'","Yo mama's so stupid when they said it was chilly outside, she grabbed a bowl.","Yo mama's so stupid, she put lipstick on her forehead to make up her mind.","Yo mama's so stupid, when they said, 'Order in the court', she asked for fries and a shake.","Yo mama's so stupid, she got locked in the grocery store and starved to death.","Yo mama's so stupid, when I said, 'Drinks on the house', she got a ladder.","Yo mama's so poor, the ducks throw bread at her.","Yo mama's so classless, she's a Marxist utopia.","Yo mama so dumb, she went to the eye doctor to get an iPhone.","Yo mama's so short, you can see her feet on her driver's license."]
                await message.channel.send(random.choice(momlist))
                # await message.channel.send('YOUR MUMMM!!')
                # await message.channel.send('Heh, yes i know im funny :)')
        # if message.content =='dad':
        #     if random.randint(0, 10)==9:
        #         momlist=["Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.","Yo mama's so fat, when she skips a meal, the stock market drops.","Yo mama's so fat, it took me two buses and a train to get to her good side.","Yo mama's so fat, when she goes camping, the bears hide their food.","Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said 'concentrate.'","Yo mama's so stupid when they said it was chilly outside, she grabbed a bowl.","Yo mama's so stupid, she put lipstick on her forehead to make up her mind.","Yo mama's so stupid, when they said, 'Order in the court', she asked for fries and a shake.","Yo mama's so stupid, she got locked in the grocery store and starved to death.","Yo mama's so stupid, when I said, 'Drinks on the house', she got a ladder.","Yo mama's so poor, the ducks throw bread at her.","Yo mama's so classless, she's a Marxist utopia.","Yo mama so dumb, she went to the eye doctor to get an iPhone.","Yo mama's so short, you can see her feet on her driver's license."]
        #         await message.channel.send(random.choice(momlist))
        #         momjokes()


client = MyClient()
client.run(ENTER TOKEN HERE!)


# def momjokes():
#     momlist=["Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.","Yo mama's so fat, when she skips a meal, the stock market drops.","Yo mama's so fat, it took me two buses and a train to get to her good side.","Yo mama's so fat, when she goes camping, the bears hide their food.","Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said 'concentrate.'","Yo mama's so stupid when they said it was chilly outside, she grabbed a bowl.","Yo mama's so stupid, she put lipstick on her forehead to make up her mind.","Yo mama's so stupid, when they said, 'Order in the court', she asked for fries and a shake.","Yo mama's so stupid, she got locked in the grocery store and starved to death.","Yo mama's so stupid, when I said, 'Drinks on the house', she got a ladder.","Yo mama's so poor, the ducks throw bread at her.","Yo mama's so classless, she's a Marxist utopia.","Yo mama so dumb, she went to the eye doctor to get an iPhone.","Yo mama's so short, you can see her feet on her driver's license."]
#     await message.channel.send(random.choice(momlist))

# print(thisdict["brand"])


