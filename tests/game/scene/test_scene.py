from assets.objects.vacuum import Vacuum
from game.objects import ObjectType
from game.scene import Scene


def test_add_object():
    vacuum = Vacuum()
    scene = Scene()

    # Act
    scene.add_object(vacuum)

    # Assert
    assert scene.get_all_objects() == [vacuum]
    assert scene.get_objects_by_type(ObjectType.Vacuum) == [vacuum]


def test_add_object_twice():
    vacuum = Vacuum()
    scene = Scene()

    # Act
    scene.add_object(vacuum)
    scene.add_object(vacuum)

    # Assert
    assert scene.get_all_objects() == [vacuum]
    assert scene.get_objects_by_type(ObjectType.Vacuum) == [vacuum]
