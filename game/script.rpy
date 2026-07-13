image case = Transform("images/case.jpeg", zoom=0.98)
image detective = Transform("images/detective.jpeg", zoom=1)
image hospital = Transform("images/hospital.jpeg", zoom=0.98)
image jose = Transform("images/jose.png", zoom=1)
image mina = Transform("images/mina.png", zoom=1)
image minaroom = Transform("images/minaroom.jpeg", zoom=0.98)
image park = Transform("images/park.jpeg", zoom=0.98)
image police = Transform("images/police.png", zoom=0.98)
image ruby = Transform("images/ruby.png", zoom=1)
image teacher = Transform("images/teacher.png", zoom=1)

define m = Character("Mina", color="#ff6b6b")
define j = Character("Jose", color="#4ecdc4")
define r = Character("Ruby", color="#ffb6c1")
define p = Character("Professor Tengen Ruise", color="#a8a8a8")
define v = Character("Veronica", color="#ffd93d")
define tv = Character("TV BROADCASTER", color="#ffffff")
define voice = Character("???", color="#ffffff")
define n = Character("Narrator", color="#d4d4d4")

label splash:
    show text "Valerian Crow X Two Souls Studio's \n Presents" with dissolve
    pause(2)
    hide text with dissolve 
    pause(2)
    show text "UNLIKE YOU" with dissolve 
    pause(1.5)
    hide text with dissolve 
    pause(1.5)
    return

label start:
    tv "Good Morning"
    tv "We interrupt your morning shows to bring you some shocking news"
    tv "Mina, age 19, is currently being detained at the Summer Valley Detention Center"
    tv "She is suspected of the murder of two individuals"
    
    show text "Victim #1: Jose" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    scene case
    show jose at right
    tv "The first victim has been identified as Jose, age 20"
    tv "A college student and barista at the local SUmmer Valley Cafe"
    tv "...And her unrequited love"
    hide jose with dissolve
    hide scene case

    show text "Victim #2: Ruby" with dissolve
    pause(1.5)
    hide text with dissolve

    show ruby at right
    tv "The second victim has been identified as Ruby, age 19"
    tv "A computer science major at Summer Valley University"
    tv "Ruby was Jose's girlfriend and Mina's romantic rival"
    hide ruby with dissolve

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

    scene case
    show detective at center
    p "Can ya keep ya voice levels down"
    p "I'm tryna think here"

    n "You look at him"
    n "A pale old man with a beard the size of a bush"
    n "He takes a cup of coffee and begins to sip violently"
    n "He takes a breath once done and says..."

    p "Now that you're done making noise"
    p "Let's get straight into it"

    hide detective
    show mina at center
    m "I have nothing to say"

    hide mina
    show detective at center
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

