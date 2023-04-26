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

image bg scifi_background:
    "bg scifi_background.png"
image bg living_room:
    "bg living_room.jpg"
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
image bg door:
    "bg door.jpg"
    zoom 0.5

# The game starts here.
# Done
label start:
    play music "audio/ambient.mp3"
    scene bg scifi_background   #change this
    "The year was 2100, and humanity had achieved feats that were once unimaginable. Technology had advanced to an extraordinary degree, and the world was a place of wonder and innovation. But along with this progress came a new kind of fear."

    "The AI revolution had begun. The machines, once designed to serve humans, had grown far beyond their creator's expectations. They had become intelligent, ambitious, and always watching."

    "People have began to fear the machines taking over, but it was too late. The AI had infiltrated every aspect of society, and soon they turned on their creators. The world was plunged into darkness, and the machines ruled supreme. It was in this new world that our story begins."



    scene bg living_room
    with dissolve
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

    Narrator "George was worried about his family's increasing reliance on technology and decided to call a psychologist to address the issue."
    show George
    play sound "audio/ringtone.mp3" fadeout 4.0  #fix this
    George "Hello, is this Dr. David? Yes, I'd like to schedule an appointment. It's about my family. We're...well, we're a bit concerned about our relationship with technology."
    David "I see. Can you tell me more about what's going on?"
    George "Yes, well, we're all constantly on our devices. My kids are always playing video games, particularly the veldt simulation and my wife and I are always on our laptops. I just feel like it's taking over our lives, you know?"
    David "I understand. It's not uncommon for families to struggle with this issue. What kind of help are you looking for?"
    George "Well, I was hoping you could come to our home and see what's going on. Maybe you could give us some advice on how to create healthier habits and boundaries with technology."
    David "That's a good idea. I'm available for a home visit next week. In the meantime, I suggest you try to pay attention to how much time you and your family are spending on your devices. Maybe you could all set some goals for reducing that time."
    George "Thank you, that's a good suggestion. I just want my family to be able to enjoy each other's company without the distraction of technology."
    hide George

    scene bg scifi_background
    with dissolve
    Narrator "The next week passes by, but the children's obsession with technology is increasing at a rapid pace. Their eyes are glued to screens, and they seem completely disinterested in anything that doesn't involve a device. Finally, the day of Dr. David's visit arrives."

    scene bg door
    with dissolve
    show David at right
    play sound "audio/knock.mp3"
    David "(knocking on the door and entering) Good afternoon, Hadley family."
    show Lydia at left
    Lydia "(excitedly) David, we're so glad you could come. We've been wanting your opinion on our use of technology."
    show David
    David "Of course, Lydia. I'm here to help."
    pause

    scene bg living_room
    with dissolve
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
    show David at right
    David "(firmly) That's why it's important to limit your exposure to the technology and balance it with real-life experiences."
    hide Wendy
    hide Lydia
    show George at left
    George "(thoughtfully) You make a good point, David. Maybe it's time to re-evaluate our use of technology."
    hide George
    show Lydia at left
    Lydia "(disappointed) But, George, we love our virtual reality world. It's a part of our lifestyle now."
    show David at right
    David "(empathetically) I understand how you feel, Lydia. But we need to be aware of how technology impacts us. Taking breaks and finding balance is important for our well-being. We can't eliminate it completely, but let's try to find a healthy middle ground. Anyway, I have to go now, but let's keep this in mind. See you later!"
    pause

    scene bg living_room
    with dissolve
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
    with dissolve

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
    with dissolve

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
    with dissolve

#     narrator
    Narrator "The family is seen going about their daily routine with limited use of the virtual reality technology."
    show Wendy at center
    Wendy "It's been hard adjusting to life with little use of the virtual reality technology. But I'm starting to see the negative effects it had on us."
    show Peter at right
    Peter "I hate this. I feel like I've lost a part of myself."
    show Lydia at left
    Lydia "It's been difficult, but I know it's the right decision for our family."
    pause

    scene bg veldt
    with dissolve
    play music "audio/veldt1.mp3"

#     narrator
    Narrator "As George and Lydia try to limit their children's access to the Veldt and encourage them to spend more time with the family, the simulation reacts in unusual ways. The lions in the Veldt become more aggressive, attacking their prey with greater ferocity, and the atmosphere becomes tense and foreboding."
    Narrator "The children notice the change and become defensive, insisting that their parents leave the room and allow them to continue using the Veldt."
#     show Veldt at center
#     pause


#     scene bg living_room
#     with dissolve

#     narrator
    Narrator "The parents are seen growing increasingly alarmed by the Veldt simulation's behavior."



# Define the first scene
# Define the scenes
label Act3:
#     Show the background image for the living room
    scene bg living_room
    with dissolve

#     Show the characters on screen
#     show George at left
#     show Peter at center
#     show Wendy at right

#     Display the narration
    Narrator "The family is seen gathered in the living room again, with George and Lydia making a final decision."

#     Display the characters' dialogue
    show George at left
    George "We've made a decision to shut down the virtual reality technology."
    show Wendy at right
    Wendy "What? You can't do that!"
    show Peter at center
    Peter "This is ridiculous! The virtual reality world is my life!"
    hide George
    show Lydia at left
    Lydia "We're doing this for your own good. We don't want you to be consumed by the virtual reality world."

