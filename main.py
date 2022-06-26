import discord
import requests
import json
import os
import random
from keep_alive import keep_alive
import time
import sys
import math
from weather import *
from discord.ext import commands , tasks
import giphy_clients
from giphy_clients.rest import ApiException 

#client = discord.Client()
client=command.Bot(command_prefix='$')

	

sad_words = [
    "sad", "depressed", "depressing", "miserable", "unhappy", "lonely",
    "gloomy", "troubled", "hopeless"
]

good_words = [
    "Cheer up !", "You can do it", "Have faith", "You are a great person !",
    "Hang in there!", "Be positive !!", "Keep smiling"
]

flirt_lines= [
'You’re so hot, my zipper is falling for you.',
'They say that kissing is a language of love, so would you mind starting a conversation with me?',
'I’m on top of things. Would you like to be one of them?',
'Are you an eco-friendly kind of girl? The condom in my pocket goes expires tomorrow, so why don’t you help me use it?',
'Is your name winter? Because you’ll be coming soon.',
'Do you want to commit a sin for your next confessional?',
'I’m not into watching sunsets, but I’d love to see you go down.',
'Are you an exam? Because I have been studying you like crazy.',
'Can you tell me what time you’ll come back to my place, please?',
'Give me your car keys so I can drive you crazy.',
'Is your name Earl Grey? Because you look like a hot-tea!',
'I love my bed, but I’d rather be in yours.',
'Are you a haunted house? Because I’m going to scream when I’m in you.',
'Your body is 70 percent water… and I’m thirsty.',
'Are you undressing me with your eyes?!',
'Your outfit would look great on my bedroom floor',
'Is it hot in here? Or is it just you?',
'I lost my keys… can I check your pants?',
'Did you know my lips are like Skittles and you’re about to taste the rainbow?',
'Do I have to sign for your package?',
'I know a great way to burn off the calories in that drink.',
'Please don’t let this go to your head, but do you want some?',
'Are you an elevator? Because I’ll go up and down on you.',
'You look great right now. Do you know what else would look great on you? Me!',
'With school, I just want an A. With you, I just want to F.',
'Did you have Lucky Charms for breakfast? Because you look magically delicious!',
'Roses are red. Violets are fine. You be the six. I’ll be the nine.',
'Do you drink soda? Because you look so-da-licious.',
'Do you have a shovel? Because I’m digging you.',
'What did you say your name was? I want to make sure I’m screaming the right name tonight.',
'That’s a nice shirt. Can I try it on after we have sex?',
'I think I could fall madly in bed with you.',
'Can I borrow a kiss? I promise I’ll give it back.',
'Are you a campfire? Because you’re hot and I want s’more.',
'If you’re feeling down, I can feel you up.',
'What is a nice person like you doing in a dirty mind like mine?',
'We were both born without clothes',
'I’m peanut butter. You’re jelly. Let’s have sex.'
'I’m not feeling myself today. Can I feel you instead?',
'I don’t think I want babies, but I wouldn’t mind refining my baby-making technique with you.',
'You know what winks and then screws like a tiger? ~_^',
'My doctor told me I have a vitamin D deficiency. Want to go back to my place and save me?',
'Are you my homework? Because I’m not doing you, but I definitely should be.',
'Are you a drill sergeant? Because you have my privates standing at attention.',
'Can you do telekinesis? Because you’ve made a part of me move without even touching it.',
'Treat me like a pirate and give me that booty.',
'If you were a flower, you’d be a damn-delion.',
'Let’s play Titanic. You’ll be the iceberg and I’ll go down.',
'Dinner first, or can we go straight for dessert?',
'I was feeling very off today, but then you turned me on.',
'Does your name start with “C” because I can “C” us getting down.',
'I’m having trouble sleeping by myself, can you sleep with me?',
'This might seem corny, but you’re making me horny.',
'Want to save water by showering together?',
'I’m an adventurer and I want to explore you.',
'Want to go half on a baby?',
'Do you have room for an extra tongue in your mouth?',
'Are you a sea lion? Because I can sea you lion in my bed tonight.',
'Are you Dracula? You looked a little thirsty when you were looking at me.',
'Don’t ever change. Just get naked.',
'Go ahead, feel my shirt. Its made of boyfriend material!',
'If you were a Transformer you would be Optimus Fine!',
'Do you believe in love at first sight? Or should I walk past you again?',
'I am learning about important dates in history. Wanna be one of them?',
'I seem to have lost my phone number. Can I have yours?',
'Are you a parking ticket? Cause you have got fine written all over you!',
'Did you invent the airplane? Because you seem Wright for me!',
'I was wondering if you had an extra heart. Because mine was just stolen!',
'Can I follow you where you are going right now? Cause my parents always told me to follow my dreams!',
'Are you Siri? Because you autocomplete me!',
'I hope you know CPR, because you are taking my breath away!',
'If I had four quarters to give to the four prettiest women in the world, you would have a dollar!',
'Let me guess, your middle name is Gillette, right? Because you are the best a man can get!',
'Your eyes are bluer than the Atlantic ocean. And I dont mind being lost at sea!',
"If you were a burger at McDonald's, you'd be named the McGorgeous!",
"Are you a camera? Because every time I look at you, I smile!",
'Is there an airport nearby, or was that just my heart taking off?',
"Are you a loan? 'Cause you've got my interest!",
"I'm in the mood for pizza. A pizza you, that is!",
"Are you a 45-degree angle? Because you're a cutie!",
"You're so sweet, you'd put Hershey's out of business!",
'If nothing lasts forever, will you be my nothing?',
"If you were a phaser on Star Trek, you'd be set to stun!",
"Do you have a name? Or can I call you mine?",
"Is your name Google? Because you have everything I've been searching for.",
"Have you been covered in bees recently? I just assumed, because you look sweeter than honey.",
"There must be something wrong with my eyes. I can't take them off you.",
"Are you from Tennessee? Because you're the only Ten I See.",
"You must be a campfire. Because you're super hot and I want s'more.",
"My buddies bet me that I wouldn't be able to start a conversation with the most beautiful person in the club. What should we do with their money?",
"Well, here I am. What are your other two wishes for the genie?",
"Remember me? Oh, that's right, I've only met you in my dreams.",
"I'm glad I remembered to bring my library card. ‘Cause I am totally checking you out!",
"If you were a vegetable, you would be a cute-cumber!",
"I'm no mathematician, but I'm pretty good with numbers. Tell you what, give me yours and watch what I can do with it.",
"Are you a time traveler? Because I see you in my future!",
"If you and I were socks, we'd make a great pair!",
"Do you work at Dick's? Because you're sporting the goods!",
"Are your parents bakers? Because you're a cutie pie!",
"Aside from being drop-dead gorgeous, what do you do for a living?",
"Hey, my name's Microsoft. Can I crash at your place?",
"Kiss me if I'm wrong. But dinosaurs still exist, right?",
"You owe me a drink. Because when I looked at you, I dropped mine!",
"Want a raisin? No? Well, how about a date?",
"You must be a high test score. Because I want to take you home and show you to my mother.",
'I may not be a photographer. But I can totally picture us together.',
'You must be a magician. Because any time I look at you, everyone else disappears.',
"Was your dad a boxer? Because you're a knockout!",
"I think you're suffering from a lack of vitamin me.",
"I want our love to be like the number Pi: irrational and never-ending.",
"Is your name Ariel? Cause we Mermaid for each other.",
"If you were words on a page you'd be the fine print.",
'You are the reason even Santa has a naughty list.',
"Where have I seen you before? Oh yeah, I remember now. It was in the dictionary next to the word GORGEOUS!",
"Don't tell me if you want me to take you out to dinner. Just smile for yes, or do a backflip/somersault/counter-spin gymnastics combination for no.",
"I wasn't always religious. But I am now, because you're the answer to all my prayers.",
"If I could rearrange the alphabet, I'd put ‘I' and ‘U' together.",
"You must be exhausted. You've been running through my mind all day."
]




