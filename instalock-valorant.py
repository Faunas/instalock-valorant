import pyautogui
from time import sleep
import random


agents = ["Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Jett", "BOT", "Killjoy", "Neon", "Omen", "Phoenix",
          "Raze", "Reyna", "Sage", "Skye", "Sova", "Yoru", "Harbor"]

art = '''
$$$$$$\ $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$\       $$$$$$\   $$$$$$\  $$\   $$\ 
\_$$  _|$$$\  $$ |$$  __$$\\__$$  __|$$  __$$\ $$ |     $$  __$$\ $$  __$$\ $$ | $$  |
  $$ |  $$$$\ $$ |$$ /  \__|  $$ |   $$ /  $$ |$$ |     $$ /  $$ |$$ /  \__|$$ |$$  / 
  $$ |  $$ $$\$$ |\$$$$$$\    $$ |   $$$$$$$$ |$$ |     $$ |  $$ |$$ |      $$$$$  /  
  $$ |  $$ \$$$$ | \____$$\   $$ |   $$  __$$ |$$ |     $$ |  $$ |$$ |      $$  $$<   
  $$ |  $$ |\$$$ |$$\   $$ |  $$ |   $$ |  $$ |$$ |     $$ |  $$ |$$ |  $$\ $$ |\$$\  
$$$$$$\ $$ | \$$ |\$$$$$$  |  $$ |   $$ |  $$ |$$$$$$$$\ $$$$$$  |\$$$$$$  |$$ | \$$\ 
\______|\__|  \__| \______/   \__|   \__|  \__|\________|\______/  \______/ \__|  \__|
                                                   
Рекомендованное разрешение: 1920x1080                                                          
'''
print(art)

screen = pyautogui.screenshot("myscreen.png", region=(580, 722, 830, 240))

def lock_agent(path_to_agent_png, coords, working_mode):
    agent_has_been_choosen = False
    if working_mode == "1":  # работа по координатам
        print("Выбран режим работы по координатам.")
        while not agent_has_been_choosen:
            # print(pyautogui.locateOnScreen("agents/8.png"))
            findsky = pyautogui.locateOnScreen(f"agents/bluesky.png", region=(580, 722, 830, 240))
            if findsky:
                for i in range(3):
                    pyautogui.moveTo(coords)
                    pyautogui.click(coords)

                    pyautogui.moveTo(956, 813)
                    pyautogui.click(956, 813)
                agent_has_been_choosen = True
    else:
        print("А: Выбран режим работы по изображению")
        while not agent_has_been_choosen:
            find_agent = pyautogui.locateOnScreen(f"agents/{path_to_agent_png}", region=(480, 722, 930, 340))
            if find_agent:
                pyautogui.moveTo(find_agent)
                pyautogui.click(find_agent)
                for i in range(3):
                    pyautogui.moveTo(956, 813)
                    pyautogui.click(956, 813)
                    sleep(0.4)
                agent_has_been_choosen = True
    print("--- Агент выбран ---")


def generate_path(agent_name, variant):
    if agent_name == agents[0] or agent_name == "0":
        img_path = f"{agents[0]}.png"
        agent_coords = 581, 920
    elif agent_name == agents[1] or agent_name == "1":
        img_path = f"{agents[1]}.png"
        agent_coords = 665, 925
    elif agent_name == agents[2] or agent_name == "2":
        img_path = f"{agents[2]}.png"
        agent_coords = 750, 922
    elif agent_name == agents[3] or agent_name == "3":
        img_path = f"{agents[3]}.png"
        agent_coords = 832, 922
    elif agent_name == agents[4] or agent_name == "4":
        img_path = f"{agents[4]}.png"
        agent_coords = 923, 924
    elif agent_name == agents[5] or agent_name == "5":
        img_path = f"{agents[5]}.png"
        agent_coords = 1086, 927
    elif agent_name == agents[6] or agent_name == "6":
        img_path = f"{agents[6]}.png"
        agent_coords = 1174, 919
    elif agent_name == agents[7] or agent_name == "7":
        img_path = f"{agents[7]}.png"
        agent_coords = 1254, 929
    elif agent_name == agents[8] or agent_name == "8":
        img_path = f"{agents[8]}.png"
        agent_coords = 1339, 924
    elif agent_name == agents[9] or agent_name == "9":
        img_path = f"{agents[9]}.png"
        agent_coords = 586, 1008
    elif agent_name == agents[10] or agent_name == "10":
        img_path = f"{agents[10]}.png"
        agent_coords = 667, 1007
    elif agent_name == agents[11] or agent_name == "11":
        img_path = f"{agents[11]}.png"
        agent_coords = 750, 1008
    elif agent_name == agents[12] or agent_name == "12":
        img_path = f"{agents[12]}.png"
        agent_coords = 837, 1007
    elif agent_name == agents[13] or agent_name == "13":
        img_path = f"{agents[13]}.png"
        agent_coords = 922, 1007
    elif agent_name == agents[14] or agent_name == "14":
        img_path = f"{agents[14]}.png"
        agent_coords = 1004, 1009
    elif agent_name == agents[15] or agent_name == "15":
        img_path = f"{agents[15]}.png"
        agent_coords = 1086, 1009
    elif agent_name == agents[16] or agent_name == "16":
        img_path = f"{agents[16]}.png"
        agent_coords = 1173, 1010
    elif agent_name == agents[17] or agent_name == "17":
        img_path = f"{agents[17]}.png"
        agent_coords = ""
    else:
        print("Выбран неизвестный агент.")
        img_path = "Undefined"
        agent_coords = "Undefined"
        quit()

    lock_agent(path_to_agent_png=img_path, coords=agent_coords, working_mode=variant)



print("Доступны только агенты из следующего списка: \n\n"
      " [0]Breach   [1]Brimstone    [2]Chamber\n [3]Cypher   [4]Fade         [5]Jett\n [6]BOT      [7]Killjoy      [8]Neon\n [9]Omen     [10]Phoenix     [11]Raze\n [12]Reyna   [13]Sage        [14]Skye\n [15]Sova "
      "   [16]Yoru        [17]Harbor\n")
print('Для выбора рандомного агента, укажите "-1" или "Random"')
print("A: Какого агента вы хотите инсталокнуть? (Можно вводить как индексы, так и полное имя)")
agent_to_instapick = input("B: Введите Агента: ")
if agent_to_instapick == "-1" or agent_to_instapick == "Random":
    agent_to_instapick = random.choice(agents)
    work_variant = "2"
else:
    print("\nA: Выберите вид работы: \n    [1] Работа по координатам (Дольше) \n    [2] Работа по поиску изображения")
    work_variant = input("B: Введите выбранную цифру: ")
if work_variant != "1" and work_variant != "2":
    print("Выбрана неправильная цифра, доступны только 1 или 2.")
    quit()

generate_path(agent_name=agent_to_instapick, variant=work_variant)
