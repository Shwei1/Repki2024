from constants import FIELD

field = FIELD.copy()

bot_field = FIELD.copy()

if __name__ == "__main__":
    field[5] = "shalom"
    bot_field[3][3] = 2
    print(FIELD)
    print(field)
    # print(bot_field)