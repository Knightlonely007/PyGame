#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = ENTITY_SPEED.get(self.name, 2)  # velocidade inicial
        self.moving_up = True  # Começa movendo para cima

    def move(self):
        # Movimento horizontal (sempre da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical com comportamento específico para o Enemy3
        if self.name == 'Enemy3':
            if self.moving_up:
                self.rect.centery -= self.vertical_speed
                if self.rect.top <= 0:  # Se bater na borda superior
                    self.moving_up = False
                    self.vertical_speed *= 2  # Dobra a velocidade ao descer
            else:
                self.rect.centery += self.vertical_speed
                if self.rect.bottom >= WIN_HEIGHT:  # Se bater na borda inferior
                    self.moving_up = True
                    self.vertical_speed = ENTITY_SPEED[self.name]  # Volta à velocidade inicial ao subir

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
