from Vect3D import Vect3D
import numpy as np

class HyperPanel:

    def __init__(self, v0, v1, v2, v3):
        self.a0 = Vect3D()
        self.a1 = Vect3D()
        self.a2 = Vect3D()
        self.a3 = Vect3D()

        self.a0.x = 0.25 * (v0.x + v1.x + v3.x + v2.x)
        self.a1.x = 0.25 * (-v0.x + v1.x - v3.x + v2.x)
        self.a2.x = 0.25 * (-v0.x - v1.x + v3.x + v2.x)
        self.a3.x = 0.25 * (v0.x - v1.x - v3.x + v2.x)

        self.a0.y = 0.25 * (v0.y + v1.y + v3.y + v2.y)
        self.a1.y = 0.25 * (-v0.y + v1.y - v3.y + v2.y)
        self.a2.y = 0.25 * (-v0.y - v1.y + v3.y + v2.y)
        self.a3.y = 0.25 * (v0.y - v1.y - v3.y + v2.y)

        self.a0.z = 0.25 * (v0.z + v1.z + v3.z + v2.z)
        self.a1.z = 0.25 * (-v0.z + v1.z - v3.z + v2.z)
        self.a2.z = 0.25 * (-v0.z - v1.z + v3.z + v2.z)
        self.a3.z = 0.25 * (v0.z - v1.z - v3.z + v2.z)

    def get_panel_point_uv(self, u, v):
        point = Vect3D()

        point.x = self.a0.x + self.a1.x * u + self.a2.x * v + self.a3.x * u * v
        point.y = self.a0.y + self.a1.y * u + self.a2.y * v + self.a3.y * u * v
        point.z = self.a0.z + self.a1.z * u + self.a2.z * v + self.a3.z * u * v

        return point

    def get_panel_point(self, x, y):
        point = Vect3D()

        return point

    # u, v point position: u=v=0 for middle of panel
    def get_panel_normal(self, u, v):
        dp1 = Vect3D()
        dp2 = Vect3D()

        dp1.x = self.a1.x + self.a3.x * v
        dp1.y = self.a1.y + self.a3.y * v
        dp1.z = self.a1.z + self.a3.z * v

        dp2.x = self.a2.x + self.a3.x * u
        dp2.y = self.a2.y + self.a3.y * u
        dp2.z = self.a2.z + self.a3.z * u

        res = dp1.cross(dp2)
        res = res.normalize()

        return res


