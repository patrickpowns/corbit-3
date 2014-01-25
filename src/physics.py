from entity import Entity
from sys import stderr
import scipy
import scipy.linalg as LA
from unum.units import m,s
from math import sqrt

def resolve_collision(A, B, time):
    # general overview of this function:
    # 1. find if the objects will collide in the given time
    # 2. if yes, calculate collision:
    # 2.1 represent velocities as normal velocity and tangential velocity
    # 2.2 do a 1D collision using the normal veloctiy
    # 2.3 add the normal and tangential velocities to get the new velocity

    scipy.seterr(divide="raise", invalid="raise")
    
    # for this function I make one of the objects the frame of reference
    # which means my calculations are much simplified
    
    # this code finds when the the two entities will collide. See
    # http://www.gvu.gatech.edu/people/official/jarek/graphics/material/collisionsDeshpandeKharsikarPrabhu.pdf
    # for how I got the algorithm
    
    a = (A.velocity * B.velocity)**2
    
    
    # at this point, we know there is a collision
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    print("Collision:", A.name, "and", B.name)
    t_to_impact = t_neg

    # move until the point of impact
    A.move(t_to_impact);
    B.move(t_to_impact);

    # for this section, basically turn the vectors into normal velocity and tangential velocity,
    # then do a 1D collision calculation, using the normal velocities
    # since a ' (prime symbol) wouldn't work, I've replaced it with a _ in variable names

    n = A.displacement - B.displacement   # normal vector
    un = n / (m*LA.norm(n.asNumber(m))) # normal unit vector
    unt = un;           # normal tangent vector
    unt[0], unt[1] = \
    -unt[1], unt[0]

    # A's centripetal velocity
    vAn = m/s * scipy.dot(un.asNumber(), A.velocity.asNumber(m/s))
    # A's tangential velocity
    vAt = m/s * scipy.dot(unt.asNumber(), A.velocity.asNumber(m/s))

    # B's centripetal velocity
    vBn = m/s * scipy.dot(un.asNumber(), B.velocity.asNumber(m/s))
    # B's tangential velocity
    vBt = m/s * scipy.dot(unt.asNumber(), B.velocity.asNumber(m/s))

    # tangent velocities are unchanged, nothing happens to them
    vAt_ = vAt
    vBt_ = vBt

    # centripetal velocities are calculated with a simple 1D collision formula
    vAn_ = \
     (vAn * (A.mass() - B.mass()) + 2*B.mass() * vBn) / (A.mass() + B.mass())

    vBn_ = \
     (vBn * (B.mass() - A.mass()) + 2*A.mass() * vAn) / (B.mass() + A.mass())

    # convert scalar normal and tangent velocities to vector quantities
    VAn = vAn_ * un
    VAt = vAt_ * unt

    VBn = vBn_ * un
    VBt = vBt_ * unt

    # add em up to get v'
    A.velocity = VAn + VAt
    B.velocity = VBn + VBt

    # move for the rest of the frame
    A.move(time - t_to_impact);
    B.move(time - t_to_impact);
