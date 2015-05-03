import media
import coconut_water

#Create instances of the movies to display
doubtfire = media.Movie("Mrs Doubtfire",
                        "125 minutes",
                        "12",
                        "Divorced husband disguised as a house keeper for his divorced wife and children",
                        "http://upload.wikimedia.org/wikipedia/en/5/5a/Mrs_Doubtfire.jpg",
                        "https://www.youtube.com/watch?v=DoAEouJTdWY")

beautiful_mind = media.Movie("A Beautiful Mind",
                             "135 minutes",
                             "12",
                             "Mathematician John Nash life story",
                             "http://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                             "https://www.youtube.com/watch?v=aS_d0Ayjw4o")


furious7 = media.Movie("Fast and Furious 7",
                       "137 minutes",
                       "12A",
                       "Fast cars, ... money, ... revenge ",
                       "http://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
                       "https://www.youtube.com/watch?v=Skpu5HaVkOc")

imitation_game = media.Movie("Imitation Game",
                             "114 minutes",
                             "12",
                             "Alan Turing build the Enigma to broke the German code",
                             "http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
                             "https://www.youtube.com/watch?v=j2jRs4EAvWM")

gladiator = media.Movie("Gladiator",
                        "164 minutes",
                        "15",
                        "Commodus anger for power ... Maximus save Rome",
                        "http://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=0BLZbrLogTo")

generals_daughter = media.Movie("The General's Daughter",
                                "116 minutes",
                                "18",
                                "The General is convicted for murdering his own daughter ...",
                                "http://upload.wikimedia.org/wikipedia/en/d/db/Generaldposter.jpg",
                                "https://www.youtube.com/watch?v=LsC8Kd6tfs4")

movies = [gladiator, generals_daughter,  beautiful_mind, doubtfire, furious7, imitation_game]
coconut_water.open_movies_page(movies)
