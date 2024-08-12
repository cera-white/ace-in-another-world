define g = Character("God", color="#9595b9")
define w = Character("Wolf", color="#9595b9")
define k = Character("Knight Captain", color="#9c5636")
define p = Character("Princess", color="#b66b89")
define d = Character("Demon Lord", color="#5b2c37")

image bg_white = Solid("#fff")
image person_2 = "images/person.png"

default encounter_wolf_complete = False
default encounter_knight_complete = False
default encounter_princess_complete = False
default skipped_encounters = 0

transform small: 
    zoom 0.4

transform flip:
    xzoom -1.0

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

label splashscreen:
    scene bg_white

    pause 1.0

    show intro_1
    with dissolve

    pause 2.0

    hide intro_1
    show intro_2
    with dissolve

    pause 2.0

    hide intro_2
    with dissolve

    return

label start:
    stop music fadeout 2.0

    scene bg_white
    with Dissolve(2.0)

    g "Welcome, lost soul."

    g "Your life as you knew it is over, but do not fear."

    g "You have been chosen to be reborn as the champion of a world in peril."

    g "It is up to you to defeat the wicked Demon Lord and restore peace and balance to all."

    g "Now, chosen one, it is time..."

    g "Go forth and save your new world."

    play music "audio/music/Forest Ambience.ogg" fadein 3.0

    scene bg_forest
    with Dissolve(2.0)

    "You wake in a strange forest, the memory of your divine encounter already beginning to fade."

    play sound "audio/sound/Bird Call.ogg" volume 0.3

    show bird at top
    with moveinright

    hide bird
    with moveoutleft

    "A large two-headed bird flies overhead, high above the alien-looking trees. There can be no doubt you’re now in a different world from the one you knew."

    "You rummage through your pockets looking for something useful – but come up empty. No water, no weapon, no map, not even a snack."

    "Before you can even think about facing the Demon Lord, you need to make it out of this forest."

    menu:
        "Where do you go?"

        "North":
            $ forest_direction = "North"
            
        "South":
            $ forest_direction = "South"

        "East":
            $ forest_direction = "East"

        "West":
            $ forest_direction = "West"

    play sound "audio/sound/Walking.ogg" volume 0.5
    "With some sort of plan in mind, you pick a direction and start walking – and hope you don’t get eaten or worse along the way."

    stop music fadeout 1.0

