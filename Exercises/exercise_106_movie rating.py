# check for rating for this movie:

checking_rating = input('What is the rating for this movie?\n:')
checking_rating = checking_rating.strip().upper()

## universal -> everyone can watch    - if doing both functions, do in and or
if checking_rating == 'U' or checking_rating == 'UNIVERSAL':
    print('everyone can watch')

## pg --> General viewing, but some scenes may be unsuitable for young children
elif checking_rating == 'PG':
    print('General viewing, but some scenes may be unsuitable for young children')

## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
elif checking_rating == '12A':
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.')

## 15 --> No one younger than 15 may see a 15 film in a cinema.
elif checking_rating == '15':
    print('No one younger than 15 may see a 15 film in a cinema.')

## 18 --> No one younger than 18 may see an 18 film in a cinema.
elif checking_rating == '18':
    print('No one younger than 18 may see an 18 film in a cinema.')

else:
   print('You sure thats a movie rating? Please try again.')