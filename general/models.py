from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
class Constants(BaseConstants):
    name_in_url = 'general'
    players_per_group = 3
    num_rounds = 1
    names = {
        'male' : ['Anup','Ashok','Anupam','Akash','Deepak','Gaurav','Gautam','Hemanth','Harshit',
                 'Ishan','Jatin','Jitesh','Karan','Kapil','Kartik','Mukesh','Mihir','Nikhil',
                 'Nitish','Naveen','Pankaj','Rajat','Rahul','Rohan','Sourav','Sachin','Tarun',
                 'Tanmay','Udit','Vivek','Arpit','Raj','Nitin','Viren','Avijit','Siddharth','Himanshu',
                 'Anil','Rakesh','Abhishek','Chetan','Aditya','Vipul','Rishi','Mohan','Raghav',
                 'Dhruv','Yash','Sameer', 'Neel'],
        'female' : ['Aditi','Ananya','Deepa','Divya','Ekta','Garima','Gargi','Hema','Ishita','Jyoti',
                    'Jhanvi','Kanika','Kritika','Lata','Meera','Meghna','Nupur','Priya','Preeti',
                    'Reena','Ritu','Ritika','Simran','Sonia','Tina','Tanvi','Urvashi','Vedika','Vidya',
                    'Yamini','Geeta','Tania','Khushboo','Lalita','Sneha','Arpita','Ishani','Neha',
                    'Megha','Priyanka','Piyali','Vidushi','Reema','Amrita','Nina','Bhavna','Shreya',
                    'Ankita','Saumya','Preetika']
        }

class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['used'] = []
        for group in self.get_groups():
            group.set_names(1)

class Group(BaseGroup):
    def set_names(self,x):
        if(x):
            male_names = random.sample(Constants.names['male'],k=5)
            female_names = random.sample(Constants.names['female'],k=5)
        else:
            main_list_m = list(set(Constants.names['male']) - set(self.session.vars['used']))
            main_list_f = list(set(Constants.names['female']) - set(self.session.vars['used']))
            male_names = random.sample(main_list_m,k=5)
            female_names = random.sample(main_list_f,k=5)
        for p in self.get_players():
            p.participant.vars['male_names'] = male_names
            p.participant.vars['female_names'] = female_names
        return


class Player(BasePlayer):

    audio = models.StringField(label = "Enter the word in lowercase",blank=False)
    def audio_error_message(self, value):
        if value not in ['CAT','cat','Cat']:
            return 'Entered word is wrong, please try again'


    Q1 = models.IntegerField(label='Will you play with the same group members in every round?',choices=[[1,'Yes'],[2,'No']])
    Q2 = models.IntegerField(label='How much time do you have to decide?',choices=[[1,'45 secs'], [2,'90 secs'], [3,'randomly between the range of 45-90 seconds']])
    Q3 = models.IntegerField(label='Suppose in a round, you do not invest but someone else invests from your group. How much do you earn?',choices=[[1,'100M'], [2,'300M'], [3,'900M'], [4,'NOTA']])
    Q4 = models.IntegerField(label='Suppose in a round, you invest before anyone else in the group. How much do you earn?',choices=[[1,'100M'], [2,'300M'], [3,'900M'], [4,'NOTA']])
    Q5 = models.IntegerField(label='Suppose in a round, no one from your group invests. How much do you earn?',choices=[[1,'100M'], [2,'300M'], [3,'900M'], [4,'NOTA']])
    Q6 = models.IntegerField(label='Which round will you be paid for?',choices=[[1,'All'], [2,'random from 1-10 & 11'], [3,'Last'], [4,'First']])


    age = models.IntegerField(label="Please enter your age",min=15,max=50)
    gender = models.StringField(label="Please select your gender",choices = ['Male','Female'],widget=widgets.RadioSelect)


    def set_name_1(self):
        self.participant.vars['name'] = self.name[1:]
        self.session.vars['used'].append(self.name[1:])

    def checknames(self):
        if(self.gender=='Male'):
            set(self.participant.vars['male_names']).issubset(set(self.session.vars['used']))
        else:
            set(self.participant.vars['female_names']).issubset(set(self.session.vars['used']))

    name = models.StringField(label="Please select a name from the list given below",
                                widget=widgets.RadioSelect,blank=False)
    def name_choices(player):
        choices = [['M'+i,i] for i in player.participant.vars['male_names']] + [['F'+i,i] for i in player.participant.vars['female_names']]
        return choices

    def name_error_message(self, value):
        if value[1:] in self.session.vars.get('used',[]):
            if(self.checknames()):
                self.group.set_names()
            return 'This name is already taken please choose another name'
        if (value[0]!=self.gender[0]):
            return 'Please choose a gender-appropriate name'

    def set_name_2(self):
        self.participant.vars['name'] = self.first_name.capitalize()
    first_name = models.StringField(label="Please enter your First Name",blank=False)
    last_name = models.StringField(label="Please Enter your Last Name",blank=False)
