import pygame
import pygame.constants


if __name__ == "__main__":
    pygame.init()

    joystick = pygame.joystick.Joystick(0)

    while True:
        for event in pygame.event.get(): # get the events (update the joystick)
            if event.type == pygame.constants.QUIT: # allow to click on the X button to close the window
                pygame.quit()
                exit()
        print(joystick.get_guid())
        print(joystick.get_name())
        if joystick.get_button(1):
            print("1")
        if joystick.get_button(0):
            print("stopped")
            break

# WORKS