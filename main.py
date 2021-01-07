from tkinter import *
from tkinter import ttk

import requests

APIKey = "RGAPI-8a1474d7-373a-45ab-b8b6-65617bd848c8"


class QuickMatchFinder:

    def __init__(self, root):
        # create a frame widget, which holds content of UI in place
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # create data entry widget
        self.name = StringVar()
        self.name_entry = ttk.Entry(mainframe, width=7, textvariable=self.name)
        self.name_entry.grid(column=2, row=1,
                             sticky=(N, W, E, S))  # sticky at w and e margins

        # button widget
        submit = ttk.Button(mainframe, text="find",
                            command=self.find).grid(
            column=3,
            row=1,
            sticky=(N, W, E, S))

        # try greeting
        # greeting = ttk.Label(text="Welcome to QuickMatch")
        # greeting.grid(column=1, row=2, sticky=(N, W))

        # try players
        self.player1 = ttk.Label(text="summoner1")
        self.player1.grid(column=0, row=2, sticky=(N, W, E, S))
        self.player2 = ttk.Label(text="summoner2")
        self.player2.grid(column=0, row=3, sticky=(N, W, E, S))
        self.player3 = ttk.Label(text="summoner3")
        self.player3.grid(column=0, row=4, sticky=(N, W, E, S))
        self.player4 = ttk.Label(text="summoner4")
        self.player4.grid(column=0, row=5, sticky=(N, W, E, S))
        self.player5 = ttk.Label(text="summoner5")
        self.player5.grid(column=0, row=6, sticky=(N, W, E, S))
        self.player6 = ttk.Label(text="summoner6")
        self.player6.grid(column=1, row=2, sticky=(N, W, E, S))
        self.player7 = ttk.Label(text="summoner7")
        self.player7.grid(column=1, row=3, sticky=(N, W, E, S))
        self.player8 = ttk.Label(text="summoner8")
        self.player8.grid(column=1, row=4, sticky=(N, W, E, S))
        self.player9 = ttk.Label(text="summoner9")
        self.player9.grid(column=1, row=5, sticky=(N, W, E, S))
        self.player10 = ttk.Label(text="summoner10")
        self.player10.grid(column=1, row=6, sticky=(N, W, E, S))

        # small optimization details
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.name_entry.focus()
        root.bind("<Return>", self.find)

    def find(self, *args):

        summoner = str(self.name.get())
        if summoner is None:
            print('hah gay')
            pass
        if summoner == '':
            print('heh gay')
            pass
        else:
            region = "na1"

            summonerName = summoner
            responseJSON = self.requestSummonerData(region, summonerName,
                                                    APIKey)
            # print(responseJSON)
            ID = responseJSON['id']
            ID = str(ID)
            # print(ID)
            responseJSON2 = self.requestRankedData(region, ID, APIKey)
            # print(responseJSON2)
            # print(responseJSON2[0]['tier'])
            # print(responseJSON2[0]['rank'])
            responseJSON3 = self.requestLiveData(region, ID, APIKey)
            try:
                for item in responseJSON3:
                    print(item + ": " + str(responseJSON3[item]))

                participants = responseJSON3["participants"]
                players = []
                for player in participants:
                    print(player["summonerName"])
                    players.append(player["summonerName"])
                # blue team
                self.player1 = ttk.Label(text=players[0])
                self.player1.grid(column=0, row=2, sticky=(N, W, E, S))
                self.player2 = ttk.Label(text=players[1])
                self.player2.grid(column=0, row=3, sticky=(N, W, E, S))
                self.player3 = ttk.Label(text=players[2])
                self.player3.grid(column=0, row=4, sticky=(N, W, E, S))
                self.player4 = ttk.Label(text=players[3])
                self.player4.grid(column=0, row=5, sticky=(N, W, E, S))
                self.player5 = ttk.Label(text=players[4])
                self.player5.grid(column=0, row=6, sticky=(N, W, E, S))

                # red team
                self.player6 = ttk.Label(text=players[5])
                self.player6.grid(column=1, row=2, sticky=(N, W, E, S))
                self.player7 = ttk.Label(text=players[6])
                self.player7.grid(column=1, row=3, sticky=(N, W, E, S))
                self.player8 = ttk.Label(text=players[7])
                self.player8.grid(column=1, row=4, sticky=(N, W, E, S))
                self.player9 = ttk.Label(text=players[8])
                self.player9.grid(column=1, row=5, sticky=(N, W, E, S))
                self.player10 = ttk.Label(text=players[9])
                self.player10.grid(column=1, row=6, sticky=(N, W, E, S))
            except:
                print("an error occurred")

    @staticmethod
    def requestSummonerData(region, summonerName, Key):
        URL = "https://" + region + ".api.riotgames.com/lol/" + \
              "summoner/v4/summoners/by-name/" + summonerName + \
              '?api_key=' + Key
        # https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/ori%C3%B3n
        print(URL)
        response = requests.get(URL)
        return response.json()

    @staticmethod
    def requestRankedData(region, ID, Key):
        URL = "https://" + region + \
              ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + \
              '?api_key=' + Key
        # /lol/league/v4/entries/by-summoner/{encryptedSummonerId}

        print(URL)
        response = requests.get(URL)
        return response.json()

    @staticmethod
    def requestLiveData(region, ID, Key):
        URL = "https://" + region + \
              ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + \
              ID + '?api_key=' + Key
        print(URL)
        response = requests.get(URL)
        return response.json()


if __name__ == '__main__':
    root = Tk()
    root.title("QuickMatchFinder")
    QuickMatchFinder(root)

    root.mainloop()
