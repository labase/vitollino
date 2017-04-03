from random import random, shuffle
from _spy.circus.braser import Braser, PHASER

DETAIL, DETAILURL = "dungeon_detail", "http://i-games.readthedocs.io/en/latest/_images/DungeonWall.jpg"
MONSTER, MONSTERURL = "monster", "http://i-games.readthedocs.io/en/latest/_images/monstersheets.png"
DETILE = "dungeon_detile"
FIRE, FIREURL = "fire", "http://s19.postimg.org/z9iojs2c3/magicfire.png"
FSP = 1.5
MOVES = {0: (0, FSP * 150), 90: (FSP * -150, 0), 180: (0, FSP * -150), 270: (FSP * 150, 0)}
DIR = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

# DETAIL, DETAILURL = "dungeon_detail", "http://s19.postimg.org/uoe2ycclv/Dungeon_Wall.jpg"
# MONSTER, MONSTERURL = "monster", "http://s19.postimg.org/fpvo3wxjn/monstersheets.png"
TILEN = "ABCDEFGHIJKLMN"
DIREN = "NLSO"


def desafio0(masmorra):
    return DesafioA(masmorra)


class Masmorra:
    _instance = None

    def __init__(self):
        self.gamer = Braser(800, 600)
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.hero = Hero(self)
        self.sprite = Monster(self)
        self.monsters = self.magic = None
        self.monster_list = []

    @classmethod
    def created(cls):
        cls._instance = Masmorra()
        cls.created = lambda *_: Masmorra._instance
        return cls._instance

    def posiciona_monstro(self, m, x, y):
        self.monster_list.append((m, x, y))

    def preload(self):
        self.game.load.spritesheet(MONSTER, MONSTERURL, 64, 63, 16 * 12)
        self.game.load.spritesheet(DETILE, DETAILURL, 128, 128, 12)
        self.game.load.spritesheet(FIRE, FIREURL, 96, 96, 25)

    def create(self):
        self.game.physics.startSystem(PHASER.Physics.ARCADE)
        self.game.add.sprite(0, 0, DETILE)
        rotate = 0
        for i in range(6):
            for j in range(5):
                detail = self.game.add.sprite(64 + i * 128, 64 + j * 128, DETILE)
                detail.anchor.setTo(0.5, 0.5)
                detail.angle = rotate
                detail.frame = (6 * j + i) % 12
                rotate += 90

        self.monsters = self.game.add.group()
        self.magic = self.game.add.group()
        self.monsters.enableBody = True
        self.magic.enableBody = True
        self.magic.checkWorldBounds = True
        self.magic.outOfBoundsKill = True

    def update(self):
        def kill(_, monster):
            monster.kill()

        def killall(magic, monster):
            magic.kill()
            monster.kill()

        self.game.physics.arcade.overlap(self.hero.sprite, self.sprite.sprite, kill, None, self)
        # self.game.physics.arcade.overlap(self.magic, self.monsters, killall, None, self)
        self.game.physics.arcade.overlap(self.magic, self.hero.sprite, killall, None, self)


class Monster:
    def __init__(self, masmorra):
        self.masmorra = masmorra
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.sprite = None
        self.direction = 0
        self.first = True

    def create(self):

        sprite = self.game.add.sprite(148, 148, MONSTER)
        sprite.animations.add('mon', [6 * 16 + 0, 6 * 16 + 1, 6 * 16 + 2, 6 * 16 + 3], 4, True)
        sprite.play('mon')
        self.game.physics.arcade.enable(sprite)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        sprite.body.bounce.setTo(1, 1)
        self.masmorra.monsters.add(sprite)
        self.sprite = sprite

    def preload(self):
        pass

    def update(self):
        player = self.sprite
        player.angle = (self.direction * 45 + 270) % 360
        if self.sprite.alive and int(random() + 0.02) or self.first:
            player.body.velocity.x, player.body.velocity.y = self.redirect(player, self.direction)
        player.animations.play('mon')

    def redirect(self, play, dd):
        self.first = False
        vx, vy = DIR[dd]
        self.direction = d = int(random() * 8.0)
        x, y = play.body.position.x, play.body.position.y
        if vx or vy:
            Magic(self.masmorra, x + 30, y + 30, vx * 150, vy * 150, (dd * 45 + 180) % 360)
        x, y = DIR[d]
        return x * 150, y * 150


