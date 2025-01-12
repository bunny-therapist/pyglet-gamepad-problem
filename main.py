import pyglet
from pyglet.input import Controller, get_controllers
from pyglet.input import get_joysticks
from pyglet.input.controller import get_mapping

def setup_gamepad(
    gamepad,
) -> None:
    def on_button_press(controller, key: str) -> None:
        print(f"{key} pressed on {controller}")

    def on_button_release(controller, key: str) -> None:
        print(f"{key} released on {controller}")

    def on_dpad_motion(
        controller,
        left: bool,
        right: bool,
        up: bool,
        down: bool,
    ) -> None:
        pressed = []
        if left:
            pressed.append("L")
        if right:
            pressed.append("R")
        if up:
            pressed.append("U")
        if down:
            pressed.append("D")
        print(f"dpad motion: {pressed} on {controller}")

    guid = gamepad.device.get_guid()
    print(type(gamepad.device))
    # <class 'pyglet.input.win32.directinput.DirectInputDevice'>
    # print(f"product guid Data1: {gamepad.device.product_guid.Data1}")
    # 32760 without window
    # 0 with window

    print(f"guid = {guid}")
    # 03000000f87f00000000000000000000 without window
    # 03000000000000000000000000000000 with window

    # NOTE: gamepad works with pygame and gives guid = 0300dafe830500006020000000000000

    mapping = get_mapping(guid)
    assert mapping is not None, "No mapping found!"
    # No mapping found, both with and without window
    # This used to work though, back in version
    print(f"mapping found: {mapping}")
    game_controller = Controller(
        gamepad.device, mapping
    )
    game_controller.open()
    handlers = (on_button_press, on_button_release, on_dpad_motion)
    game_controller.push_handlers(*handlers)

if __name__ == "__main__":
    print(f"pyglet v{pyglet.version}")  # pyglet v2.1.0
    window = pyglet.window.Window()  # Commenting this out changes guid of gamepad

    joysticks = get_joysticks()
    print(f"Found joysticks: {joysticks}")
    # Found joysticks: [Joystick(device=USB,2-axis 8-button gamepad  )]
    # NOTE: This is what pygame also calls it
    controllers = get_controllers()
    print(f"Found controllers: {controllers}")
    # Found controllers: [] - why is this not a controller?

    gamepad = joysticks[0]
    print(gamepad)  # Joystick(device=USB,2-axis 8-button gamepad  )

    setup_gamepad(gamepad)
    print("gamepad setup")
    pyglet.app.run()


# GAMEPAD INFORMATION.
# Buffalo Classic USB Gamepad
# BSGP801 Series
# S/N: A10328
# https://armchairarcade.com/perspectives/2016/04/25/review-buffalo-classic-usb-gamepad-super-nes-style/
# Works with games, used to work with pyglet, works with pygame
# Pygame gives the guid as 0300dafe830500006020000000000000 and calls it "USB,2-axis 8-button gamepad"

# Broken in this commit:
# https://github.com/pyglet/pyglet/commit/6357ce0707e152fc13473b052a024e431003af1d
