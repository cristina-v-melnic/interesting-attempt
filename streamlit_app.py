import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write("Hello world!")
st.write("The change syncs instantly to localhost.")


with st.expander("**Exercise 1** Guess my favourite!"):
    st.write("Please create:")
    st.checkbox("A list of comparable things you like ex. movies, books, songs, artists, foods, ice-creams etc.", key="1.1")
    st.checkbox("A selection interface, i.e. drop-down", key="1.2")
    st.checkbox("User clicks on a submit button.", key="1.3")
    st.checkbox("Feedback pop-up on whether the user guessed it or not.", key="1.4")
    st.checkbox("Give your riddle a header with and a short description.", key="1.5")
    st.info("Useful commands: st.header(), st.write(), st.selectbox(), st.select_slider(), st.radio(), st.button(), st.success(), st.error(), st.info(), st.balloons()")


favourite_things = ["Shakira", "Charlie Chaplin", "Jung Kook",
                    "Lady Gaga", "Michael Jackson"]
 
guess = st.selectbox("Which dancer so you think is my No1 inspiration?", options=favourite_things, index=None)
submitted = st.button("Submit!")
 
if (guess and submitted):
    if guess=="Jung Kook":
        st.success("That's correct!")
        st.balloons()
    else:
        st.error("Sadly not. Try again!")
