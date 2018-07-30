#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
solid - 3D primitives and transformations
"""

from solidcad import utils


#TODO: REFACTOR CHECK VALUES
class Solid(object):
    """Solid Base 3D Primitive"""

    def __init__(self):
        super(Solid, self).__init__()

        self._str_render = None

        # self.root=False            # root=!
        # self.disable=False         # disable=*
        # self.background=False      # backgroun=%
        # self.debug=False           # debug=#

    def _transform(self, t):
        self._str_render = t + " " + self._str_render 
        


    def rotate(self, a):
        """
        rotate. Rotates its child 'a' degrees about the axis
        of the coordinate system

        Rotate with a single scalar argument rotates around the Z axis.
        This is useful in 2D contexts where that is the only axis for rotation. 

        .rotate(a=[x,y,z])
        .rotate(a=z)

        :a:                                         
        Angle in degrees
        """
        #TODO: unittest
        if not isinstance(a, (list, tuple)):
            angle = a % 360
        else:
            if not all(isinstance(_, (int, float)) for _ in a) and (len(a) != 3):
                raise AssertionError('vector v is have a not numeric value')
            angle=a
        rotate_str = "rotate(a={:s})".format(str(angle).replace(" ", ""))
        return self._transform(rotate_str)

    def translate(self, v):
        """
        translate. Translates (moves) its child elements along the
        specified vector. 

        .translate(v=[x,y,z])

        :v:                                         
        Position vector
        """
        #TODO: unittest
        if not all(isinstance(_, (int, float)) for _ in v) and (len(v) != 3):
            raise AssertionError('vector v is have a not numeric value')
        move_str = "translate(v={:s})".format(str(v))
        return self._transform(move_str)

    def scale(self, v):
        """
        scale. Scales its child elements using the specified vector.

        .scale(v=[x,y,z])

        :v:                                         
        Scale vector
        """
        #TODO: unittest
        if not all(isinstance(_, (int, float)) for _ in v) and (len(v) != 3):
            raise AssertionError('vector v is have a not numeric value')
        scale_str = "scale(v={:s})".format(str(v))
        return self._transform(scale_str)

    def mirror(self, v):
        """
        mirror. Mirrors the child element on a plane through the origin.

        .mirror(v=[x,y,z])

        :v:                                         
        Mirror vector
        """
        #TODO: unittest
        if not all(isinstance(_, (int, float)) for _ in v) and (len(v) != 3):
            raise AssertionError('vector v is have a not numeric value')
        mirror_str = "mirror(v={:s})".format(str(v))
        return self._transform(mirror_str)

    def resize(self, v, auto=false):
        """
        resize. Modifies the size of the child object to match the given
        x,y, and z.

        .resize(v=[x,y,z])

        :v:                                         
        Resize vector

        :auto:
        Boolean or boolean vector
        """
        #TODO: unittest
        if isinstance(a, (list, tuple)):
            if not all(isinstance(_, bool) for _ in auto) and (len(auto) != 3):
                raise AssertionError('vector v is have a not numeric value')
        if not all(isinstance(_, (int, float)) for _ in v) and (len(v) != 3):
            raise AssertionError('vector v is have a not numeric value')
        resize_srt = "resize(v={:s}, auto={:s})".format(
            str(v), str(auto).replace(" ", ""))
        return self._transform(resize_srt)

    def __str__(self):
        return self._str_render

    def __repr__(self):
        return repr(self._str_render)


class Group(Solid):
    """Group solids."""

    def __init__(self, *args):
        super(Group, self).__init__()
        self._solids = args
        self._str_render = None

        self._grouped()

    def _grouped(self):
        if all(isinstance(s, Solid) for s in self._solids):
            solids = list(map(str, self._solids))
            self._str_render = "{\n    " + "\n    ".join(solids) + "\n}"
        else:
            raise AssertionError("Group, accepts Solids only.")


class Union(Group):
    """Union creates a union of all its child nodes."""

    def __init__(self, *args):
        super(Union, self).__init__()
        self._solids = args

        self._union()

    def _union(self):
        self._grouped()
        self._str_render = "union() {:s}".format(self._str_render)
        return self


class Diference(Group):
    """
    Diference subtracts the 2nd (and all further)
    child nodes from the first one.
    """

    def __init__(self, *args):
        super(Diference, self).__init__()
        self._solids = args

        self._diference()

    def _diference(self):
        self._grouped()
        self._str_render = "diference() {:s}".format(self._str_render)
        return self


class Intersection(Group):
    """
    Diference creates the intersection of all child nodes.
    This keeps the overlapping portion
    """

    def __init__(self, *args):
        super(Intersection, self).__init__()
        self._solids = args

        self._intersection()

    def _intersection(self):
        self._grouped()
        self._str_render = "intersection() {:s}".format(self._str_render)
        return self


class Cube(Solid):
    """Cube 3D Primitive.

    Cube(size=[x,y,z], center=True/False)
    Cube(size=x ,center=True/False)
    Cube()

    :size:                                         [Defautl=[0,0,0]]
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

        self._str_render = self._render()

    @property
    def size(self):
        if not isinstance(self._size, (list, tuple)):
            return [self._size, self._size, self._size]
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, (list, tuple)):
            self._size = [size, size, size]
        else:
            self._size = list(size)
        self._str_render = self._render()

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        utils.check_bool_error(center)
        self._center = center
        self._str_render = self._render()

    def _render(self):
        return 'cube(size={size:s}, center={center:s});'.format(
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
        # TODO: CHECK IF IS ARE VALID VALUE FS, FS, FN
        self._fa = fa
        self._fs = fs
        self._fn = fn

        self._str_render = self._render()

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
        return (
            "sphere($fn={self.fn:g}, $fa={self.fa:g}, "
            "$fs={self.fs:g}, d={self.d:g});").format(self=self)


#TODO: TEST
class Cylinder(Solid):
    """Sphere 3D Primitive.

    cylinder(h,d1,d2,center,fn, fa, fs)
    cylinder()

    :h: height of the cylinder or cone      [Default=1]
    :d1: diameter, bottom of cone           [Default=2]
    :d2: diameter, top of cone              [Default=2]

    :center:
        false (default), z ranges from 0 to h
        true, z ranges from -h/2 to +h/2
    $fa : minimum angle (in degrees) of each fragment.         [Default=12]
    $fs : minimum circumferential length of each fragment.     [Default=2]
    $fn : fixed number of fragments in 360 degrees.            [Default=0]


    **Default**
    >>> print(Cylinder())
    cylinder($fn=0, $fa=12, $fs=2, h=1, d1=2, d2=2, center=false);
    """

    def __init__(self, h=1, d1=2, d2=2, center=False, fa=12, fn=0, fs=2):
        super(Cylinder, self).__init__()
        self._h = h
        self._d1 = d1
        self._d2 = d2
        self._center = center
        # TODO: CHECK IF IS ARE VALID VALUE FS, FS, FN
        self._fa = fa
        self._fs = fs
        self._fn = fn

        self._str_render = self._render()

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        utils.check_number_error(h)
        self._h = h

    @property
    def d1(self):
        return self._d1

    @d1.setter
    def d1(self, d1):
        utils.check_number_error(d1)
        self._d = d1

    @property
    def d2(self):
        return self._d2

    @d2.setter
    def d2(self, d2):
        utils.check_number_error(d2)
        self._d2 = d2

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        utils.check_bool_error(center)
        self._center = center
        self._str_render = self._render()

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
        return (
            "cylinder($fn={self.fn:g}, $fa={self.fa:g}, "
            "$fs={self.fs:g}, h={self.h:g}, d1={self.d1:g},d1={self.d2:g}"
            "center={center:s});").format(self=self,
                                          center=str(self.center).lower())

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