label common_route:
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

    show jose at center
    j "Hi there"

    hide jose
    show mina at center
    m "Oh hi, how are you?"

    hide mina
    show jose at center
    j "I'm great thanks!"
    j "My name is Josephine but everyone calls me Jose"
    j "I'm new here so I hope we can be friends"

    hide jose
    show mina at center
    m "Sure I'd love to"

    hide mina
    v "MINAA!!!"
    v "Oh you sneaky little bastard running off when you have work to do"
    
    show mina at center
    m "Ahhh, bye Jose! I'll see you next time"
    hide mina

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

    show mina at center
    m "Come on, Jose!, Let me show you my room"
    hide mina

    scene minaroom
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
    scene hospital
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

    scene minaroom
    show jose at center
    j "MINAA!!! Wake up! We're going to be late for class!"
    hide jose

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
            show jose at center
            j "Thank god for once you actually liistened!"
            hide jose
            show mina at center
            m "Happy Birthday, Josephine"
            hide mina
            show jose at center
            j "Aww, you remembered!"
            j "But hurry up! We're going to be late on our first day"
            hide jose
        "Sleep more":
            show mina at center
            m "Let me sleep a bit more... I'm tired"
            hide mina
            "I wasn't tired, I was scared"
            "Today was the day I was going to confess"
            "And I was terrified"
            show jose at center
            j "There's no tme to sleep, Mina"
            j "We're going to be late for our fisrt day at university"
            hide jose
            show mina at center
            m "I completely forgot about that..."
            hide mina
            "I scrambled out of bed almost ruining everything"
            "I had to tell her today"
            show mina at center
            m "Happy Birthday by the way"
            hide mina
            show jose at center
            j "Thanks! Now hurry up!"
            hide jose

    "I began to dress quickly and leave the house"
    "Jose was outside waiting for me"
    "And we began hurrieddly running to class"
    
    "And during that time, we had our usual conversation"
    "She spoke for minutes on end and I became bored of what she was saying"
    "I only cared about the voice of my Goddess"

    "Until one sentence made me snap back into all of it"

    show jose at center
    j "I have a girlfriend now"
    hide jose

    "Everything stopped, the world around me had shattered"
    "My heart....it stopped beating"

    show mina at center
    m "What?!"
    m "When? How did this happen?"
    hide mina

    show jose at center
    j "We met on a dating app called Bù xiàng nǐ"
    j "He took me out 3 days ago"
    j "I couln't tell you since you were busy at the gym all day"
    hide jose

    "3 Days"
    "3 Days and she was already in love"
    "3 Days and everything I had built...."
    "Everything I had spent my life protectng"
    "Shattered"

    menu:
        "What do you say"
        "I'm happy for you":
            show mina at center
            m "I'm....I'm really happy for you Jose"
            m "Really, I am"
            hide mina
            "I lied through my teeth, my heart was bleeding"
            "But I smiled, because that's what she wanted"
            "If she was happy then maybe....that was enough"
            jump route_choice
        "Don't trust anyone you meet online":
            show mina at center
            m "Jose....don't trust anyone you meet online"
            m "You don't know who he really is"
            hide mina
            show jose at center
            j "Mina, don't be like that!"
            j "He's not like that!"
            hide jose
            show mina at center
            m "How do you know? You've only known him for 3 days"
            hide mina
            show jose at center
            j "Because.... when I'm with him, I feel like myself"
            j "The real me"
            j "Don't you want me to be happy"
            hide jose
            "I wanted her to be happy"
            "But I wanted her to be happy WITH ME!!!"
            "Not some stranger, not with some....girl!"
            show mina at center
            m "....  just don't want you to get hurt"
            hide mina
            show jose at center
            j "I won't"
            j "Because Ruby would never hurt me"
            hide jose
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

    n "Whose perspective do you wish to play"
    n "This affects how you see the story"
    n "It is recommended you start with Mina then Jose then Ruby"
    n "But th choice is yours"

    menu:
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

    show mina at center
    m "How dare he"
    m "How dare he touch her"
    m "How dare he make her smile lke that"
    m "SHE'S MINE"
    hide mina

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

    show mina at center
    m "She's mine"
    m "She's always been mine"
    m "I protected her, I loved her, I sacrificed everything for her"
    m "And she chooses HIM"
    hide mina

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

    show mina at center
    m "You must be Ruby"
    hide mina

    show ruby at center
    r "Ah, you must be Mina"
    r "Jose talks about you all the time"
    r "You're his childhood friend, right"
    hide ruby

    show mina at center
    m "I'm more than a friend, I've known him for 15 years"
    m "I've protected him and I love him"
    hide mina

    show ruby at center
    r "Oh, I know"
    r "He tells me everything"
    r "How you followed him around, how you scared away anyone who tried to get close to him"
    r "And how you treated him like a possesion"
    hide ruby

    show mina at center
    m "That's not true!"
    hide mina

    show ruby at center
    r "Isn't it?"
    r "He told me he felt trapped, Mina"
    r "He told me you smothered him, He told me he needed space"
    r "And I....I gave him space"
    r "I let him breathe, I let him be himself"
    hide ruby

    "His words stabbed me like knifes"

    show ruby at center
    r "You know why he chose me?"
    r "Because I accepted him for who he is"
    r "I don't try change him, I don't try possess him"
    r "I just.... love him"
    hide ruby

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
    
    scene park
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

    show jose at center
    j "Mina...?"
    j "What...what did you do?"
    hide jose

    show mina at center
    m "I'm setting you free"
    m "I'm saving you"
    hide mina

    "She tried to run, but I was too fast"
    "I grabbed her, I held her close"
    "I told her I loved her"

    "And then..."
    "I plunged the knife into her heart"

    show jose at center
    j "...Why?"
    hide jose

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

    show detective at center
    p "And that's what happened?"
    p "You killed them both because you loved her?"
    hide detective

    show mina at center
    m "....Yes"
    hide mina

    show detective at center
    p "Mina..."
    p "Love isn't about possession"
    p "Love isn't about control"
    p "Love is about letting go"
    p "If you truly loved her...."
    p "You would have let her be happy"
    hide detective

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
    "My name is Josephine"
    "But I've always hated that name"
    "It's too soft, too feminine"
    "Too... wrong"

    "Ever since I was a child, I felt different"
    "I didn't fit in"
    "I didn't feel like the other girl"
    "I felt like a girl trapped in a girl's body"

    "When I was 5 years old, I refused to wear dresses"
    "My mother cried"
    "She said I was a pretty girl and I was being ungrateful"
    "But I did not feel pretty"
    "I felt wrong"

    "When I was 7,  cut my hair short"
    "My father yelled at me"
    "He said I looked like a boy"
    "And I thought... 'Good'"

    "When I was 9, I started wearing boy's clothes"
    "I was punished, I was told to act like a lady"
    "I was told to be normal"

    "But I wasn't normal and I would never be"
    "Then we moved to a new house"
    "And I met Mina"

    "She was small and shy"
    "But she looked at me like I was the most beutiful thing she had ever seen"
    "And for the first time...."
    "I felt accepted"

    "We became best friends"
    "She never questioned my clothes, she never questioned my short hair"
    "She just... accepted me"

    "I thought she understood"
    "I thought she saw me for who I was"
    "But I was wrong"
    
    "As we grew up, things changed"
    "Mina started getting possesive"
    "She followed me everywhere, she scared anyone who tried to get close to me"
    "She treated me like I was hers"

    "At first, I thought it was sweet"
    "I thought she was protecting me"
    "But then it became suffocating"

    show mina at center
    m "Who were you talking to?"
    m "Why didn't you wait for me?"
    m "You shouldn't be friends with them"
    hide mina

    "She was everywhere, she was always there"
    "And I couldn't breathe"
    "It got so bad that I started having panic attacks"
    "I couldn't sleep, I couldn't eat"
    "I felt like I was drowning"

    "My parents sent me to the hospital"
    scene hospital
    "The psychiatric ward"
    "I stayed there for a year"
    "I was diagnosed with gender dysphoria and anxiety"

    "It was the best year of my life"
    "Because for the first time...."
    "I was surrounded by people who understood"
    "I learned to accept myself"
    "I learned that I was allowed to be who I wanted to be"

    "When I came back, I was ready"
    "I told everyone I wanted to be called Jose"
    "I told everyone I wanted to be seen as male"
    "I cut my hair even shorter"
    "I started binding"

    "And Mina..."
    "Mina smiled and she accepted me"

    "But I knew, I saw the look in her eyes"
    "She hated it, she hated who I was becoming"
    "She wanted the old me"
    "The girl she fell in love with"

    "And university was supposed to be a fresh start"
    "But Mina was still there"
    "Still following me and remaining possesive over me"

    "I felt trapped"
    "I felt like I would never escape"
    "And then...."
    "I met Ruby"

    "We met on the dating app 'Bù xiàng nǐ'"
    "It means 'Unlike You'"
    "I thought it was poetic"

    "Ruby was.... beautiful"
    "He was soft and feminine"
    "He wore dresses and makeup"
    "He was a femboy but he was so confident"
    "So unapologetically himself"

    "And he accepted me, He saw me as a man"
    "He held my hand, he kissed me"
    "And for the first tme in my life..."
    "I felt free"

    show jose at center
    j "Ruby... I have to tell you something"
    j "I'm not... I'm not like other people"
    j "I was born female"
    j "But I Identify as male"
    hide jose

    show ruby at center
    r "I know..."
    r "I've known since we started talkng"
    r "It does not matter to me"
    r "You're Jose"
    r "The person I fell in love with"
    hide ruby

    "I cried, I cred soo much"
    "Because someone finally saw me"
    "Someone finally Understood"

    "I knew Mina wouldn't understand"
    "I knew she would never accept Ruby"
    "So I hide it"
    "But then one day..."
    "I couldn't hide it anymore"

    show jose at center
    j "Mina... I have a girlfriend now"
    hide jose

    "The look on her face was devastating"
    "Pure betrayal and heartbreak"

    "And I felt guilty"
    "I felt like I had betrayed her"
    "I knew she wasn't in love with the real me"
    "But simple a idea of me that she created in her head"

    "But I couln't stop"
    "I loved Ruby and I needed Ruby"
    "He was my escape"

    "So Ruby and I started dating"
    "Not in secret but out in public"
    "And I knew Mina was watching, following us"
    "I had a gut feeling she was planning something"

    "I was extremely scared"
    "But I did not know what to do"
    "Especially since Mina was my best friend"
    "She was the one person who had been there with me for the longest time"
    "I couldn't just abondon her"

    "But I should have"
    "I should have ran, I should have protected Ruby"
    "From such an awful fate"

    "It happened at the park"
    scene park
    "We were sitting on a bench"
    "And we were kissing"
    "And all of a sudden..."
    "Ruby collapsed"

    "Blood was everywhere so I screamed"
    "And then I saw her... Mina"
    "She had a knife"
    "And her eyes... her eyes were empty"

    show jose at center
    j "Mina! What are you doing?"
    hide jose

    show mina at center
    m "I'm saving you and setting you free"
    hide mina

    show jose at center
    j "From what?"
    hide jose

    show mina at center
    m "From him, from the world"
    m "From everyone who wants to take you away from me"
    hide mina

    "I tried my best to run, but she grabbed me"
    "She held me close, I could feel her breath on my neck"

    show mina at center
    m "I've loved you for the past 15 years"
    m "You were mine"
    m "You were always mine"
    hide mina

    show jose at center
    j "Mina... please..."
    j "I was never yours"
    hide jose

    show mina at center
    m "I know"
    m "And because of that I won't allow you to be with anyone else"
    hide mina

    "And then..."
    "I felt the knife penetrate my body"
    "And I fell to the ground"

    "As I lay dying"
    "I thought about everything"
    "My life, identity, love and fear"

    "I thought about how I had spent my whole life running"
    "Running from myself, from others and from the truth"
    "And in the end... I ran too late"

    "I thought about Mina"
    "My best friend, my protector, my jailer"
    "And unfortunatly"
    "My murderer"

    "I should have told her the truth"
    "I should have told her that I was never the girl she loved"
    "I was never hers"

    "But I was too scared"
    "And now...."
    "I would never get the chance"

    jump ending_choice

