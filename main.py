import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import time
import requests
import sqlite3

#creates a table using sqLite3, stores user responses and the user id + top genre associated to that id

conn = sqlite3.connect('user_responses.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS responses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    energy_preference TEXT,
                    feeling_preference TEXT,
                    vocals_preference TEXT,
                    listening_location TEXT,
                    tempo_preference TEXT,
                    instrument_preference TEXT,
                    tempo TEXT,
                    epic_songs_preference TEXT,
                    user_id INTEGER,
                    top_genre TEXT
                    )''')
conn.commit()


conn = sqlite3.connect("user_responses.db")
cursor = conn.cursor()

#begin developing my front end using streamlit

st.set_page_config(page_title="Music Personality Quiz", layout="centered")

#initalize a genre class, has two attributes, its name and weight
class Genre:
    def __init__(self, name):
        self.name = name
        self.weight = 0  
#define a function for the genre class, allowing it to add weight to it
    def add_weight(self, weight):
        self.weight += weight
#create a bunch of instances of said genre class (objects)
class Pop(Genre):
    def __init__(self):
        super().__init__("Pop")
        self.weight = 0  

class Rock(Genre):
    def __init__(self):
        super().__init__("Rock")
        self.weight = 0

class Metal(Genre):
    def __init__(self):
        super().__init__("Metal")
        self.weight = 0

class Jazz(Genre):
    def __init__(self):
        super().__init__("Jazz")
        self.weight = 0


class Electronic(Genre):
    def __init__(self):
        super().__init__("Electronic")
        self.weight = 0


class Blues(Genre):
    def __init__(self):
        super().__init__("Blues")
        self.weight = 0


class HipHop(Genre):
    def __init__(self):
        super().__init__("Hip-Hop")
        self.weight = 0

class Indie(Genre):
    def __init__(self):
        super().__init__("Indie")
        self.weight = 0


class Classical(Genre):
    def __init__(self):
        super().__init__("Classical")
        self.weight = 0

class Reggae(Genre):
    def __init__(self):
        super().__init__("Reggae")
        self.weight = 0

class Punk(Genre):
    def __init__(self):
        super().__init__("Punk")
        self.weight = 0

class Folk(Genre):
    def __init__(self):
        super().__init__("Folk")
        self.weight = 0

class Ambient(Genre):
    def __init__(self):
        super().__init__("Ambient")
        self.weight = 0

class RnB(Genre):
    def __init__(self):
        super().__init__("R&B")
        self.weight = 0

class Experimental(Genre):
    def __init__(self):
        super().__init__("Experimental")
        self.weight = 0

class Progressive(Genre):
    def __init__(self):
        super().__init__("Progressive")
        self.weight = 0
        
class KPop(Genre):
    def __init__(self):
        super().__init__("K-Pop")
        self.weight = 0
        

#define a question class, give it three attributes, 
#the question itself, the answers, and the weights associated

class Question:
    def __init__(self, question_text, options, weights):
        self.question_text = question_text
        self.options = options
        self.weights = weights  

#define a function to get the  weight to the corresponding answer
    def get_answer_weight(self, answer):
        return self.weights.get(answer, 0)
#intalize the genre objects and store them in a dictonary
genres = {
    "Pop": Pop(),
    "Rock": Rock(),
    "Metal": Metal(),
    "Jazz": Jazz(),
    "Electronic": Electronic(),
    "Blues": Blues(),
    "Hip-Hop": HipHop(),
    "Indie": Indie(),
    "Classical": Classical(),
    "Reggae": Reggae(),
    "Punk": Punk(),
    "Folk": Folk(),
    "Ambient": Ambient(),
    "RnB": RnB(),
    "Experimental": Experimental(),
    "Progressive": Progressive(),
    "K-Pop": KPop()
}

#more frontend development
st.title("🎵 Music Genre Quiz 🎵")
st.write("Select the genres you enjoy, and we'll find music recommendations for you!")

st.divider()

st.image("https://daily.jstor.org/wp-content/uploads/2023/01/good_times_with_bad_music_1050x700.jpg", caption="Music for Any Mood!")


#create a list of the objects in the Question Class, associate weights to each answer
questions = [
    Question(
        "What type of energy do you prefer in your music?",
        ["Calm and Chill", "High-energy and Aggressive", "Something in between"],
        {
            "Calm and Chill": {"Ambient": 3, "Classical": 2, "Jazz": 2, "Folk": 1, "Blues": 1, "Reggae": 1, "Hip-Hop" : 2},
            "High-energy and Aggressive": {"Metal": 5, "Rock": 2, "Hip-Hop": 2, "Punk": 1, "K-Pop": 1},
            "Something in between": {"Pop": 4, "Indie": 2, "RnB": 1, "Reggae": 1, "Rock": 1, "K-Pop": 1, "Hip-Hop" : 2},
        }
    ),
    Question(
        "How do you want to feel while listening to music?",
        ["Relaxed", "Empowered", "Excited"],
        {
            "Relaxed": {"Ambient": 3, "Classical": 2, "Jazz": 2, "Folk": 1, "Blues": 3, "Reggae": 2},
            "Empowered": {"Hip-Hop": 3, "Rock": 2, "Pop": 2, "Punk": 1, "K-Pop": 2},
            "Excited": {"Pop": 3, "Hip-Hop": 2, "Metal": 2, "Rock": 1, "Reggae": 1, "K-Pop": 2},
        }
    ),
    Question(
        "How important are vocals to you when listening to music?",
        ["I prefer songs with powerful vocals and lyrics", "Instrumentals are just as important, I’m okay without vocals", "I love a balance of both"],
        {
            "I prefer songs with powerful vocals and lyrics": {"Metal": 2, "RnB": 2, "Rock": 1, "Pop": 1, "Reggae": 2, "K-Pop": 3},
            "Instrumentals are just as important, I’m okay without vocals": {"Electronic": 3, "Ambient": 2, "Classical": 3, "Jazz": 1, "Blues": 1},
            "I love a balance of both": {"Indie": 3, "Folk": 2, "Metal": 1, "Pop": 1, "Reggae": 1},
        }
    ),
    Question(
        "Where do you typically listen to music?",
        ["While studying", "During workouts", "At home, relaxing..."],
        {
            "While studying": {"Classical": 3, "Jazz": 2, "Ambient": 1, "Indie": 1, "Blues": 1, "Reggae": 2},
            "During workouts": {"Hip-Hop": 3, "Pop": 2, "Rock": 1, "Electronic": 1, "Punk": 1, "K-Pop": 0, "Metal" : 2},
            "At home, relaxing...": {"Indie": 3, "Classical": 2, "Jazz": 1, "Ambient": 1, "Reggae": 2, "K-Pop": 1},
        }
    ),
    Question(
        "How fast do you like your music?",
        ["Slow and Mellow", "Medium-paced", "Fast and energetic"],
        {
            "Slow and Mellow": {"Classical": 3, "Jazz": 2, "Ambient": 2, "Indie": 1, "Blues": 2, "Reggae": 2, "K-Pop": 1},
            "Medium-paced": {"Pop": 3, "RnB": 2, "Indie": 2, "Folk": 1, "Reggae": 2, "K-Pop": 2},
            "Fast and energetic": {"Rock": 1, "Metal": 3, "Punk": 2, "Hip-Hop": 1, "Reggae": 1, "K-Pop": 3},
         
        }
    ),
   
    Question(
        "Which instrument do you connect with most in music?",
        ["Electric guitar", "Piano", "Drums", "Synthesizers", "Bass"],
        {
            "Electric guitar": {"Rock": 2, "Metal": 3, "Punk": 2, "Blues": 1},
            "Piano": {"Classical": 3, "Jazz": 2, "Blues": 2, "Ambient": 1},
            "Drums": {"Metal": 3, "Hip-Hop": 2, "Punk": 2, "Rock": 1},
            "Synthesizers": {"Electronic": 3, "Experimental": 2, "Ambient": 2, "Pop": 3, "K-Pop": 2},
            "Bass": {"Jazz": 3, "Reggae": 2, "Blues": 2, "Rock": 1, "K-Pop": 2},
        }
    ),
    Question(
        "What’s your preferred tempo in music?",
        ["Slow and steady", "Moderate", "Fast and upbeat"],
        {
            "Slow and steady": {"Classical": 3, "Ambient": 2, "Blues": 2, "Jazz": 1, "K-Pop": 1},
            "Moderate": {"Pop": 4, "RnB": 2, "Indie": 2, "Rock": 1, "K-Pop": 2},
            "Fast and upbeat": {"Rock": 1, "Metal": 3, "Punk": 2, "Hip-Hop": 1, "Reggae": 1, "K-Pop": 3},
        }
    ),
    Question(
        "Do you enjoy long, epic songs or short, punchy tracks?",
        ["I enjoy long, epic songs", "I prefer shorter tracks"],
        {
            "I enjoy long, epic songs": {"Rock": 3, "Metal": 3, "Progressive": 2, "Classical": 2},
            "I prefer shorter tracks": {"Pop": 3, "Punk": 3, "Hip-Hop": 3, "Indie": 3, "K-Pop": 3},
        }
    ),
]

#intialize a place to store the answers

answers = {}

#for each question in the questions list, I will print the question using st.radio 
#then i will store the weights of each answer in the selected weights
for question in questions:
    answer = st.radio(question.question_text, question.options)
    answers[question.question_text] = answer

    selected_weights = question.get_answer_weight(answer)

#add the corresponding weights
    for genre_name, weight in selected_weights.items():
        genres[genre_name].add_weight(weight)

#create a list that associates the genre name with its weight for each genre
sorted_genres = [(genre_name, genre.weight) for genre_name, genre in genres.items()]

#sort through the genres and find the top genre
for i in range(len(sorted_genres)):
    for j in range(0, len(sorted_genres) - i - 1):
        if sorted_genres[j][1] < sorted_genres[j + 1][1]:
            sorted_genres[j], sorted_genres[j + 1] = sorted_genres[j + 1], sorted_genres[j]

top_genre = sorted_genres[0][0]

# Spotify API credentials
client_id =   # Replace with your client ID
c_secret =  # Replace with your client secret

#**THIS WAS REMOVED TO ALLOW GIT TO PUSH IT**

# Obtain access token
url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": c_secret
}

response = requests.post(url, headers=headers, data=data)

#verify that the acsess token is working correctly
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    st.write("")
else:
    st.write(f"Error: {response.status_code}")
    access_token = None



#define a function that takes one input, using that input to search for tracks.
#authorize it with my token and return a JSON text with the tracks and items
def search_tracks(query):
    search_url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=50"  
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    search_response = requests.get(search_url, headers=headers)
    if search_response.status_code == 200:
        return search_response.json()['tracks']['items']
    else:
        return []


#create my query with my top genre
#create a list of the tracks and call it all tracks
query = f"genre:{top_genre}"
all_tracks = search_tracks(query)

#filter through all_tracks and return 5 tracks with specific artists
def filterArtist(tracks):
    unique_artists = set()
    filtered_tracks = []
    
    for track in tracks:
        artist_name = track.get('artists', [{}])[0].get('name', 'Unknown artist')
        
        if artist_name not in unique_artists:
            unique_artists.add(artist_name)
            filtered_tracks.append(track)
        
        if len(filtered_tracks) == 5:  
            break
    
    return filtered_tracks


#run the filtertracks function 
recommended_tracks = filterArtist(all_tracks)

#handle cases where no answers have been provided
if "answers" not in st.session_state:
    st.session_state.answers = {}



if "previous_top_genre" not in st.session_state:
    st.session_state.previous_top_genre = None

# Button for displaying listener profile
if st.button("View Listeners Profile:"):
    with st.spinner('Loading music recommendations...'):
        time.sleep(5)
        if recommended_tracks:
            st.write("🎶 Based on your selected genres, we recommend these tracks: 🎶")
            st.write(f"🎧 **Your Listener Profile:** {top_genre} 🎧")
            st.write(f"Based on your answers, we recommend you explore music in the **{top_genre}** genre!")
            st.divider()
            st.write("Here are some recommended tracks, Happy Listening!")
            for track in recommended_tracks:
                track_name = track.get('name', 'Unknown track')
                artist_name = track.get('artists', [{}])[0].get('name', 'Unknown artist')
                album_cover = track['album']['images'][1]['url']  
                track_url = track.get('external_urls', {}).get('spotify', '#')

                st.write(f"**{track_name}** by {artist_name}")
                st.image(album_cover, caption=f"Album cover for {track_name}", use_container_width=False) 
                st.markdown(f"[Listen on Spotify]({track_url})")
        else:
            st.write("Sorry, we couldn't find any recommendations based on your input.")

   
    st.session_state.previous_top_genre = top_genre
    #make it so the top genre is only updated when the button is clicked
#initialize a user id
user_id = st.text_input("Enter your User ID:")



if user_id:
    cursor.execute('''
        INSERT INTO responses (energy_preference, feeling_preference, vocals_preference, listening_location, 
                               tempo_preference, instrument_preference, tempo, epic_songs_preference, user_id, top_genre)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        answers.get("What type of energy do you prefer in your music?", ""),
        answers.get("How do you want to feel while listening to music?", ""),
        answers.get("How important are vocals to you when listening to music?", ""),
        answers.get("Where do you typically listen to music?", ""),
        answers.get("How fast do you like your music?", ""),
        answers.get("Which instrument do you connect with most in music?", ""),
        answers.get("What’s your preferred tempo in music?", ""),
        answers.get("Do you enjoy long, epic songs or short, punchy tracks?", ""),
        user_id,
        top_genre
    ))
    conn.commit()

# Check for previous results based on user ID
if user_id:
    cursor.execute('''
        SELECT top_genre FROM responses WHERE user_id = ? ORDER BY id DESC LIMIT 1
    ''', (user_id,))
    previous_response = cursor.fetchone()

    if previous_response:
        previous_top_genre = previous_response[0]
        if st.button("View Previous Results!"):
            # Display previous top genre stored before any updates
            if st.session_state.previous_top_genre:
                st.write(f"🎶 Your previous top genre was **{st.session_state.previous_top_genre}** 🎶")
            else:
                st.write(f"🎶 Your top genre was **{previous_top_genre}** 🎶")
    else:
        st.write("You haven't taken this quiz before, Have Fun!")

st.divider()

if st.button("Retake Quiz"):
    st.session_state.answers.clear()
 
   