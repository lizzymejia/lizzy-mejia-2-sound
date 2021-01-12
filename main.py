while True:
    if input.sound_level() < 40:
        light.show_animation(light.rainbowAnimation, 30000)
else:
        light.clear()