# Food Tournament 
A tournament style comparison tool for food. This is a project for UBC's CPSC 344 course by team Winter Soldier.

## Setup for Mac
1. Open terminal and navigate to a directory where you want to store this project.
2. Enter `git clone https://github.com/ehauner/food-tournament.git`. This will download the code to your current directory.
3. CD into the `food-tournament/tournament/`.
4. Run the setup script `./setup.sh` to install pip, numpy, pandas, and django.
5. Run the local server `python manage.py runserver` and leave the terminal running.
6. In your Internet browser, navigate to `127.0.0.1:8000/game/upload`.
7. Enjoy.

## Upload 
Required: csv file of foods to be compared with the following attributes:
- name (string)
- description (string)
- photo_url (fqdn)
- group (e.g. "cereal")
- matches_played (int)
- matches_won (int)
- price ($)
- amount (g)
- serving_size (g)
- calories
- fat (g)
- cholesterol (mg)
- sodium (mg)
- carbohydrates (g)
- sugar (g)
- protein (g)
- vitA (%)
- vitC (%)
- calcium (%)
- iron (%)
- fiber (g)
- vegan (0 or 1)
- organic (0 or 1)
- gluten-free (0 or 1)
- nut-free (0 or 1)
- lactose-free (0 or 1)
- target_serving_size (g)
