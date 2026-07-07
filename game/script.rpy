init python:
    mina_obsession = 0
    jose_identity = 0
    ruby_manipulation = 0
    route_chosen = ""

define m = Character("Mina", color="#ff6b6b")
define j = Character("Jose", color="#4ecdc4")
define r = Character("Ruby", color="#ffb6c1")
define p = Character("Professor Tengen Ruise", color="#a8a8a8")
define v = Character("Veronica", color="#ffd93d")
define tv = Character("TV BROADCASTER", color="#ffffff")
define voice = Character("???", color="#ffffff")
define n = Character("Narrator", color="#d4d4d4")

label splash:
    show text "Valerian Crow X Two Souls Studio's \n Presents" with dissolve at centre
    pause(2)
    hide text with dissolve 
    pause(2)
    return

label start:
    tv "Good Morning"
    tv "We interrupt your morning shows to bring you some shocking news"
    tv "Mina, age 19, is currently being detained at the Summer Valley Detention Center"
    tv "She is suspected of the murder of two individuals"
    
    show text "Victim #1: Jose" with dissolve
    pause(1.5)
    hide text with dissolve

    tv "The first victim has been identified as Jose, age 20"
    tv "A college student and barista at the local SUmmer Valley Cafe"
    tv "...And her unrequited love"

    show text "Victim #2: Ruby" with dissolve
    pause(1.5)
    hide text with dissolve

    tv "The second victim has been identified as Ruby, age 19"
    tv "A computer science major at Summer Valley University"
    tv "Ruby was Jose's girlfriend and Mina's romantic rival"

    tv "The police state the murders may have been caused by obsessive love and possesiveness"
    tv "Mina is currently being questioned by Professor Tengen Ruise"
    tv "A renowned psychologist and therapist brought in to examine this case"

    tv "Stay safe, folks"
    tv "You may never know..."
    tv "Maybe you will be the next victim of an obsessive murder case"
    tv "That's all for today. Thank you for watching"

    n "TV turns off"
    n "Silence fills the room"
    n "The only sound is the hum of fluorescent lights"

    n "You look down at your hands"
    n "All you can see is blood"
    n "Crimson Red"
    n "Your hands, bound together by handcuffs"

    n "Your mind begins to clear...."
    n "Slowly...."
    n "Painfully...."
    n "And you begin to realise what you have become"

    n "Your stomach churns"
    n "But that pain...."
    n "Is nothing compared to the screams echong from behind the door"

    n "A voice you know all too well"
    n "Mina's mother"
    n "Her cries are loud and filled with pain"

    voice "Why?!"
    voice "Why did you do that?!"
    voice "WHy?!"

    n "Her screams begin to fill your heart with guilt"
    n "And you begin to cry"
    n "Not because you are sorry"
    n "But because she is right"
    n "You did it"
    n "And would do it again"

    p "Can ya keep ya voice levels down"
    p "I'm tryna think here"

    n "You look at him"
    n "A pale old man with a beard the size of a bush"
    n "He takes a cup of coffee and begins to sip violently"
    n "He takes a breath once done and says..."

    p "Now that you're done making noise"
    p "Let's get straight into it"

    m "I have nothing to say"

    p "Why don't we start from the begining"

    menu:
        p "Watcha say"
        "I don't want to talk about it":
            p "That's fine"
            p "But you're going to be here a long time"
            p "And I have nothing but time"
            n "He begins to look at me"
            n "He's eyes are patient"
            n "Waiting"
            n "And you realize he is right"
            n "You want someone to know"
            n "You want someone to understand you"
            jump common_route
        "I'll tell you everything":
            p "Good"
            p "That's the first step"
            p "Why not start from the beginning"

