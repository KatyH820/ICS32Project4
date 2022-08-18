from columns import *
from project4 import *
import unittest


class GameRunningTest(unittest.TestCase):
    def test_game_running_with_an_empty_field(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        self.assertEqual(game_state.game_is_running(), True)

    def test_game_running_with_an_content_field(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', 'Y', 'Z'],
             ['X', 'X', 'Y']])
        self.assertEqual(game_state.game_is_running(), True)


class GameSetUpTest(unittest.TestCase):
    def test_jewels_fall_when_there_is_hole_in_contents_field(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', 'Y'],
             ['X', 'Y', ' '],
             [' ', ' ', 'Y'],
             [' ', 'Z ', ' ']])
        game_state.matching()
        game_state.update_matching_game_board()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['X', 'Y', 'Y'],
                                                           ['X', 'Z ', 'Y']])

    def test_jewels_fall_and_match_when_given_contents_field(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', 'Y'],
             ['X', 'Y', ' '],
             ['X', ' ', 'Y'],
             [' ', 'Z ', ' ']])
        game_state.matching()
        game_state.update_matching_game_board()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', 'Y', 'Y'],
                                                           [' ', 'Z ', 'Y']])


class GameOver(unittest.TestCase):
    def test_quit_with_Q_command(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        game_state.stop_running()
        self.assertEqual(game_state.game_is_running(), False)

    def test_game_do_not_over_when_matching_enough_jewels_which_make_everything_fit(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', ' '],
             ['X', ' ', ' '],
             ['Y', ' ', ' ']])
        faller = Faller(['Y', 'X', 'X'], 0)
        game_state.add_faller(faller)
        game_state.matching()
        game_state.update_matching_game_board()
        self.assertEqual(game_state.game_is_over(), False)

    def test_game_over_when_faller_freeze_but_cannot_display_entirely_on_field(self):
        game_state = GameState([['X', ' ', ' '],
                                ['Y', ' ', ' '],
                                ['Z', ' ', ' '],
                                ['X', ' ', ' '],
                                ['X', ' ', ' '],
                                ['Y', ' ', ' ']])
        faller = Faller(['Y', 'X', 'X'], 0)
        game_state.add_faller(faller)
        self.assertEqual(game_state.game_is_over(), True)


class MatchingTest(unittest.TestCase):
    def test_horizontal_matching(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', 'X', 'X'],
             ['X', 'S', 'Y'],
             ['Y', 'Z', 'Z'],
             ['S', 'Z', 'Y']])
        game_state.matching()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['*X*', '*X*', '*X*'],
                                                           ['X', 'S', 'Y'],
                                                           ['Y', 'Z', 'Z'],
                                                           ['S', 'Z', 'Y']])

    def test_vertical_matching(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', 'Y', 'Z'],
             ['X', 'S', 'Y'],
             ['X', 'Z', 'Z'],
             ['X', 'S', 'X']])
        game_state.matching()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['*X*', 'Y', 'Z'],
                                                           ['*X*', 'S', 'Y'],
                                                           ['*X*', 'Z', 'Z'],
                                                           ['*X*', 'S', 'X']])

    def test_diagnol_matching(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', 'Y', 'Z'],
             ['S', 'X', 'Y'],
             ['X', 'Z', 'X'],
             ['X', 'S', 'X']])
        game_state.matching()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['*X*', 'Y', 'Z'],
                                                           ['S', '*X*', 'Y'],
                                                           ['X', 'Z', '*X*'],
                                                           ['X', 'S', 'X']])

    def test_combo_matching(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', 'Y', 'Z'],
             ['X', 'X', 'Y'],
             ['X', 'Z', 'X'],
             ['X', 'X', 'X']])
        game_state.matching()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['*X*', 'Y', 'Z'],
                                                           ['*X*', '*X*', 'Y'],
                                                           ['*X*', 'Z', '*X*'],
                                                           ['*X*', '*X*', '*X*']])

    def test_entire_board_matching(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', 'X', 'X'],
             ['X', 'X', 'X'],
             ['X', 'X', 'X'],
             ['X', 'X', 'X']])
        game_state.matching()
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['*X*', '*X*', '*X*'],
                                                           ['*X*', '*X*', '*X*'],
                                                           ['*X*', '*X*', '*X*'],
                                                           ['*X*', '*X*', '*X*']])


class AddFallerTest(unittest.TestCase):
    def test_add_faller_correctly(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        self.assertEqual(game_state.current_game_board(), [['[X]', ' ', ' '],
                                                           ['[Y]', ' ', ' '],
                                                           ['[Z]', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])


class EnterTest(unittest.TestCase):
    def test_normal_enter_action_move_faller_down(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        game_state.enter_action(faller)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           ['[X]', ' ', ' '],
                                                           ['[Y]', ' ', ' '],
                                                           ['[Z]', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])

    def test_change_land_and_freeze_enter_action(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        game_state.enter_action(faller)
        game_state.enter_action(faller)
        game_state.enter_action(faller)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['|X|', ' ', ' '],
                                                           ['|Y|', ' ', ' '],
                                                           ['|Z|', ' ', ' ']])
        game_state.enter_action(faller)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])


