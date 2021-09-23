$fn=36;
union() {
  difference() {
    cube(size=30, center=true);
    sphere(r=20.1);
  }
  translate([0, 0, 30]) {
    cylinder(40, r=10);
  }
}
