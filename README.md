# Game_Engine2D 

This Project is my try to develop a Game/GameEngine from Scratch.
I want to understand how all the parts of a Gameengine work together like
animation handling and A.I.

The Game (when finished) will be a simple ARPG.
If you want to build your own game with this code just go on and do it. Its 100% opensource.

I will add a small description for all the *.py files here later.

AnimationDataClass:
  this file is just one class which defines animations as a data class. . 
  
AnimationHandler:
  This is a class which will return an image based on a given animation.
  
BrainstateMachine:
  Is like a casual StateMachine but without a render function.
  
Camera:
  The Camera is used to display the positions of everything correctly so that only
  the necessary things will be rendered and updated.
  
Character:
  This is the parent for all Characters / NPCs / Enemys and so on.
  
InputHandler:
  Will save the Input of the Player in a seperate List so that it can be passed more then once
  per Tick.
  
Level1.py
  First Level of the Game. Will be reworked later on.

MapRender.py
  This is the class for the Map rendering. Levels are given and the Maprenderer will display the Map as we want it.
  Will be able to render up to 5 layers of map.

Playerclass.py
  A kid of the Character.py. Here we define our Player for the Game.
  
ScreenState.py
  The first State for our StateMachine. This is the State in which we will play/see the map and player.
  
StateMachine.py
  A simple StateMachine Class to change between States. Will then update and render them.
  
main.py
  This is were the gameloop is located and the first things are initalized.
