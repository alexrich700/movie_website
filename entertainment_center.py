#imports the fresh_tomatoes page // contains the html
import fresh_tomatoes
#imports the media file // contains the class Movie and class variables
import media


#movie instance for our class Movie // contains (movie title, storyline, image, and trailer link)
wonder_woman = media.Movie("Wonder Woman",
                        "Wonder Woman against the evil that plagues the world",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=F0lZgaz0CIE")

get_out = media.Movie("Get Out",
                     "Black man discovers tristed truth of a white suburban community",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNTE2Nzg1NjkzNV5BMl5BanBnXkFtZTgwOTgyODMyMTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=d1_y1gQ7RyvgXU")

spiderman_homecoming = media.Movie("Spiderman Homecoming",
                        "Bit by a spider",
                        "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8571065/spider_man_poster2.jpg",
                        "https://www.youtube.com/watch?v=xrzXIaTt99U")

school_of_rock = media.Movie("School Of Rock",
                        "Using rock music to learn",
                        "https://images-na.ssl-images-amazon.com/images/I/51v8TQDTF-L._SY300_.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

life = media.Movie("Life",
                        "Space station encounters alien life",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzAwMmQxNTctYjVmYi00MDdlLWEzMWUtOTE5NTRiNDhhNjI2L2ltYWdlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=cuA-xqBw4jE")

the_passion = media.Movie("The Passion",
                        "The story of the crucification of Jesus Christ",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2NDY5NDAwMV5BMl5BanBnXkFtZTcwMTcwMDUyMQ@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=4Aif1qEB_JU")


# Creates an array called movies that holds each movie instance
movies = [wonder_woman, get_out, spiderman_homecoming, school_of_rock, life, the_passion]

#Runs code and opens up website // Run on this page after any development is done
fresh_tomatoes.open_movies_page(movies)


