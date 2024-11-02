import runner_and_tournament as rt
import unittest



class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_tour1(self):
        tour_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        result = tour_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним.')
        self.all_results['test_tour1'] = result


    def test_tour2(self):
        tour_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        result = tour_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним.')
        self.all_results['test_tour2'] = result

    def test_tour3(self):
        tour_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним.')
        self.all_results['test_tour3'] = result



    def test_tour4(self):
        tour_4 = rt.Tournament(6, self.runner_1, self.runner_2, self.runner_3)
        result = tour_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним.')
        self.all_results['test_tour4'] = result

    def test_tour5(self):
        tour_5 = rt.Tournament(90, self.runner_1, self.runner_2)
        result = tour_5.start()
        self.assertTrue('Ник' in self.all_results, 'Ник не участвует в забеге.')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним.')
        self.all_results['test_tour5'] = result


    if __name__ == '__main__':
        unittest.main()