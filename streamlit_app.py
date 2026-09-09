import streamlit as st
import pandas as pd
import numpy as np

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

#st.write(guess)
clicker_done = st.button("Submit!") # True or False
 

#if (guess and submitted):
if clicker_done:
    if guess=="Jung Kook":
            st.success("That's correct!")
            st.balloons()
    #elif guess == None:
    #        st.write("")
    else:
            st.error("Sadly not. Try again!")


with st.expander("**Exercise 2** Ultimate trivia"):
    st.write("Please create:")
    st.checkbox("A view with multiple tabs and place your first app there.", key="2.1")
    st.checkbox("One numeric list and one categorical list linked to the favourite things, i.e. publication year and genre.", key="2.2")
    st.checkbox("Wrap up the contents in a pandas dataframe, i.e. columns = [`authors`, `books`, `year`]", key="2.3")
    st.checkbox("Create a 2 question about the 1st and 2nd property, where the contents of the question are randomly appearing. i.e. Who is the `author`(column name) of the book (random item from the `books` column).", key="2.4")
    st.checkbox("Split the screen in two for each question with `st.columns()`",  key="2.5")
    st.checkbox("Give your riddle a header with and a short description.", key="2.6")
    st.info("Useful commands: pd.DataFrame(), st.dataframe(), st.columns(), with col1:, np.random.randint(), np.sort(), st.select_slider(), st.segmented_control(), st.success(), st.error(), st.info(), st.session_state.<var_name>")


peak_activity_approx = [2005, 1920, 2020, 2010, 1995]
dance_style = ["Latin", "Jazz", "Urban", "Experimental", "Jazz"]


dancer_df = pd.DataFrame({
    "dancer": favourite_things,
    "style": dance_style,
    "peak_activity_approx": peak_activity_approx
})

with st.expander("Full dataframe:"):
      st.dataframe(dancer_df)