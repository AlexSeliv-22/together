import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Start')
window_surface = pygame.display.set_mode((800, 600))

color = 'white'
background = pygame.Surface((800, 600))

background.fill(pygame.Color(color))

manager = pygame_gui.UIManager(((800, 600)))

switch = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Switch',
    manager=manager
)

red = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((120, 475), (100, 50)),
    text='Red',
    manager=manager
)

green = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 475), (100, 50)),
    text='Green',
    manager=manager
)

blue = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((580, 475), (100, 50)),
    text='Blue',
    manager=manager
)

difficulty = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
    options_list=['Просто', 'Средне', 'Сложно', 'УЖАСНАХ'],
    starting_option='Просто',
    relative_rect=pygame.Rect((350, 150), (100, 25)),
    manager=manager
)

entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((350, 100), (100, 25)),
    manager=manager
)

clock = pygame.time.Clock()
run = True
while run:
    time_delta = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
                rect=pygame.Rect((250, 200), (300, 200)),
                manager=manager,
                window_title='Подтвердите действие',
                action_long_desc='Вы уверены, что хотите выйти?',
                action_short_name='OK',
                blocking=True
            )
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                run = False
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                print(f'name: {event.text}')
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                print(f'difficulty: {event.text}')
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                if event.ui_element == red:
                    color = 'red'
                    # background.fill(pygame.Color(color))
                if event.ui_element == green:
                    color = 'green'
                    # background.fill(pygame.Color(color))
                if event.ui_element == blue:
                    color = 'blue'
                background.fill(pygame.Color(color))
            if event.user_type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                if event.ui_element != switch:
                    color = 'black'
                    background.fill(pygame.Color(color))
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == switch:
                    color = 'black' if color == 'white' else 'white'
                    background.fill(pygame.Color(color))
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()

