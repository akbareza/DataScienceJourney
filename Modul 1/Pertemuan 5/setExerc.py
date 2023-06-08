#MENILAI KECOCOKAN FILM
myFilm = input('Plesae enter your favourite film(s), use comma (,) to seperate item(s): ').split(',')
otherFilm = input('Plesae enter his/her favourite film(s), use comma (,) to seperate item(s): ').split(',')

setMyFilm = set(myFilm)
setOtherFilm = set(otherFilm)

myIntersectSet = setMyFilm.intersection(setOtherFilm)
otherIntersectSet = setOtherFilm.intersection(setMyFilm)

print(myIntersectSet)
print(otherIntersectSet)

print(f'Both of you match {((len(myIntersectSet)/len(setMyFilm))+(len(otherIntersectSet))/len(setOtherFilm))/2*100} %!')