label ruby_route:
    "My name is Ruby"
    "I'm 19 years old"
    "I'm a computer science major"
    "And I'm a femboy"

    "I wasn't always like this"
    "I used to be a normal boy"
    "But sooner I became bored"
    "Life was so boring, everything was the same"
    "Same clothes, personalities basically same everything"

    "So I decided to change"
    "I grew my hair long and started wearing makeup"
    "I bought dresses and skirts"
    "And I became.... beautiful"

    "From that moment on"
    "People stared at me, whispered about me"
    "And most important of all people wanted me"
    "It was exciting, I felt powerful, I felt in control"

    "But the best part..."
    "The best part was the game"

    "I joined a dating app called Bù xiàng nǐ"
    "It means 'Unlike You'"
    "I thought it was fitting"
    "Because I was unlike everyone"
    
    "I started matching with people"
    "Going on dates, breaking hearts"

    "It was easy, everyone fell for my act"
    "They saw a beautiful, innocent girl"
    "They didn't see the real me"

    "Then...."
    "I met Jose"
    "Jose was different, labelled as male"
    "But I knew, I always know"

    "She was so shy"
    "So unsure of herself"
    "She had vulnerabilities and that was soo... delicious"
    
    "I could see it in her eyes"
    "The longing and confusion"
    "The need to be accepted"
    "She was perfect prey"

    show ruby at center
    r "Hi there, I'm Ruby"
    hide ruby

    show jose at center
    j "Oh! Hi! I'm...I'm Jose"
    j "You're really pretty"
    hide jose

    show ruby at center
    r "Thank you~"
    r "You're not so bad yourself"
    hide ruby

    "She blushed, so easy"
    "We went on a few dates"
    "I played my role perfectly"
    "Sweet, soft, romantic"
    "Everything she needed"

    "She told me about Mina"
    "Her best friend, stalker and prison fuard"
    "I could see the pain in her eyes"
    "The fear, the guilt"

    "And I knew I could use that"

    show ruby at center
    r "Mina sounds so possesive"
    r "You should be careful"
    hide ruby

    show jose at center
    j "She's not... she's not like that"
    j "She just cares about me"
    hide jose

    show ruby at center
    r "Are you sure?"
    r "It sounds like she wants to own you"
    hide ruby

    "Jose was silent, She knew I was right"
    "She just didn't want to admit it"

    "I kissed her forehead"
    "Gentle, Soft, Reassuring"

    show ruby at center
    r "I'm here now, I'll protect you"
    r "I'll never treat you like a possesion"
    hide ruby

    "She cried then thanked me"
    "I could tell that she had already fallen in love with me"
    "So easy"

    "But I wasn't in love with her, I never was"
    "I just loved the game and the chase"
    
    "Jose was a problem"
    "She was broken and confused and I wanted to fix her"
    "I wanted to make her mine"
    "Not because I loved her but because I could"

    "And then... I met Mina"
    "She confronted me at the cafe"
    "She was angry, so angry"
    
    show mina at center
    m "You're Ruby?"
    hide mina

    show ruby at center
    r "Ah, you must be Mina"
    r "Jose talks about you all the time"
    r "You're her childhood friend, right?"
    hide ruby

    "I could see the jealousy in her eyes"
    "She was just like me, she wanted to own Jose"
    "She wanted to control her"
    "But I was better at it"

    show mina at center
    m "I love her"
    hide mina

    show ruby at center
    r "Oh, I know"
    r "She tells me everything"
    hide ruby

    "I told her exactly what she did not want to hear"
    "How Jose felt trapped, how she needed space"
    "How I was the one who saved her"
    "And the look on Mina's face... Priceless"

    show ruby at center
    r "You know why she chose me?"
    r "Because I accept her for who she is"
    r "I don't try change her nor possess her"
    r "I just... love her"
    hide ruby

    "Mina walked away, she was furious"
    "She was broken and most importantly she was planning something"
    "And I knew... This was getting interesting"

    "I knew Mina would try something"
    "I could see it in her eyes"
    "But I didn't care, I was ready"

    "I had been playing this game for many years"
    "And I have always won"
    "But not this time..."

    scene park
    "We were at the park, Jose and I"
    "She was so happy"
    "I saw Mina approaching with a knife"
    "And I laughed"

    "I laughed because I won"
    "I had broken her and taken everything away from her"

    "And then...."
    "The knife went in"
    "Quickly and almost painless and in a moment of seconds..."
    "I collapsed"
    "I could hear Jose and Mina screaming"

    "And as I lay there dying I begin to think of everything"
    "All the games, control and power"
    "In the end... I was just another player"
    "Another life cut short"

    "I thought about Jose"
    "The girl I never loved, I used and most importantly....."
    "Destroyed"

    "I thought about Mina"
    "The mad lover an murderer"
    "Who won in the end"

    "But did she really win"
    "She killed us both and now was alone"
    "I smiled"
    "Even the darkness told me"

    show text "CHECKMATE" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    jump ending_choice

