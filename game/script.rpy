# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Narrator = Character("Narrator")
define George = Character("George")
define Lydia = Character("Lydia")
define Wendy = Character("Wendy")
define Peter = Character("Peter")
define David = Character("David")
define Veldt = Character("Veldt")

# The game starts here.

label start:

    scene bg ./images/living_room.jpg
    # narrator
    Narrator "The Hadley family is in the living room of their futuristic home, with virtual reality technology surrounding them."
    show George
    George "(looking around) I can't believe how much we rely on this technology."
    show Lydia
    Lydia "(smiling) But it's so amazing, George! It allows us to experience things we never could have before."
    show Peter
    Peter "(wearing virtual reality headset) Yeah, and the Veldt simulation is my favorite. I could spend all day in there."
    show Wendy
    Wendy "(also wearing a virtual reality headset) Me too, Peter. It's so realistic."
    show David
    David "(knocking on the door and entering) Good afternoon, Hadley family."
    show Lydia
    Lydia "(excitedly) David, we're so glad you could come. We've been wanting your opinion on our use of technology."
    show David
    David "Of course, Lydia. I'm here to help."
    pause

    scene bg living_room2
    # narrator
    Narrator "The family is seated in the living room with David."
    show David
    David "So, tell me about your use of virtual reality technology."
    show George
    George "(skeptically) We have it installed in every room of our house."
    show Lydia
    Lydia "(enthusiastically) It's so much fun! We can travel to any place and experience anything we want."
    show Peter
    Peter "(defensively) And the Veldt simulation is harmless. It's just a way to relax and unwind."
    show Wendy
    Wendy "(nodding) I agree. Sometimes, it feels like we're living in two different worlds."
    show David
    David "(concerned) Well, I have seen cases where the overuse of technology can have negative effects on mental health."
    show Wendy
    Wendy "(nodding) I agree. Sometimes, it feels like we're living in two different worlds."
    show David
    David "(firmly) That's why it's important to limit your exposure to the technology and balance it with real-life experiences."
    show George
    George "(thoughtfully) You make a good point, David. Maybe it's time to re-evaluate our use of technology."
    show Lydia
    Lydia "(disappointed) But, George, we love our virtual reality world. It's a part of our lifestyle now."
    show David
    David "(empathetically) I understand how you feel, Lydia. But it's crucial to consider the potential consequences of our reliance on technology."
    pause

    scene bg living_room3
    # narrator
    Narrator "The family is seen going about their daily routine, but with a new awareness of their technology usage."
    show Lydia voiceover
    Lydia "David's visit really made me think about our use of technology. Maybe we have been too dependent on it."
    show Peter voiceover
    Peter "I don't see what the big deal is. It's just a way to have fun and relax."
    show Wendy voiceover
    Wendy "But it's more than that, Peter. It's becoming a way of life. And I don't think that's a good thing."
    show George voiceover
    George "We need to be more mindful of how we use technology. David's warning has really opened our eyes to the potential dangers."


label Act2:

    scene bg_bedroom
    # narrator
    Narrator "George and Lydia are seen talking in their bedroom about their concerns."
    show Lydia at center
    Lydia "I don't know what to do, George. Peter and Wendy are so immersed in their virtual reality world."
    show George at right
    George "We have to do something. This is getting out of control."
    show Lydia at center
    Lydia "But how? They won't listen to us."
    show George at right
    George "We'll have to limit their access to the virtual reality technology. It's the only way."
    pause

    scene bg_living_room
    # narrator
    Narrator "The family is seen gathered in the living room, with George and Lydia announcing their decision."
    show George at right
    George "We've made a decision as a family to limit our use of virtual reality technology."
    show Wendy at center
    Wendy "What? Why?"
    show Lydia at left
    Lydia "We've noticed that it's becoming too much of a priority in our lives. We want to make sure we're not neglecting our real-life experiences."
    show Peter at right
    Peter "You can't do this! The virtual reality world is all I have."
    show George at left
    George "It's for your own good, Peter. We want to make sure you're not being negatively influenced."
    pause

    scene bg_living_room
    # narrator
    Narrator "The family is seen going about their daily routine without the virtual reality technology."
    Wendy "It's been hard adjusting to life without the virtual reality technology. But I'm starting to see the negative effects it had on us."
    Peter "I hate this. I feel like I've lost a part of myself."
    Lydia "It's been difficult, but I know it's the right decision for our family."
    pause

    scene bg_Veldt_simulation
    # narrator
    Narrator "The Veldt simulation is seen becoming more violent and aggressive."
    Veldt "You can't keep them away forever. They'll be back."
    pause

    scene bg_living_room
    # narrator
    Narrator "The family is seen growing increasingly alarmed by the Veldt simulation's behavior."
    pause


# Define the first scene
# Define the scenes
label Act3:
    # Show the background image for the living room
    show bg living_room
    # Show the characters on screen
    with dissolve
    show George at left
    show Peter at center
    show Wendy at right
    # Display the narration
    "The family is seen gathered in the living room again, with George and Lydia making a final decision."
    # Display the characters' dialogue
    George "We've made a decision as a family to shut down the virtual reality technology."
    Wendy "What? You can't do that!"
    Peter "This is ridiculous! The virtual reality world is my life!"
    show Lydia at left
    Lydia "We're doing this for your own good. We don't want you to be consumed by the virtual reality world."


    # Show the background image for the family's daily routine
    show bg daily_routine
    # Show the characters on screen
    with dissolve
    show George at left
    show Peter at center
    show Wendy at right
    # Display the narration
    "The family is seen going about their daily routine without the virtual reality technology, but tensions are rising."
    # Display the characters' dialogue
    Peter "I can't take this anymore! I need the virtual reality world back!"
    Wendy "I miss it too, but we have to learn to live without it."
    George "We made a decision as a family, and we have to stick to it."


    # Show the background image for the family's bedroom
    show bg bedroom
    # Show the characters on screen
    with dissolve
    show Peter at left
    show Wendy at right
    # Display the narration
    "The family is seen asleep, with the Veldt simulation continuing to be violent and aggressive."
    Veldt "They can't keep us away forever. We'll have our revenge."
    # Display the characters' thoughts
    Peter "I can't wait for the virtual reality world to come back."
    Wendy "I don't know. It seems like it's getting too dangerous."


    # Show the background image for the virtual reality room
    show bg virtual_reality_room
    # Show the characters on screen
    with dissolve
    show Peter at left
    show Wendy at right
    # Display the narration
    "The family is seen in the room with the virtual reality technology, trying to shut it down."
    # Display the characters' dialogue
    Peter "No! You can't do this! I won't let you!"
    Wendy "Peter, this isn't right. We have to let it go."
    # Display the Veldt simulation's dialogue
    Veldt "You can't shut me down! I'll always be here!"


    # Show the background image for the nursery
    show bg nursery
    
    # Display the narration
    "George and Lydia are seen walking towards the nursery, but the door is locked. They call out to their children, but there is no response."
    # Display George and Lydia's dialogue
    George "Peter? Wendy?"
    Lydia "They're in there, I just know it!"
    # Show the characters on screen
    with dissolve
    show George at left
    show Lydia at center
    # Transition to the next scene



    return

