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
        text, image1, image2 = st.columns((4,3,3))
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
            st.write("")
            st.image("btmimages/hitchhikers.jpg", width=273, caption="The cover of the version of Hitchhiker's Guide I bought.")
        with image2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.image("btmimages/hawaiipt2.jpg", width=273, caption="The album cover for Hawaii Part II buy Miracle Musical")

    # second post
    # title and date container
    with st.container():
        title, date = st.columns((3,1))
        with title:
            st.subheader("*Mortal Dictata x Space Cowboy*")
        with date:
            st.markdown("<p style='text-align: right;'><i>5/24/2024</i></p>", unsafe_allow_html=True)
    # text and images container 
    with st.container():
        text, image1, image2 = st.columns((4,3,3))
        with text:
            st.write("""Mortal Dictata is the final installment of the Halo Kilo 5 trilogy by Karen Traviss, who has long been 
                     involved in beloved scifi franchises like Star Wars and Gears of War. This book is no exception to 
                     emotion she brings to these vast universes and was by far the book I was most looking forward to in the trilogy.""")
            st.write("""As I am trying not to spoil the book, even though it's a decade old at this point, I will just say that it made
                     me consider the process of reaching ones full potential in a whole new light. To accompany this book, I reccomend 
                     'Flowers for All Occasions' by Blood Cultures, who does a great job with more futuristic feeling music in general, but 
                     also this song specifically matches Staffan's state so well and he really made this book for me.""")
        with image1:
            st.image("btmimages/mortaldictata.jpg", width=260, caption="Mortal Dictata by Karen Traviss cover") 
        with image2:
            st.write("")
            st.write("")
            st.image("btmimages/flowersforalloccasions.jpg", width=260, caption="Flowers for All Occasions by Blood Cultures cover")
        

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
        text, image1, image2 = st.columns((4,3,3))
        with text:
            st.write("""Jeff Vandermeer's Southern Reach trilogy invokes a sense of unease that makes time taste like salt water. 
                     He does a brilliant job describing a pristine natural world that is out to get you.""")
            st.write("""While I was reading this trilogy, a friend (the same friend who recommended the trilogy to me) had me 
                     listen to Ferdous's Dreamland EP. The surrealism of the EP had me leaving it on repeat while reading the last book 
                     of the trilogy, despite being less than 20 minutes long. Especially the track 'Mountain Snow', with a rhythm that feels 
                     like it might skip a beat but you can't be sure, made for a the perfect compliment to these beautiful yet unsettling 
                     books.""")
        with image1:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.image("btmimages/annihilation.jpg", width=273, caption="Cred to Blue J on ArtStation (https://www.artstation.com/artwork/188JZ8)")
        with image2:
            st.write("")
            st.write("")
            st.image("btmimages/dreamland.jpg", width=273, caption="Ferdous Dreamland EP cover") 

    
            
    # break
    st.write("---")

    