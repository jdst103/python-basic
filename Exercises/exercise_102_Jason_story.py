
#Creating Begininng of story dictionary
beginning_dict = {
    'start_of_beginning': 'On a cold evening in the bathroom was a man called Tito.'
                          ' His wife Tina has been calling him all day so he can pick up a loaf of bread',
'middle_of_beginning': 'Tina was angry that Lidl was shutting at 1pm for black friday',
'end_of_beginning': 'Tito being the timid guy, the type most aggressive indivduals go for ''aledgely''he responds ''comming dear!!'' ..  '}

#Creating middle of story dictionary
middle_dict = { 'start_of_middle': 'Tito rans down the road in his with all his heart, desperate to save 3p',
                'end_of_middle': 'As he reaches Lidl, he takes out his phone to call Tina, ''I MADE IT!!''. '}

#Creating end of story dictionary
end_dict = {'end_of_story': 'As crucially saves 3p, he realises he is 2p short!! '}
# use your hero as well

#Creating hero aspect of story
hero_dict = {'save_the_day':'Tina right behinds him looks at him in disgust, quoting ''you cant do anything right''. '
                            'Tito embarrasingly laughs and they alive happily ever after'}

#Creating a dictionary for jason story for its parts
Jason_story_dict = {'beginning': beginning_dict, 'middle': middle_dict,'end':end_dict,'Hero': hero_dict}

# beginning
# middle
# end
# heroine/hero
# Creating a dictionary for a story no one cares about!!
Noone_cares_story = {'beginning': 'you', 'middle':'dont', 'end': 'really', 'hero': 'care!!'}

#Stories list compiling of Jason story and a irrelevant story
Stories_list = (Jason_story_dict, Noone_cares_story)


# print the story by calling the dictionary keys individually
#interpolate!

whole_story = input('do you want to read the whole story? (yes or no?)     :')
if whole_story == 'yes':
    print(Stories_list[0])

if whole_story == 'no':
    which_chapter = input('what part of the chapter do you want? (beginning, middle or end)       :')
    if which_chapter == 'beginning':
        print(Stories_list[0]['beginning'].values())
    if which_chapter == 'middle':
        print(Stories_list[0]['middle'])
    if which_chapter == 'end':
        print(Stories_list[0]['end'])

#--> ignore
# #print(Stories_list[0]['beginning']['end_of_beginning'])
#print(Stories_list[0]['beginning']['middle_of_beginning'])
#print(Stories_list[0]['end']['end_of_story'])
#print(Stories_list[1]['beginning'])