label ending_choice:
    scene bg black
    with fade

    "Three perspectives"
    "Three sides of the same tragedy"

    "Now...."
    "You must decide how the story ends"

    menu:
        "Which ending do you want to see"
        "Mystery #1":
            jump ending_murder
        "Mystery #2":
            jump ending_dream

label ending_murder:
    scene case
    show detective at center
    p "SO...."
    "You killed them both"
    hide detective

    show mina at center
    m "... Yes"
    hide mina

    show detective at center
    p "And how do you feel now, Mina?"
    p "Now that they're gone and you'll never see them again"
    hide detective

    "I thought about it, about Jose"
    "Her smile, her laugh, her voice"

    "I thought about Ruby"
    "His beauty, his confidence and his love for her"

    "And I thought about myself"
    "The monster I had become"

    show mina at center
    m ".... Empty"
    m "I feel.... empty"
    hide mina

    show detective at center
    p "And what about the love?"
    p "The love you felt for her"
    hide detective

    show mina at center
    m "Is it love?"
    m "If you destroy what you love?"
    m "If you kill the goddess you claim to adore"
    hide mina

    show detective at center
    p "No, Mina"
    p "That's not love, that's obsession"
    p "And obsession is just love that forgot to let go"
    hide detective

    "I cried"
    "For the first tme in a long time"
    "Not for myself, Jose or Ruby"

    "I cried for what could have been"
    "If I had confessed, If I had let go"
    "If... I had been brave"

    "But it was too late"
    "I was sentenced to 25 years to life"
    "I'm in a cell now where I'll never see the sun"
    "Nor her again"

    "But sometimes before I sleep "
    "When there is no noise and lights are off"
    "I see her face"

    "Jose"
    "My Josephine, my angel, my victim"
    "And I whsisper to the darkness"

    show mina at center
    m "I'm sorry"
    m "I'm so sorry"
    m "I loved you"
    m "I loved you more than anything"
    m "And I still do"
    hide mina

    "But love is not enough"

    show text "IT NEVER WAS" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1.5)

    jump credits

