import discord
import asyncio
import time 

client = discord.Client()
@client.event
async def on_ready():
	print("Logged in as :",client.user.name)
	print("ID:",client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('?Y'):
        channelA = str(message.channel)
        #await client.send_message(message.channel, channelA)
        if message.content == "?Ytest div" and channelA == "test-division":
            auteur = str(message.author) 
            roleU = discord.utils.find(lambda r: r.name == "1ere Division", message.author.roles)
            divok = False
            try:
                if roleU.name == "1ere Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "2eme Division", message.author.roles)
            try:
                if roleU.name == "2eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "3eme Division", message.author.roles)
            try:
                if roleU.name == "3eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "4eme Division", message.author.roles)
            try:
                if roleU.name == "4eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "5eme Division", message.author.roles)
            try:
                if roleU.name == "5eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "6eme Division", message.author.roles)
            try:
                if roleU.name == "6eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "7eme Division", message.author.roles)
            try:
                if roleU.name == "7eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "8eme Division", message.author.roles)
            try:
                if roleU.name == "8eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "9eme Division", message.author.roles)
            try:
                if roleU.name == "9eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "10eme Division", message.author.roles)
            try:
                if roleU.name == "10eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "11eme Division", message.author.roles)
            try:
                if roleU.name == "11eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "12eme Division", message.author.roles)
            try:
                if roleU.name == "12eme Division": divok = True
            except: 
                pass
            roleU = discord.utils.find(lambda r: r.name == "13eme Division", message.author.roles)
            try:
                if roleU.name == "13eme Division": divok = True
            except: 
                pass
            if divok == False:
                q0 = ("q5","q1","Vous êtes plutot intéllectuel ou sportif ?")
                q1 = ("q7","q2","Dans le fête comme dans les bagarres, vous êtes plus acteur que spectateur ?")
                q2 = ("q3","q8","Dans les fratries, ce qui compte est de bien s'entendre ?")
                q3 = ("q9","q4","Etre une personne gracieuse est un objectif ?")
                q4 = ("q29","q36","Les bonsaïs vous passionnent ?")
                q5 = ("q10","q6","Les hommes sont amateur de thé ?")
                q6 = ("q12","q11","""Le mot "gros buveur" vous attire""")
                q7 = ("q14","q13","Hiroshima est votre patrie de coeur ?")
                q8 = ("q14","q15","Vous admirez les femmes fortes ?")
                q9 = ("q15","q16","Vous aimeriez travailler dans l'edition ?")
                q10 = ("q17","q18","Kaki seché ou patate douce sechée ?")
                q11 = ("q18","q19","Vous n'etes pas tranquille si vous n'enquetez pas par vous même ?")
                q12 = ("q19","q13","Vous préférez le football ou le base-ball")
                q13 = ("q20","q21","Vous lisez tous les jours ?")
                q14 = ("21","q15","Pour vous être un gros bras ne fait pas tout, il faut aussi avoir un talent literaire ?")
                q15 = ("q22","q28","Vous aimez les grandes femmes ?")
                q16 = ("q29","rt","Admirez vous les femmes douées pour le thé et l'ikébana")
                q17 = ("q30","q23","Les lunettes c'est indispensable ?")
                q18 = ("q25","q24","La culture anglo-saxonne vous attire ?")
                q19 = ("q38","q32","Dans un groupe, vous voudriez être guitariste ?")
                q20 = ("q26","q19","Pour votre supérieur, vous accepteriez d'etre un cobaye ?")
                q21 = ("q27","q22","La St-Valentin et/ou le White day sont important pour vous ?")
                q22 = ("q34","q33","Vous aimeriez vous faire encourager par une jolie femme ?")
                q23 = ("q31","q30","Les femmes aussi doivent etre génereuse ?")
                q24 = ("q23","q25","Vous préferez les sucreries aux repas ?")
                q25 = ("q37","q19","Pour vous la rommance de l'homme c'est lunettes de soleil et moustache ?")
                q26 = ("q32","q33","Vous aver/aimeriez un abri secret ?")
                q27 = ("q33","q26","Vous aimez autant les études que le sport ?")
                q28 = ("q39","q34","Vous préferez les chats que les chiens ?")
                q29 = ("q35","q41","Vous avez plus de 2 paires de lunettes ?")
                q30 = ("rv","q42","Vous êtes/voudriez etres doué en caligraphie ?")
                q31 = ("q42","q37",""""Vous aimez les mots "plan" et "stratagème" ?""")
                q32 = ("rj","q38","Pour vous un homme doit accorder de la valeur a son honneur ?")
                q33 = ("q44","q34","En cas de rénovation le chauffage au sol est important ?")
                q34 = ("q47","rp","Vous êtes un bon calculateur ?")
                q35 = ("q45","q40","Vous ne ferez jamais de traitement pour cheveux ?")
                q36 = ("q41","q46","Vous êtes le cheri a sa mamie ?")
                q37 = ("rr","q43","Vous avez encore votre ami d'enfance ?")
                q38 = ("rx","q37","Vous aimez plus que tout les expériences ?")
                q39 = ("rp","q47","Vous n'avez pas peur des abeilles ?")
                q40 = ("q45","q39","Vous voudirez un beau corp ?")
                q41 = ("rf","q45","Vous feriez tout pour votre ami d'enfance ?")
                q42 = ("q48","rr","Vous préferez le thé au café ?")
                q43 = ("rb","q49","Personne ne peut vous battre en nombre de lettre d'amour ?")
                q44 = ("q43","q47","Vous aimez toujours votre 1er amour ?")
                q45 = ("rz","q51","Vous pouvez/aimeriez parler au chiens ?")
                q46 = ("q45","rf","Vous apliquez le principe un guerrier n'a qu'une parole ?")
                q47 = ("q49","q43","""Le mot "justice" vous fait bouillir le sang ?""")
                q48 = ("rh","q49","Vous créer souvent des embrouille ?")
                q49 = ("rd","q50","Pour vous un homme doit svaoir faire la cuisine ?")
                q50 = ("rk","ri","Personne ne peut vous battre en nombre d'amis ?")
                q51 = ("ri","q50","Il faut bien traiter les personne agées ?")
                ri = ("r","1ere Division")
                rp = ("r","2eme Division")
                rr = ("r","3eme Division")
                rt = ("r","4eme Division")
                rv = ("r","5eme Division")
                rx = ("r","6eme Division")
                rz = ("r","7eme Division")
                rb = ("r","8eme Division")
                rd = ("r","9eme Division")
                rf = ("r","10eme Division")
                rh = ("r","11eme Division")
                rj = ("r","12eme Division")
                rk = ("r","13eme Division")

                FinTest = False
                dirQ = "q0"
                rep = 0
                await client.send_message(message.channel, message.author.mention + "Tu a déclenche le test pour connaitre ta division")
                await client.send_message(message.channel, "Répond 1 pour dire oui ou choisire la première possibilité")
                await client.send_message(message.channel, "Répond 2 pour dire non ou choisire la seconde possibilité")
                await client.send_message(message.channel, "Répond exit pour quitter le test")
                while FinTest == False:
                    rep = 0
                    await client.send_message(message.channel, message.author.mention + " " + eval(dirQ)[2])
                    rep = await client.wait_for_message(timeout=60,author=message.author,channel=message.channel)
                    try:
                        if rep.content == "exit":
                            FinTest = True
                            await client.send_message(message.channel, message.author.mention + " Vous avez quitter le test")
                        elif rep.content == "1":
                                dirQ = eval(dirQ)[0]
                        elif rep.content == "2":
                                dirQ = eval(dirQ)[1]
                        else : await client.send_message(message.channel, message.author.mention + " Réponse invalide")
                        if eval(dirQ)[0] == "r":
                            await client.send_message(message.channel, message.author.mention + " Votre division est la " + eval(dirQ)[1])
                            dirQrole = eval(dirQ)[1]
                            role = discord.utils.find(lambda r: r.name == dirQrole, message.author.server.roles)
                            await client.add_roles(message.author, role)
                            FinTest = True
                    except:
                        FinTest = True
                        await client.send_message(message.channel, message.author.mention + " timeout")
            if divok == True:
                await client.send_message(message.channel, message.author.mention + " Vous faite déja patie d'une division")

print("ok")
client.run("NDE4OTM5Mjk1NzYwNjQ2MTU1.DXo3Kw.xcDF_P8enN27z6nndn0MlLSlx28")
