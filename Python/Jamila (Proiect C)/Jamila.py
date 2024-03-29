import json
import os
import requests
from bs4 import BeautifulSoup
import re
import sys
from tkinter import *
from tkinter import ttk

# region constants

SHOPPING_CART_FILE_NAME = 'shopping_cart.json'
SHOPPING_CART_FILE_PATH = os.path.join(os.path.dirname(__file__), SHOPPING_CART_FILE_NAME)

# endregion


class JamilaC:

    def __init__(self):
        self.data = {}

    def validateURL(self, url):
        return re.search("^https\:\/\/jamilacuisine\.ro\/(.*\-{1})+reteta\-video\/$", url)

    def getRecipeName(self, url):
        recipe_name = url.replace("https://jamilacuisine.ro/", "")
        recipe_name = recipe_name.replace("-reteta-video/", "")
        recipe_name = recipe_name.replace("-", " ")
        return recipe_name

    def loadJSON(self):
        try:
            with open(SHOPPING_CART_FILE_PATH, "r+") as file:
                try:
                    self.data = json.load(file)
                except:
                    self.data = {}
                    json.dump(self.data, file)
        except:
            self.data = {}
            with open(SHOPPING_CART_FILE_PATH, "w+") as file:
                json.dump(self.data, file)

    def printJSON(self):
        if 'items' in self.data:
            for item in self.data['items']:
                string = "Name: " + item['name']
                if item['amount'] != "" and item['amount'] > 0:
                    string += " - Amount: " + str(item['amount'])
                if item['unit'] != "":
                    string += " - Unit: " + item['unit']
                if item['note'] != "":
                    string += " - Note: " + item['note']
                print(string)
        if 'recipes' in self.data:
            recipes_list = "Recipes: "
            for i in range(0, len(self.data['recipes'])):
                if (i == len(self.data['recipes']) - 1):
                    recipes_list += self.data['recipes'][i]['name']
                else:
                    recipes_list += self.data['recipes'][i]['name'] + ", "
            recipes_list += "\n"
            print(recipes_list)

    def getIngredientIndex(self, ingredient_name):
        for index in range(0, len(self.data['items'])):
            if self.data['items'][index]['name'] == ingredient_name:
                return index

    def validateIngredientName(self, name):
        name_ingredient = ""
        if name is not None:
            name_ingredient = name.text.lower().strip()
        return name_ingredient

    def validateIngredientAmount(self, amount):
        amount_ingredient = 1
        if amount is not None:
            if not re.search("^[0-9]+$", amount.text.lower().strip()):
                if '/' in amount.text:
                    amount_ingredient = float(int(amount.text.lower().strip().split('/')[0]) / int(amount.text.lower().strip().split('/')[1]))
                if '-' in amount.text:
                    amount_ingredient = int(amount.text.lower().strip()[1])
            else:
                amount_ingredient = int(amount.text.lower().strip())
        return amount_ingredient

    def validateIngredientUnit(self, unit):
        unit_ingredient = ""
        if unit is not None:
            unit_ingredient = unit.text.lower().strip()
        return unit_ingredient

    def validateIngredientNote(self, note):
        note_ingredient = ""
        if note is not None:
            note_ingredient = note.text.lower().strip()
        return note_ingredient

    def getIngredientsFromRecipeURL(self):
        URL = ""
        if (len(sys.argv) == 1):
            URL = input("Please enter a recipe's URL:\n")

            while not self.validateURL(URL):
                URL = input(
                    "Incorrect URL format, please enter a correct recipe URL:\n")
        else:
            URL = sys.argv[1]

        page = requests.get(URL)
        html_parser = BeautifulSoup(page.content, "html.parser")

        ingredients_element = html_parser.find_all("li", {"class": "wprm-recipe-ingredient"})

        items_list = []

        for ingredient in ingredients_element:
            amount_data = ingredient.find(
                "span", class_="wprm-recipe-ingredient-amount")
            unit_data = ingredient.find(
                "span", class_="wprm-recipe-ingredient-unit")
            name_data = ingredient.find(
                "span", class_="wprm-recipe-ingredient-name")
            note_data = ingredient.find(
                "span", class_="wprm-recipe-ingredient-notes")

            name_ingredient = self.validateIngredientName(name_data)
            amount_ingredient = self.validateIngredientAmount(amount_data)
            unit_ingredient = self.validateIngredientUnit(unit_data)
            note_ingredient = self.validateIngredientNote(note_data)

            item = {
                "name": name_ingredient,
                "amount": amount_ingredient,
                "unit": unit_ingredient,
                "note": note_ingredient
            }

            items_list.append(item)

        if 'items' not in self.data:
            self.data['items'] = items_list
        else:
            self.updateCart(items_list)

        recipe_name = self.getRecipeName(URL)

        if 'recipes' not in self.data and recipe_name != "":
            self.data['recipes'] = [{'name': recipe_name}]
        else:
            self.addRecipeToCart(recipe_name)

        with open(SHOPPING_CART_FILE_PATH, "w") as file:
            json.dump(self.data, file)

    def updateCart(self, items_list):
        for item in items_list:
            update_index = -1
            if (self.data != {}):
                if (any(ingredient['name'] == item['name'] for ingredient in self.data['items'])):
                    update_index = self.getIngredientIndex(item['name'])

            if update_index != -1:
                self.__structurizeIncomingIngredients(update_index, item)
                if item['amount'] != '' and item['unit'] == self.data['items'][update_index]['unit'] and item['note'] == self.data['items'][update_index]['note']:
                    self.data['items'][update_index]['amount'] = round(
                        item['amount'] + self.data['items'][update_index]['amount'], 2)
                    self.__structurizeOutgoingIngredients(update_index)
                elif item['amount'] == '' and item['unit'] == self.data['items'][update_index]['unit'] and item['note'] == self.data['items'][update_index]['note']:
                    item['amount'] = 1
                    self.data['items'][update_index]['amount'] = round(
                        item['amount'] + self.data['items'][update_index]['amount'], 2)
                    self.__structurizeOutgoingIngredients(update_index)
            else:
                self.data['items'].append(item)

    def addRecipeToCart(self, recipe_name):
        if (self.data != {}):
            if not any(recipe['name'] == recipe_name for recipe in self.data['recipes']):
                item = {'name': recipe_name}
                self.data['recipes'].append(item)

    def __structurizeIncomingIngredients(self, update_index, item):
        if self.data['items'][update_index]['unit'].lower() == "l" and item['unit'].lower() == "ml":
            item['unit'] = "L"
            item['amount'] /= 1000
        if self.data['items'][update_index]['unit'].lower() == "kg" and item['unit'].lower() == "g":
            item['unit'] = "L"
            item['amount'] /= 1000
        if self.data['items'][update_index]['unit'].lower() == "linguri" and item['unit'].lower() == "lingura":
            item['unit'] = "linguri"
        if self.data['items'][update_index]['unit'].lower() == "lingurite" and item['unit'].lower() == "lingurita":
            item['unit'] = "lingurite"
        if self.data['items'][update_index]['unit'].lower() == "legaturi" and item['unit'].lower() == "legatura":
            item['unit'] = "legaturi"
        if self.data['items'][update_index]['unit'].lower() == "lingurite rase" and item['unit'].lower() == "lingurita rasa":
            item['unit'] = "lingurite rase"
        if self.data['items'][update_index]['unit'].lower() == "lingurite cu varf" and item['unit'].lower() == "lingurita cu varf":
            item['unit'] = "lingurite cu varf"

    def __structurizeOutgoingIngredients(self, update_index):
        if int(self.data['items'][update_index]['amount']) >= 1000:
            if self.data['items'][update_index]['unit'].lower() == "ml":
                self.data['items'][update_index]['unit'] = "L"
                self.data['items'][update_index]['amount'] /= 1000
            if self.data['items'][update_index]['unit'].lower() == "g":
                self.data['items'][update_index]['unit'] = "Kg"
                self.data['items'][update_index]['amount'] /= 1000
        if int(self.data['items'][update_index]['amount']) > 1:
            if self.data['items'][update_index]['unit'].lower() == "lingura":
                self.data['items'][update_index]['unit'] = "linguri"
            if self.data['items'][update_index]['unit'].lower() == "lingurita":
                self.data['items'][update_index]['unit'] = "lingurite"
            if self.data['items'][update_index]['unit'].lower() == "legatura":
                self.data['items'][update_index]['unit'] = "legaturi"
            if self.data['items'][update_index]['unit'].lower() == "lingurita rasa":
                self.data['items'][update_index]['unit'] = "lingurite rase"
            if self.data['items'][update_index]['unit'].lower() == "lingurita cu varf":
                self.data['items'][update_index]['unit'] = "lingurite cu varf"

    def initializeInterfaceWithTable(self):
        root = Tk()
        root.title("Shopping List")

        style = ttk.Style()
        style.theme_use('clam')

        main_frame = Frame(root)
        main_frame.pack()

        table = ttk.Treeview(main_frame, height=len(self.data['items']))

        table['columns'] = ('name', 'amount', 'unit', 'note')

        table.column("#0", width=0, stretch=NO)
        table.column('name', anchor=CENTER, width=150)
        table.column('amount', anchor=CENTER, width=100)
        table.column('unit', anchor=CENTER, width=100)
        table.column('note', anchor=CENTER, width=200)

        table.heading("#0", text="", anchor=CENTER)
        table.heading('name', text="Name", anchor=CENTER)
        table.heading('amount', text="Amount", anchor=CENTER)
        table.heading('unit', text="Unit", anchor=CENTER)
        table.heading('note', text="Note", anchor=CENTER)

        for i in range(0, len(self.data['items'])):
            table.insert(parent='', index='end', iid=i, text='', values=(
                self.data['items'][i]['name'], self.data['items'][i]['amount'], self.data['items'][i]['unit'], self.data['items'][i]['note']))
            if i % 2 == 0:
                table.item(i, tags='light_gray')
            else:
                table.item(i, tags='dark_gray')
        table.tag_configure('light_gray', background='gray')
        table.tag_configure('white', background='white')

        table.pack()

        root.mainloop()


jc = JamilaC()
jc.loadJSON()
jc.getIngredientsFromRecipeURL()
jc.initializeInterfaceWithTable(jc)
jc.printJSON()