label ending_dream:
    scene hospital
    "I open my eyes"
    "Everything is bright and white"
    "I'm in a hospital"
    "I can hear the beeping of machines and the smell of antiseptic"

    "And then..."
    "I see her"

    "Jose, she's sleeping"
    "Her head resting on my bed, her hand holding mine"
    "She looks peaceful but tired"

    show mina at center
    m "....Jose?"
    hide mina

    "She raises her head, her eyes open and she sees me"
    "Tears immediatly fill her eyes"

    show jose at center
    j "Mina!"
    j "Mina, you're awake!"
    j "Oj my god, you're awake"
    hide jose

    "She hugs me"

    show jose at center
    j "I thought you were gone"
    j "I thought I had lost you"
    j "I was so scared"
    hide jose

    show mina at center
    m ".... What Happened?"
    hide mina

    show jose at center
    j "You were in a coma, Mina"
    j "For 3 years after a serious car accident"
    j "You... you nearly died"
    hide jose

    "A car accident?"
    "That cannot be right"
    "I remember..."
    "I remember..."

    "The knife"
    "The blood"
    "The murder"

    "But those may have been horrible dreams"
    "Horrible, terrible dreams"
    "Or were they?"

    show jose at center
    j "The doctors said you might never wake up"
    j "But I came here daily never giving up hope"
    j "I spoke to you about everything"
    j "My life, my identity and how I felt"
    hide jose

    show mina at center
    m ".... You did"
    hide mina

    show jose at center
    j "YES!"
    j "I told you how scared and confused I was"
    j "How  wanted to be seen for who I really am"
    hide jose

    "She took my hands, her eyes were sincere"

    show jose at center
    j "Mina... I love you"
    j "In fact I've always loved you"
    j "But I was scared of what you would think, scared of being myself"
    hide jose

    "She's... she's telling me this now?"
    "After everything, After that horrible dream"

    show jose at center
    j "When I thought I was losing you I began to realize something"
    j "Life is too short to be scared"
    j "Life is too scared to hide"
    j "So I want to be honest with both you and me"
    j "I love you"
    hide jose

    "I smiled then cried then held her hand"

    show mina at center
    m "I love you too, Jose"
    hide mina

    show jose at center
    j "I know, I was just too blind to see it"
    hide jose

    "And for the first time in my life..."
    "I felt free"

    "Years passed and Jose and I got married"
    "And Ruby..."
    "He was also a real person"
    "More specifcally Jose's friend"

    "The dreams were just dreams"
    "The nightmares were just nightmares"

    "But sometimes I wonder"
    "What if it was real"

    "But that does not matter"
    "Because my love story is 'UNLIKE YOU'"

    show text "The end" with dissolve
    pause(3.0)
    hide text with dissolve
    pause(1.0)

    jump credits

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

    show text "TO EVERYONE WHO HAS EVER FELT UNSEEN \n YOU ARE NOT ALONE" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    show text "THANK YOU FOR PLAYING!" with dissolve
    pause(1.5)
    hide text with dissolve
    pause(1)

    return