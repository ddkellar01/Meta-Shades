// Meta Shades - Parametric Glass Frame Shell
$fn = 100;

module glasses_frame() {
    difference() {
        // Main Front Outer Housing
        cube([145, 18, 48], center=true);
        
        // Left Lens Optical Cutout
        translate([-35, 0, 0])
            cylinder(h=50, r=21, center=true);
            
        // Right Lens Optical Cutout
        translate([35, 0, 0])
            cylinder(h=50, r=21, center=true);
            
        // Temple EEG Electrode Wire Channel
        translate([65, 0, 10])
            cube([20, 10, 5], center=true);
    }
}

glasses_frame();
