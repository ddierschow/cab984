<?php // DONE
$subtitle = 'CY009B';
// CY-9-B KENWORTH T2000 CONTAINER TRUCK, issued 2000
$desc = "Matchbox Kenworth T2000 Box";
$year = '2000';
include "cypage.php";

function body() {
    global $subtitle;

// NOTE: Below models with chrome interior, 8-spoke wheels, & China casting.
    show_table([
// 1. Red cab with chrome base, clear windows, white container, roof & rear doors, white trailer chassis, "McDonald's" labels 
	['mod' => $subtitle, 'var' => '01a',
	    'cab' => 'MB432', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "McDonald's", 'cod' => '1', 'rar' => '2',
            'cdt' => 'red with black chassis, chrome base and interior, clear windows',
            'tdt' => "white container, chassis, roof and rear doors, MCDONALD'S labels",
	],
// 2. Silver-gray cab with gray base, yellow windows, brown container, roof and rear doors, brown trailer chassis, "Hershey's King Size" labels 
	['mod' => $subtitle, 'var' => '02a',
	    'cab' => 'MB432', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "Hershey", 'cod' => '1', 'rar' => '2',
            'cdt' => 'silver-gray with gray base, yellow windows',
            'tdt' => "brown container, roof and rear doors, brown chassis, HERSHEY'S KING SIZE labels",
	],
// 3. Red cab with black base, clear windows, black container and rear doors with red roof, black trailer chassis, "McDonald's" labels (ROW)
	['mod' => $subtitle, 'var' => '03a',
	    'cab' => 'MB432', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "McDonald's", 'cod' => '1', 'rar' => '2',
            'cdt' => 'red with black base, clear windows',
            'tdt' => "black container and rear doors with red roof, black chassis, MCDONALD'S labels",
	],
// 4. Red cab with chrome base, clear windows, red container and rear doors with red roof, black trailer chassis, "The Pause that Refreshes-Coca Cola" tempa, chrome disc with rubber tires (PC)
	['mod' => $subtitle, 'var' => '04a',
	    'cab' => 'MB318', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "Coca-Cola", 'cod' => '1', 'rar' => '2',
            'cdt' => 'red cab with chrome base, clear windows',
            'tdt' => 'red container and rear doors with red roof, black chassis, THE PAUSE THAT REFRESHES-COCA COLA" tampo',
	],
	['mod' => $subtitle, 'var' => '05a',
	    'cab' => 'MB318', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "Coca-Cola", 'cod' => '1', 'rar' => '2',
            'cdt' => 'green with black lower, black chassis, silver base and exhaust with black interior, clear windows, COCA COLA CALENDAR GIRLS tampo',
            'tdt' => 'black base, green box and doors, dark blue roof, MARCH AND APRIL 1947 calendar labels, nail head hitch pin',
	],
	['mod' => $subtitle, 'var' => '06a',
	    'cab' => 'MB318', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "Coca-Cola", 'cod' => '1', 'rar' => '2',
            'cdt' => 'Red with white lower, white chassis, silver base and exhaust with white interior, clear windows. COCA COLA CALENDAR GIRLS tampo',
            'tdt' => 'white base and roof, red box and doors, "MAY and JUNE 1947 calendar lables, nail head hitch pin',
	],
    ]);
}
?>