label commmon route:
    "I first met Jose 15 years ago"
    "When her family moved into the house next door"

    "I remember that day like yesturday"
    "I was playing on the porch when I saw a truck pass by"
    "It stopped right next to my house"

    "Like any other child, I was intrigued"
    "I ran to the fence and peaked through the gaps"

    "And there she was...."
    "Like a Angel falling from the sky"

    "Blue hair that shimmered in the sunlight"
    "Bright eyes that sparkled with curiosity"
    "A smile that could light up the world"

    "She was the prettiest girl I had ever seen"

    j "Hi there"

    m "Oh hi, how are you?"

    j "I'm great thanks!"
    j "My name is Josephine but everyone calls me Jose"
    j "I'm new here so I hope we can be friends"

    m "Sure I'd love to"

    v "MINAA!!!"
    v "Oh you sneaky little bastard running off when you have work to do"
    
    m "Ahhh, bye Jose! I'll see you next time"

    "I ran back home"
    "And got the beating of my life"

    "But I didn't care"
    "Because I made a new friend"
    "The most beutiful friend in the world"

    "That night, I convinced my parents to invite the new neighbours for dinnner"
    "But my mother seemed...off"
    "But I was too young to understand why"
    "All I cared about was seeing Jose again"

    "She sat next to me at the table"
    "She was so polite and well mannered"
    "Her parents were kind too"

    "But the whole night, I just wanted to be alone with her"

    m "Come on, Jose!, Let me show you my room"

    "I grabbed her hand and dragged her upstairs"
    "We played until dinner was over"
    "And from that night on..."
    "We were inseperable"

    "Years passed"
    "We grew up together"
    "And I was always there for her"

    "But when we started 6th grade...everything changed"
    "I saw her differently, she was'nt just my best friend anymore"
    "She was someone I loved"
    "Someone I wanted to protect, Someone I wanted to be with forever"

    "But I was afraid"
    "What if she did not feel the same?, What if I ruined everything"
    "So  chose not to say anything"

    "I began gong to the gym to build muscle and become stronger"
    "I wanted to protect her from everyone and be the only person she needed"
    "I followed her everywhere"
    "And scared away anyone who tried to get close to her"
    "I treated her like a princess"
    "So then she would not need love from anyone else"

    "I thought she was mine"
    "I thought that if I loved her enough...."
    "She would love me back"

    "Then it happened"
    "Jose began having mental health issues and was later hospitalized for a year"
    "That was the final year of primary school"
    "And the longest year of my life"

    "Luckily that did not affect her studies and she was able to get into highschool"
    "But when she returned she had changed"

    "She no longer just dressed as a tomboy"
    "She decded to identify as a male"
    "She wanted me to use he/him pronouns despite me knowing the truth"

    "And I hated it"
    "I hated seeing my Goddess turn into something I could no longer recognize"

    "But I had no choice but to play along"
    "Because if I did'nt..."
    "I might lose her forever"

    "High school had ended and we decided to go to university together"
    "We were still inseperable"

    "Everyone thought we were dating"
    "And I let them believe it"
    "Because that was the closest I would ever get to having her"

    "Then came 3th of June 2024"
    "The day everything shattered"

    j "MINAA!!! Wake up! We're going to be late for class!"

    "I opened my eyes"
    "She was looking at me beside my bed, already dressed"
    "Her smile was bright, too bright"

    menu:
        "What will you do"
        "Wake up immediately":
            m "Okay, okay! I'm waking up!"
            "I jumped out of bed"
            "I couldn't be late, not today"
            "Today was her birthday and I had a plan"
            "A confession"
            j "Thank god for once you actually liistened!"
            m "Happy Birthday, Josephine"
            j "Aww, you remembered!"
            j "But hurry up! We're going to be late on our first day"
        "Sleep more":
            m "Let me sleep a bit more... I'm tired"
            "I wasn't tired, I was scared"
            "Today was the day I was going to confess"
            "And I was terrified"
            j "There's no tme to sleep, Mina"
            j "We're going to be late for our fisrt day at university"
            m "I completely forgot about that..."
            "I scrambled out of bed almost ruining everything"
            "I had to tell her today"
            m "Happy Birthday by the way"
            j "Thanks! Now hurry up!"

    "I began to dress quickly and leave the house"
    "Jose was outside waiting for me"
    "And we began hurrieddly running to class"
    
    "And during that time, we had our usual conversation"
    "She spoke for minutes on end and I became bored of what she was saying"
    "I only cared about the voice of my Goddess"

    "Until one sentence made me snap back into all of it"

    j "I have a girlfriend now"

    "Everything stopped, the world around me had shattered"
    "My heart....it stopped beating"

    m "What?!"
    m "When? How did this happen?"

    j "We met on a dating app called Bù xiàng nǐ"
    j "He took me out 3 days ago"
    j "I couln't tell you since you were busy at the gym all day"

    "3 Days"
    "3 Days and she was already in love"
    "3 Days and everything I had built...."
    "Everything I had spent my life protectng"
    "Shattered"

    menu:
        "What do you say"
        "I'm happy for you":
            m "I'm....I'm really happy for you Jose"
            m "Really, I am"
            "I lied through my teeth, my heart was bleeding"
            "But I smiled, because that's what she wanted"
            "If she was happy then maybe....that was enough"
            jump route_choice
        "Don't trust anyone you meet online":
            m "Jose....don't trust anyone you meet online"
            m "You don't know who he really is"
            j "Mina, don't be like that!"
            j "He's not like that!"
            m "How do you know? You've only known him for 3 days"
            j "Because.... when I'm with him, I feel like myself"
            j "The real me"
            j "Don't you want me to be happy"
            "I wanted her to be happy"
            "But I wanted her to be happy WITH ME!!!"
            "Not some stranger, not with some....girl!"
            m "....  just don't want you to get hurt"
            j "I won't"
            j "Because Ruby would never hurt me"
            "She said it with such conviction as if she knew him her whole lfe"
            "As if I had never been there"
            jump route_choice

