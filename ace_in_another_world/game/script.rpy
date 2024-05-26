define g = Character("God", color="#9595b9")
define w = Character("Wolf", color="#9595b9")
define k = Character("Knight Captain", color="#9c5636")
define p = Character("Princess", color="#b66b89")
define d = Character("Demon Lord", color="#5b2c37")

transform small: 
    zoom 0.4

label start:
    $ encounter_wolf_complete = False
    $ encounter_knight_complete = False
    $ encounter_princess_complete = False

    scene bg_white

    pause 1.0

    show intro_1
    with Dissolve(1.0)

    pause 2.0

    hide intro_1
    show intro_2
    with Dissolve(1.0)

    pause 2.0

    hide intro_2
    with Dissolve(2.0)

    g "Welcome, lost soul."

    g "Your life as you knew it is over, but do not fear."

    g "You have been chosen to be reborn as the champion of a world in peril."

    g "It is up to you to defeat the wicked Demon Lord and restore peace and balance to all."

    g "Now, chosen one, it is time..."

    g "Go forth and save your new world."

    scene bg_forest
    with Dissolve(2.0)

    "You wake in a strange forest, the memory of your divine encounter already beginning to fade."

    "A small two-headed bird flies overhead, high above the alien-looking trees. There can be no doubt you’re now in a different world from the one you knew."

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

    "With some sort of plan in mind, you pick a direction and start walking – and hope you don’t get eaten or worse along the way."

label encounter_wolf:

    scene black

    "Some time later..."

    scene bg_forest

    "As you make your way through the forest, an ominous wolf-like howl suddenly sends a chill up your spine."

    menu:
        "What do you do?"

        "Ignore it":
            "It's not your problem, so you decide to carry on."

            scene black

            "With laser focus, you make it out of the forest in record time."

            jump encounter_knight
            
        "Investigate":
            "Despite the danger, you decide to investigate the source of the beastly howl."

    show wolf at top

    "You arrive at a clearing to find a huge, magnificent silver wolf."

    "It rises and growls as you approach, claws outstretched and poised to strike at the slightest provocation."

    w "Grrr... Your kind is not welcome here, {i}human{/i}. How dare you invade my forest?"

    menu:
        "What do you say?"

        "Sorry, I got lost":
            $ wolf_choice_1 = "lost"
            
        "I'm here to slay you":
            $ wolf_choice_1 = "slay"

    "Clearly displeased by your answer, the giant wolf attacks, lunging at you and swinging one of its enormous – and very sharp – claws."

    "You leap out of the way just in time. But, with no weapon or shield to defend yourself, your prospects look grim."

    "Fear grips you as you stare up at the great silver wolf, its giant maw opening to reveal massive dripping fangs."

    "You can’t fight the beast, and there’s no way you can outrun it. Death seems inevitable."

    "However, as you lament your fate, you notice a pulsating power beginning to swell within you. Perhaps there’s something you can do, after all..."

    menu:
        "What do you do?"

        "Use fire magic":
            $ magic = "fire"
            "A powerful burst of fire magic erupts from your outstretched hands, scorching your opponent."
            
        "Use earth magic":
            $ magic = "earth"
            "A powerful burst of earth magic erupts from your outstretched hands, crushing your opponent."

        "Use water magic":
            $ magic = "water"
            "A powerful burst of water magic erupts from your outstretched hands, submerging your opponent."

        "Use wind magic":
            $ magic = "wind"
            "A powerful burst of wind magic erupts from your outstretched hands, trapping your opponent."

    "Defeated, the great wolf collapses with a cry..."

    hide wolf
    show wolf_girl at small, center

    "...and, much to your surprise, transforms into a cute girl."

    show wolf_girl at top

    w "Oh wow, you’re sooooo strong! I didn’t know a human could even have power like that."

    w "Please, allow me to serve you, Master!"

    menu:
        "What do you say?"

        "What are you talking about?":
            $ wolf_choice_2 = "confused"
            
        "You lost once and you’re giving up?":
            $ wolf_choice_2 = "annoyed"

    w "You defeated and humiliated me in battle, so I’ve {i}obviously{/i} fallen head over heels in love with you, Master~!"

    w "Plus... I honestly have a bit of a submission kink."

    w "Anyway, I’ll do anything you want – be your slave, or your housewife, or your mewling fangirl. Please, just let me stay by your side!"

    menu:
        "What do you say?"

        "No, thanks":
            $ wolf_choice_3 = "nope"
            
        "Get stronger and protect your forest instead":
            $ wolf_choice_3 = "redirect"

    show wolf_girl at small, center

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

    "The girl transforms back into a giant wolf and leans down to allow you to ride on her back."

    "Grateful for the assistance – albeit a little weirded out by the concept – you hop on and cling tight to your makeshift mount, ready to leave this strange forest behind."

    $ encounter_wolf_complete = True

    scene black

    "The next day..."

