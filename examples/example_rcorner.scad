$fn = 120;
color("red") {
  linear_extrude(1) {
    difference() {
      square([10, 10]);
      translate([5, 5]) {
        circle(r=5);
      }
      translate([5, 0]) {
        square([5, 5]);
      }
      translate([5, 5]) {
        square([5, 5]);
      }
      translate([0, 5]) {
        square([5, 5]);
      }
    }
  }
}
color("blue") {
  linear_extrude(1) {
    rotate(90, [0, 0, 1]) {
      difference() {
        square([10, 10]);
        translate([5, 5]) {
          circle(r=5);
        }
        translate([5, 0]) {
          square([5, 5]);
        }
        translate([5, 5]) {
          square([5, 5]);
        }
        translate([0, 5]) {
          square([5, 5]);
        }
      }
    }
  }
}
color("yellow") {
  linear_extrude(1) {
    rotate(180, [0, 0, 1]) {
      difference() {
        square([10, 10]);
        translate([5, 5]) {
          circle(r=5);
        }
        translate([5, 0]) {
          square([5, 5]);
        }
        translate([5, 5]) {
          square([5, 5]);
        }
        translate([0, 5]) {
          square([5, 5]);
        }
      }
    }
  }
}
color("green") {
  linear_extrude(1) {
    rotate(270, [0, 0, 1]) {
      difference() {
        square([10, 10]);
        translate([5, 5]) {
          circle(r=5);
        }
        translate([5, 0]) {
          square([5, 5]);
        }
        translate([5, 5]) {
          square([5, 5]);
        }
        translate([0, 5]) {
          square([5, 5]);
        }
      }
    }
  }
}
