#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
solid - 3D primitives and transformations
"""

from solidcad import utils


class Solid(object):
    """Solid Base 3D Primitive"""

    def __init__(self):
        super(Solid, self).__init__()

    def _render(self):
        return NotImplementedError

    def __str__(self):
        return self._render() + ";"

    def __repr__(self):
        return repr(self.__str__)


class Cube(Solid):
    """Cube 3D Primitive.

    Cube(size=[x,y,z], center=True/False)
    Cube(size=x ,center=True/False)
    Cube()

    :size:
    single value, cube with all sides this length
    3 value array [x,y,z], cube with dimensions x, y and z.

    :center:
    False (default), 1st (positive) octant, one corner at (0,0,0)
    True, cube is centered at (0,0,0)


    **Default**
    >> print(Cube())
    Cube(size=[1,1,1], center=False)

    """

    def __init__(self, size=1, center=False):
        super(Cube, self).__init__()
        self._size = size  # size=[x,y,z]
        self._center = center

    @property
    def size(self):
        if not isinstance(self._size, (list, tuple)):
            return [self._size, self._size, self._size]
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, (list, tuple)):
            self._size = [size, size, size]
        self._size = list(size)

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        utils.check_bool_error(center)
        self._center = center

    def _render(self):
        return 'cube(size={:s}, center={:s})'.format(
            str(self.size),
            str(self.center).lower(),
        )

class Sphere(Solid):
    """Sphere 3D Primitive.

    sphere(d=diameter, fn=resolution, fa=degrees, fs=mm)
    Sphere()

    :d: Diameter. This is the diameter of the sphere.

    :$fa: Fragment angle in degrees   [Default=12]
    :$fs: Fragment size in mm         [Default=2]
    :$fn: Resolution                  [Default=0]


    **Default**
    >> print(Sphere())
    sphere($fn=0, $fa=12, $fs=2, d=2)

    """

    def __init__(self, d=2, fa=12, fn=0, fs=2):
        super(Sphere, self).__init__()
        self._d = d
        self._fa = fa
        self._fs = fs
        self._fn = fn

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, d):
        utils.check_number_error(d)
        self._d = d

    @property
    def fa(self):
        return self._fa

    @fa.setter
    def fa(self, fa):
        utils.check_number_error(fa)
        self._fa = fa

    @property
    def fn(self):
        return self._fn

    @fn.setter
    def fn(self, fn):
        utils.check_number_error(fn)
        self._fn = fn

    @property
    def fs(self):
        return self._fs

    @fs.setter
    def fs(self, fs):
        utils.check_number_error(fs)
        self._fs = fs

    def _render(self):
        return 'sphere($fn={:g}, $fa={:g}, $fs={:g}, d={:g})'.format(
            self.fn, self.fa, self.fs,
            self.d,
        )

# cylinder(h,r|d,center)
# cylinder(h,r1|d1,r2|d2,center)
# polyhedron(points, triangles, convexity)


def main():

    #  object();
    #  operator()   action();
    #  operator() { action();    action(); }
    #  operator()   operator() { action(); action(); }
    #  operator() { operator()   action();
    #               operator() { action(); action(); } }

    # cube(5);
    #    rotate(40) square(5,10);
    #    translate([10,5]) { circle(5); square(4); }
    #    color("blue") { translate([5,3,0]) sphere(5); rotate([45,0,45]) { cylinder(10); cube([5,6,7]); } }

    # Cube(5)
    # Square(5,10).rotate(40)
    # GroupSolids(Circle(5), Square(4)).translate([10,5])
    # GroupSolids(
    #     Sphere(5).translate([5,3,0]),
    #     GroupSolids(
    #         Cylinder(10),
    #         Cube([5,6,7]),
    #     ).rotate([45,0,45])
    # ).color("blue")

    print(Cube(100))
    print(Cube([10, 50, 30], True))
    cube = Cube([10, 50, 30], True)
    print(cube.size)


if __name__ == '__main__':
    main()