label encounter_wolf:

    scene black
    with dissolve

    "Some time later..."

    scene bg_forest
    with dissolve

    play sound "audio/sound/Wolf Howl.ogg" volume 0.3

    "As you make your way through the forest, an ominous wolf-like howl suddenly sends a chill up your spine."

    menu:
        "What do you do?"

        "Ignore it":
            $ skipped_encounters += 1
            play sound "audio/sound/Walking.ogg" volume 0.5
            "It's not your problem, so you decide to carry on."

            scene black
            with dissolve

            "With laser focus, you make it out of the forest in record time."

            jump encounter_knight
            
        "Investigate":
            play sound "audio/sound/Walking.ogg" volume 0.5
            "Despite the danger, you decide to investigate the source of the beastly howl."

    play music "audio/music/Forest Ambience.ogg" fadein 2.0

    show wolf at top
    with dissolve

    "You arrive at a clearing to find a huge, magnificent silver wolf."

    "It rises and growls as you approach, claws outstretched and poised to strike at the slightest provocation."

    play sound "audio/sound/Wolf Growl.ogg"

    w "Grrr... Your kind is not welcome here, {i}human{/i}. How dare you invade my forest?"

    menu:
        "What do you say?"

        "Sorry, I got lost":
            $ wolf_choice_1 = "lost"
            
        "I'm here to slay you":
            $ wolf_choice_1 = "slay"

    play music "audio/music/Tense.ogg"

    play sound "audio/sound/Swipe.ogg" volume 0.5
    with hpunch

    "Clearly displeased by your answer, the giant wolf attacks, lunging at you and swinging one of its enormous – and very sharp – claws."

    "You leap out of the way just in time. But, with no weapon or shield to defend yourself, your prospects look grim."

    "Fear grips you as you stare up at the great silver wolf, its giant maw opening to reveal massive dripping fangs."

    "You can’t fight the beast, and there’s no way you can outrun it. Death seems inevitable."

    "However, as you lament your fate, you notice a pulsating power beginning to swell within you. Perhaps there’s something you can do, after all..."

    menu:
        "What do you do?"

        "Use fire magic":
            $ magic = "fire"
            play sound "audio/sound/Fire Magic.ogg"
            with hpunch
            "A powerful burst of fire magic erupts from your outstretched hands, scorching your opponent."
            
        "Use earth magic":
            $ magic = "earth"
            play sound "audio/sound/Earth Magic.ogg"
            with hpunch
            "A powerful burst of earth magic erupts from your outstretched hands, crushing your opponent."

        "Use water magic":
            $ magic = "water"
            play sound "audio/sound/Water Magic.ogg"
            with hpunch
            "A powerful burst of water magic erupts from your outstretched hands, submerging your opponent."

        "Use wind magic":
            $ magic = "wind"
            play sound "audio/sound/Wind Magic.ogg"
            with hpunch
            "A powerful burst of wind magic erupts from your outstretched hands, trapping your opponent."

    stop music fadeout 1.0

    hide wolf
    with Dissolve(1.0)

    "Defeated, the great wolf collapses with a cry..."

    play music "audio/music/Happy Meeting.ogg" fadein 2.0
    
    show wolf_girl at small, center
    with Dissolve(1.0)

    "...and, much to your surprise, transforms into a cute girl."

    show wolf_girl at top
    with dissolve

    w "Oh wow, you’re sooooo strong! I didn’t know a human could even have power like that."

    show wolf_girl at bounce, top

    w "Please, allow me to serve you, Master!"

    menu:
        "What do you say?"

        "What are you talking about?":
            $ wolf_choice_2 = "confused"
            
        "You lost once and you’re giving up?":
            $ wolf_choice_2 = "annoyed"

    w "You defeated and humiliated me in battle, so I’ve {i}obviously{/i} fallen head over heels in love with you, Master~!"

    w "Plus... I honestly have a bit of a submission kink."

    show wolf_girl at bounce, top

    w "Anyway, I’ll do anything you want – be your slave, or your housewife, or your mewling fangirl. Please, just let me stay by your side!"

    menu:
        "What do you say?"

        "No, thanks":
            $ wolf_choice_3 = "nope"
            
        "Get stronger and protect your forest instead":
            $ wolf_choice_3 = "redirect"

    play music "audio/music/Forest Ambience.ogg"
    show wolf_girl at small, center
    with dissolve

    w "Alright, fine... I guess you can go. I won’t stop you."

    menu:
        "What do you do?"

        "Thank her for not eating you":
            $ wolf_choice_4 = "thanks"
            
        "Ask for directions":
            $ wolf_choice_4 = "directions"

    "The wolf girl nods in understanding and points toward a distant mountain peak."

    w "There’s a human city that way. I think that’s where their leader lives."

    w "Please, allow me to at least take you to the edge of the forest."
    w "After all, it’d be a shame if the human who bested me died in some horribly pathetic way – like starving to death or something."

    hide wolf_girl
    show wolf at top
    with dissolve

    "The girl transforms back into a giant wolf and leans down to allow you to ride on her back."

    "Grateful for the assistance – albeit a little weirded out by the concept – you hop on and cling tight to your makeshift mount, ready to leave this strange forest behind."

    $ encounter_wolf_complete = True

    stop music fadeout 1.0

    scene black

    "The next day..."

