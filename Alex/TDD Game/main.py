import unittest  ## importam ceva inexistent momentan
'''
package-ul = "game"
module = "Enemy"
class = "Enemy" (al doilea Enemy)'''
from game.Enemy import Enemy

class EnemyConstructorTest(unittest.TestCase):
    def test_EnemyName(self):
        enemy1 = Enemy("Orc")
        result = enemy1.name
        self.assertEqual(result, "Orc")
    def test_EnemyLives(self):
        enemy1 = Enemy("Wizzard")
        result = enemy1.lives
        self.assertEqual(result, 10)

    def test_receive_dmg(self):
        orc = Enemy("Orc")
        orc.receive_dmg()
        result = orc.lives
        self.assertEqual(result, 9)

    def test_receive_dmg(self):
        orc = Enemy("Orc")
        result = orc.is_alive()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()