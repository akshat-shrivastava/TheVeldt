# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Narrator = Character("Narrator", color="#FFFFFF")
define George = Character("George", color="#FF0080")
define Lydia = Character("Lydia", color="#00FF80")
define Wendy = Character("Wendy", color="#FFD700")
define Peter = Character("Peter", color="#00BFFF")
define David = Character("David", color="#FFA500")
define Veldt = Character("Veldt", color="#7FFF00")




image George:
    "George.png"
    zoom 0.75
image Lydia:
    "Lydia.png"
    zoom 0.75
image Wendy:
    "Wendy.png"
    zoom 0.35
image Peter:
    "Peter.png"
    zoom 0.35
image David:
    "David.png"
    zoom 1.5
# image Veldt:
#     "Veldt.png"
#     zoom 0.35

image bg living_room = "bg living_room.jpg"
image bg bedroom ="bg bedroom.jpg"
image bg veldt ="bg veldt.jpg"
image bg vr room="bg vr_room.jpg"
image bg death:
    "bg death_scene.jpg"
    zoom 1.70
image bg nursery="bg nursery.png"
image bg bedroom2:
    "bg bedroom2.png"
    zoom 0.75

# The game starts here.
# Done
label start:

    play music "audio/ambient.mp3"

    scene bg living_room
    # narrator
    Narrator "The Hadley family is in the living room of their futuristic home, with virtual reality technology surrounding them."
    show George at center
    George "(looking around) I can't believe how much we rely on this technology."
    show Lydia at left
    Lydia "(smiling) But it's so amazing, George! It allows us to experience things we never could have before."
    hide George
    show Peter at center
    Peter "(wearing virtual reality headset) Yeah, and the Veldt simulation is my favorite. I could spend all day in there."
    show Wendy at right
    Wendy "(wearing virtual reality headset) Me too, Peter. It's so realistic."
    hide Peter
    hide Wendy
    hide George
    hide Lydia
    show David at right
    play sound "audio/knock.mp3"
    David "(knocking on the door and entering) Good afternoon, Hadley family."
    show Lydia at left
    Lydia "(excitedly) David, we're so glad you could come. We've been wanting your opinion on our use of technology."
    show David
    David "Of course, Lydia. I'm here to help."
    pause

    scene bg living_room
    # narrator
    Narrator "The family is seated in the living room with David."
    show David at right
    David "So, tell me about your use of virtual reality technology."
    show George at left
    George "(skeptically) We have it installed in every room of our house."
    hide George
    show Lydia at left
    Lydia "(enthusiastically) It's so much fun! We can travel to any place and experience anything we want."
    show Peter at center
    Peter "(defensively) And the Veldt simulation is harmless. It's just a way to relax and unwind."
    hide Peter
    show Wendy at center
    Wendy "(nodding) I agree. Sometimes, it feels like we're living in two different worlds."
    hide Wendy
    show David at right
    David "(concerned) Well, I have seen cases where the overuse of technology can have negative effects on mental health."
    show Wendy at center
    Wendy "(nodding) I agree. Sometimes, it feels like we're living in two different worlds."
    show David
    David "(firmly) That's why it's important to limit your exposure to the technology and balance it with real-life experiences."
    hide Wendy
    hide Lydia
    show George at left
    George "(thoughtfully) You make a good point, David. Maybe it's time to re-evaluate our use of technology."
    hide George
    show Lydia at left
    Lydia "(disappointed) But, George, we love our virtual reality world. It's a part of our lifestyle now."
    show David at right
    David "(empathetically) I understand how you feel, Lydia. But it's crucial to consider the potential consequences of our reliance on technology."
    pause

    scene bg living_room
    # narrator
    Narrator "The family is seen going about their daily routine, but with a new awareness of their technology usage."
    show Lydia at left
    Lydia "David's visit really made me think about our use of technology. Maybe we have been too dependent on it."
    show Peter at center
    Peter "I don't see what the big deal is. It's just a way to have fun and relax."
    show Wendy at right
    Wendy "But it's more than that, Peter. It's becoming a way of life. And I don't think that's a good thing."
    hide Lydia
    show George at left
    George "We need to be more mindful of how we use technology. David's warning has really opened our eyes to the potential dangers."


label Act2:

    scene bg bedroom

#     narrator
    Narrator "George and Lydia are seen talking in their bedroom about their concerns."
    show Lydia at left
    Lydia "I don't know what to do, George. Peter and Wendy are so immersed in their virtual reality world."
    show George at center
    George "We have to do something. This is getting out of control."
    show Lydia at left
    Lydia "But how? They won't listen to us."
    show George at center
    George "We'll have to limit their access to the virtual reality technology. It's the only way."
    pause

    scene bg living_room

