from tkinter import *
from tkinter import ttk
import logic
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
                             sticky=(W, E))  # sticky at w and e margins

        ttk.Button(mainframe, text="find",
                   command=self.find).grid(
            column=3,
            row=3,
            sticky=W)
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
            print(responseJSON)
            ID = responseJSON['id']
            ID = str(ID)
            print(ID)
            responseJSON2 = self.requestRankedData(region, ID, APIKey)
            print(responseJSON2)
            print(responseJSON2[0]['tier'])
            print(responseJSON2[0]['rank'])
            responseJSON3 = self.requestLiveData(region, ID, APIKey)
            for item in responseJSON3:
                print(item + ": " + str(responseJSON3[item]))

            participants = responseJSON3["participants"]
            for player in participants:
                print(player["summonerName"])

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