label encounter_knight:

    scene bg_town

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

    "Suddenly, a blood-curdling scream pierces through the otherwise cheery atmosphere."

    "Villager 1" "Help!! Demons!"
    
    "Villager 2" "Everyone, run for cover!"

    "Vicious black-winged beasts, talons outstretched, swoop down from the sky as the townsfolk run for their lives."

    "An authoritative voice nearby cuts through the chaos – a knight captain telling her frightened men to stand their ground."

    "It sounds like they’re struggling to keep the demons at bay."

    menu:
        "What do you do?"

        "Help them out":
            show knight_captain at small, center
            
        "Escape":
            "It's not your problem, so you decide to get out of there as fast as possible."

            scene black

            "Having escaped the demons' attack, you breathe a sigh of relief and carry on with your mission."

            jump encounter_princess

    "As you approach, a beautiful woman in highly decorated armor is knocked over and pinned to the ground by one of the flying beasts."

    "Knight" "Captain!!"

    k "Don’t – ugh – worry about me. Focus on your own opponent!"

    "Despite the knight captain’s bravado, things don’t look so good for her."
    "She’s lost her sword and is bleeding heavily from where the demon’s claws are digging into her shoulders."

    hide knight_captain

    menu:
        "What do you do?"

        "Use fire magic":
            $ magic = "fire"
            "Power swells within you. Flames shoot from your hands and knock the demon to the ground."
            
        "Use earth magic":
            $ magic = "earth"
            "Power swells within you. Shards of rock shoot from your hands and knock the demon to the ground."

        "Use water magic":
            $ magic = "water"
            "Power swells within you. A wave of water shoots from your hands and knocks the demon to the ground."

        "Use wind magic":
            $ magic = "wind"
            "Power swells within you. A blast of wind shoots from your hands and knocks the demon to the ground."

    "You quickly finish the demon off with a follow-up spell."

    show knight_captain at small, center

    "The knight captain looks at you in wide-eyed awe as you help her up."

    show knight_captain at top

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

    k "You’re right, I’ve failed as a knight. I’m so ashamed."

    k "It’s like all of my established martial prowess and years of dedication and training flew out the window as soon as you arrived on the scene..."

    show knight_captain at top

    k "Oh well, guess I’ll have to give it all up and be your doting wifey instead~"

    k "You don’t mind having to save me all the time, right? You’re just so good at it!"

    menu:
        "What do you say?"

        "No, thanks":
            $ knight_choice_2 = "nope"
            
        "I have enough problems to deal with":
            $ knight_choice_2 = "busy"

    k "Awwww, you’re such a meanie."

    "In the background, another knight is viciously torn apart by the demons still rampaging through the city."

    show knight_captain at small, center

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

    k "Oh wow, so humble~!"

    show knight_captain at small, center

    k "*ahem* Very well, I’ll give you what I have."

    k "May you return victorious, my friend."

    "The knight captain hands you a small pouch and offers a proud salute before returning to the fray."

    $ encounter_knight_complete = True

    scene black
    
    "You can only hope that you both survive long enough to see your return..."

