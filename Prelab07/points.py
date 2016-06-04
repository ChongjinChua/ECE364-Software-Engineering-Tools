#! /usr/bin/env python3.4

#$Author: ee364g13 $
#$Date: 2016-02-28 12:40:34 -0500 (Sun, 28 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab07/points.py $
#$Revision: 88965 $
#$Id: points.py 88965 2016-02-28 17:40:34Z ee364g13 $

            
class PointND:

    def __init__(self, *args):
        for item in args:
            if type(item) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.n = len(args)
        self.t = args

    def __str__(self):
        rtn_str = ""
        for item in self.t:
            item = round(item,2)
            rtn_str += format(item,'.2f')
            rtn_str += ", "

        rtn_str = rtn_str.strip()
        rtn_str = rtn_str.strip(',')
        return "(" + rtn_str + ")"

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self,other):
        if other.n != self.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        else:
            dist = 0
            index = 0
            for item in self.t:
                dist += (item- other.t[index])**2
                index += 1
                index %= self.n + 1

            return dist**(1/2)

    def nearestPoint(self,points):
        if len(points) == 0:
            raise ValueError("Input cannot be empty")
        else:
            rtn_list = []
            closest = points[0]

            for obj in points:
                rtn_list.append(self.distanceFrom(obj))
            return points[rtn_list.index(min(rtn_list))]


    def furthestPoint(self,points):
        if len(points) == 0:
            raise ValueError("Input cannot be empty")
        else:
            rtn_list = []
            for obj in points:
                rtn_list.append(self.distanceFrom(obj))
            return points[rtn_list.index(max(rtn_list))]

    def clone(self):
        return PointND(*self.t)

    def __add__(self, other):
        if type(other) is PointND:
            if len(other.t) != len(self.t):
                raise ValueError("Cannot operate on points with different cardinalities.")
            else:
                index = 0
                new_t = []
                for item in other.t:
                    new_t.append(item+self.t[index])
                    index += 1
                return PointND(*tuple(new_t))

        elif type(other) is Point3D:
            if len(other.t) != len(self.t):
                raise ValueError("Cannot operate on points with different cardinalities.")
            else:
                index = 0
                new_t = []
                for item in other.t:
                    new_t.append(item+self.t[index])
                    index += 1
                return Point3D(*tuple(new_t))

        elif type(other) is float:
            new_t = []
            for item in self.t:
                new_t.append(item+other)
            #new_t = tuple(new_t)
            if type(self) is PointND:
                return PointND(*tuple(new_t))
            else:
                return Point3D(*tuple(new_t))

        else:
            print("error!")

    def __radd__(self,other):
        if type(other) is PointND:
            if len(other.t) != len(self.t):
                raise ValueError("Cannot operate on points with different cardinalities.")
            else:
                index = 0
                new_t = []
                for item in other.t:
                    new_t.append(item+self.t[index])
                    index += 1
                return PointND(new_t)
        else:
            new_t = []
            for item in self.t:
                new_t.append(item+other)
            #new_t = tuple(new_t)
            return PointND(*tuple(new_t))


    def __sub__(self, other):
        if type(other) is PointND or type(other) is Point3D:
            if len(other.t) != len(self.t):
                raise ValueError("Cannot operate on points with different cardinalities.")
            else:
                index = 0
                new_t = []
                for item in self.t:
                    new_t.append(item-other.t[index])
                    index += 1
                if type(other) is PointND:
                    return PointND(*tuple(new_t))
                else:
                    return Point3D(*tuple(new_t))
        else:
            new_t = []
            for item in self.t:
                new_t.append(item-other)
            return PointND(*tuple(new_t))

    def __rsub__(self,other):
        new_t = []
        for item in self.t:
            new_t.append(other-item)
        return PointND(*tuple(new_t))

    def __mul__(self,other):
        new_t = []
        for item in self.t:
            new_t.append(item*other)
        return PointND(*tuple(new_t))

    def __rmul__(self,other):
        new_t = []
        for item in self.t:
            new_t.append(item*other)
        return PointND(*tuple(new_t))        

    def __truediv__(self,other):
        new_t = []
        for item in self.t:
            new_t.append(item/other)
        return PointND(*tuple(new_t))

    def __rtruediv__(self,other):
        new_t = []
        for item in self.t:
            new_t.append(other/item)
        return PointND(*tuple(new_t))

    def __neg__(self):
        new_t = []
        for item in self.t:
            new_t.append(-item)
        return PointND(*tuple(new_t))

    def __getitem__(self,index):
        return self.t[index]

    def __eq__(self,other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        else:
            return self.t == other.t

    def __ne__(self,other):
        if len(self.t) != len(other.t):
            raise ValueError("Cannot compare points with different cardinalities.")
        else:
            return self.t != other.t

    def __gt__(self,other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        else:
            n_points = []
            for x in other.t:
                n_points.append(0.0)

            return self.distanceFrom(PointND(*tuple(n_points))) > other.distanceFrom(PointND(*tuple(n_points)))

    def __ge__(self,other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        else:
            n_points = []
            for x in other.t:
                n_points.append(0.0)
            return self.distanceFrom(PointND(*tuple(n_points))) >= other.distanceFrom(PointND(*tuple(n_points)))


    def __lt__(self,other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        else:
            n_points = []
            for x in other.t:
                n_points.append(0.0)
            return self.distanceFrom(PointND(*tuple(n_points))) < other.distanceFrom(PointND(*tuple(n_points)))


    def __le__(self,other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        else:
            n_points = []
            for x in other.t:
                n_points.append(0.0)
            return self.distanceFrom(PointND(*tuple(n_points))) <= other.distanceFrom(PointND(*tuple(n_points)))


class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x; self.y = y; self.z = z
        PointND.__init__(self,x,y,z)

class PointSet:
    def __init__(self,**kwargs):
        #print(kwargs.get('pointList','error'))
        if not kwargs:
            self.points = set()
            self.n = 0
        else:
            valid = kwargs.get('pointList','error')
            if valid != 'error':
                if not kwargs['pointList']:
                    raise ValueError("'pointList' input parameter cannot be empty.")
                else:
                    self.n = kwargs['pointList'][0].n
                    self.points = set()
                    #print(type(kwargs['pointList'][0]))
                    for point in kwargs['pointList']:
                        #print(point.n)
                        if point.n != self.n:
                            raise ValueError("Expecting a point with cardinality {0}".format(self.n))
                        else:
                            self.points.add(point)
            else:
                raise KeyError("'pointList' input parameter not found.")

    def addPoint(self,p):
        if not p:
            raise ValueError("input missing!")
        elif type(p) is PointND:
            #self.n = p.n
            if self.n != p.n:
                raise ValueError("Expecting a point with cardinality {0}".format(self.n))
            else:
                self.points.add(p)
        else:
            raise KeyError("'PointND' input parameter not found.")

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        pt_list = []
        min_list = []
        max_list = []
        elem = self.points.pop()
        self.points.add(elem)

        for point in elem:
            pt_list.append([])

        for point in self.points:
            index = 0
            for i in point:
                pt_list[index].append(i)
                index += 1

        for item in pt_list:
            min_list.append(min(item))
            max_list.append(max(item))

        return tuple([PointND(*tuple(min_list)),PointND(*tuple(max_list))])

    def computeNearestNeighbors(self, otherPointSet):
        closest = []
        for point in self.points:
            nearest = point.nearestPoint(list(otherPointSet.points))
            print(nearest)
            closest.append(tuple([point,nearest]))

        return closest

    def __add__(self,otherND):
        elem = self.points.pop()
        self.points.add(elem)

        if elem.n != otherND.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(elem.n))
        else:
            self.points.add(otherND)
            return self

    def __contains__(self,otherND):
        if otherND in self.points:
            return True
        else:
            return False

    def __sub__(self,otherND):
        elem = self.points.pop()
        self.points.add(elem)

        if elem.n != otherND.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(elem.n))
        elif self.__contains__(otherND):
            self.points.remove(otherND)
            return self
        else:
            return self

if __name__ == "__main__":
    var = PointND(3.423213, 25.4, -231213.0)
    var2 = PointND(3.423213, 25.4, -231213.0)
    #print(len(var2.t))
    #print(var.distanceFrom(var2))
    p01 = PointND(5.3767, -13.4989, 6.7150, 8.8840, -1.0224)
    p02 = PointND(18.3389, 30.3492, -12.0749, -11.4707, -2.4145)
    p03 = PointND(-22.5885, 7.2540, 7.1724, -10.6887, 3.1921)
    p04 = PointND(8.6217, -0.6305, 16.3024, -8.0950, 3.1286)
    p05 = PointND(3.1877, 7.1474, 4.8889, -29.4428, -8.6488)
    p06 = PointND(-13.0769, -2.0497, 10.3469, 14.3838, -0.3005)
    p07 = PointND(-4.3359, -1.2414, 7.2689, 3.2519, -1.6488)
    p08 = PointND(3.4262, 14.8970, -3.0344, -7.5493, 6.2771)
    p09 = PointND(35.7840, 14.0903, 2.9387, 13.7030, 10.9327)
    p10 = PointND(27.6944, 14.1719, -7.8728, -17.1152, 11.0927)
    pointList = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]
    ps = PointSet(pointList=pointList)

    pass
    
