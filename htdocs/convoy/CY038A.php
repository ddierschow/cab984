<?php // DONE
$subtitle = 'CY038A';
// CY-38-A KENWORTH CONTAINER TRUCK, issued 1993
$desc = "Kenworth Container Truck";
$year = '1993';

$defaults = ['mod' => $subtitle];

include "cypage.php";

function body() {
    show_table([
// 1. MB45-C cab in black, black container, "Matchbox Racing 5" labels 
	['var' => '01a', 'cab' => 'MB045', 'tlr' => 'Container', 'mfg' => 'Macau',
	    'liv' => 'Matchbox', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => 'black container, MATCHBOX RACING 5 labels',
	],
    ]);
}
?>