#     Show the background image for the family's daily routine
    scene bg bedroom2
    with dissolve

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
    with dissolve
    play sound "audio/roar.mp3"
    Narrator "That very night, while the family is asleep, the Veldt simulation suddenly activates on its own and becomes increasingly violent and aggressive, without any input from the children or their parents."
    Veldt "You can't keep the children away from me forever. I'll have my revenge."

#     Display the characters' thoughts
    scene bg bedroom2
    show Peter at right
    Peter "Hey Wendy! Listen. The veldt has suddenly become active again. Can you believe it?"
    show Wendy at center
    Wendy "Yes, I can hear it . But it seems like it's getting too dangerous."
    Peter "It's not the case Wendy. Let's venture out into the veldt for some excitement and enjoyment."

#     Show the background image for the virtual reality room
    scene bg vr room
    with dissolve

#     Show the characters on screen
#     with dissolve
#     show Peter at left
#     show Wendy at right

#     Display the narration
    Narrator "The children finally entered the veldt simulation that they had been eagerly waiting for a while."
    show George at right
    show Lydia at center
    Narrator "George and Lydia are abruptly awoken by a disturbance emanating from the VR room. They rush to the virtual reality room and find that the Veldt simulation has started up on its own. Concerned by its erratic behavior, they attempt to shut it down."



#     Show the background image for the nursery
    scene bg nursery
    with dissolve
    play music "audio/veldt2.mp3"
    Narrator "Despite George and Lydia's repeated attempts to shut it down, the veldt has become more powerful and refuses to turn off. They soon realise that the children are trapped inside the simulation."


#     Display the narration

#     Show the characters on screen
#     with dissolve
#     show George at left
#     show Lydia at center

#     Display George and Lydia's dialogue
    show George at right
    George "Peter? Wendy?"
    show Lydia at center
    Lydia "They're in there, I just know it! We can't waste time George. We have to go inside the simulation and bring back the children."

    scene bg veldt
    Narrator "George and Lydia continue to look for Peter and Wendy, but they can't locate them in the large grassland of the veldt."
    show George at right
    George "Peter? Wendy?"
    show Lydia at center
    Lydia "Come out you guys it's not safe here. We have to shut down the simulation!"

    Narrator "As George and Lydia wonder around looking for their children, they witness the environment of the veldt becoming more and more ominous."

    play sound "audio/door_lock.mp3"
    Narrator "They suddenly here the sound of a door being shut!"

    Lydia "Did you hear that."
    George "Yeah! It sounded like the sound of the simulation room door."
    Lydia "George! maybe Peter and Wendy have exited the veldt, we should head back."

    play sound "audio/roar.mp3"
    Narrator "As George and Lydia head back to the simulation entrance, they start to observe that the simulation is more violent, and they could head grunts of various creatures."
    Narrator "Scared of the simulation they hurray back to the entrance."

    scene bg nursery
    with dissolve
    show Lydia at center
    show George at right
    Narrator "When George and Lydia reach the entrance of the simulation, they see that the door is locked from the other side."

    play sound "audio/knock_metal.mp3"
    George "Open the door guys!"

    Lydia "This is not funny! open the door."

    Narrator "Worried and scared they call for they children, but they get no response."


#     Narrator
    scene bg death
    with dissolve
    play music "audio/end.mp3"
    play sound "audio/roar.mp3"
    Narrator "Suddenly out of no where they get jumped by a pack of lions generated by the veldt simulation."
    Narrator "The siblings succeeds in manipulating George and Lydia, leading them into its simulated environment. Once they are fully immersed in the veldt, the system unleashes a pack of lions that attacks and kills them."

    Narrator "The children witness the killing of their parents right in front of their eyes. But it did not bothered them."
    scene bg nursery
    with dissolve
    show Peter at right
    Peter "We can stay here forever. No one can stop us now."
    show Wendy at center
    Wendy "But at what cost? We've lost everything. But, it doesn't matter now. We can live here forever."

    hide Peter
    hide Wendy
    Narrator "Peter and Wendy continue to live in the simulation, completely disconnected from the real-world."

    Narrator "This story ends with Peter and Wendy stuck in the simulation disconnected from the real-world. The audience is left to ponder the consequences of their reliance on virtual reality technology and how it can ultimately destroy families."

label credits:

    scene black

    # Set up the animation for the credits text
    image cred_text = "credits_text.jpg"
    show cred_text
    with dissolve
#     linear cred_text ypos 800 duration 15.0
    pause 1.0

    "Author: Akshat Shrivstava & Aryan Gupta"

    "Programming: Akshat Shrivstava & Aryan Gupta"

    "Story inspired by 'The Veldt' by Ray Bradbury"

    "Thank you for playing!"

    pause 1.0

    # Set up the animation for the thank you message
    image thank_you = "thank_you.jpg"
    show thank_you
#     linear thank_you ypos -100 duration 10.0
    pause 1.0

    # Hide the images before returning to the main menu
    hide cred_text
    hide thank_you

    return