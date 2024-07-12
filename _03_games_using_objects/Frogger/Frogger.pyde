
def setup():
    # 1. Use the size function to set the size of your sketch
    size(1000, 1000)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    global frog_x, frog_y
    global bg, ch
    global car1
    global car2
    global car3
    bg = loadImage("froggerBackground.png")
    ch = loadImage("frog.png")
    frog_x = 500
    frog_y = 950
    car1 = Car(500, 500, 150, 20)
    car2 = Car(500, 775, 120, -10)
    car3 = Car(500, 275, 180, -30)
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    bg.resize(1000, 1000)
    ch.resize(50, 50)
def draw():
    global frog_x, frog_y
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    image(ch, frog_x, frog_y)
    if(keyPressed == True):
        if(keyCode == UP):
            frog_y -= 5
        if(keyCode == DOWN):
            frog_y += 5
        if(keyCode == LEFT):
            frog_x -= 5
        if(keyCode == RIGHT):
            frog_x += 5
    if car1.intersects():
        frog_x = 500
        frog_y = 950
    if car2.intersects():
        frog_x = 500
        frog_y = 950
    if car3.intersects():
        frog_x = 500
        frog_y = 950
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    car1.draw()
    car1.update()
    car2.draw()
    car2.update()
    car3.draw()
    car3.update()
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
        
    # 9. Create more car objects of different lengths, speed, and size

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
    
    def  intersects(self):
        if frog_x <= self.x + self.length and frog_x >= self.x:
            if frog_y <= self.y + (.33 * self.length) and frog_y >= self.y:
                return True
        else:
            return False