class Magic:
    def __init__(self, masmorra, x, y, vx, vy, d):
        self.masmorra, self.x, self.y, self.d = masmorra, x, y, d
        self.v = vx * 1.5, vy * 1.5
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.sprite = None
        self._create = self.create

    def kill(self):
        if not self.sprite.inWorld:
            # print("kill")
            self.sprite.alive = False

    def create(self):
        sprite = self.game.add.sprite(self.x, self.y, FIRE)
        sprite.animations.add('fire', [10, 11, 12, 13, 14], 16, True)
        sprite.play('fire')
        sprite.scale.setTo(0.5, 0.5)
        self.game.physics.arcade.enable(sprite)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        self.masmorra.magic.add(sprite)
        self.sprite = sprite
        player = self.sprite
        player.body.velocity.x, player.body.velocity.y = self.v
        player.angle = self.d
        self._create = self.kill

    def preload(self):
        pass

    def update(self):
        self._create()


class Hero:
    def __init__(self, gamer):
        self.gamer = gamer.gamer
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.sprite = self.cursors = None

    def create(self):
        sprite = self.game.add.sprite(20, 148, MONSTER)
        sprite.animations.add('ani', [0, 1, 2, 3], 16, True)
        sprite.play('ani')
        self.game.physics.arcade.enable(sprite)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        self.sprite = sprite
        self.cursors = self.game.input.keyboard.createCursorKeys()

    def preload(self):
        pass

    def update(self):
        crs, player = self.cursors, self.sprite
        player.body.velocity.x, player.body.velocity.y = 0, 0
        player.animations.play('ani')
        moves = [(crs.left.isDown, 90, (-150, 0)), (crs.right.isDown, 270, (150, 0)),
                 (crs.up.isDown, 180, (0, -150)), (crs.down.isDown, 0, (0, 150))]

        stopped = True
        for move in moves:
            if move[0]:
                player.angle = move[1]
                player.body.velocity.x, player.body.velocity.y = move[2]
                stopped = False
        if stopped:
            player.animations.stop()


TOPO_ESQUERDA = "LS"
TOPO_DIREITA = "KO"
TOPO_CENTRO = "JN"
MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "IO", "FN", "IL"
FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA = "GS", "JS", "GL"

MASMORRA = [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
                                                         MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]]
ORDERED_KEYS = [['Coycol', 'Cauha', 'Tetlah'],
                ['Huatlya', 'Zitllo', 'Micpe'],
                ['Nenea', 'Cahuitz', 'Pallotl']]
PLAIN_KEYS = ['Coycol', 'Cauha', 'Tetlah'] + \
             ['Huatlya', 'Zitllo', 'Micpe'] + \
             ['Nenea', 'Cahuitz', 'Pallotl']
SHUFFLE_KEYS = PLAIN_KEYS[:]
shuffle(SHUFFLE_KEYS)
SHUFFLE_DIRS = list("NLSO")
ROTATE_DIRS = list("NLSO")
ROTATE_DIRS = ROTATE_DIRS[1:] + [ROTATE_DIRS[0]]
DIRS = list("NLSO")
shuffle(SHUFFLE_DIRS)
ODD = False


class DesafioA:
    ODD = False

    def __init__(self, masmorra=MASMORRA, off=0):
        self.masmorra = masmorra
        self.off = off
        self.odd = False
        self.gamer = Braser(768, 640)
        self.gamer.subscribe(self)
        self.game = self.gamer.game

    def preload(self):
        # self.game.load.image(DETAIL, DETAILURL)

        self.game.stage.backgroundColor = "#FFFFFF"
        self.game.load.spritesheet(MONSTER, MONSTERURL, 64, 63, 16 * 12)
        self.game.load.spritesheet(DETILE, DETAILURL, 128, 128, 12)

    def create(self):
        for i, line in enumerate(self.masmorra):
            for j, cell in enumerate(line):
                detail = self.game.add.sprite(self.off + 64 + j * 128, 64 + i * 128, DETILE)
                detail.anchor.setTo(0.5, 0.5)
                tile = cell  # MASMORRA[3*j+i]
                detail.frame = ord(tile[0]) - ord("A")
                detail.angle = 90 * DIREN.index(tile[1])

    def update(self):
        pass


