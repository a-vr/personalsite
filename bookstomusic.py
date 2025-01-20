import streamlit as st

### extra st.write statements are being used for spacing purposes 

# CSS to set image width... TO BE USED LATER
image_css = """<style>
    .custom-image {width: 50%; height: auto;}
</style>"""

def app():
    # head of page
    st.title("Books to Music")
    st.write("Welcome to Books to Music, where I set some of the books I've read recently to music that I think matches them.")
    st.write("""This is NOT a book review page, but if you have thoughts about any of these, 
             I would love to hear from you through my contacts page.""" )
    st.write("---")

    # ninth post
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Marigold and Rose x She Said I'm Gloomy")
        with date:
            st.markdown("<p style='text-align: right;'><i>1/19/2025</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""Marigold and Rose is a profound little book that follows twin girls, Marigold and Rose, in their very first year of life. 
            Through this year, they grapple with time, safety, language, loss, and so much more: far more than you'd expect to fit into a neat 55 pages.""")
            st.write("""Marigold's slightly melancholic nature, mixed with her large aspirations for the future, made me think she and the book she narrates 
            would pair perfectly with an anime inspired song.""")
            st.write("""For that reason, I suggest reading this book while listening to 'She Said I'm Gloomy' by Nouvelle Story. The cartoonish and hopeful song 
            invoke such an undescribable variety of emotions that mirror those you find in Marigold and Rose's story. And I would like to think Marigold would find 
            some comfort in the song even though she realizes quickly that life is difficult.""")
        with image1:
            st.image("btmimages/MarigoldAndRose.jpg", use_container_width=True, caption="Marigold and Rose by Louise Glück")
        with image2:
            st.image("btmimages/shesaidimgloomy.jpg", use_container_width=True, caption="Cover Art for She Said I'm Gloomy by Nouvelle Story")
            st.audio("soundbites/she-said-im-gloomy-remastered.mp3")
    st.write("---")
    
    # eighth post 
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*A Face Like Glass x Cloud*")
        with date:
            st.markdown("<p style='text-align: right;'><i>10/19/2024</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""For a lack of better words, the media I choose for this blog is heavily curated (shocking I know). 
            Because of this, when I started reading "A Face Like Glass" by Frances Hardinge, I did not intend to use it for this blog. 
            But I couldn't shake it's hold on me, so now I feel the strong compulsion to throw my thoughts about it into the void.""")
            st.write("""This book eludes description but I will try my best. A young girl with no memories is adopted by a master maker of magical cheeses in 
            an underground kingdom where people have to buy facial expressions. As sheexplores this world, she uncovers classism, mortality, 
            and kleptomancy (an intriguing idea on it's own), among other things.""")
            st.write("""The book stuck with me most for the way it highlights how experience can hurt you. 
            Experience literally mars the main character's face, to a point where she worries she has to erase her memory to fix it. 
            After extending his life, the King finds his wealth of experience dulls any new ones. 
            And with all the artisinal cheeses and concoctions floating around, it becomes evident that a new experience has the potential 
            to kill you.""")
            st.write("""I don't know what all of this means, but it brought to mind the song Cloud by Galdive, featuring floaty vocals and lyrics pondering where "all of this feeling" 
            leaves her. I will leave you now with both and the strong recommendation to read "A Face Like Glass" if it's description interests you.""")
        with image1:
            st.image("btmimages/aFaceLikeGlass.jpg", use_container_width=True, caption="The cover of A Face Like Glass by Frances Hardinge")
        with image2:
            st.image("btmimages/cloudgaldive.jpg", use_container_width=True, caption="Album cover for Cloud by Galdive")
            st.audio("soundbites/cloud.mp3")
    st.write("---")
    
    
    #seventh post 
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Borne x She Looked Like Me!*")
        with date:
            st.markdown("<p style='text-align: right;'><i>9/4/2024</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""I'm too sleepy to pretend to have anything interesting to say so I'm just going to go with, I love Jeff Vandermeer and 
            I love Magdalena Bay, and as such, I absolutely have to have one post about both of them, for me.""")
            st.write("""Borne by Jeff Vandermeer is another fantastic eco-horror read about characters who are really just bystanders to 
            the greater conflict of their world. I could give more of a description but I really think the book is better going in blind, 
            which is the way I read it.""")
            st.write("""Usually when I'm looking for a song for a book, I'm not actually looking. I just listen to music and sometimes relate 
            it to something I've been reading. However in this case, I really really really wanted to find a Magdalena Bay song for this book 
            because I think in general, the duo also is creating a creepy scifi atmosphere that invokes the feeling of being forced into 
            another world. I think I did just that with the song "She Looked Like Me!", which without spoiling too much of Borne, introduces 
            the idea of confronting another version of yourself that they build on throughout their album.""")
        with image1:
            st.image("btmimages/borne.jpg", use_container_width=True, caption="Illustration of Borne by rhunevild from DeviantArt")
        with image2:
            st.image("btmimages/imaginaldisk.jfif", use_container_width=True, caption="Album cover for Imaginal Disk by Magdalena Bay")
            st.audio("soundbites/shelookedlikeme.mp3")
    st.write("---")

    #sixth post 
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Symposium x Everything is Romantic*")
        with date:
            st.markdown("<p style='text-align: right;'><i>7/17/2024</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""It's probably not a secret at this point that my literary preferences lean towards scifi and fantasy. But after enough time, those vast 
            universes can leave me feeling unsatisfied with this seemingly dull reality and I end up taking little ventures into philosophy to cope.""")
            st.write("""The Symposium, in my very-much-not-expert opinion, is a good entry point for reading philosophy because it's really 
            more of a fictional dialogue than anything else. As in much work by Plato, ideas are relayed through speeches by Socrates and other characters, and in this case, 
            centered the god and idea of love.""")
            st.write("""It's easy for me to set this text to classical music, and have you imagine reveling with these philosophers, as they work to understand one of the most 
            fundemental human emotions and you are too inebriated to care. But luckily, charli xcx dropped the Brat album this summer so 
            I get to be a little more creative than that.""")
            st.write("""The song Everything is romantic is short but perfectly encapsulates that true beauty, the Form of Beauty as its called in Symposium, can be anywhere.
            And no matter how dull your surroundings, if you care to look, you'll fall in love, again, and again, and again.""")
        with image1:
            st.image("btmimages/thesymposium.jpg", use_container_width=True, caption="The Penguin Classics cover of The Symposium")
        with image2:
            st.image("btmimages/brat.jpg", use_container_width=True, caption="Brat by Charli xcx album cover (it's supposed to be a little blurry)")
            st.audio("soundbites/everythingisromantic.mp3")
    st.write("---")

    #fifth post 
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Mockingjay x Rather Be*")
        with date:
            st.markdown("<p style='text-align: right;'><i>6/22/2024</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""In honor of the new Hunger Games book being announced, I would like to point out a book-music match that has been on my mind since 2015.""")
            st.write("""Rather Be by Clean Bandit feat. Jess Glyne and Mockingjay by Suzanne Collins (last book of the Hunger Games trilogy).""")
            st.write("""Mockingjay already has many songs literally made for its story since the movie has its own soundtrack. But when I heard this song, I 
            was utterly convinced the movie needs to be rereleased with this at the end. It references taking "a shot in the dark" and Katniss is famously an archer.
            It's a song about finally being with someone after going through a lot to be with them. It's even easy to switch "Exalted in the scene" for "Exalted in the 
            Seam", where Katniss grew up in the books, and it would make so much sense. In conclusion, please add this song to the official Mockingjay soundtrack, 
            thank you :).""")
        with image1:
            st.image("btmimages/katniss_epilogue.jpg", use_container_width=True, caption="Jennifer Lawrence as Katniss in the epilogue of Mockingjay")
        with image2:
            st.image("btmimages/rather_be_video_cover.jpg", use_container_width=True, caption="Youtube thumbnail for the music video of Rather Be by Clean Bandit (feat. Jess Glyne)")
            st.audio("soundbites/rather_be.mp3")
    st.write("---")
    
    # fourth post 
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*My Lady Jane x Horsey*")
        with date:
            st.markdown("<p style='text-align: right;'><i>6/10/2024</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""Is this post just an excuse for me to talk bring up Macross 82-99? Yes. Am I still writing it anyway? Also yes. """)
            st.write("""My Lady Jane is a historical fantasy novel that I cannot describe at all without potentially spoiling it. Just know it is 
                     weird and it is brilliant and there are horses and you should read it.""")
            st.write("""The only thing that has ever surprised me in the way that this book did was listening to Horsey for the first time. 
                     I am a huge fan of the citypop for its funky and uplifting attitude so naturely I listen to a lot of Macross 82-99's 
                     work. Horsey (feat. Sarah Bonito) is unlike anything else I've heard from them. It's still very danceable but it's got a certain desperation 
                     to it that I didn't expect from Macross and I could not for the life of me figure out what this song was for. This book is 
                     the answer.  """)
        with image1:
            st.image("btmimages/myladyjane.jpg", use_container_width=True, caption="The cover of My Lady Jane by Brodi Ashton, Cynthia Hand, and Jodi Meadows.")
        with image2:
            st.image("btmimages/horsey.jpeg", use_container_width=True, caption="The album cover for A Million Miles Away by Macross 82-99")
            st.audio("soundbites/horsey.mp3")

    st.write("---")
    # third post
    # title and date container
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Hitchhikers Guide x Dream Sweet in Sea Major*")
        with date:
            st.markdown("<p style='text-align: right;'><i>5/30/2024</i></p>", unsafe_allow_html=True)
    # text and images container
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""Hitchhiker's Guide is a scifi classic by Douglas Adams that I somehow only recently got around to reading this year 
                     because I got the complete collection on sale at Barnes and Noble. """)
            st.write("""Many years before I ever read Hitchhiker's Guide, while I was still an undecided freshmen in college, I came across
                     the song 'Dream Sweet in Sea Major' off the album Hawaii Part II by Miracle Musical. The song itself paints many absurdist pictures
                     but I find that it all comes back to the first line:""")
            st.write("*Alone at the edge of the universe humming a tune*")
            st.write("""I imagine Hitchhiker's Guide would be the perfect thing to read if I were sitting at the edge of the universe so I think
                     it would be fun to let this song traansport you there when you read it.""")
        with image1:
            st.image("btmimages/hitchhikers.jpg", use_container_width=True, caption="The cover of the version of Hitchhiker's Guide I bought.")
        with image2:
            st.image("btmimages/hawaiipt2.jpg", use_container_width=True, caption="The album cover for Hawaii Part II buy Miracle Musical")
            st.audio("soundbites/dream-sweet-in-sea-major.mp3")

    st.write("---")
    # second post
    # title and date container
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Mortal Dictata x Flowers for All Occasions*")
        with date:
            st.markdown("<p style='text-align: right;'><i>5/24/2024</i></p>", unsafe_allow_html=True)
    # text and images container 
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""Mortal Dictata is the final installment of the Halo Kilo 5 trilogy by Karen Traviss, who has long been 
                     involved in beloved scifi franchises like Star Wars and Gears of War. This book is no exception to 
                     emotion she brings to these vast universes and was by far the book I was most looking forward to in the trilogy.""")
            st.write("""As I am trying not to spoil the book, even though it's a decade old at this point, I will just say that it made
                     me consider the process of reaching ones full potential in a whole new light. To accompany this book, I reccomend 
                     'Flowers for All Occasions' by Blood Cultures, who does a great job with more futuristic feeling music in general, but 
                     also this song specifically matches Staffan's state so well and he really made this book for me.""")
        with image1:
            st.image("btmimages/mortaldictata.jpg", use_container_width=True, caption="Mortal Dictata by Karen Traviss cover") 
        with image2:
            st.image("btmimages/flowersforalloccasions.jpg", use_container_width=True, caption="Flowers for All Occasions by Blood Cultures cover")
            st.audio("soundbites/flowers-for-all-occasions.mp3")
        
    st.write("---")
    # first post
    # title and date container
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*The Southern Reach Trilogy x Dreamland*")
        with date:
            st.markdown("<p style='text-align: right;'><i>5/23/2024</i></p>", unsafe_allow_html=True)
    # text and images container 
    with st.container():
        text, image1, image2 = st.columns((5,3,3))
        with text:
            st.write("""Jeff Vandermeer's Southern Reach trilogy invokes a sense of unease that makes time taste like salt water. 
                     He does a brilliant job describing a pristine natural world that is out to get you.""")
            st.write("""While I was reading this trilogy, a friend (the same friend who recommended the trilogy to me) had me 
                     listen to Ferdous's Dreamland EP. The surrealism of the EP had me leaving it on repeat while reading the last book 
                     of the trilogy, despite being less than 20 minutes long. Especially the track 'Mountain Snow', with a rhythm that feels 
                     like it might skip a beat but you can't be sure, made for a the perfect compliment to these beautiful yet unsettling 
                     books.""")
        with image1:
            st.image("btmimages/annihilation.jpg", use_container_width=True, caption="Cred to Blue J on ArtStation (https://www.artstation.com/artwork/188JZ8)")
        with image2:
            st.image("btmimages/dreamland.jpg", use_container_width=True, caption="Ferdous Dreamland EP cover") 
            javascript_code = """
            <audio controls>
            <source src="soundbites/celestial-kiss-official-visualizer.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>
            """
            st.audio("soundbites/celestial-kiss-official-visualizer.mp3")
    

    
