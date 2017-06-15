<?php // DONE
$subtitle = 'CY004B';
// CY-4-B SCANIA BOX TRUCK, issued 1985 (AU)
$desc = "Scania Box Truck";
$year = '1985';

$defaults = ['mod' => $subtitle, 'cab' => 'MB147', 'tlr' => 'Box', 'mfg' => 'England',
	    'liv' => 'Ansett', 'cod' => '1',
];

include "cypage.php";

function body() {
    show_table([
// 1. White cab, white container, black trailer, "Ansett" (towards front) labels (S12-15)(AU)
	['var' => '01a',
	    'rar' => '2', 'cdt' => 'white',
            'tdt' => 'black, white container, ANSETT labels (name towards front)',
	],
// 2. White cab, white container, black trailer, "Ansett" (towards rear) labels (S12-15)(AU)
	['var' => '02a', 'rar' => '4',
            'cdt' => 'white',
            'tdt' => 'black, white container, ANSETT labels (name towards rear)',
	],
    ]);
}
?>
