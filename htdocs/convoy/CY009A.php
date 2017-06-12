<?php // DONE
$subtitle = 'CY009A';
// CY-9-A KENWORTH BOX TRUCK, issued 1982
// NOTE: All models with amber windows, 8-spoke wheels, no antennas, and chrome exhausts unless otherwise noted.
$desc = "Kenworth Conventional Box Trailer";
$year = '1982';
include "cypage.php";

function body() {
    global $subtitle;

    show_table([
// 1. MB103 cab in black, black container, "Midnight X-Press" labels, England
	['mod' => $subtitle, 'var' => '01a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'England',
	    'liv' => 'Midnight X-Press', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container, MIDNIGHT X-PRESS labels",
        ],
// 2. MB103 cab in black, clear windows, black container, "Midnight X-Press" labels, England
	['mod' => $subtitle, 'var' => '02a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'England',
	    'liv' => 'Midnight X-Press', 'cod' => '1', 'rar' => '',
            'cdt' => 'black, clear windows',
            'tdt' => "black container, MIDNIGHT X-PRESS labels",
        ],
// 3. MB045 cab in black, amber windows, black container, "Midnight X-Press" tampo, England
	['mod' => $subtitle, 'var' => '03a',
	    'cab' => 'MB045', 'tlr' => 'Box', 'mfg' => 'England',
	    'liv' => 'Midnight X-Press', 'cod' => '1', 'rar' => '',
            'cdt' => 'black, amber windows',
            'tdt' => "black container, MIDNIGHT X-PRESS tampo",
        ],
// 4. MB103 cab in black, black container, "Midnight X-Press" tampo, Macau
	['mod' => $subtitle, 'var' => '04a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Midnight X-Press', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container, MIDNIGHT X-PRESS tampo",
        ],
// 5. MB103 cab in black, black container, "Moving In New Directions" tampo, Macau (AU)
	['mod' => $subtitle, 'var' => '05a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => '', 'cod' => '1', 'rar' => '4',
            'cdt' => 'black',
            'tdt' => "black container, MOVING IN NEW DIRECTIONS tampo",
        ],
// 6. MB103 cab in black, black container, "Moving In New Directions" tampo with "Personal Contact Is Barry Oxford" roof label, Macau (AU)
	['mod' => $subtitle, 'var' => '06a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => '', 'cod' => '1', 'rar' => '5',
            'cdt' => 'black',
            'tdt' => "black container, MOVING IN NEW DIRECTIONS tampo with PERSONAL CONTACT IS BARRY OXFORD roof label",
        ],
// 7. MB103 cab in black, black container, "Moving In New Directions" tampo with "Personal Contact Is Anita Jones" roof label, Macau (AU)
	['mod' => $subtitle, 'var' => '07a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => '', 'cod' => '1', 'rar' => '5',
            'cdt' => 'black',
            'tdt' => "black container, MOVING IN NEW DIRECTIONS tampo with PERSONAL CONTACT IS ANITA JONES roof label",
        ],
// 8. MB103 cab in black, black container, "Moving In New Directions" tampo with "Personal Contact Is Keith Mottram" roof label, Macau (AU)
	['mod' => $subtitle, 'var' => '08a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => '', 'cod' => '1', 'rar' => '5',
            'cdt' => 'black',
            'tdt' => "black container, MOVING IN NEW DIRECTIONS tampo with PERSONAL CONTACT IS KEITH MOTTRAM roof label",
        ],
// 9. MB103 cab in black, black container, "Moving In New Directions" tampo with "Personal Contact Is Terry Blyton" roof label (AU)
	['mod' => $subtitle, 'var' => '09a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => '', 'cod' => '1', 'rar' => '5',
            'cdt' => 'black',
            'tdt' => "black container, MOVING IN NEW DIRECTIONS tampo with PERSONAL CONTACT IS TERRY BLYTON roof label",
        ],
// 10. MB103 cab in black, black container, "Moving In New Directions" tampo with "Personal Contact Is Jenny Brindley" roof label (AU)
	['mod' => $subtitle, 'var' => '10a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => '', 'cod' => '1', 'rar' => '5',
            'cdt' => 'black',
            'tdt' => "black container, MOVING IN NEW DIRECTIONS tampo with PERSONAL CONTACT IS JENNY BRINDLEY roof label",
        ],
// 11. MB103 cab in black, yellow container, "Stanley" tampo, Macau (US)(OP)
	['mod' => $subtitle, 'var' => '11a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Stanley', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "yellow container, STANLEY tampo",
        ],
// 12. DAF cab in yellow, yellow container, "IPEC" tampo, Macau (AU)
	['mod' => $subtitle, 'var' => '12a',
	    'cab' => 'MB183', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'IPEC', 'cod' => '1', 'rar' => '',
            'cdt' => 'yellow',
            'tdt' => "yellow container, IPEC tampo",
        ],
// 13. MB103 cab in white, white container, "Paul Arpin Van Lines" tampo, Macau (US)
	['mod' => $subtitle, 'var' => '13a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Paul Arpin', 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, PAUL ARPIN VAN LINES tampo",
        ],
// 14. MB103 cab in white, white container, "Matchbox/ Compliments Macau Diecast Co. Ltd.," Macau
	['mod' => $subtitle, 'var' => '14a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Matchbox', 'cod' => '1', 'rar' => '5',
            'cdt' => 'white',
            'tdt' => "white container, MATCHBOX/ COMPLIMENTS MACAU DIECAST CO. LTD., Macau",
        ],
// 15. MB103 cab in white, white container, "Matchbox-ln Celebration of Universal Group's 20th Anniversary" tampo, Macau
	['mod' => $subtitle, 'var' => '15a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Matchbox', 'cod' => '1', 'rar' => '5',
            'cdt' => 'white',
            'tdt' => "white container, MATCHBOX-LN CELEBRATION OF UNIVERSAL GROUP'S 20TH ANNIVERSARY tampo",
        ],
// 16. MB103 cab in white, white container, "Canadian Tire" tampo, Macau (CN)
	['mod' => $subtitle, 'var' => '16a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Canadian Tire', 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, CANADIAN TIRE tampo",
        ],
// 17. MB103 cab in white, white container, "Merry Christmas 1988 MICA Members" with calendar roof label (C2)
	['mod' => $subtitle, 'var' => '17a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'MICA', 'cod' => '2', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, MERRY CHRISTMAS 1988 MICA MEMBERS with calendar roof label",
        ],
// 18. MB103 cab in blue, blue container, "Mitre 10" tampo, Macau (AU)
	['mod' => $subtitle, 'var' => '18a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Mitre 10', 'cod' => '1', 'rar' => '',
            'cdt' => 'blue',
            'tdt' => "blue container, MITRE 10 tampo",
        ],
// 19. MB103 cab in blue, white container, "Spaulding" tampo, Macau (US)
	['mod' => $subtitle, 'var' => '19a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'Spaulding', 'cod' => '1', 'rar' => '',
            'cdt' => 'blue',
            'tdt' => "white container, SPAULDING tampo",
        ],
// 20. MB103 cab in white, white container, "Merry Christmas MICA Members 1990" labels with calendar roof label (C2)
	['mod' => $subtitle, 'var' => '20a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Macau',
	    'liv' => 'MICA', 'cod' => '2', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, MERRY CHRISTMAS MICA MEMBERS 1990 labels with calendar roof label",
        ],
// 21. MB103 cab in black, black container, "Midnight X-Press" tampo, Thailand
	['mod' => $subtitle, 'var' => '21a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Midnight X-Press', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container, MIDNIGHT X-PRESS tampo, Thailand",
        ],
// 22. MB103 cab in black, black container, "Cool Paint Co." labels, Thailand
	['mod' => $subtitle, 'var' => '22a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Cool Paint', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container, COOL PAINT CO. labels, Thailand",
        ],
// 23. MB103 cab in black, black container, Thailand, "Cool Paint Co." labels applied over "Midnight X-Press"
	['mod' => $subtitle, 'var' => '23a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Cool Paint', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container, Thailand, COOL PAINT CO. labels applied over MIDNIGHT X-PRESS",
        ],
// 24. MB103 cab in white, white container, Thailand, "Truckin' USA" labels
	['mod' => $subtitle, 'var' => '24a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => "Truckin' USA", 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, Thailand, TRUCKIN' USA labels",
        ],
// 25. MB103 cab in white, white container, Thailand, "Hershey's" labels
	['mod' => $subtitle, 'var' => '25a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => "Hershey's", 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, Thailand, HERSHEY'S labels",
        ],
// 26. MB103 cab in white, white container, Thailand, "Paul Arpin Van Lines" with "NFL" logo
	['mod' => $subtitle, 'var' => '26a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Paul Arpin', 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container, Thailand, PAUL ARPIN VAN LINES with NFL logo",
        ],
// 27. MB103 cab in white, white container and base, Thailand, "Hershey's" (with small candy bar) labels
	['mod' => $subtitle, 'var' => '27a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => "Hershey's", 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "white container and base, Thailand, HERSHEY'S (with small candy bar) labels",
        ],
// 28. MB103 cab in orange, orange container and base, Thailand, "Reese's" labels
	['mod' => $subtitle, 'var' => '28a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => "Reese's", 'cod' => '1', 'rar' => '',
            'cdt' => 'orange',
            'tdt' => "orange container and base, Thailand, REESE'S labels",
        ],
// 29. MB103 cab in red, red container and base, Thailand, "Skittles" labels
	['mod' => $subtitle, 'var' => '29a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Skittles', 'cod' => '1', 'rar' => '',
            'cdt' => 'red',
            'tdt' => "red container and base, Thailand, SKITTLES labels",
        ],
// 30. MB103 cab in silver/gray, orange container, silver/gray base, Thailand, "Skittles" labels
	['mod' => $subtitle, 'var' => '30a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Skittles', 'cod' => '1', 'rar' => '',
            'cdt' => 'silver-gray',
            'tdt' => "orange container, silver-gray base, Thailand, SKITTLES labels",
        ],
// 31. MB103 cab in white, red container, white base, Thailand, "Skittles" labels
	['mod' => $subtitle, 'var' => '31a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Skittles', 'cod' => '1', 'rar' => '',
            'cdt' => 'white',
            'tdt' => "red container, white base, Thailand, SKITTLES labels",
        ],
// 32. MB103 cab in yellow, yellow container and base, Thailand, "M and M's" labels
	['mod' => $subtitle, 'var' => '32a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => "M&amp;M's", 'cod' => '1', 'rar' => '',
            'cdt' => 'yellow',
            'tdt' => "yellow container and base, Thailand, M&amp;M'S labels",
        ],
// 33. MB103 cab in black, black container and base, Thailand, "Roller Blade" labels
	['mod' => $subtitle, 'var' => '33a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'Thailand',
	    'liv' => 'Roller Blade', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container and base, Thailand, ROLLER BLADE labels",
        ],
// 34. MB103 cab in black, black container and base, China, "Roller Blade" labels
	['mod' => $subtitle, 'var' => '34a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => 'Roller Blade', 'cod' => '1', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container and base, ROLLER BLADE labels",
        ],
// 35. MB103 cab in yellow, yellow container and base, China, "M and M's" labels
	['mod' => $subtitle, 'var' => '35a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "M&amp;M's", 'cod' => '1', 'rar' => '',
            'cdt' => 'yellow',
            'tdt' => "yellow container and base, M&amp;M'S labels",
        ],
// 36. MB103 cab in bright blue, red container and base, China, "Kellogg's Froot Loops" labels
	['mod' => $subtitle, 'var' => '36a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "Kellog's", 'cod' => '1', 'rar' => '',
            'cdt' => 'bright blue',
            'tdt' => "red container and base, KELLOGG'S FROOT LOOPS labels",
        ],
// 37. MB103 cab in lemon, lemon container, black base, China, "Stop. Go. Pennzoil" tampo, rubber tires, antennas cast (PC)
	['mod' => $subtitle, 'var' => '37a',
	    'cab' => 'MB310', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => 'Pennzoil', 'cod' => '1', 'rar' => '',
            'cdt' => 'lemon',
            'tdt' => "lemon container, black base, STOP. GO. PENNZOIL tampo",
        ],
// 38. MB103 cab in red, red container, black base, China, "Coca-Cola" with sideways bottle tampo, rubber tires, antennas cast (PC)
	['mod' => $subtitle, 'var' => '38a',
	    'cab' => 'MB310', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => 'Coca-Cola', 'cod' => '1', 'rar' => '',
            'cdt' => 'red',
            'tdt' => "red container, black base, COCA-COLA with sideways bottle tampo",
        ],
// 39. MB103 cab in blue, red container and base, China, "Kellogg's Froot Loops!" labels
	['mod' => $subtitle, 'var' => '39a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => "Kellog's", 'cod' => '1', 'rar' => '',
            'cdt' => 'blue',
            'tdt' => "red container and base, KELLOGG'S FROOT LOOPS! labels",
        ],
// 40. MB103 cab in white, green container, yellow base, China and "Mattel", "Kellogg's Corn Flakes" labels (ROW)
	['mod' => $subtitle, 'var' => '40a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'China, MATTEL',
	    'liv' => "Kellog's", 'cod' => '1', 'rar' => '4',
            'cdt' => 'white',
            'tdt' => "green container, yellow base, KELLOGG'S CORN FLAKES labels",
        ],
// 41. MB103 cab in black, black container and base, China, "18th Annual Matchbox USA Convention and Toy Show" labels (C2)
	['mod' => $subtitle, 'var' => '41a',
	    'cab' => 'MB103', 'tlr' => 'Box', 'mfg' => 'China',
	    'liv' => 'Matchbox USA', 'cod' => '2', 'rar' => '',
            'cdt' => 'black',
            'tdt' => "black container and base, 18TH ANNUAL MATCHBOX USA CONVENTION AND TOY SHOW labels",
        ],

    ]);
// NOTE: Versions 36 and 39 with either "Matchbox International" or "Mattel Inc." cab casting.
}
?>
