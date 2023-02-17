import pytest

from math import sqrt
from angry_oleg.assets import Vacuum
from game.exceptions import InvalidMapSizeError
from game.scenes.map import Direction, Map, Position


def test_size():
    # Act
    game_map = Map(5, 4)

    # Assert
    assert game_map.size_x == 5
    assert game_map.size_y == 4


@pytest.mark.parametrize('size_x, size_y', [
    (-1, 4),
    (0, 4),
    (5, -1),
    (5, 0),
])
def test_wrong_size(size_x, size_y):
    # Act and assert
    with pytest.raises(InvalidMapSizeError):
        Map(size_x, size_y)


def test_find_object():
    vacuum = Vacuum()
    game_map = Map(5, 4)

    # Act
    game_map.place_object(vacuum.id, Position(2, 3))

    # Assert
    assert game_map.find_object(vacuum.id) == Position(2, 3)


def test_find_missing_object():
    vacuum = Vacuum()
    game_map = Map(5, 4)

    # Assert
    assert game_map.find_object(vacuum.id) is None


def test_get_objects():
    object_1 = Vacuum()
    object_2 = Vacuum()
    game_map = Map(5, 4)

    # Act
    game_map.place_object(object_1.id, Position(2, 3))
    game_map.place_object(object_2.id, Position(2, 3))

    # Assert
    object_ids = game_map[Position(2, 3)]
    assert set(object_ids) == {object_1.id, object_2.id}


def test_calc_distance():
    object_1 = Vacuum()
    object_2 = Vacuum()
    game_map = Map(5, 4)

    # Act
    game_map.place_object(object_1.id, Position(1, 1))
    game_map.place_object(object_2.id, Position(3, 3))

    # Assert
    real_distance = sqrt(8)
    assert game_map.calc_distance(object_1.id, object_2.id) == real_distance
    assert game_map.calc_distance(object_2.id, object_1.id) == real_distance


@pytest.mark.parametrize('position, expected_direction', [
    (Position(3, 2), Direction.East),
    (Position(1, 2), Direction.West),
    (Position(2, 3), Direction.North),
    (Position(2, 1), Direction.South),
    (Position(3, 3), Direction.NorthEast),
    (Position(1, 1), Direction.SouthWest),
    (Position(3, 1), Direction.SouthEast),
    (Position(1, 3), Direction.NorthWest),
])
def test_get_direction(position, expected_direction):
    object_1 = Vacuum()
    object_2 = Vacuum()
    game_map = Map(5, 4)

    # Act
    game_map.place_object(object_1.id, Position(2, 2))
    game_map.place_object(object_2.id, position)

    # Assert
    assert game_map.get_direction(object_1.id, object_2.id) == expected_direction


@pytest.mark.parametrize('position, expected_is_valid', [
    (Position(0, 2), False),
    (Position(-1, 2), False),
    (Position(6, 2), False),
    (Position(5, 2), True),
    (Position(1, 2), True),
    (Position(2, 0), False),
    (Position(2, -1), False),
    (Position(2, 5), False),
    (Position(2, 4), True),
    (Position(2, 1), True),
])
def test_is_valid_position(position, expected_is_valid):
    game_map = Map(5, 4)

    # Act
    is_valid = game_map.is_valid_position(position)

    # Assert
    assert is_valid == expected_is_valid


def test_place_object_in_random_position():
    vacuum = Vacuum()
    game_map = Map(5, 4)

    # Act
    game_map.place_object_in_random_position(vacuum.id)

    # Assert
    assert game_map.find_object(vacuum.id) is not None


def test_remove_object():
    vacuum = Vacuum()
    game_map = Map(5, 4)
    game_map.place_object_in_random_position(vacuum.id)

    # Act
    game_map.remove_object(vacuum.id)

    # Assert
    assert game_map.find_object(vacuum.id) is None