def desafio3(mmap):
    marray = []
    for line in ORDERED_KEYS:
        mline = []
        for key in line:
            mline.append(mmap[key])
        marray.append(mline)
    desafio0(marray)


def _matriz(m):
    mo = []
    for l in (0, 3, 6):
        mo.append(m[l: l + 3])
    return mo


def desafio4(mmap):
    global ODD
    marray = []
    keys = _matriz(SHUFFLE_KEYS)
    for line in keys:
        mline = []
        for key in line:
            mline.append(mmap[key])
        marray.append(mline)
    desafio0(marray)
    ODD = not ODD
    if ODD:
        return
    shuffle(SHUFFLE_KEYS)


def desafio7(mmap):
    global ODD, ROTATE_DIRS
    marray = []
    keys = _matriz(SHUFFLE_KEYS)
    for line in keys:
        mline = []
        for key in line:
            code = mmap[key]
            mline.append(code[0] + ROTATE_DIRS[DIRS.index(code[1])])
        marray.append(mline)
    desafio0(marray)
    ROTATE_DIRS = ROTATE_DIRS[1:] + [ROTATE_DIRS[0]]
    ODD = not ODD
    if ODD:
        return
    shuffle(SHUFFLE_KEYS)
    shuffle(ROTATE_DIRS)


def desafio6(mmap):
    global ODD
    marray = []
    keys = _matriz(SHUFFLE_KEYS)
    for line in keys:
        mline = []
        for key in line:
            code = mmap[key]
            rotate = (SHUFFLE_KEYS.index(key) + SHUFFLE_DIRS.index(code[1])) % 4
            mline.append(code[0] + DIRS[rotate])
        marray.append(mline)
    desafio0(marray)
    ODD = not ODD
    if ODD:
        return
    shuffle(SHUFFLE_KEYS)
    shuffle(SHUFFLE_DIRS)


def desafio5(mmap):
    global ODD, ROTATE_DIRS
    marray = []
    keys = _matriz(SHUFFLE_KEYS)
    for line in keys:
        mline = []
        for key in line:
            code = mmap[key]
            # mline.append(code[0] + DIRS[SHUFFLE_DIRS.index(code[1])])
            mline.append(code[0] + ROTATE_DIRS[DIRS.index(code[1])])
        marray.append(mline)
    desafio0(marray)
    ODD = not ODD
    if ODD:
        return
    shuffle(SHUFFLE_KEYS)
    shuffle(SHUFFLE_DIRS)
    ROTATE_DIRS = ROTATE_DIRS[1:] + [ROTATE_DIRS[0]]


def desafio8(mmap):
    global ODD, ROTATE_DIRS
    marray = []
    keys = _matriz(SHUFFLE_KEYS)
    for line in keys:
        mline = []
        for key in line:
            code = mmap[key]
            # mline.append(code[0] + DIRS[SHUFFLE_DIRS.index(code[1])])
            mline.append(code[0] + ROTATE_DIRS[DIRS.index(code[1])])
        marray.append(mline)
    desafio0(marray)
    ODD = not ODD
    if ODD:
        return
    shuffle(SHUFFLE_KEYS)
    ROTATE_DIRS = ROTATE_DIRS[1:] + [ROTATE_DIRS[0]]


def main(_=None):
    from browser import document
    document["pydiv"].html = ""
    Masmorra()


DES = [main, desafio0, desafio0, desafio3, desafio4, desafio5, desafio6, desafio7]


def posiciona_monstro(m, x, y):
    masmorra = Masmorra.created()
    masmorra.posiciona_monstro(m, x, y)


def circus(desafio=1, param=MASMORRA):
    from browser import document
    document["pydiv"].html = ""

    DES[desafio](param)


print(__name__)
if __name__ == "__main__":
    circus(0)
