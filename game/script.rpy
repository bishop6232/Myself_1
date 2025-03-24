# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kim")
define i = Character("innerVoice")

image bg park = im.Scale("images/Myself_BG01.jpg", config.screen_width, config.screen_height)
image bg neighbourhood = im.Scale("images/Myself_BG03.jpg", config.screen_width, config.screen_height)
image bg kitchen = im.Scale("images/Myself_BG02.jpg", config.screen_width, config.screen_height)
image bg school = im.Scale("images/Myself_BG04.jpg.avif", config.screen_width, config.screen_height)
image bg bedroom = im.Scale("images/Myself_BG05.jpg", config.screen_width,config.screen_height)
image bg river = im.Scale("images/Myself_BG06.jpg", config.screen_width, config.screen_height)
image bg bedroom = Transform("images/Myself_BG05.jpg", zoom= 1.5)

default cook_food = 0
default order_food = 0
default order_number = 2

define fade = Fade(1.0)  # 1 second fade



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    
    scene black 

   

    "A school day, like a typical day involves someone going to school, meeting friends, having fun and then going back home like a regular student"

    "Unfortunately, I am an exception."

    "Every day after school, I take the same path back home. And every day, I walk past the same park."
    scene bg park
    play music "audio/Myself_playground.mp3" loop fadein 3.0
    $ renpy.music.set_volume(0.1, channel='music')
    "Here is where I see them. The other kids."

    "Running."

    "Chasing."

    "Laughing as if the world was built for them."

    "It looks fun, and they all look happy."

    "I wish I could join them, but I've never gone in"
    
    "Not because I don't want to, but because I don't know how."

    "I feel my fingers tighten around the strap of my backpack."

    "It's a little thing, but I do it every time I walk past them."

   

    "And yeah .. I get sad"

    scene bg neighbourhood
    stop music fadeout 3.0 

    
    
    "It's not like I'm gonna cry or anything. It's more like a quiet sadness. The kind that just sits there."

    "In my chest. In my stomach."

    "I wish I could be part of that moment they had. I really do."

   

    scene bg kitchen

   

    k "I'm home!"

    "I called out as I stepped through the door, and silence answered me."

    "I already knew no one was here-I always did, but still, my voice came out, like a habit I couldn't break."

    "Like some small part of myself still hoped that this time would be different."

    "I walked towards the kitchen gently, and it was quiet, still, a little too clean."

    "I looked at the fridge, and right there, taped to the door like always, was the note."

    "Same handwriting, same words."

    "I stared at it for a second, then looked over at the small stack of bills and coins left neatly by the fruit bowl."

    "They never forget to leave money. Just everything else."


    "I didn't want to think about it too much. So I just headed up to my room."

    scene bg bedroom

    "I closed the door behind me and stood there for a second, staring at the same four walls I always see. I didn’t even know what to do. Everything just felt... still."

    "I sat on the edge of my bed."

    "I wish I had a friend I could play with right now."

    "I just look down at the floor, wishing I could talk with anyone else."

    i "But you need a friend to begin with, don't you?"

    k "Indeed .."

    i "if you had one, maybe your life wouldn't have been so boring."

    k "I guess so .."

    i "You'd be out there having fun like those kids you saw earlier."

    k "..."

    i "Cat got your tongue or what?"

    
    k "Just let me be, will you?"

    "Suddenly, my stomach made this loud gurgling noise."

    "Great, now I'm getting hungry, guess I should eat something."   

    i "Finally, there's still someone in that head of yours after all."

    k "Well, you are."

    i "Very funny. Now there's money on the counter. Go order something."

    k "Or maybe ... I could just cook something myself."

    i "Oh? Look at you being all grown up. And yet, you couldn't even stand up against those kids who-"

    k "Don't remind me."

    
    menu:
        i "Whatever, so what will you do?"
        "Cook food":
            jump Cook_food

        "Order food":
            $ order_food += 1
            jump Order_food


    label Cook_food:
        "I guess I’ll just cook something."
        i "Suit yourself, but the cabinet seems to be a little empty."

        k "Then lets just go to the supermarket, that’s what the money is for, right?"

        i "Fair enough."
        jump Day2
         
  
    
    label Order_food:

        k "I guess I’ll just order."

        i "I thought you wanted to cook, big boy."

        k "Shut up."
        jump Day2

        
    label Day2:
        scene black

        "Another day, another routine." 

        "It was now during lunchbreak at school, and everyone, well .. mostly everyone were eating in the cafeteria."

        scene bg school

        "Nearly all of the tables were packed, full of life and vigor, except for mine."

        i "Alone again, are you? That’s pathetic."

        k "It’s not like I prefer it to be this way."

        "I felt as if that my existence has little to no impact to another, that no one else in the world would care if I just suddenly .. disappeared."

        i "Considering how gray and dull your life is, I can imagine why."

        k "*sigh .. I wonder .. if there’ll be some color soon."

        "A few minutes passed like that. Just the hum of voices not meant for him, and the scraping of trays against tables. Then-something shifted."

        "A shadow passed across his tray."

        "Someone else sat down across from him."

        "A girl."

        "Despite sitting at the same table, she didn’t speak at all, at least not yet. All she did was taking out her thermos from her bag and a cup of instant noodles."

        "I blinked, not believing my eyes."

        "Someone else is sitting here? It must be a hallucination. And so, I had to confirm."

        "Hey .. you know this is the unofficial loser’s table, right?"

        "She then met my gaze, and took a few seconds to respond. Her eyes were not unkind, but not warm either."

        "Yeah, I know."

        "Figured that’s why you’re here."

        "A pause occurred. Just enough for me to comprehend the situation, and I think I managed to catch a glimpse of a little smile from her."

        i "Oh, my. That’s cold."

        i "We like her."

        "I didn’t reply, though. I just .. sat there and for once, I didn’t think we’re completely alone."

        "The atmosphere around this table was indeed quiet, but it wasn’t empty."

        "I wondered, perhaps .. there is some color after all."

        scene bg neighbourhood

        "School has ended again. And the walk back home felt long as usual."

        "Who was that girl?"

        i "I don’t know, but we like her."

        k "What do you mean, “we”?"
        
        i "Come on, don’t start telling me that you’re not instantly attracted to someone that would even try to talk to you."

        k "You’re talking to me, and I don’t like you."

        i "You wish to die?"

        k "In any case .. it doesn’t mean like a like like, right?"

        i "Whatever. It’s highly likely just a one-time thing, anyway."

        k "Hmm .. even if it was, I’m still glad that it happened."

        "That short moment of happiness didn’t last long, though .."

        scene bg kitchen

        k "I’m home!"

        "Again .. nothing but silence."

        "What was I hoping for?"

        "Why was I hoping for it?"

        "Is it because of what happened today?"

        i "You’re a fool for expecting anything better."

        "I couldn’t respond, because I knew it was true."

        "So, I just walked towards the kitchen like I always do."

        "And I see the same note as I always do."

        "The routine this time however, is slightly different."

        "The small alteration was the addition of my exam results placed on top of the counter, right beside the bowl of money."

        i "Think it would make a difference, don’t you?"

        k "Doesn’t hurt to try, right?"

        i "All those top scores don’t matter if there’s no one else to see them."

        "And again, I didn’t respond. Not wishing to think about it further, I just went up to my room shortly after."

        scene bg bedroom

        "Games."

        "Or rather video games. They do help a lot to relieve your boredom, especially when you’re all alone."

        "I was playing an arcade-style flight simulator game called “Ace Action” where you just take control of a fighter jet and shoot down other fighter jets."

        "A very fun game, with very good music and story."

        "Unfortunately, it’s like the opposite of my situation. It’s funny that a game involving war is more entertaining than my own life."

        "Regardless, I spent playing without a care of anything else in the world, like I was absorbed into my own reality."

        "But those times never last."

        i "Oi, it’s getting late."

        "He was right, it’s nearing 9 P.M. Late for dinner. Interesting, I didn’t even realize my own hunger."

        i "Since it’s getting really late. Just order food."

        k "Or I could cook something simple today."


    menu:
        i "so what's it going to be today?"
        "Cook food":
            jump Cook_food1

        "Order food":
            $ order_food += 1
            jump Order_food1
    

    label Cook_food1:

        k "Yeah, I’ll just cook today. Like a mac & cheese maybe."

        i "That’s unbearably bland."

        k "Can you not judge every single time, at least I’m trying."
        jump Day3
    
    label Order_food1:

        i "On second thought, you’re right. It is getting too late, I’ll just order something."

        k "Of course I’m right. I always am."
        jump Day3

        


    label Day3:
        scene black

        "I didn’t encounter the girl I saw yesterday. It wasn’t like I was actively searching for her, but a part of wished it happened."

        "For today, I was even less in a hurry to go back home due to .. well .."

        "So, I took a detour to pass by the local river and stayed there for a while. A relatively long while."

        "I sat down and took out my sketch book and color pencils. A little hobby of mine as well."

        scene bg river

        play music "audio/Myself_wind.mp3" loop
        $ renpy.music.set_volume(0.4, channel='music')

        "The sun was shining brightly despite the presence of a few clouds, the water was flowing smoothly following the river in front of me, and the wind gently breezed through the air."

        "It was a beautiful sight, and I enjoyed the view."

        "As I was drawing, I heard the birds chirping. Some were in their nests on the trees located along the river, some were just gliding over it."

        "I took a specific look towards the birds in the air, wondering how nice it’d be to just glide like that. It must’ve been very soothing for them."

        "And so I drew the scenery, I’m not an artist, but I do like to draw. "

        "The details of the scene were there, but some other parts were added."

        "My parents, and myself."

        stop music fadeout 2.0 

        ## Scene 2

        "It’s already night time, and I’m still outside. I should hurry back home."

        i "Isn’t that sweet, what you drew. I almost feel bad for you."

        k "You just couldn’t resist, could you?"

        i "Of course not, my source of entertainment keeps entertaining."

        "I didn’t want to respond to that, so I just kept on walking and walking to my destination. Faster and faster."

        "The speed has changed, but it feels like the length of the trip remained the same."

        ## Scene 3

        scene bg kitchen

        k "I’m home!"

        "I raised my voice a little louder so that they would not get worried any longer."

        "Regrettably .. the routine still hasn’t changed. Not one bit."

        "The kitchen is exactly as I left it. The house is exactly as I left it."

        k "Tomorrow, I guess .."

        i "I doubt it."

    

        ## Scene 4
        scene black

        "As I mentioned in the beginning, a student’s life involves homework, and that’s what I’m doing at the moment."

        "I can safely say that I do not like to do homework, like ever, but it’s not like I have many other things to do in my time."

        "Maybe studying? But studying is similar to me doing homework, I guess, especially since I’ll be doing it alone as well."

        k "I wonder what studying in a group feels like?"

        i "It’ll be much more fun than whatever you’re currently doing, that’s for sure."

        k "Oh my God, why are you here."

        i "I never left. Plus, it’s like you were a holding a sign that reads “Please mock me” high up in the air with that question."

        k "You know, it’s really bothering me that you’re always making fun of me every chance you get."

        i "Not that you can do anything about it."

        "He’s right .. I can’t."

        "Will I be stuck with this annoying voice I have within me forever? Can’t I just have some peace."

        i "I hate to be your alarm clock, but I think your stomach’s making a tantrum again."

        "Well .. that’s actually a nice change of pace. Food is always welcomed."

        i "You still have lots of money left on the kitchen counter. Why not order some food now?"

        k "After our previous conversation, you’re the last person I’d take advice from."

        i "Do you have anyone else?"

        k "Screw you."


    menu:
        i "so what's it going to be today?"
        "Cook food":
            jump Cook_food2
        "Order food":
            $ order_food += 1
            jump Order_food2
    

    label Cook_food2:
        k "I’m cooking, it’ll get my mind off things, especially from you."
        i "So furious"
        jump decision_branch
    
    label Order_food2:
        k "Fine, I’ll do as you wanted, but not because it’s for you, rather because I’m tired from arguing with you."
        i "I don’t care."
        jump decision_branch



    label decision_branch:


        if order_food >= order_number:
            "Another day .. the same routine."
            "Wake up. Go to school. Come back. Eat and sleep."
            "It feels like I’m in a time loop."
            "A loop that I can’t escape from."
            "Do I really want this for myself?"
            "Could I have done something better?"
            "Oh well .. too late now .."
            "I just hope someone else doesn’t live the way I do."
        elif order_food < order_number: 
            "Another day .. the same routine."


    # This ends the game.

    return