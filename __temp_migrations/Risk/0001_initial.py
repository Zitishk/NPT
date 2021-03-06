# Generated by Django 2.2.12 on 2022-01-15 19:23

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Risk_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risk_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Risk_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('Risk1', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk2', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk3', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk4', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk5', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk6', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk7', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk8', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk9', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('Risk10', otree.db.models.IntegerField(choices=[[1, 'Option A'], [0, 'Option B']], null=True)),
                ('q1', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='If you win a prize for the best all round performance in your university, how likely are you to inform your friends about it?\u2028')),
                ('q2', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='If you win a prize for the best all round performance in your university, how likely are you to inform your family about it?\u2028')),
                ('q3', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='If you win a prize for the best all round performance in your university, how likely are you to post on Facebook or other social media about it\u2028')),
                ('q4', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='How stressed did the time make you feel during the decision task?\u2028')),
                ('q5', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='How do you see yourself: are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?\u2028')),
                ('q6', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='How likely are you to admit that your tastes are different from those of your friends?\u2028')),
                ('q7', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='How likely are you to argue with a friend about an issue on which he or she has a very different opinion?\u2028')),
                ('q8', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='How likely are you to defend an unpopular issue that you believe in at a social occasion?\u2028')),
                ('q9', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='People should be willing to help others who are less fortunate\u2028')),
                ('q10', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='These days people need to look after themselves and not overly worry about others.\u2028')),
                ('q11', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='It is important to help one another so that the community in general is a better place.\u2028')),
                ('q12', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who tends to find fault with others\u2028')),
                ('q13', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who can be cold and aloof\u2028')),
                ('q14', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who is considerate and kind to almost everyone\u2028')),
                ('q15', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who likes to cooperate with others\u2028')),
                ('q16', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who is sometimes rude to others\u2028')),
                ('q17', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who is helpful and unselfish with others\u2028')),
                ('q18', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who starts quarrels with others\u2028')),
                ('q19', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who has a forgiving nature\u2028')),
                ('q20', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='I see myself as someone who is generally trusting\u2028')),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10000, null=True, verbose_name='Gender')),
                ('caste', otree.db.models.StringField(choices=[('General', 'General'), ('Scheduled Caste', 'Scheduled Caste'), ('Scheduled Tribe', 'Scheduled Tribe'), ('OBC', 'OBC'), ('Prefer not to say', 'Prefer not to say')], max_length=10000, null=True, verbose_name='Caste')),
                ('relegion', otree.db.models.StringField(choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Prefer not to say', 'Prefer not to say')], max_length=10000, null=True, verbose_name='Relegion')),
                ('year', otree.db.models.StringField(choices=[('UG First Year', 'UG First Year'), ('UG Second Year', 'UG Second Year'), ('UG Third Year', 'UG Third Year'), ('UG Fourth Year', 'UG Fourth Year'), ('Masters First Year', 'Masters First Year'), ('Masters Second Year', 'Masters Second Year')], max_length=10000, null=True, verbose_name='Which year in college are you ?')),
                ('income', otree.db.models.IntegerField(null=True, verbose_name='What is your approximate monthly family income in Rupees?\u2028')),
                ('freeform', otree.db.models.StringField(max_length=10000, null=True, verbose_name='We are interested in the reasons why you did or did not choose to invest in this study. Please explain what affected your decisions.')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Risk.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Risk.Subsession')),
            ],
            options={
                'db_table': 'Risk_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Risk.Subsession'),
        ),
    ]
