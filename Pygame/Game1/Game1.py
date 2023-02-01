import pygame
pygame.init()
# Các biến khởi tạo trong game
p = 0.1 #Hằng trọng lực
bird_y = 0 # Tạo độ y của chim
score  = 0
H_score = 0
game_play = True
#Score
game_font = pygame.font.Font(r'04B_19.TTF',40)
def score_view():
    if game_play:
        score_f = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_f.get_rect(center = (200,100))
        screen.blit(score_f,score_rect)
    else:
        score_f = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_f.get_rect(center = (200,100))
        screen.blit(score_f,score_rect)
        hscore_f = game_font.render(f'High score: {int(score)}',True,(255,255,255))
        hscore_rect = hscore_f.get_rect(center = (200,150))
        screen.blit(hscore_f,hscore_rect)

# Tiêu đề và icon
pygame.display.set_caption('Game 1')
icon = pygame.image.load(r'assets\yellowbird-downflap.png')
pygame.display.set_icon(icon)
# Background 
bg = pygame.image.load(r'assets\background-night.png')
bg = pygame.transform.scale2x(bg)
floor = pygame.image.load(r'assets\floor.png')
floor = pygame.transform.scale2x(floor)
fl_x = 0
# Tạo cửa sổ game
screen = pygame.display.set_mode((432,768))
# Đưa bird vào
bird = pygame.image.load(r'assets\yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_rec = bird.get_rect(center = (100,386))
# Màn hình game over
overscreen = pygame.image.load(r'assets\message.png')
overscreen = pygame.transform.scale2x(overscreen)
overscreen_rect = overscreen.get_rect(center = (216,384))
#Hàm check va chạm
def check_vc():
    if bird_rec.bottom >=668 or bird_rec.top <= -75:
        return False
    else:
        return True
    
# Vòng lặp xử lý game
running = True
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_play:
                bird_y += -10
                bird_rec.centery += bird_y
            if event.key == pygame.K_SPACE and game_play == False:
                game_play=True
                bird_y = 0
                bird_rec.center = (100,386)

    # thêm vào màn hình game
    screen.blit(bg,(0,0))
    fl_x -=1
    screen.blit(floor,(fl_x,600))
    screen.blit(floor,(fl_x+432,600))
    if fl_x == -432:
        fl_x = 0

    if game_play:
        # Đưa bird vào game
        screen.blit(bird,bird_rec)
        bird_y += p
        bird_rec.centery += bird_y
        score +=0.01
        if score > H_score: H_score = score
        score_view()
        game_play = check_vc()
    else:
        screen.blit(overscreen,overscreen_rect)
        score_view()

    pygame.display.update()