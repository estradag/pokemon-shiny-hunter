import subprocess

exclusions = [201,351]

for i in range (1,386):
    if i in exclusions:
        continue
    subprocess.run(['wget', '-P', 'shiny_sprites','https://www.pokencyclopedia.info/sprites/gen3/spr_emerald_shiny/spr_e-S_{}_1.png'.format(str(i).rjust(3, '0'))])