label encounter_princess:

    scene bg_demon_castle

    "After a long and arduous journey, you finally arrive at the Demon Lord’s castle, ready for the climactic battle between the forces of good and evil."

    "This is the task for which you were sent to this world. Failure is not an option."

    "However, as you traverse the dark and gloomy halls of your enemy’s fortress, you encounter surprisingly little resistance."

    "The only exception is a large, elaborate door guarded by two bored-looking demons wielding spears."

    "You can hear the soft sounds of a girl crying on the other side of the door."

    menu:
        "What do you do?"

        "Move on":
            scene black

            "It's not your problem, so you decide to ignore it. You have more important things to worry about – like saving the world."

            jump encounter_demon_lord
            
        "Investigate":
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

    show princess at small, center

    p "Surprised, aren’t you? I bet you’re wondering why the demons are taking orders from a human."

    p "You see, in order to broker peace between our peoples, I’ve agreed to marry the Demon Lord and become his queen."

    menu:
        "What do you say?"

        "You don't look happy about that":
            $ princess_choice_2 = "happy"
            
        "Your marriage won’t last long":
            $ princess_choice_2 = "marriage"

    p "It matters not. This is my duty as a princess, and I have resigned myself to this fate."

    show princess at top

    p "That said... if some valiant knight were to ask for my hand instead, I would be much obliged."

    menu:
        "What do you say?"

        "I’m no knight":
            $ princess_choice_3 = "knight"
            
        "Why get married at all?":
            $ princess_choice_3 = "married"

    p "But you came all the way here to rescue me, didn’t you?"

    p "I am forever in your debt. The only way I could {i}possibly{/i} repay you is to marry you and ask you to rule my kingdom for me."

    p "And, {i}of course{/i}, we would also need to secure the royal line of succession..."

    menu:
        "What do you say?"

        "No, thanks":
            $ princess_choice_4 = "nope"
            
        "Your kingdom needs you":
            $ princess_choice_4 = "redirect"

    show princess at small, center

    p "Are you certain?"

    p "You would truly turn down all the power and riches offered to royalty?"

    show princess at top

    p "Amazing! I would expect nothing less of my daring rescuer."

    show princess at small, center

    p "You’ll find my husband-to-be down the hall with the fire-breathing dragon statues. You can’t miss him."

    p "Be a dear and give him a good beating for me, okay?"

    "Thankful for the princess’ support, you bow politely and continue on your way."

    $ encounter_princess_complete = True

    scene black

    "Your foe awaits..."

label encounter_demon_lord:

    scene bg_demon_castle

    "At last, you enter the grand chamber where the Demon Lords sits on his throne."

    show demon_lord at small, center

    "As you stroll towards him, the Demon Lord rises to meet you, three-pronged spear in hand. He looks you up and down with a sneer."

    d "So, you are the Champion sent by the gods to defeat me. I expected... more."

    "Your entire journey has been to prepare you for this moment."

    "You ready yourself for a fight. The Demon Lord readies himself in kind."

    menu:
        "What do you do?"

        "Use fire magic":
            $ magic = "fire"
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of flame." 
            
        "Use earth magic":
            $ magic = "earth"
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of earth." 

        "Use water magic":
            $ magic = "water"
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of water." 

        "Use wind magic":
            $ magic = "wind"
            "Powerful magic bursts forth from your fingertips, lighting up the room and surrounding your foe with pillars of wind." 

    "However, as the effects of the magic fade, the Demon Lord remains standing, relatively unscathed."

    d "Hah! Is that all you can do, Champion? What a disappointment."

    show demon_lord at top

    "Seeing an opportunity for a swift victory, the Demon Lord leaps towards you, spear outstretched. He quickly closes the distance between you."

    d "You cannot defeat me! DIE!!"

    "It’s now or never..."

    menu:
        "What do you do?"

        "Punch him in the face":
            $ attack = "punch"
            
        "Kick him the groin":
            $ attack = "kick"

    show demon_lord at small, center

    "The Demon Lord howls and recoils, leaping back to recover from the injury."

    d "Ow, ow, ow! You weren’t supposed to actually {i}hurt{/i} me!"

    "You blink in confusion at your enemy across the room."
    
    if attack == "punch":
        "You look down at your still-closed fist, then back at him."
    else:
        "You look down at your still-raised leg, then back at him."

    d "Wait! No more, please! I surrender."

    d "I won’t attack the humans anymore – oh, and I’ll let their princess go, I promise!"

    menu:
        "What do you say?"

        "Just like that?":
            $ demon_lord_choice_1 = "confused"
            
        "If you say so":
            $ demon_lord_choice_1 = "shrug"

    hide demon_lord

    "As the Demon Lord runs away, you feel a sense of accomplishment. You managed to do what you set out to do – which is no small feat."

    "However, something keeps nagging at you..."

    "What do you even do once you’ve fulfilled your life’s purpose?"

    "Where will you go? What can you do?"

    scene bg_white
    with Dissolve(2.0)

    "..."

    "...Well, looks like it’s time to be reincarnated again."

label end:

    scene black
    with Dissolve(1.0)

    "Congratulations! You defeated the Demon Lord and saved the world."
    
    "END"

    return
