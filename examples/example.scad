union() {
  difference() {
    cube(size=30, center=true);
    sphere(r=20);
  }
  translate(v=[0, 0, 30]) {
    cylinder(h=40, r=10);
  }
}
