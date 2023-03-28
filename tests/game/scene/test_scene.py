from angry_oleg.assets.objects.vacuum import Vacuum
from game.scenes import Scene


def test_add_object():
    vacuum = Vacuum()
    scene = Scene()

    # Act
    scene.add_object(vacuum)

    # Assert
    assert scene.get_all_objects() == [vacuum]
    assert scene.get_objects_by_tag(vacuum.tag) == [vacuum]


def test_add_object_twice():
    vacuum = Vacuum()
    scene = Scene()

    # Act
    scene.add_object(vacuum)
    scene.add_object(vacuum)

    # Assert
    assert scene.get_all_objects() == [vacuum]
    assert scene.get_objects_by_tag(vacuum.tag) == [vacuum]
