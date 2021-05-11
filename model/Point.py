class Point:
    nbr_point = 0

    def __init__(self):
        self._id = 0
        self._x = 0
        self._y = 0
        self._z = 0
        Point.nbr_point += 1

    def _get_id(self):
        return self._id
    
    def _get_x(self):
        return self._x

    def _get_y(self):
        return self._y

    def _get_z(self):
        return self._z

    def _set_id(self, id):
        self._id = id
        
    def _set_x(self, x):
        self._x = x
        
    def _set_y(self, y):
        self._y = y

    def _set_z(self, z):
        self._z = z
    
    def __str__(self):
        chaine = "point{}".format(self._id)
        return chaine
    
    id = property(_get_id, _set_id)
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    z = property(_get_z, _set_z)
