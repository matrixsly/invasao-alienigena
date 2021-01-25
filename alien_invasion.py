 
import pygame # importando todo o modulo
from settings import settings # importando apenas funcao settings
from ship import Ship  # importando apenas a funcao ship
import game_functions as gf # importando todo o modulo e mudando o nome do mesmo 
def run_game():

    # Inicializar o jogo, e as configuracoes e o objeto screen
    pygame.init() #inicializa as configuracoes de segundo plano de que o pygame precisa para funciona de forma apropriada 

    ai_settings = settings() # aqui e uma instancia da classe settings
    
    # aqui em baixo e codigo da tela que define largura e coprimento 
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    # aqui e o titulo 
    pygame.display.set_caption("alien Ivasion")

    # cria uma espaconave
    ship = Ship(screen)
    
 
    # Inicia o laco principal
    
    while True:
        
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)

        
        
        

        

run_game()



        