label encounter_knight:

    play music "audio/music/Joyous Town.ogg" fadein 3.0

    scene bg_town
    with Dissolve(2.0)

    "You arrive at a large, bustling city eager to stock up for your journey to battle the Demon Lord."

    "It feels like it’s been ages since you’ve eaten a filling meal or gotten a good night’s sleep, and you still feel naked without a weapon."

    menu:
        "Where do you go first?"

        "Inn":
            $ town_direction = "Inn"
            
        "Restaurant":
            $ town_direction = "Restaurant"

        "Blacksmith":
            $ town_direction = "Blacksmith"

    stop music

    "Suddenly, a blood-curdling scream pierces through the otherwise cheery atmosphere."

    play sound "audio/sound/Scream.ogg" volume 0.3

    "Villager 1" "Help!! Demons!"
    
    "Villager 2" "Everyone, run for cover!"

    play music "audio/music/Tense.ogg"

    show flying_demon at topleft
    with moveintop

    show flying_demon at truecenter
    with moveintop

    "Vicious black-winged beasts, talons outstretched, swoop down from the sky as the townsfolk run for their lives."

    show flying_demon at topright
    with moveintop

    hide flying_demon
    with moveouttop

    "An authoritative voice nearby cuts through the chaos – a knight captain telling her frightened men to stand their ground."

    "It sounds like they’re struggling to keep the demons at bay."

    menu:
        "What do you do?"

        "Help them out":
            show knight_captain at small, center
            with dissolve
            
        "Escape":
            $ skipped_encounters += 1
            play sound "audio/sound/Walking.ogg" volume 0.5
            "It's not your problem, so you decide to get out of there as fast as possible."

            stop music fadeout 1.0

            scene black
            with dissolve

            "Having escaped the demons' attack, you breathe a sigh of relief and carry on with your mission."

            jump encounter_princess


    show flying_demon at topright
    with moveintop

    show flying_demon at truecenter
    with moveintop

    play sound "audio/sound/Slash.ogg" volume 0.5
    with hpunch

    "As you approach, a beautiful woman in highly decorated armor is knocked over and pinned to the ground by one of the flying beasts."

    "Knight" "Captain!!"

    k "Don’t – ugh – worry about me. Focus on your own opponent!"

    "Despite the knight captain’s bravado, things don’t look so good for her."
    "She’s lost her sword and is bleeding heavily from where the demon’s claws are digging into her shoulders."

    menu:
        "What do you do?"

        "Use fire magic":
            $ magic = "fire"
            play sound "audio/sound/Fire Magic.ogg"
            with hpunch
            "Power swells within you. Flames shoot from your hands and knock the demon to the ground."
            
        "Use earth magic":
            $ magic = "earth"
            play sound "audio/sound/Earth Magic.ogg"
            with hpunch
            "Power swells within you. Shards of rock shoot from your hands and knock the demon to the ground."

        "Use water magic":
            $ magic = "water"
            play sound "audio/sound/Water Magic.ogg"
            with hpunch
            "Power swells within you. A wave of water shoots from your hands and knocks the demon to the ground."

        "Use wind magic":
            $ magic = "wind"
            play sound "audio/sound/Wind Magic.ogg"
            with hpunch
            "Power swells within you. A blast of wind shoots from your hands and knocks the demon to the ground."

    stop music fadeout 1.0

    hide flying_demon
    with Dissolve(1.0)

    "You quickly finish the demon off with a follow-up spell."

    play music "audio/music/Happy Meeting.ogg" fadein 2.0

    show knight_captain at small, center
    with dissolve

    "The knight captain looks at you in wide-eyed awe as you help her up."

    show knight_captain at top
    with dissolve

    show knight_captain at bounce, top
    k "Ohmigosh, wow, you’re so strong~! I can’t believe you saved me!"

    menu:
        "What do you say?"

        "Neither can I":
            $ knight_choice_1 = "disbelief"
            
        "Isn’t this your job?":
            $ knight_choice_1 = "annoyed"

        "Not this again" if encounter_wolf_complete:
            $ knight_choice_1 = "dejavu"

    show knight_captain at small, center
    with dissolve

    k "You’re right, I’ve failed as a knight. I’m so ashamed."

    k "It’s like all of my established martial prowess and years of dedication and training flew out the window as soon as you arrived on the scene..."

    show knight_captain at top
    with dissolve

    k "Oh well, guess I’ll have to give it all up and be your doting wifey instead~"

    show knight_captain at bounce, top

    k "You don’t mind having to save me all the time, right? You’re just so good at it!"

    menu:
        "What do you say?"

        "No, thanks":
            $ knight_choice_2 = "nope"
            
        "I have enough problems to deal with":
            $ knight_choice_2 = "busy"

    k "Awwww, you’re such a meanie."

    play sound "audio/sound/Death Cry.ogg" volume 0.3

    "In the background, another knight is viciously torn apart by the demons still rampaging through the city."

    play music "audio/music/Joyous Town.ogg"

    show knight_captain at small, center
    with dissolve

    k "Well, allow me to at least give you some guidance – as a fellow warrior."

    k "Have you heard of the Demon Lord? He’s the one controlling these fiends. With your incredible power, you may be able to defeat him and end this infernal war once and for all."

    k "If there’s anything you require, I will do my best to see that you receive it."

    menu:
        "What do you need?"

        "Some money":
            $ knight_choice_3 = "money"
            
        "A map":
            $ knight_choice_3 = "map"

    show knight_captain at top
    with dissolve

    k "Oh wow, so humble~!"

    show knight_captain at small, center
    with dissolve

    k "*ahem* Very well, I’ll give you what I have."

    k "May you return victorious, my friend."

    "The knight captain hands you a small pouch and offers a proud salute before returning to the fray."

    $ encounter_knight_complete = True

    stop music fadeout 1.0

    scene black
    with dissolve
    
    "You can only hope that you both survive long enough to see your return..."

