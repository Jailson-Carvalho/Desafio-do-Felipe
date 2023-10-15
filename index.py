# Desafio do Felipe

xp_adquirida = 10.001
nome = 'Atirador'
nivel1 = 1.000
nivel01 = 'você alcançou o nível Ferro.'
nivel2 = [1.001 or 2.000]
nivel02 = 'você alcançou o nível Broze.'
nivel3 = [2.001 or 5.000]
nivel03 = 'você alcançou o nível Prata.'
nivel4 = [5.001 or 7.000]
nivel04 = 'você alcançou o nível Ouro.'
nivel5 = [7.001 or 8.000]
nivel05 = 'você alcançou o nível Platina.'
nivel6 = [8.001 or 9.000]
nivel06 = 'você alcançou o nível Ascendente.'
nivel7 = [9.001  or 10.000]
nivel07 = 'você alcançou o nível Imortal.'
nivel8 = 10.001
nivel08 = 'você alcançou o nível Radiante.'
if xp_adquirida <= 1.000:
    print(f'Olá {nome}, {nivel01}')
elif xp_adquirida >= 1.001 and xp_adquirida <= 2.000:
    print(f'Olá {nome}, {nivel02}')
elif xp_adquirida >= 2.001 and xp_adquirida <= 5.000:
    print(f'Olá {nome}, {nivel03}')
elif xp_adquirida >= 5.001 and xp_adquirida <= 7.000:
    print(f'Olá {nome}, {nivel04}')
elif xp_adquirida >= 7.001 and xp_adquirida <= 8.000:
    print(f' Olá {nome}, {nivel05}')
elif xp_adquirida >= 8.001 and xp_adquirida <= 9.000:
    print(f'Olá {nome}, {nivel06}')
elif xp_adquirida >= 9.001 and xp_adquirida <= 10.000:
    print(f'Olá {nome}, {nivel07}')
if xp_adquirida >= 10.001:
    print(f'Olá {nome}, {nivel08}')
print(f'Olá {nome}, você está no nível Radiante, o mais alto nível que um atirador pode alcançar, parabéns!')