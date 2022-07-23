
self.acceleration.x += self.velocity.x * -.10
self.velocity.x += self.acceleration.x * dt
print(self.velocity.x)
self.delpos.x = self.velocity.x *dt + ((self.acceleration.x *0.5) * (dt * dt))
self.px = self.rect.x + self.delpos.x
self.rect.x  = round(self.px)