label encounter_princess:

    play music "audio/music/Somber.ogg" fadein 3.0

    scene bg_demon_castle
    with Dissolve(2.0)

    "After a long and arduous journey, you finally arrive at the Demon Lord’s castle, ready for the climactic battle between the forces of good and evil."

    "This is the task for which you were sent to this world. Failure is not an option."

    "However, as you traverse the dark and gloomy halls of your enemy’s fortress, you encounter surprisingly little resistance."

    show person at left
    show person_2 at flip, right
    with dissolve

    "The only exception is a large, elaborate door guarded by two bored-looking demons wielding spears."

    play sound "audio/sound/Woman Crying.ogg" volume 0.3

    "You can hear the soft sounds of a girl crying on the other side of the door."

    menu:
        "What do you do?"

        "Move on":
            $ skipped_encounters += 1
            stop music fadeout 1.0

            play sound "audio/sound/Walking.ogg" volume 0.5

            scene black
            with dissolve

            "It's not your problem, so you decide to ignore it. You have more important things to worry about – like saving the world."

            jump encounter_demon_lord
            
        "Investigate":
            play music "audio/music/Tense.ogg"
            
            play sound "audio/sound/Sword Clash 1.ogg" volume 0.5
            with hpunch

            "As you approach, the guards move to stop you."

    "Demon 1" "Halt, intruder!"

    "Demon 2" "What business do you have with Her Highness?"

    menu:
        "What do you say?"

        "I’m here to save the girl":
            $ princess_choice_1 = "save"
            
        "I’m here to slay the Demon Lord":
            $ princess_choice_1 = "slay"

    p "Let them in. I wish to speak to this intruder."

    "The guards look at each other in confusion at the soft voice coming from behind the door, but ultimately step aside."

    play music "audio/music/Somber.ogg"

    hide person
    hide person_2
    with dissolve

    show princess at small, center
    with dissolve

    p "Surprised, aren’t you? I bet you’re wondering why the demons are taking orders from a human."

    p "You see, in order to broker peace between our peoples, I’ve agreed to marry the Demon Lord and become his queen."

    menu:
        "What do you say?"

        "You don't look happy about that":
            $ princess_choice_2 = "happy"
            
        "Your marriage won’t last long":
            $ princess_choice_2 = "marriage"

    stop music fadeout 1.0

    p "It matters not. This is my duty as a princess, and I have resigned myself to this fate."

    play music "audio/music/Happy Meeting.ogg" fadein 1.0

    show princess at top
    with dissolve

    p "That said... if some valiant knight were to ask for my hand instead, I would be much obliged."

    menu:
        "What do you say?"

        "I’m no knight":
            $ princess_choice_3 = "knight"
            
        "Why get married at all?":
            $ princess_choice_3 = "married"

    p "But you came all the way here to rescue me, didn’t you?"

    show princess at bounce, top

    p "I am forever in your debt. The only way I could {i}possibly{/i} repay you is to marry you and ask you to rule my kingdom for me."

    p "And, {i}of course{/i}, we would also need to secure the royal line of succession..."

    menu:
        "What do you say?"

        "No, thanks":
            $ princess_choice_4 = "nope"
            
        "Your kingdom needs you":
            $ princess_choice_4 = "redirect"

    show princess at small, center
    with dissolve

    p "Are you certain?"

    p "You would truly turn down all the power and riches offered to royalty?"

    show princess at top
    with dissolve

    show princess at bounce, top

    p "Amazing! I would expect nothing less of my daring rescuer."

    play music "audio/music/Somber.ogg" fadein 1.0

    show princess at small, center
    with dissolve

    p "You’ll find my husband-to-be down the hall with the fire-breathing dragon statues. You can’t miss him."

    p "Be a dear and give him a good beating for me, okay?"

    "Thankful for the princess’ support, you bow politely and continue on your way."

    $ encounter_princess_complete = True

    stop music fadeout 1.0

    scene black
    with dissolve

    "Your foe awaits..."

