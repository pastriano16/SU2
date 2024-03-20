lc = 2e-2;
uc = 1e-1;

Point(1) = {0, 0, 0, lc};
Point(2) = {6, 0,  0, uc};
Point(3) = {6, 2.5, 0, uc};
Point(4) = {0,  2.5, 0, uc};
Point(5) = {0, 0.25, 0, lc};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 1};

Curve Loop(6) = {4, 5, 1, 2, 3};

Plane Surface(7) = {6};

Physical Curve("inlet",8) = {5};
Physical Curve("freestream",9) = {2, 3};
Physical Curve("symmetry",10) = {1};
Physical Curve("wall",12) = {4};

Physical Surface("fluid",13) = {7};
