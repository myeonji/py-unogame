from typing import Tuple, Union, Optional, Dict, Iterable

import pygame
from pygame_gui.core import IContainerLikeInterface, UIElement, ObjectID
from pygame_gui.core.interfaces import IUIManagerInterface

from widgets import FocusableUIButton


class ScrollableUIButton(FocusableUIButton):
    def __init__(self, relative_rect: Union[pygame.Rect, Tuple[float, float], pygame.Vector2], text: str,
                 manager: Optional[IUIManagerInterface] = None, container: Optional[IContainerLikeInterface] = None,
                 tool_tip_text: Union[str, None] = None, starting_height: int = 1, parent_element: UIElement = None,
                 object_id: Union[ObjectID, str, None] = None, anchors: Dict[str, Union[str, UIElement]] = None,
                 allow_double_clicks: bool = False,
                 generate_click_events_from: Iterable[int] = frozenset([pygame.BUTTON_LEFT]), visible: int = 1, *,
                 tool_tip_object_id: Optional[ObjectID] = None, text_kwargs: Optional[Dict[str, str]] = None,
                 tool_tip_text_kwargs: Optional[Dict[str, str]] = None):
        super().__init__(relative_rect, text, manager, container, tool_tip_text, starting_height, parent_element,
                         object_id, anchors, allow_double_clicks, generate_click_events_from, visible,
                         tool_tip_object_id=tool_tip_object_id, text_kwargs=text_kwargs,
                         tool_tip_text_kwargs=tool_tip_text_kwargs)
        self.starting_rect = relative_rect

