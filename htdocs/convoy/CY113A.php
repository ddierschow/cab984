<?php // DONE
$subtitle = 'CY113A';
// CY-113-A FORD AEROMAX SUPERSTAR TRANSPORTER, issued 1994
$desc = "Ford Aeromax Superstar Transporter";
$year = '1994';

$defaults = ['mod' => $subtitle, 'cab' => 'MB214', 'tlr' => 'Superstar Transporter', 'cod' => '2'];

include "cypage.php";

function body() {
    show_table([
// 1. Metallic blue cab with blue chassis, blue container, "Family Channel" labels (WR)
	['var' => '001a', 'mfg' => 'Macau', 'liv' => "Family Channel",
	    'cdt' => 'metallic blue, blue chassis',
	    'tdt' => "blue container, FAMILY CHANNEL labels",
        ],
// 2. Blue cab with red chassis, blue container, "Quality Care Racing" labels (WR)
	['var' => '002a', 'mfg' => 'Macau', 'liv' => "Quality Care Racing",
	    'cdt' => 'blue, red chassis',
	    'tdt' => "blue container, QUALITY CARE RACING labels",
	],
// 3. White cab with white chassis, white container, "7 Exide Batteries" labels (WR)
	['var' => '003a', 'mfg' => 'Macau', 'liv' => "7 Exide Batteries",
	    'cdt' => 'white, white chassis',
	    'tdt' => "white container, 7 EXIDE BATTERIES labels",
	],
// 4. White cab with white chassis, white container, "Hooters Racing" labels (WR)
	['var' => '004a', 'mfg' => 'Macau', 'liv' => "Hooters Racing",
	    'cdt' => 'white, white chassis',
	    'tdt' => "white container, HOOTERS RACING labels",
	],
// 5. Black cab with chrome chassis, black container, "Finger-hut Racing" labels (WR)
	['var' => '005a', 'mfg' => 'Macau', 'liv' => "Finger-hut Racing",
	    'cdt' => 'black, chrome chassis',
	    'tdt' => "black container, FINGER-HUT RACING labels",
	],
// 6. White cab with chrome chassis, blue container, "Colts 94" labels (WR)
	['var' => '006a', 'mfg' => 'Macau', 'liv' => "Colts 94",
	    'cdt' => 'white, chrome chassis',
	    'tdt' => "blue container, COLTS 94 labels",
	],
// 7. White cab with chrome chassis, light blue container, "Oilers 94" labels (WR)
	['var' => '007a', 'mfg' => 'Macau', 'liv' => "Oilers 94",
	    'cdt' => 'white, chrome chassis',
	    'tdt' => "light blue container, OILERS 94 labels",
	],
// 8. White cab with chrome chassis, dark blue container, "Chargers 94" labels (WR)
	['var' => '008a', 'mfg' => 'Macau', 'liv' => "Chargers 94",
	    'cdt' => 'white, chrome chassis',
	    'tdt' => "dark blue container, CHARGERS 94 labels",
	],
// 9. White cab with chrome chassis, black container, "Raiders 94" labels (WR)
	['var' => '009a', 'mfg' => 'Macau', 'liv' => "Raiders 94",
	    'cdt' => 'white, chrome chassis',
	    'tdt' => "black container, RAIDERS 94 labels",
	],
// 10. White cab with chrome chassis, red container, "Bills 94" labels (WR)
	['var' => '010a', 'mfg' => 'Macau', 'liv' => "Bills 94",
	    'cdt' => 'white, chrome chassis',
	    'tdt' => "red container, BILLS 94 labels",
	],
// 11. Yellow cab with chrome chassis, red container, "Cardinals 94" labels (WR)
	['var' => '011a', 'mfg' => 'Macau', 'liv' => "Cardinals 94",
	    'cdt' => 'yellow, chrome chassis',
	    'tdt' => "red container, CARDINALS 94 labels",
	],
// 12. Yellow cab with chrome chassis, red container, "KC Chiefs 94" labels (WR)
	['var' => '012a', 'mfg' => 'Macau', 'liv' => "KC Chiefs 94",
	    'cdt' => 'yellow, chrome chassis',
	    'tdt' => "red container, KC CHIEFS 94 labels",
	],
// 13. Yellow cab with chrome chassis, green container, "Packers 94" labels (WR)
	['var' => '013a', 'mfg' => 'Macau', 'liv' => "Packers 94",
	    'cdt' => 'yellow, chrome chassis',
	    'tdt' => "green container, PACKERS 94 labels",
	],
// 14. Yellow cab with chrome chassis, black container, "Steelers 94" labels (WR)
	['var' => '014a', 'mfg' => 'Macau', 'liv' => "Steelers 94",
	    'cdt' => 'yellow, chrome chassis',
	    'tdt' => "black container, STEELERS 94 labels",
	],
// 15. Orange cab with chrome chassis, red container, "Buccaneers 94" labels (WR)
	['var' => '015a', 'mfg' => 'Macau', 'liv' => "Buccaneers 94",
	    'cdt' => 'orange, chrome chassis',
	    'tdt' => "red container, BUCCANEERS 94 labels",
	],
// 16. Orange cab with chrome chassis, white container, "Browns 94" labels (WR)
	['var' => '016a', 'mfg' => 'Macau', 'liv' => "Browns 94",
	    'cdt' => 'orange, chrome chassis',
	    'tdt' => "white container, BROWNS 94 labels",
	],
// 17. Orange cab with chrome chassis, white container, "Bengals 94" labels (WR)
	['var' => '017a', 'mfg' => 'Macau', 'liv' => "Bengals 94",
	    'cdt' => 'orange, chrome chassis',
	    'tdt' => "white container, BENGALS 94 labels",
	],
// 18. Orange cab with chrome chassis, turquoise container, "Dolphins 94" labels (WR)
	['var' => '018a', 'mfg' => 'Macau', 'liv' => "Dolphins 94",
	    'cdt' => 'orange, chrome chassis',
	    'tdt' => "turquoise container, DOLPHINS 94 labels",
	],
// 19. Red-brown cab with chrome chassis, yellow container, "Redskins 94" labels (WR)
	['var' => '019a', 'mfg' => 'Macau', 'liv' => "Redskins 94",
	    'cdt' => 'red-brown, chrome chassis',
	    'tdt' => "yellow container, REDSKINS 94 labels",
	],
// 20. Red cab with chrome chassis, dark blue container, "Patriots 94" labels (WR)
	['var' => '020a', 'mfg' => 'Macau', 'liv' => "Patriots 94",
	    'cdt' => 'red, chrome chassis',
	    'tdt' => "dark blue container, PATRIOTS 94 labels",
	],
// 21. Red cab with chrome chassis, black container, "Falcons 94" labels (WR)
	['var' => '021a', 'mfg' => 'Macau', 'liv' => "Falcons 94",
	    'cdt' => 'red, chrome chassis',
	    'tdt' => "black container, FALCONS 94 labels",
	],
// 22. Silver-gray cab with chrome chassis, dark blue container, "Cowboys 94" labels (WR)
	['var' => '022a', 'mfg' => 'Macau', 'liv' => "Cowboys 94",
	    'cdt' => 'silver-gray, chrome chassis',
	    'tdt' => "dark blue container, COWBOYS 94 labels",
	],
// 23. Gold cab with chrome chassis, red container, "SF 49ers" labels (WR)
	['var' => '023a', 'mfg' => 'Macau', 'liv' => "SF 49ers",
	    'cdt' => 'gold, chrome chassis',
	    'tdt' => "red container, SF 49ERS labels",
	],
// 24. Green-gold cab with chrome chassis, black container, "Saints 94" labels (WR)
	['var' => '024a', 'mfg' => 'Macau', 'liv' => "Saints 94",
	    'cdt' => 'green-gold, chrome chassis',
	    'tdt' => "black container, SAINTS 94 labels",
	],
// 25. Purple cab with chrome chassis, yellow container, "Vikings" labels (WR)
	['var' => '025a', 'mfg' => 'Macau', 'liv' => "Vikings",
	    'cdt' => 'purple, chrome chassis',
	    'tdt' => "yellow container, VIKINGS labels",
	],
// 26. Dark blue cab with chrome chassis, white container, "Giants 94" labels (WR)
	['var' => '026a', 'mfg' => 'Macau', 'liv' => "Giants 94",
	    'cdt' => 'dark blue, chrome chassis',
	    'tdt' => "white container, GIANTS 94 labels",
	],
// 27. Dark blue cab with chrome chassis, orange container, "Bears 94" labels (WR)
	['var' => '027a', 'mfg' => 'Macau', 'liv' => "Bears 94",
	    'cdt' => 'dark blue, chrome chassis',
	    'tdt' => "orange container, BEARS 94 labels",
	],
// 28. Bright blue cab with chrome chassis, orange container, "Broncos 94" labels (WR)
	['var' => '028a', 'mfg' => 'Macau', 'liv' => "Broncos 94",
	    'cdt' => 'bright blue, chrome chassis',
	    'tdt' => "orange container, BRONCOS 94 labels",
	],
// 29. Blue cab with chrome chassis, yellow container, "Rams 94" labels (WR)
	['var' => '029a', 'mfg' => 'Macau', 'liv' => "Rams 94",
	    'cdt' => 'blue, chrome chassis',
	    'tdt' => "yellow container, RAMS 94 labels",
	],
// 30. Blue cab with chrome chassis, gray container, "Lions 94" labels (WR)
	['var' => '030a', 'mfg' => 'Macau', 'liv' => "Lions 94",
	    'cdt' => 'blue, chrome chassis',
	    'tdt' => "gray container, LIONS 94 labels",
	],
// 31. Green cab with chrome chassis, gray container, "Eagles 94" labels (WR)
	['var' => '031a', 'mfg' => 'Macau', 'liv' => "Eagles 94",
	    'cdt' => 'green, chrome chassis',
	    'tdt' => "gray container, EAGLES 94 labels",
	],
// 32. Green cab with chrome chassis, white container, "Jets 94" labels (WR)
	['var' => '032a', 'mfg' => 'Macau', 'liv' => "Jets 94",
	    'cdt' => 'green, chrome chassis',
	    'tdt' => "white container, JETS 94 labels",
	],
// 33. Bright green cab with chrome chassis, gray container, "Seahawks 94" labels (WR)
	['var' => '033a', 'mfg' => 'Macau', 'liv' => "Seahawks 94",
	    'cdt' => 'bright green, chrome chassis',
	    'tdt' => "gray container, SEAHAWKS 94 labels",
	],
// 34. Red cab and chassis, red container, "McDonald's Racing Team" labels (WR)
	['var' => '034a', 'mfg' => 'Macau', 'liv' => "McDonald's Racing Team",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, MCDONALD'S RACING TEAM labels",
	],
// 35. Green cab with yellow chassis, green container, "Quaker State Racing Team" labels (WR)
	['var' => '035a', 'mfg' => 'Macau', 'liv' => "Quaker State Racing Team",
	    'cdt' => 'green, yellow chassis',
	    'tdt' => "green container, QUAKER STATE RACING TEAM labels",
	],
// 36. Blue and yellow cab with yellow chassis, blue container, "Team Lowe's Racing" labels (WR)
	['var' => '036a', 'mfg' => 'Macau', 'liv' => "Team Lowe's Racing",
	    'cdt' => 'blue and yellow, yellow chassis',
	    'tdt' => "blue container, TEAM LOWE'S RACING labels",
	],
// 37. Black cab and chassis, black container, "Helig-Myers" labels (WR)
	['var' => '037a', 'mfg' => 'Macau', 'liv' => "Helig-Myers",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, HELIG-MYERS labels",
	],
// 38. White and blue cab with blue chassis, blue container, "Valvoline Rousch Racing" labels (WR)
	['var' => '038a', 'mfg' => 'Macau', 'liv' => "Valvoline Rousch Racing",
	    'cdt' => 'white and blue, blue chassis',
	    'tdt' => "blue container, VALVOLINE ROUSCH RACING labels",
	],
// 39. Metallic blue cab with blue chassis, blue container, "Raybestos Racing" labels (WR)
	['var' => '039a', 'mfg' => 'Macau', 'liv' => "Raybestos Racing",
	    'cdt' => 'metallic blue, blue chassis',
	    'tdt' => "blue container, RAYBESTOS RACING labels",
	],
// 40. Black cab with chrome chassis, black container, "Havoline" labels (WR)
	['var' => '040a', 'mfg' => 'Macau', 'liv' => "Havoline",
	    'cdt' => 'black, chrome chassis',
	    'tdt' => "black container, HAVOLINE labels",
	],
// 41. Black cab and chassis, black container, "Winn Dixie Racing" labels (WR)
	['var' => '041a', 'mfg' => 'Macau', 'liv' => "Winn Dixie Racing",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, WINN DIXIE RACING labels",
	],
// 42. Red cab and chassis, red container, "Happy Holidays" labels (WR)
	['var' => '042a', 'mfg' => 'Macau', 'liv' => "Happy Holidays",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, HAPPY HOLIDAYS labels",
	],
// 43. Blue cab with lemon chassis, blue container, "Kleenex Racing 40" labels (WR)
	['var' => '043a', 'mfg' => 'Macau', 'liv' => "Kleenex Racing 40",
	    'cdt' => 'blue, lemon chassis',
	    'tdt' => "blue container, KLEENEX RACING 40 labels",
	],
// 44. Red cab with gold chassis and wheels, red container, Ail-Star Game 1996" labels (WR)
	['var' => '044a', 'mfg' => 'Macau', 'liv' => "All-Star Game 1996",
	    'cdt' => 'red, gold chassis and wheels',
	    'tdt' => "red container, ALL-STAR GAME 1996 labels",
	],
// 45. White cab and chassis, white container, "K-Mart/Little Caesars" labels (WR)
	['var' => '045a', 'mfg' => 'Macau', 'liv' => "K-Mart/Little Caesars",
	    'cdt' => 'white cab and chassis',
	    'tdt' => "white container, K-MART/LITTLE CAESARS labels",
	],
// 46. White cab with red chassis, white container, "Jasper Engines and Transmissions" labels (WR)
	['var' => '046a', 'mfg' => 'Macau', 'liv' => "Jasper Engines and Transmissions",
	    'cdt' => 'white, red chassis',
	    'tdt' => "white container, JASPER ENGINES AND TRANSMISSIONS labels",
	],
// 47. Red and black cab with red chassis, red container, "McDonald's Racing" with two-line "McDonald's" roof label (WR)
	['var' => '047a', 'mfg' => 'Macau', 'liv' => "McDonald's",
	    'cdt' => 'red and black, red chassis',
	    'tdt' => "red container, MCDONALD'S RACING with two-line MCDONALD'S roof label",
	],
// 48. Blue cab with orange chassis, blue container, "Team ASE" labels (WR)
	['var' => '048a', 'mfg' => 'Macau', 'liv' => "Team ASE",
	    'cdt' => 'blue, orange chassis',
	    'tdt' => "blue container, TEAM ASE labels",
	],
// 49. Orange cab with blue chassis, orange container, "Florida Gators 96" labels (WR)
	['var' => '049a', 'mfg' => 'Macau', 'liv' => "Florida Gators 96",
	    'cdt' => 'orange, blue chassis',
	    'tdt' => "orange container, FLORIDA GATORS 96 labels",
	],
// 50. Dark blue and yellow cab with yellow chassis, dark blue container, "Michigan 96" labels (WR)
	['var' => '050a', 'mfg' => 'Macau', 'liv' => "Michigan 96",
	    'cdt' => 'dark blue and yellow, yellow chassis',
	    'tdt' => "dark blue container, MICHIGAN 96 labels",
	],
// 51. White and red cab with black chassis, red container, "Nebraska Huskers 96" labels (WR)
	['var' => '051a', 'mfg' => 'Macau', 'liv' => "Nebraska Huskers 96",
	    'cdt' => 'white and red, black chassis',
	    'tdt' => "red container, NEBRASKA HUSKERS 96 labels",
	],
// 52. White and orange cab with orange chassis, orange container, "Syracuse University Orangemen 96" labels (WR)
	['var' => '052a', 'mfg' => 'Macau', 'liv' => "Syracuse University Orangemen 96",
	    'cdt' => 'white and orange, orange chassis',
	    'tdt' => "orange container, SYRACUSE UNIVERSITY ORANGEMEN 96 labels",
	],
// 53. Black cab with red chassis, red container, "Maryland Terrapins 96" labels (WR)
	['var' => '053a', 'mfg' => 'Macau', 'liv' => "Maryland Terrapins 96",
	    'cdt' => 'black, red chassis',
	    'tdt' => "red container, MARYLAND TERRAPINS 96 labels",
	],
// 54. Dark blue and white cab with white chassis, dark blue container, "Penn State Nittany Lions 96" labels (WR)
	['var' => '054a', 'mfg' => 'Macau', 'liv' => "Penn State Nittany Lions 96",
	    'cdt' => 'dark blue and white, white chassis',
	    'tdt' => "dark blue container, PENN STATE NITTANY LIONS 96 labels",
	],
// 55. Pale orange cab with chrome chassis, black container, "Super Bowl XXX" labels (WR)
	['var' => '055a', 'mfg' => 'Macau', 'liv' => "Super Bowl XXX",
	    'cdt' => 'pale orange, chrome chassis',
	    'tdt' => "black container, SUPER BOWL XXX labels",
	],
// 56. Dark blue cab with red chassis, dark blue container, "Quality Care Ford Credit Racing" labels (WR)
	['var' => '056a', 'mfg' => 'Macau', 'liv' => "Quality Care Ford Credit Racing",
	    'cdt' => 'dark blue, red chassis',
	    'tdt' => "dark blue container, QUALITY CARE FORD CREDIT RACING labels",
	],
// 57. Dark blue cab and chassis, dark blue container, "Spam Racing" labels (WR)
	['var' => '057a', 'mfg' => 'Macau', 'liv' => "Spam Racing",
	    'cdt' => 'dark blue cab and chassis',
	    'tdt' => "dark blue container, SPAM RACING labels",
	],
// 58. White and dark blue cab with dark blue chassis, dark blue container, "Penn State 96" labels (WR)
	['var' => '058a', 'mfg' => 'Macau', 'liv' => "Penn State 96",
	    'cdt' => 'white and dark blue, dark blue chassis',
	    'tdt' => "dark blue container, PENN STATE 96 labels",
	],
// NOTE: All below models with chrome chassis
// 59. Dark blue and silver cab, gray container, "Patriots 96" labels (WR)
	['var' => '059a', 'mfg' => 'Macau', 'liv' => "Patriots 96",
	    'cdt' => 'dark blue and silver cab, chrome chassis',
	    'tdt' => "gray container, PATRIOTS 96 labels",
	],
// 60. Dark blue and silver cab, gray container, "Cowboys 1996" labels (WR)
	['var' => '060a', 'mfg' => 'Macau', 'liv' => "Cowboys 1996",
	    'cdt' => 'dark blue and silver cab, chrome chassis',
	    'tdt' => "gray container, COWBOYS 1996 labels",
	],
// 61. Dark blue and red cab, red container, "Giants 1996" labels (WR)
	['var' => '061a', 'mfg' => 'Macau', 'liv' => "Giants 1996",
	    'cdt' => 'dark blue and red cab, chrome chassis',
	    'tdt' => "red container, GIANTS 1996 labels",
	],
// 62. Dark blue and green cab, green container, "Seahawks 96" labels (WR)
	['var' => '062a', 'mfg' => 'Macau', 'liv' => "Seahawks 96",
	    'cdt' => 'dark blue and green cab, chrome chassis',
	    'tdt' => "green container, SEAHAWKS 96 labels",
	],
// 63. Dark blue and yellow cab, yellow container, "Chargers 1996" labels (WR)
	['var' => '063a', 'mfg' => 'Macau', 'liv' => "Chargers 1996",
	    'cdt' => 'dark blue and yellow cab, chrome chassis',
	    'tdt' => "yellow container, CHARGERS 1996 labels",
	],
// 64. Dark blue and yellow cab, yellow container, "Rams 96" labels (WR)
	['var' => '064a', 'mfg' => 'Macau', 'liv' => "Rams 96",
	    'cdt' => 'dark blue and yellow cab, chrome chassis',
	    'tdt' => "yellow container, RAMS 96 labels",
	],
// 65. Dark blue and orange cab, orange container, "Bears 96" labels (WR)
	['var' => '065a', 'mfg' => 'Macau', 'liv' => "Bears 96",
	    'cdt' => 'dark blue and orange cab, chrome chassis',
	    'tdt' => "orange container, BEARS 96 labels",
	],
// 66. Blue and silver cab, gray container, "Lions 96" labels (WR)
	['var' => '066a', 'mfg' => 'Macau', 'liv' => "Lions 96",
	    'cdt' => 'blue and silver cab, chrome chassis',
	    'tdt' => "gray container, LIONS 96 labels",
	],
// 67. Bright blue and orange cab, orange container, "Broncos 96" labels (WR)
	['var' => '067a', 'mfg' => 'Macau', 'liv' => "Broncos 96",
	    'cdt' => 'bright blue and orange cab, chrome chassis',
	    'tdt' => "orange container, BRONCOS 96 labels",
	],
// 68. Bright blue and red cab, red container, "Bills 96" labels (WR)
	['var' => '068a', 'mfg' => 'Macau', 'liv' => "Bills 96",
	    'cdt' => 'bright blue and red cab, chrome chassis',
	    'tdt' => "red container, BILLS 96 labels",
	],
// 69. Blue-green and orange cab, orange container, "Dolphins 96" labels (WR)
	['var' => '069a', 'mfg' => 'Macau', 'liv' => "Dolphins 96",
	    'cdt' => 'blue-green and orange cab, chrome chassis',
	    'tdt' => "orange container, DOLPHINS 96 labels",
	],
// 70. Turquoise and mustard cab, mustard container, "Jacksonville Jaguars 96" labels (WR)
	['var' => '070a', 'mfg' => 'Macau', 'liv' => "Jacksonville Jaguars 96",
	    'cdt' => 'turquoise and mustard cab, chrome chassis',
	    'tdt' => "mustard container, JACKSONVILLE JAGUARS 96 labels",
	],
// 71. Black and orange cab, orange container, "Bengals 96" labels (WR)
	['var' => '071a', 'mfg' => 'Macau', 'liv' => "Bengals 96",
	    'cdt' => 'black and orange cab, chrome chassis',
	    'tdt' => "orange container, BENGALS 96 labels",
	],
// 72. Black and red cab, red container, "Falcons 96" labels (S8-12MWR)
	['var' => '072a', 'mfg' => 'Macau', 'liv' => "Falcons 96",
	    'cdt' => 'black and red cab, chrome chassis',
	    'tdt' => "red container, FALCONS 96 labels",
	],
// 73. Black and silver cab, gray container, "Raiders 96" labels (S8-12)(WR)
	['var' => '073a', 'mfg' => 'Macau', 'liv' => "Raiders 96",
	    'cdt' => 'black and silver cab, chrome chassis',
	    'tdt' => "gray container, RAIDERS 96 labels",
	],
// 74. Black and gold cab, gold container, "Saints 96" labels (S8-12)(WR)
	['var' => '074a', 'mfg' => 'Macau', 'liv' => "Saints 96",
	    'cdt' => 'black and gold cab, chrome chassis',
	    'tdt' => "gold container, SAINTS 96 labels",
	],
// 75. Black and yellow cab, yellow container, "Steelers 96" labels (WR)
	['var' => '075a', 'mfg' => 'Macau', 'liv' => "Steelers 96",
	    'cdt' => 'black and yellow cab, chrome chassis',
	    'tdt' => "yellow container, STEELERS 96 labels",
	],
// 76. Black and green cab, green container, "Jets 96" labels (S8-12)(WR)
	['var' => '076a', 'mfg' => 'Macau', 'liv' => "Jets 96",
	    'cdt' => 'black and green cab, chrome chassis',
	    'tdt' => "green container, JETS 96 labels",
	],
// 77. Black and purple cab, purple container, "Ravens Inaugural Season 1996" labels (WR)
	['var' => '077a', 'mfg' => 'Macau', 'liv' => "Ravens Inaugural Season 1996",
	    'cdt' => 'black and purple cab, chrome chassis',
	    'tdt' => "purple container, RAVENS INAUGURAL SEASON 1996 labels",
	],
// 78. black and blue cab, blue container, "Panthers 96" labels iS8-12)(WR)
	['var' => '078a', 'mfg' => 'Macau', 'liv' => "Panthers 96",
	    'cdt' => 'black and blue cab, chrome chassis',
	    'tdt' => "blue container, PANTHERS 96 labels iS8-12)",
	],
// 79. Black and dark blue-green cab, dark blue-green container, "Eagles 96" labels (WR)
	['var' => '079a', 'mfg' => 'Macau', 'liv' => "Eagles 96",
	    'cdt' => 'black and dark blue-green cab, chrome chassis',
	    'tdt' => "dark blue-green container, EAGLES 96 labels",
	],
// 80. Purple and yellow cab, yellow container, "Vikings 96" labels (S8-12)(WR)
	['var' => '080a', 'mfg' => 'Macau', 'liv' => "Vikings 96",
	    'cdt' => 'purple and yellow cab, chrome chassis',
	    'tdt' => "yellow container, VIKINGS 96 labels",
	],
// 81. Green and yellow cab, yellow container, "Packers 96" labels (WR)
	['var' => '081a', 'mfg' => 'Macau', 'liv' => "Packers 96",
	    'cdt' => 'green and yellow cab, chrome chassis',
	    'tdt' => "yellow container, PACKERS 96 labels",
	],
// 82. Rose and gold cab, gold container, "49ers 96" labels (WR)
	['var' => '082a', 'mfg' => 'Macau', 'liv' => "49ers 96",
	    'cdt' => 'rose and gold cab, chrome chassis',
	    'tdt' => "gold container, 49ERS 96 labels",
	],
// 83. Rose and yellow cab, yellow container, "Cardinals 96" labels (WR)
	['var' => '083a', 'mfg' => 'Macau', 'liv' => "Cardinals 96",
	    'cdt' => 'rose and yellow cab, chrome chassis',
	    'tdt' => "yellow container, CARDINALS 96 labels",
	],
// 84. Rose and yellow cab, yellow container, "Redskins 96" labels (WR)
	['var' => '084a', 'mfg' => 'Macau', 'liv' => "Redskins 96",
	    'cdt' => 'rose and yellow cab, chrome chassis',
	    'tdt' => "yellow container, REDSKINS 96 labels",
	],
// 85. Red and yellow cab, yellow container, "Chiefs 96" labels (WR)
	['var' => '085a', 'mfg' => 'Macau', 'liv' => "Chiefs 96",
	    'cdt' => 'red and yellow cab, chrome chassis',
	    'tdt' => "yellow container, CHIEFS 96 labels",
	],
// 86. Red and orange cab, orange container, "Buccaneers 96" labels (WR)
	['var' => '086a', 'mfg' => 'Macau', 'liv' => "Buccaneers 96",
	    'cdt' => 'red and orange cab, chrome chassis',
	    'tdt' => "orange container, BUCCANEERS 96 labels",
	],
// 87. Red and light blue cab, light blue container, "Oilers 96" labels (WR)
	['var' => '087a', 'mfg' => 'Macau', 'liv' => "Oilers 96",
	    'cdt' => 'red and light blue cab, chrome chassis',
	    'tdt' => "light blue container, OILERS 96 labels",
	],
// 88. White and dark blue cab, blue container, "Colts 96" labels (WR)
	['var' => '088a', 'mfg' => 'Macau', 'liv' => "Colts 96",
	    'cdt' => 'white and dark blue cab, chrome chassis',
	    'tdt' => "blue container, COLTS 96 labels",
	],
// 89. Black cab with chrome chassis, black container, "Associated Truck and Brake Supply" labels (WR)
	['var' => '089a', 'mfg' => 'Macau', 'liv' => "Associated Truck and Brake Supply",
	    'cdt' => 'black, chrome chassis',
	    'tdt' => "black container, ASSOCIATED TRUCK AND BRAKE SUPPLY labels",
	],
// 90. Black cab and chassis, black container, "Exide 99 Racing Team"(WR)
	['var' => '090a', 'mfg' => 'Macau', 'liv' => "Exide 99 Racing Team",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, EXIDE 99 RACING TEAM",
	],
// 91. Black cab, chrome chassis, black container, "Miller Lite Racing" labels (WR)
	['var' => '091a', 'mfg' => 'Macau', 'liv' => "Miller Lite Racing",
	    'cdt' => 'black cab, chrome chassis',
	    'tdt' => "black container, MILLER LITE RACING labels",
	],
// 92. Silver-gray cab, chrome chassis, gray container, "68th Ail-Star Game 1997" labels (WR)
	['var' => '092a', 'mfg' => 'Macau', 'liv' => "68th Ail-Star Game 1997",
	    'cdt' => 'silver-gray cab, chrome chassis',
	    'tdt' => "gray container, 68TH AIL-STAR GAME 1997 labels",
	],
// 93. White cab, chrome chassis, white container, "New Holland" labels (WR)
	['var' => '093a', 'mfg' => 'Macau', 'liv' => "New Holland",
	    'cdt' => 'white cab, chrome chassis',
	    'tdt' => "white container, NEW HOLLAND labels",
	],
// 94. Blue and red cab, blue container, "1997 New England Patriots" labels (WR)
	['var' => '094a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and red cab, chrome chassis',
	    'tdt' => "blue container, 1997 NEW ENGLAND PATRIOTS labels",
	],
// 95. Blue and red cab, blue container, "1997 New York Giants" labels (WR)
	['var' => '095a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and red cab, chrome chassis',
	    'tdt' => "blue container, 1997 NEW YORK GIANTS labels",
	],
// 96. Blue and red cab, blue container, "1997 Buffalo Bills" labels (WR)
	['var' => '096a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and red cab, chrome chassis',
	    'tdt' => "blue container, 1997 BUFFALO BILLS labels",
	],
// 97. Blue and red cab, blue container, "1997 Atlanta Falcons" labels (WR)
	['var' => '097a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and red cab, chrome chassis',
	    'tdt' => "blue container, 1997 ATLANTA FALCONS labels",
	],
// 98. Blue and orange cab, blue container, "1997 Denver Broncos" labels (WR)
	['var' => '098a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and orange cab, chrome chassis',
	    'tdt' => "blue container, 1997 DENVER BRONCOS labels",
	],
// 99. Blue and yellow cab, blue container, "1997 San Diego Chargers" labels (WR)
	['var' => '099a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and yellow cab, chrome chassis',
	    'tdt' => "blue container, 1997 SAN DIEGO CHARGERS labels",
	],
// 100. Dark blue and orange cab, dark blue container, "1997 Cincinnati Bengals" labels (WR)
	['var' => '100a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'dark blue and orange cab, chrome chassis',
	    'tdt' => "dark blue container, 1997 CINCINNATI BENGALS labels",
	],
// 101. Dark blue and yellow cab, dark blue container, "1997 St. Louis Rams" labels (WR)
	['var' => '101a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'dark blue and yellow cab, chrome chassis',
	    'tdt' => "dark blue container, 1997 ST. LOUIS RAMS labels",
	],
// 102. Dark blue and orange cab, blue container, "1997 Chicago Bears" labels (WR)
	['var' => '102a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'dark blue and orange cab, chrome chassis',
	    'tdt' => "blue container, 1997 CHICAGO BEARS labels",
	],
// 103. Dark blue and mustard cab, blue container, "1997 Baltimore Ravens" labels (WR)
	['var' => '103a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'dark blue and mustard cab, chrome chassis',
	    'tdt' => "blue container, 1997 BALTIMORE RAVENS labels",
	],
// 104. Blue and black cab, dark blue container, "1997 Indianapolis Colts" labels (WR)
	['var' => '104a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and black cab, chrome chassis',
	    'tdt' => "dark blue container, 1997 INDIANAPOLIS COLTS labels",
	],
// 105. Blue and green cab, blue container, "1997 Seattle Seahawks" labels (WR)
	['var' => '105a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue and green cab, chrome chassis',
	    'tdt' => "blue container, 1997 SEATTLE SEAHAWKS labels",
	],
// 106. Blue-green and mustard cab, blue-green container, "1997 Jacksonville Jaguars" labels (WR)
	['var' => '106a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue-green and mustard cab, chrome chassis',
	    'tdt' => "blue-green container, 1997 JACKSONVILLE JAGUARS labels",
	],
// 107. Blue-green and orange cab, blue-green container, "1997 Miami Dolphins" tampo (WR)
	['var' => '107a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'blue-green and orange cab, chrome chassis',
	    'tdt' => "blue-green container, 1997 MIAMI DOLPHINS tampo",
	],
// 108. Purple and yellow cab, purple container, "1997 Minnesota Vikings" labels (WR)
	['var' => '108a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'purple and yellow cab, chrome chassis',
	    'tdt' => "purple container, 1997 MINNESOTA VIKINGS labels",
	],
// 109. Black and silver-gray cab, black containers, "1997 Oakland Raiders" labels (WR)
	['var' => '109a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'black and silver-gray cab, chrome chassis',
	    'tdt' => "black containers, 1997 OAKLAND RAIDERS labels",
	],
// 110. Black and blue cab, black container, "1997 Carolina Panthers" labels (WR)
	['var' => '110a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'black and blue cab, chrome chassis',
	    'tdt' => "black container, 1997 CAROLINA PANTHERS labels",
	],
// 111. Black and dark green cab, black container, "1997 New York Jets" labels (WR)
	['var' => '111a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'black and dark green cab, chrome chassis',
	    'tdt' => "black container, 1997 NEW YORK JETS labels",
	],
// 112. Black and mustard cab, black container, "1997 New Orleans Saints" labels (WR)
	['var' => '112a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'black and mustard cab, chrome chassis',
	    'tdt' => "black container, 1997 NEW ORLEANS SAINTS labels",
	],
// 113. Black and yellow cab, black container, "1997 Pittsburgh Steelers" labels (WR)
	['var' => '113a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'black and yellow cab, chrome chassis',
	    'tdt' => "black container, 1997 PITTSBURGH STEELERS labels",
	],
// 114. Black and dark green cab, black container, "1997 Philadelphia Eagles" labels (WR)
	['var' => '114a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'black and dark green cab, chrome chassis',
	    'tdt' => "black container, 1997 PHILADELPHIA EAGLES labels",
	],
// 115. Dark green and yellow cab, dark green container, "1997 Green Bay Packers" labels (WR)
	['var' => '115a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'dark green and yellow cab, chrome chassis',
	    'tdt' => "dark green container, 1997 GREEN BAY PACKERS labels",
	],
// 116. Silver-gray and dark blue cab, blue container, "1997 Dallas Cowboys" labels (WR)
	['var' => '116a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'silver-gray and dark blue cab, chrome chassis',
	    'tdt' => "blue container, 1997 DALLAS COWBOYS labels",
	],
// 117. Silver-gray and blue cab, gray container, "1997 Detroit Lions" labels (WR)
	['var' => '117a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'silver-gray and blue cab, chrome chassis',
	    'tdt' => "gray container, 1997 DETROIT LIONS labels",
	],
// 118. Red and yellow cab, red container, "1997 Kansas City Chiefs" labels (WR)
	['var' => '118a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'red and yellow cab, chrome chassis',
	    'tdt' => "red container, 1997 KANSAS CITY CHIEFS labels",
	],
// 119. Red and blue cab, red container, "1997 Tennessee Oilers" labels (WR)
	['var' => '119a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'red and blue cab, chrome chassis',
	    'tdt' => "red container, 1997 TENNESSEE OILERS labels",
	],
// 120. Orange and red cab, red container, "1997 Tampa Bay Buccaneers" labels (WR)
	['var' => '120a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'orange and red cab, chrome chassis',
	    'tdt' => "red container, 1997 TAMPA BAY BUCCANEERS labels",
	],
// 121. Rose and yellow cab, rose container, "1997 Washington Redskins" labels (WR)
	['var' => '121a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'rose and yellow cab, chrome chassis',
	    'tdt' => "rose container, 1997 WASHINGTON REDSKINS labels",
	],
// 122. Rose and yellow cab, rose container, "1997 Arizona Cardinals" labels (WR)
	['var' => '122a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'rose and yellow cab, chrome chassis',
	    'tdt' => "rose container, 1997 ARIZONA CARDINALS labels",
	],
// 123. Rose and gold cab, red container, "1997 San Francisco 49ers" labels (WR)
	['var' => '123a', 'mfg' => 'Macau', 'liv' => "NFL",
	    'cdt' => 'rose and gold cab, chrome chassis',
	    'tdt' => "red container, 1997 SAN FRANCISCO 49ERS labels",
	],
// 124. Green and yellow cab, green container, "Packers Super Bowl XXXI" labels (WR)
	['var' => '124a', 'mfg' => 'Macau', 'liv' => "Packers Super Bowl XXXI",
	    'cdt' => 'green and yellow cab, chrome chassis',
	    'tdt' => "green container, PACKERS SUPER BOWL XXXI labels",
	],
// 125. Blue cab, chrome chassis, white container, "Miller Lite" labels, sealed in plexibox (WR)
	['var' => '125a', 'mfg' => 'Macau', 'liv' => "Miller Lite",
	    'cdt' => 'blue cab, chrome chassis',
	    'tdt' => "white container, MILLER LITE labels, sealed in plexibox",
	    'nts' => 'Sealed in plexibox',
	],
// 126. Dark red cab, chrome chassis, dark red container, "Circuit City 8" labels (WR)
	['var' => '126a', 'mfg' => 'Macau', 'liv' => "Circuit City 8",
	    'cdt' => 'dark red cab, chrome chassis',
	    'tdt' => "dark red container, CIRCUIT CITY 8 labels",
	],
// 127. White cab and chassis, white container, "QVC Racing Team 7" labels (WR)
	['var' => '127a', 'mfg' => 'Macau', 'liv' => "QVC Racing Team 7",
	    'cdt' => 'white cab and chassis',
	    'tdt' => "white container, QVC RACING TEAM 7 labels",
	],
// 128. Green cab, chrome chassis, red container, "Merry Christmas Happy New Year- White Rose Collectibles 1997" labels (WR)
	['var' => '128a', 'mfg' => 'Macau', 'liv' => "Merry Christmas Happy New Year- White Rose Collectibles 1997",
	    'cdt' => 'green cab, chrome chassis',
	    'tdt' => "red container, MERRY CHRISTMAS HAPPY NEW YEAR- WHITE ROSE COLLECTIBLES 1997 labels",
	],
    ]);
}
?>
