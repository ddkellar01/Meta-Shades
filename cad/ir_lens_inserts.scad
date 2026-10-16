// Meta Shades - IR Transmissive Optical Lens Inserts
$fn = 100;

module ir_lens_insert() {
    difference() {
        // Outer lens perimeter matching frame socket
        cylinder(h=2.5, r=20.5, center=true);
        
        // Inner optical distortion clearance
        cylinder(h=3.0, r=19.0, center=true);
    }
}

ir_lens_insert();