class RotateTest(unittest.TestCase):
    def test_rotate_color_list_move_color_correctly(self):
        faller = Faller(['X', 'Y', 'Z'], 0)
        self.assertEqual(faller.rotate_color_list(), ['Z', 'X', 'Y'])

    def test_rotate_action(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        game_state.rotate_action(faller)
        self.assertEqual(game_state.current_game_board(), [['[Z]', ' ', ' '],
                                                           ['[X]', ' ', ' '],
                                                           ['[Y]', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])
        game_state.rotate_action(faller)
        self.assertEqual(game_state.current_game_board(), [['[Y]', ' ', ' '],
                                                           ['[Z]', ' ', ' '],
                                                           ['[X]', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])

    def test_can_rotate_until_frozen(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        game_state.rotate_action(faller)
        self.assertEqual(game_state.current_game_board(), [['[Z]', ' ', ' '],
                                                           ['[X]', ' ', ' '],
                                                           ['[Y]', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])
        game_state.enter_action(faller)
        game_state.enter_action(faller)
        game_state.enter_action(faller)
        game_state.rotate_action(faller)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           ['|Y|', ' ', ' '],
                                                           ['|Z|', ' ', ' '],
                                                           ['|X|', ' ', ' ']])
        game_state.enter_action(faller)
        self.assertEqual(game_state.faller_on_gameboard(), False)
        # If there is no faller on gameboard, it will not rotate


class MoveTest(unittest.TestCase):
    def test_move_left_correcly(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 1)
        game_state.add_faller(faller)
        game_state.move_action(faller, -1)
        self.assertEqual(game_state.current_game_board(), [['[X]', ' ', ' '],
                                                           ['[Y]', ' ', ' '],
                                                           ['[Z]', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])

    def test_move_right_correcly(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 1)
        game_state.add_faller(faller)
        game_state.move_action(faller, 1)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', '[X]'],
                                                           [' ', ' ', '[Y]'],
                                                           [' ', ' ', '[Z]'],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' '],
                                                           [' ', ' ', ' ']])

    def test_moving_faller_from_land_to_nothing_underneath_change_its_status_from_land_to_fall(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', ' '],
             ['Y', ' ', ' '],
             ['Z', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        self.assertEqual(game_state.current_game_board(), [['|X|', ' ', ' '],
                                                           ['|Y|', ' ', ' '],
                                                           ['|Z|', ' ', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])
        game_state.move_action(faller, 1)
        self.assertEqual(game_state.current_game_board(), [[' ', '[X]', ' '],
                                                           [' ', '[Y]', ' '],
                                                           [' ', '[Z]', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])

    def test_moving_faller_to_something_underneath_change_its_status_from_fall_to_land(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', ' '],
             ['Y', ' ', ' '],
             ['Z', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 1)
        game_state.add_faller(faller)
        self.assertEqual(game_state.current_game_board(), [[' ', '[X]', ' '],
                                                           [' ', '[Y]', ' '],
                                                           [' ', '[Z]', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])
        game_state.move_action(faller, -1)
        self.assertEqual(game_state.current_game_board(), [['|X|', ' ', ' '],
                                                           ['|Y|', ' ', ' '],
                                                           ['|Z|', ' ', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])

    def test_faller_cannot_move_if_they_are_blocked_by_jewels(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', ' '],
             ['Y', ' ', ' '],
             ['Z', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 1)
        game_state.add_faller(faller)
        self.assertEqual(game_state.current_game_board(), [[' ', '[X]', ' '],
                                                           [' ', '[Y]', ' '],
                                                           [' ', '[Z]', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])
        game_state.enter_action(faller)
        if game_state.can_move(faller, -1):
            game_state.move_action(faller, -1)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', ' '],
                                                           [' ', '[X]', ' '],
                                                           [' ', '[Y]', ' '],
                                                           ['X', '[Z]', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])

    def test_faller_cannot_move_right_if_they_on_the_most_right_position_of_game_board(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', ' '],
             ['Y', ' ', ' '],
             ['Z', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 2)
        game_state.add_faller(faller)
        if game_state.can_move(faller, 1):
            game_state.move_action(faller, 1)
        self.assertEqual(game_state.current_game_board(), [[' ', ' ', '[X]'],
                                                           [' ', ' ', '[Y]'],
                                                           [' ', ' ', '[Z]'],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])

    def test_faller_cannot_move_right_if_they_on_the_most_left_position_of_game_board(self):
        game_state = GameState(
            [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             ['X', ' ', ' '],
             ['Y', ' ', ' '],
             ['Z', ' ', ' ']])
        faller = Faller(['X', 'Y', 'Z'], 0)
        game_state.add_faller(faller)
        if game_state.can_move(faller, -1):
            game_state.move_action(faller, -1)
        self.assertEqual(game_state.current_game_board(), [['|X|', ' ', ' '],
                                                           ['|Y|', ' ', ' '],
                                                           ['|Z|', ' ', ' '],
                                                           ['X', ' ', ' '],
                                                           ['Y', ' ', ' '],
                                                           ['Z', ' ', ' ']])


if __name__ == '__main__':
    unittest.main()
