from prefabs.components.transform import TransformState
from .component_pane import ComponentPane


class TransformPane(ComponentPane[TransformState]):
    def __str__(self) -> str:
        return f'Вы находитесь в координатах {self._component.position.x}x{self._component.position.y}'
