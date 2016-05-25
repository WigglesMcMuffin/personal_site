var game = new Phaser.Game(800, 600, Phaser.AUTO, 'c', { preload: preload, create: create, update: update });

function preload() {

	game.load.image('sky', 'static/assets/sky.png');
    game.load.image('ground', 'static/assets/platform.png');
    game.load.image('star', 'static/assets/star.png');
	game.load.image('tank_base', 'static/assets/tank_base.png');
	game.load.image('tank_head', 'static/assets/tank_head.png');
    game.load.spritesheet('dude', 'static/assets/dude.png', 32, 48);
}

function create() {
	//  We're going to be using physics, so enable the Arcade Physics system
    game.physics.startSystem(Phaser.Physics.ARCADE);
	
    //  A simple background for our game
    game.add.sprite(0, 0, 'sky');
	
	player = game.add.group();
	
	player.create(25, 100, 'tank_base');
	player.create(25, 100, 'tank_head');
	
	walls = game.add.group();
	walls.enableBody = true;
	
	//var graphic = Phaser.Graphics(game, 0, 0);
	//graphic.beginFill(0x0fffff);
	
	//graphic.drawRect(new Phaser.Rectangle(100, 80, 40, game.world.height - 160));
	//graphic.drawRect(new Phaser.Rectangle(game.world.width - 140, 80, 40, game.world.height - 160));
	//graphic.drawRect(new Phaser.Rectangle(game.world.width / 2, game.world.height / 2, game.world.width / 4, 40));
	
	//graphic.endFill();
	
	//walls.add(graphic);
	
    //  The platforms group contains the ground and the 2 ledges we can jump on
    //platforms = game.add.group();

    //  We will enable physics for any object that is created in this group
    //platforms.enableBody = true;

    // Here we create the ground.
    //var ground = platforms.create(new Phaser.Rectangle(120, game.world.height - 64, 60, 200));

    //  Scale it to fit the width of the game (the original sprite is 400x32 in size)
    //ground.scale.setTo(2, 2);

    //  This stops it from falling away when you jump on it
    //ground.body.immovable = true;

    //  Now let's create two ledges
    //var ledge = platforms.create(400, 400, 'ground');

    //ledge.body.immovable = true;

    //ledge = platforms.create(-150, 250, 'ground');

    //ledge.body.immovable = true;
}

function update() {
}