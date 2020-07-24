import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    parameters={}
    parameters['q']=movie
    parameters['type']="movies"
    parameters['limit']=5
    serviceurl="https://tastedive.com/api/similar"
    tastedive_resp=requests_with_caching.get(serviceurl, params=parameters)
    #print(tastedive_resp.url)
    #print(tastedive_resp.text[:100])
    data=tastedive_resp.json()
    return data


def extract_movie_titles(data):
    print(data)
    print(json.dumps(data, indent=2))
    #print("FOR UNDERSTAND EXECUTE AND REPEAT")
    dis=data["Similar"]["Results"]
    movie_lst=[]
    for d in dis:
        movie_lst.append(d["Name"])
    return movie_lst

#print(get_movies_from_tastedive('Captain Marvel'))
#print(get_movies_from_tastedive('Black Panther'))
def get_related_titles(movie_lst):
    single_lst=[]
    for movie in movie_lst:
        dict_data=get_movies_from_tastedive(movie)
        new_lst=extract_movie_titles(dict_data)
        for movie in new_lst:
            if movie not in single_lst:
                single_lst.append(movie)
    return single_lst

def get_movie_data(title):
    baseurl="http://www.omdbapi.com/"
    parameters={}
    parameters['t']=title
    parameters['r']="json"
    resp=requests_with_caching.get(baseurl, params=parameters)
    #print(resp.url)
    #print(resp.text[0:150])
    data=resp.json()
    return data

def get_movie_rating(dict_data):
    #print(json.dumps(dict_data, indent=2))
    #print("UNDERSTAND,EXECUTE AND REPEAT-------------------------- ")
    ratings=(dict_data["Ratings"])
    for rate in ratings:
        if rate["Source"]== "Rotten Tomatoes":
            #print(rate["Value"][:2])
            return int(rate["Value"][:2])
    return 0

def get_sorted_recommendations(movie_lst):
    rel_lst=sorted(get_related_titles(movie_lst))
    #print("Main OUTPUT")
    #print(rel_lst)
    new_lst=[]
    for movie in rel_lst:
        print(movie)
        data=get_movie_data(movie)
        rating=get_movie_rating(data)
        new_lst.append((movie, rating))
    lst=sorted(new_lst, key = lambda x: (x[1], x[0]) , reverse=True)
    new_lst=[movie for movie, rate in lst]
    return new_lst