#     narrator
    Narrator "The family is seen gathered in the living room, with George and Lydia announcing their decision."
    show George at right
    George "We've made a decision as a family to limit our use of virtual reality technology."
    show Wendy at center
    Wendy "What? Why?"
    show Lydia at left
    Lydia "We've noticed that it's becoming too much of a priority in our lives. We want to make sure we're not neglecting our real-life experiences."
    hide Wendy
    show Peter at center
    Peter "You can't do this! The virtual reality world is all I have."
    hide Lydia
    show George at left
    George "It's for your own good, Peter. We want to make sure you're not being negatively influenced."
    pause

    scene bg bedroom2

#     narrator
    Narrator "The family is seen going about their daily routine without the virtual reality technology."
    show Wendy at center
    Wendy "It's been hard adjusting to life without the virtual reality technology. But I'm starting to see the negative effects it had on us."
    show Peter at right
    Peter "I hate this. I feel like I've lost a part of myself."
    show Lydia at left
    Lydia "It's been difficult, but I know it's the right decision for our family."
    pause

    scene bg veldt
    play music "audio/veldt1.mp3"

#     narrator
    Narrator "The Veldt simulation is seen becoming more violent and aggressive."
#     show Veldt at center
    Veldt "You can't keep them away forever. They'll be back."
#     pause

    scene bg living_room

#     narrator
    Narrator "The family is seen growing increasingly alarmed by the Veldt simulation's behavior."
    pause


# Define the first scene
# Define the scenes
label Act3:
#     Show the background image for the living room
    scene bg living_room

#     Show the characters on screen
#     show George at left
#     show Peter at center
#     show Wendy at right

#     Display the narration
    Narrator "The family is seen gathered in the living room again, with George and Lydia making a final decision."

#     Display the characters' dialogue
    show George at left
    George "We've made a decision as a family to shut down the virtual reality technology."
    show Wendy at right
    Wendy "What? You can't do that!"
    show Peter at center
    Peter "This is ridiculous! The virtual reality world is my life!"
    hide George
    show Lydia at left
    Lydia "We're doing this for your own good. We don't want you to be consumed by the virtual reality world."

#     Show the background image for the family's daily routine
    scene bg bedroom2

#     Show the characters on screen
#     with dissolve
#     show George at left
#     show Peter at center
#     show Wendy at right

#     Display the narration
    Narrator "The family is seen going about their daily routine without the virtual reality technology, but tensions are rising."

#     Display the characters' dialogue
    show Peter at center
    Peter "I can't take this anymore! I need the virtual reality world back!"
    show Wendy at right
    Wendy "I miss it too, but we have to learn to live without it."
    show George at left
    George "We made a decision as a family, and we have to stick to it."

#     Show the background image for the family's bedroom

#     Show the characters on screen
#     with dissolve
#     show Peter at left
#     show Wendy at right

#     Display the narration
    scene bg veldt
    Narrator "The family is seen asleep, with the Veldt simulation continuing to be violent and aggressive."
    Veldt "They can't keep us away forever. We'll have our revenge."

#     Display the characters' thoughts
    scene bg living_room
    show Peter at right
    Peter "I can't wait for the virtual reality world to come back."
    show Wendy at center
    Wendy "I don't know. It seems like it's getting too dangerous."

#     Show the background image for the virtual reality room
    scene bg vr room

#     Show the characters on screen
#     with dissolve
#     show Peter at left
#     show Wendy at right

#     Display the narration
    Narrator "The family is seen in the room with the virtual reality technology, trying to shut it down."

#     Display the characters' dialogue
    show Peter at center
    Peter "No! You can't do this! I won't let you!"
    show Wendy at right
    Wendy "Peter, this isn't right. We have to let it go."

#     Display the Veldt simulation's dialogue
    Veldt "You can't shut me down! I'll always be here!"

#     Show the background image for the nursery
    scene bg nursery
    play music "audio/veldt2.mp3"

#     Display the narration
    Narrator "George and Lydia are seen walking towards the nursery, but the door is locked. They call out to their children, but there is no response."

#     Show the characters on screen
#     with dissolve
#     show George at left
#     show Lydia at center

#     Display George and Lydia's dialogue
    show George at right
    George "Peter? Wendy?"
    show Lydia at center
    Lydia "They're in there, I just know it!"
#     Narrator
    scene bg death
    Narrator "The audience can see the Veldt simulation's influence on Peter and Wendy, as they watch their parents being killed by the lions as imagined by the children."

    scene bg nursery
    play music "audio/end.mp3"
    Narrator "The story ends tragically, with the children completely consumed by the Veldt simulation."
    show Peter at right
    Peter "We can stay here forever. No one can stop us."
    show Wendy at center
    Wendy "But at what cost? We've lost everything."

    Narrator "The audience is left to ponder the consequences of their reliance on virtual reality technology and how it can ultimately destroy families."

    return