label encounter_demon_lord:

    play music "audio/music/Alarm.ogg" fadein 3.0

    scene bg_demon_castle
    with Dissolve(2.0)

    "At last, you enter the grand chamber where the Demon Lords sits on his throne."

    show demon_lord at small, center
    with dissolve

    "As you stroll towards him, the Demon Lord rises to meet you, three-pronged spear in hand. He looks you up and down with a sneer."

    play sound "audio/sound/Evil Laugh.ogg" volume 0.5

    d "So, you are the Champion sent by the gods to defeat me. I expected... more."

    "Your entire journey has been to prepare you for this moment."

    "You ready yourself for a fight. The Demon Lord readies himself in kind."

    menu:
        "What do you do?"

        "Use fire magic":
            $ magic = "fire"
            play sound "audio/sound/Fire Magic.ogg"
            scene bg_white
            with hpunch
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of flame." 
            
        "Use earth magic":
            $ magic = "earth"
            play sound "audio/sound/Earth Magic.ogg"
            scene bg_white
            with hpunch
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of earth." 

        "Use water magic":
            $ magic = "water"
            play sound "audio/sound/Water Magic.ogg"
            scene bg_white
            with hpunch
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of water." 

        "Use wind magic":
            $ magic = "wind"
            play sound "audio/sound/Wind Magic.ogg"
            scene bg_white
            with hpunch
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of wind." 

    scene bg_demon_castle
    show demon_lord at small, center
    with Dissolve(2.0)

    "However, as the effects of the magic fade, the Demon Lord remains standing, relatively unscathed."

    d "Hah! Is that all you can do, Champion? What a disappointment."

    play sound "audio/sound/Slash.ogg"
    show demon_lord at top
    with hpunch

    "Seeing an opportunity for a swift victory, the Demon Lord leaps towards you, spear outstretched. He quickly closes the distance between you."
    
    d "You cannot defeat me! DIE!!"

    "It’s now or never..."

    menu:
        "What do you do?"

        "Punch him in the face":
            $ attack = "punch"
            
        "Kick him the groin":
            $ attack = "kick"

    stop music fadeout 1.0
            
    play sound "audio/sound/Wapow.ogg" volume 0.5
    show demon_lord at small, center
    with hpunch

    "The Demon Lord howls and recoils, leaping back to recover from the injury."

    play music "audio/music/Happy Meeting.ogg" fadein 1.0

    d "Ow, ow, ow! You weren’t supposed to actually {i}hurt{/i} me!"

    "You blink in confusion at your enemy across the room."
    
    if attack == "punch":
        "You look down at your still-closed fist, then back at him."
    else:
        "You look down at your still-raised leg, then back at him."

    show demon_lord at bounce, small, center

    d "Wait! No more, please! I surrender."

    d "I won’t attack the humans anymore – oh, and I’ll let their princess go, I promise!"

    menu:
        "What do you say?"

        "Just like that?":
            $ demon_lord_choice_1 = "confused"
            
        "If you say so":
            $ demon_lord_choice_1 = "shrug"

    stop music fadeout 3.0
    
    hide demon_lord
    with dissolve

    "As the Demon Lord runs away, you feel a sense of accomplishment. You managed to do what you set out to do – which is no small feat."

    "However, something keeps nagging at you..."

    "What do you even do once you’ve fulfilled your life’s purpose?"

    "Where will you go? What can you do?"

    play sound "audio/sound/Static.ogg" loop volume 0.5 fadein 2.0
    scene bg_white
    with Dissolve(2.0)

    "..."

    "...Well, looks like it’s time to be reincarnated again."

label end:
    stop sound fadeout 2.0

    scene black
    with Dissolve(2.0)

    "Congratulations! You defeated the Demon Lord and saved the world."

    if skipped_encounters >= 3:
        "Hopefully you can speedrun saving the world just as quickly as last time."
    else:
        "You can only hope you don't run into so many distractions next time..."

    "END"

    return
