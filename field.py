from constants import FIELD
import copy

field = copy.deepcopy(FIELD)

bot_field = copy.deepcopy(FIELD)

if __name__ == "__main__":
    field[5][5] = 1
    bot_field[3][3] = 2
    print(FIELD)
    print(field)
    print(bot_field)