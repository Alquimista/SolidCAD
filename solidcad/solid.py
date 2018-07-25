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

        self._str_render = None

    # self.root=False            # root=!
    # self.disable=False         # disable=*
    # self.background=False      # backgroun=%
    # self.debug=False           # debug=#

    def rotate(self):
        return "rotate(45)"

    def _render(self):
        return NotImplementedError

    # def __sub__(self, other):
    #     """Diference of solids"""
    #     return NotImplementedError

    # def __add__(self, other):
    #     """Union of solids"""
    #     return NotImplementedError

    # def __mul__(self, other):
    #     """Intersection of solids"""
    #     return NotImplementedError

    def __str__(self):
        self._render()
        return self._str_render

    def __repr__(self):
        return repr(self.__str__)


class Group(Solid):
    """Group solids."""

    def __init__(self, *args):
        super(Group, self).__init__()
        self._solids = args
        self._str_render = None

    def __grouped(self):
        if all(isinstance(s, Solid) for s in self._solids):
            self._str_render = "{ " + " ".join(self._solids) + " }"
        else:
            raise AssertionError("Group, accepts Solids only.")


class Union(Group):
    """Union creates a union of all its child nodes."""

    def __init__(self, arg):
        super(Union, self).__init__()
        self.arg = arg


class Diference(Group):
    """
    Diference subtracts the 2nd (and all further)
    child nodes from the first one.
    """

    def __init__(self, arg):
        super(Diference, self).__init__()
        self.arg = arg


class Intersection(Group):
    """
    Diference creates the intersection of all child nodes.
    This keeps the overlapping portion
    """

    def __init__(self, arg):
        super(Intersection, self).__init__()
        self.arg = arg


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
    >>> print(Cube())
    cube(size=[1,1,1], center=false);

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
        self._str_render = 'cube(size={size:s}, center={center:s});'.format(
            size=str(self.size).replace(" ", ""),
            center=str(self.center).lower(),
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
    >>> print(Sphere())
    sphere($fn=0, $fa=12, $fs=2, d=2);
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
        self._str_render = (
            "sphere($fn={self.fn:g}, $fa={self.fa:g}, "
            "$fs={self.fs:g}, d={self.d:g});").format(self=self)

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
    # Group(Circle(5), Square(4)).translate([10,5])
    # Group(
    #     Sphere(5).translate([5,3,0]),
    #     Group(
    #         Cylinder(10),
    #         Cube([5,6,7]),
    #     ).rotate([45,0,45])
    # ).color("blue")
    # Union()
    # Diference()
    # Intersection()
    import doctest
    doctest.testmod()


if __name__ == '__main__':

    main()
