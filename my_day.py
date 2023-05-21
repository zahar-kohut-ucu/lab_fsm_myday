'''Lab 2.3 DM, Kohut'''
import random

class MyDay:
    '''
    FSM class to simulate my day.
    '''
    def __init__(self):
        self.start = self._create_start()
        self.eat = self._create_eat()
        self.code = self._create_code()
        self.dota2 = self._create_dota2()
        self.sleep = self._create_sleep()
        self.tiktok = self._create_tiktok()
        self.football = self._create_football()
        self.learn = self._create_learn()

        self.current = self.start

    def _create_start(self):
        '''
        Start state.
        '''
        while True:
            time = yield
            if time == 0:
                self.current = self.dota2

    def _create_eat(self):
        '''
        Start state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print(f'Occupation: {random.choice(["Eating delicious food", "Emptying my fridge"])}...\n')
            rand = random.random()
            if time == 2:
                self.current = self.sleep
            elif time == 11:
                self.current = self.tiktok
            elif time == 16 and rand > 0.6:
                print('Just saw cool football edit in TikTok...\n')
                self.current = self.football
            elif time == 16 and rand <= 0.6:
                print('Feeling sleepy...\n')
                self.current = self.tiktok
            elif time == 22:
                self.current = self.dota2

    def _create_code(self):
        '''
        Code state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print(f'Occupation: {random.choice(["Coding", "Fixing bugs"])}...\n')
            if time == 15 or time == 21:
                self.current = self.eat

    def _create_dota2(self):
        '''
        Dota 2 state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print(f'Occupation: {random.choice(["Playing Dota 2", "Carrying games in Dota 2"])}...\n')
            rand = random.random()
            if time == 1 and rand <= 0.7:
                print('I had a great dinner and want to sleep...\n')
                self.current = self.tiktok
            elif time == 1 and rand > 0.7:
                print('Just realised I got pizza in my fridge...\n')
                self.current = self.eat
            elif time == 21:
                self.current = self.eat

    def _create_tiktok(self):
        '''
        TikTok state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print(f'Occupation: {random.choice(["Scrolling TikTok", "Watching memes"])}...\n')
            rand1 = random.random()
            rand2 = random.random()
            if time == 2:
                self.current = self.sleep
            elif time == 12 and rand1 <= 0.65:
                print('DM is too difficult, I will code...\n')
                self.current = self.code
            elif time == 12 and rand1 > 0.65:
                print('DM Test is tomorrow, I better study...\n')
                self.current = self.learn
            elif time == 17 and rand2 > 0.8:
                print('Feeling too lazy to do anything useful...\n')
                self.current = self.dota2
            elif time == 17 and 0.2 <= rand2 <= 0.8:
                print('It is time to write some code...\n')
                self.current = self.code
            elif time == 17 and rand2 < 0.2:
                print('Mayber calculus is not too difficult...\n')
                self.current = self.learn

    def _create_football(self):
        '''
        Football state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print(f'Occupation: {random.choice(["Playing football", "Scoring goals"])}...\n')
            if time == 17:
                self.current = self.code

    def _create_sleep(self):
        '''
        Sleep state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print(f'Occupation: {random.choice(["Sleeping", "Seeing dreams"])}...\n')
            if time == 10:
                self.current = self.eat

    def _create_learn(self):
        '''
        Learn state.
        '''
        while True:
            time = yield
            if time:
                print(f'Time: {(time - 1)%24}:00 -> {time%24}:00')
                print('Occupation: Studying...\n')
            if time == 15 or time == 21:
                self.current = self.eat

    def simulate(self):
        '''
        Simulates my day.
        '''
        self.start.send(None)
        self.eat.send(None)
        self.code.send(None)
        self.dota2.send(None)
        self.sleep.send(None)
        self.tiktok.send(None)
        self.football.send(None)
        self.learn.send(None)
        print('Start of a new day:\n')
        for _t in range(25):
            self.current.send(_t)
        print('\nThe day ended:(')

#Uncomment and start to watch the simulation.
# myday = MyDay()
# myday.simulate()