label route_choice:
    "After that day everything changed, I could not stop thinking about Ruby"
    "Who was she and why would Jose chose her"
    "What did she have that I did not"

    "I needed to understand"
    "I needed to see him"

    show text "I NEEDED TO KNOW...." with dissolve 
    pause(1.5)
    hide text with dissolve

    menu:
        n "Whose perspective do you wish to play"
        n "This affects how you see the story"
        n "It is recommended you start with Mina then Jose then Ruby"
        n "But th choice is yours"
        n "Whose perspective do you wish to play"
        "Mina's Perspective":
            $ route_chosen = "mina"
            "I needed to know what made him so special"
            "I needed to to see her happiness for myself"
            "Even if it destroys me"
            jump mina_route
        "Jose's Perspective":
            $ route_chosen = "jose"
            "I needed to understand why she chose him"
            "I needed to see it through her eyes"
            "Why was he so different from me?"
            jump jose_route
        "Ruby's Perspective":
            $ route_chosen = "ruby"
            "I needed to know his game"
            "Was he truly in love wth her?"
            "Or was he playing her heart?"
            jump ruby_route

label mina_route:
    "I started following them"
    "I saw them at the cafe"
    "Ruby was...beautiful"
    "Long, flowing hair"
    "Soft features"
    "Delicate Hands"           
    "She laughed gently and touched her hand"

    "And I felt my blood boil"

    m "How dare he"
    m "How dare he touch her"
    m "How dare he make her smile lke that"
    m "SHE'S MINE"

    "I followed them to the park"
    "They walked hand in hand"
    "She looked at him like she was the sun"

    "And I realized...."
    "She never looked at me like that"

    "All those years of protection"
    "All those years of love"
    "And she looked at a stranger like he was everything"

    "Why"
    "Why wasn't I enough?"

    "I went home that night and cried"
    "I cried until there were no tears left"
    "Then got angry"
    "I got so angry"

    m "She's mine"
    m "She's always been mine"
    m "I protected her, I loved her, I sacrificed everything for her"
    m "And she chooses HIM"

    "I looked at the ring I bought"
    "The ring I was going to give her"
    "The ring that was supposed to make her mine"

    "But she was never mine"
    "She was never going to be mine"
    "Because I was too afraid to tell her how I felt"

    "And now..."
    "Now it was too late"

    "I couldn't take it anymore"
    "I had to see her, I had to her in the eyes"
    "I had to know..."

    "So I asked Jose if I could meet her and she agreed"
    "So I prepared myself and went to the local cafe"
    "And there she was..."

    m "You must be Ruby"

    r "Ah, you must be Mina"
    r "Jose talks about you all the time"
    r "You're his childhood friend, right"

    m "I'm more than a friend, I've known him for 15 years"
    m "I've protected him and I love him"

    r "Oh, I know"
    r "He tells me everything"
    r "How you followed him around, how you scared away anyone who tried to get close to him"
    r "And how you treated him like a possesion"

    m "That's not true!"

    r "Isn't it?"
    r "He told me he felt trapped, Mina"
    r "He told me you smothered him, He told me he needed space"
    r "And I....I gave him space"
    r "I let him breathe, I let him be himself"

    "His words stabbed me like knifes"

    r "You know why he chose me?"
    r "Because I accepted him for who he is"
    r "I don't try change him, I don't try possess him"
    r "I just.... love him"

    "She smiled"
    "That soft, innocent smile"
    "And I wanted to kill her"
    "But I couln't at least not yet"

    "I thought about it for weeks"
    "Every scenario and possibility out there"

    "If I killed him, he would be free"
    "If I killed him, he would be mine"

    "But he would be sad"
    "He would grieve"
    "And then he would hate me"

    "Unless..."
    "I killed him too, unless I set him free from this world"
    "Unless I made sure he was mine forever"

    "In death, he could never leave me"
    "In death, he would be mine eternally"

    "It was twisted, It was wrong"
    "But it was the only way"

    "He could never be with her"
    "He could never be without me"
    "He could only be mine"

    "So I made my plan"
    "I bought a knife"
    "I followed them to their date"
    "And I waited"
    
    "The park was empty, the moon was full"
    "They were sitting on a bench"
    "Holding hands, kissing"

    "I crept closer, my heart was pounding"
    "but my hands were locked in"

    "I could hear his laugh"
    "That beautiful, beautiful laugh"
    "The laugh I would never hear again"

    "And then...."
    "I struck"

    "Ruby fell first"
    "He didn't even scream"
    "He just... collapsed"
    "Blood pooling underneath him"

    "Jose turned, Her eyes were wide"
    "Horrified"

    j "Mina...?"
    j "What...what did you do?"

    m "I'm setting you free"
    m "I'm saving you"

    "She tried to run, but I was too fast"
    "I grabbed her, I held her close"
    "I told her I loved her"

    "And then..."
    "I plunged the knife into her heart"

    j "...Why?"

    "She whispered those words"
    "And then she was gone"

    "I sat there, Holding her body"
    "Crying, Sobbing"
    "Wishing I had said something sooner"
    "Wishing I had confessed"

    "But it was too late"
    "It was always too late"

    show text "Current Time" with dissolve
    pause(1.5)
    hide text with dissolve

    p "And that's what happened?"
    p "You killed them both because you loved her?"

    m "....Yes"

    p "Mina..."
    p "Love isn't about possession"
    p "Love isn't about control"
    p "Love is about letting go"
    p "If you truly loved her...."
    p "You would have let her be happy"

    "He was right"
    "He was so right"
    "But it didn't matter anymore"

    "Because she was gone"
    "And I was alone"
    "The way I always feared"

    show text "Mina End" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    jump ending_choice

label jose_route:
    return

label ruby_route:
    return

label ending_choice:
    scene bg black
    with fade

    "Three perspectives"
    "Three sides of the same tragedy"

    "Now...."
    "You must decide how the story ends"

    menu:
        "Which ending do you want to see"
        "The Murder":
            jump ending_murder
        "The Dream":
            jump ending_dream

label ending_murder:
    m

label ending_dream:
    m

label credits:
    scene bg black
    with fade

    show text "Unlike You" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "A Visual Novel" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)    

    show text "Created for the Toxic Yuri Visual Novel Game Jam" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "Story and Writing : THE DOCTOR" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "Art : Slash" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "Music : THE DOCTOR" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "Programming : THE DOCTOR" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "TO EVERYONE WHO HAS EVER FELT UNSEEN \n YOU ARE NOT ALONE" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "THANK YOU FOR PLAYING!" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    return