def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def get_fox():
    response = requests.get("https://randomfox.ca/floof")
    fox = json.loads(response.text)
    print(fox)
    return (fox)


def get_joke():
    response = requests.get(
        "https://official-joke-api.appspot.com/jokes/random")
    joke = json.loads(response.text)
    return (joke)
def get_cat():
	q='cats'
    #enter giphy api key here
	api_key=''
	api_instance=giphy_clients.DefaultApi()
	try:
			api_response=api_instance.gifs_search_get(api_key,q,limit=20, rating='r')
			lst=list(api_response.data)
			giff= random.choice(lst)
			x=giff.embed_url
	except ApiException as e:
			print("Exception when calling API")
	return x


@client.commands()
async def gif(ctx, *, q='Happy'):
	api_key = 'SZ4VMjJhBbCUvpS238YPrQ5eDfjhKLUW'
	api_instance=giphy_clients.DefaultApi()
	try:
		api_response=api_instance.gifs_search_get(api_key,q,limit=50,rating='r')
		lst=list(api_response.data)
		giff=random.choice(lst)
		await ctx.channel.send(embed_url)
	except ApiException as e:
		print("Exception when calling API")




@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "$help"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$help'):
       helper = ("""
				 $help - opens help menu to list all functions
				 $inspire - gives a random inpirational quote.
				 $fox - gives a random photo of a cute fox
				 $joke - gives a random poor joke (not funny btw)
				 $flirt - random flirts
				 $word - to search the meaning of a word
         $weather - to find weather of a city
				 $rps - Plays rock, paper and scissors with you.
				""")
       await message.channel.send(helper)
			

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(good_words))
    
    if msg.startswith('$flirt'):
       await message.channel.send(random.choice(flirt_lines))

    if msg.startswith("$joke"):
        joke = get_joke()
        await message.channel.send(joke)

    if msg.startswith("$fox"):
        fox = get_fox()
        await message.channel.send(fox)

    if msg.startswith("$cat"):
		#cat=get_cat()
		#await message.channel.send(cat)
        response = requests.get("http://thecatapi.com/api/images/get?format=src&type=gif")
        cat = json.loads(response.data)
        await message.channel.send(cat)
    
    if msg.startswith("$word"):
        await message.channel.send(
            "Enter a word in 10 secs to search it's meaning ( ͡• ͜ʖ ͡• )")
        s1 = await client.wait_for('message', timeout=10)
        y = str(s1.content)
        x = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
        z = str(x + y)
        response = requests.get(z)
        word = json.loads(response.text)
        await message.channel.send(word)

    if msg.startswith("$rps"):
        rpsGame = ['rock', 'paper', 'scissors']
        comp_choice = str(random.choice(rpsGame))
        await message.channel.send("choose rock or paper or scissors!!")
        a1 = await client.wait_for('message', timeout=10)
        user_choice = str(a1.content).lower()

        if user_choice == 'rock':
            if comp_choice == 'rock':
                await message.channel.send("Oh we tied !!!  ( ͡• ͜ʖ ͡• )")
                q1 = str("My choice:" + comp_choice)
                await message.channel.send(q1)
            elif comp_choice == 'paper':
                await message.channel.send("Nice try, I beat you !!  ┗(＾0＾)┓")
                q2 = str("My choice:" + comp_choice)
                await message.channel.send(q2)
            elif comp_choice == 'scissors':
                await message.channel.send(
                    "You beat me. It won't happen again  (┛ಠ_ಠ)┛彡┻━┻")
                q3 = str("My choice:" + comp_choice)
                await message.channel.send(q3)

        if user_choice == 'paper':
            if comp_choice == 'rock':
                await message.channel.send(
                    "You beat me. It won't happen again  (┛ಠ_ಠ)┛彡┻━┻")
                q1 = str("My choice:" + comp_choice)
                await message.channel.send(q1)
            elif comp_choice == 'paper':
                await message.channel.send("Oh no we tied !!!  ( ͡• ͜ʖ ͡• )")
                q2 = str("My choice:" + comp_choice)
                await message.channel.send(q2)
            elif comp_choice == 'scissors':
                await message.channel.send(
                    "Nice try, well you can't win against me  ┗(＾0＾)┓")
                q3 = str("My choice:" + comp_choice)
                await message.channel.send(q3)

        if user_choice == 'scissors':
            if comp_choice == 'rock':
                await message.channel.send(
                    "You won, it will not happen again.  (┛ಠ_ಠ)┛彡┻━┻")
                q1 = str("My choice:" + comp_choice)
                await message.channel.send(q1)
            elif comp_choice == 'paper':
                await message.channel.send(
                    "Hehe you lost. Such a noob you are.  ┗(＾0＾)┓")
                q2 = str("My choice:" + comp_choice)
                await message.channel.send(q2)
            elif comp_choice == 'scissors':
                await message.channel.send(
                    "We tied. Next time I will outwit you  ( ͡• ͜ʖ ͡• )")
                q3 = str("My choice:" + comp_choice)
                await message.channel.send(q3)
    
    if msg.startswith("$weather"):
      await message.channel.send('Enter the name of location for which you need weather data.')
      l = await client.wait_for('message',timeout = 20)
      location = str((l.content).lower())
      a = "https://api.openweathermap.org/data/2.5/weather?q="
      #enter open-weather api key in b
      b = ''
      url = str(a+location+b)
      if len(location) >= 1:
          try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
          except KeyError:
                await message.channel.send(embed=error_message(location))

	#await client.process_commands(message)#this is important idk why its showing an error 


keep_alive()

client.run(os.getenv('DiscTOKEN'))