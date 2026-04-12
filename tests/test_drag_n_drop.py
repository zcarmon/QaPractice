from playwright.sync_api import Page

from utils import drag_n_drop


def test_drag_n_drop_box(page : Page):

    drag_n_drop.drag_n_drop(page,
                            "https://www.qa-practice.com/elements/dragndrop/boxes",
                            "#rect-draggable",
                            "#rect-droppable",
                            500,
                            "Dropped!")

def test_drag_and_drop_images_back_and_forth(page: Page):

    drag_n_drop.drag_n_drop(page,
                            "https://www.qa-practice.com/elements/dragndrop/images",
                            "#rect-droppable1",
                            "#rect-droppable2",
                            500,
                            "Dropped!",
                            "img",
                            True)
