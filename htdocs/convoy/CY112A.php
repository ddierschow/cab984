<?php // DONE
$subtitle = 'CY112A';
// CY-112-A KENWORTH T600 SUPERSTAR TRANSPORTER, issued 1994
$desc = "Kenworth T600 Superstar Transporter";
$year = '1994';

$defaults = ['mod' => $subtitle, 'cab' => 'CY112', 'tlr' => 'Superstar Transporter', 'cod' => '2'];

include "cypage.php";

function body() {
    show_table([
// 1. Red cab with chrome chassis, green container, "Merry Christmas 1993" labels (WR)
	['var' => '001a', 'mfg' => 'Macau', 'liv' => "Merry Christmas 1993",
	    'cdt' => 'red cab with chrome chassis',
	    'tdt' => "green container, MERRY CHRISTMAS 1993 labels",
	],
// 2. Black cab with chrome chassis, yellow container, "White Rose Series II in '94" labels (WR)
	['var' => '002a', 'mfg' => 'Macau', 'liv' => "White Rose Series II in '94",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "yellow container, WHITE ROSE SERIES II IN '94 labels",
	],
// 3. Yellow cab with chrome chassis, yellow container, "White House Apple Juice Racing" (pink lettering) labels (WR)
	['var' => '003a', 'mfg' => 'Macau', 'liv' => "White House Apple Juice Racing",
	    'cdt' => 'yellow cab with chrome chassis',
	    'tdt' => "yellow container, WHITE HOUSE APPLE JUICE RACING (pink lettering) labels",
	],
// 4. Dark blue cab with chrome chassis, yellow container, "Matchbox/White Rose 29" labels (WR)
	['var' => '004a', 'mfg' => 'Macau', 'liv' => "Matchbox/White Rose 29",
	    'cdt' => 'dark blue cab with chrome chassis',
	    'tdt' => "yellow container, MATCHBOX/WHITE ROSE 29 labels",
	],
// 5. Black cab with chrome chassis, red container, "Phillies-National League Champions 1993" labels (WR)
	['var' => '005a', 'mfg' => 'Macau', 'liv' => "Phillies-National League Champions 1993",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "red container, PHILLIES-NATIONAL LEAGUE CHAMPIONS 1993 labels",
	],
// 6. White cab with chrome chassis, white container, "Factory Stores of America" labels (WR)
	['var' => '006a', 'mfg' => 'Macau', 'liv' => "Factory Stores of America",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "white container, FACTORY STORES OF AMERICA labels",
	],
// 7. Yellow cab with red chassis, red container, "Kellogg's Racing 5" labels (WR)
	['var' => '007a', 'mfg' => 'Macau', 'liv' => "Kellogg's Racing 5",
	    'cdt' => 'yellow cab with red chassis',
	    'tdt' => "red container, KELLOGG'S RACING 5 labels",
	],
// 8. White cab with chrome chassis, white container, "Manheim Auctions 7" labels (WR)
	['var' => '008a', 'mfg' => 'Macau', 'liv' => "Manheim Auctions 7",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "white container, MANHEIM AUCTIONS 7 labels",
	],
// 9. Black cab with chrome chassis, black container, "Shoe World 32" labels (WR)
	['var' => '009a', 'mfg' => 'Macau', 'liv' => "Shoe World 32",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, SHOE WORLD 32 labels",
	],
// 10. Black cab with chrome chassis, black container, "Baltimore Orioles 94" labels (WR)
	['var' => '010a', 'mfg' => 'Macau', 'liv' => "Baltimore Orioles 94",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, BALTIMORE ORIOLES 94 labels",
	],
// 11. Black cab with chrome chassis, red container, "65th All Star Game-Pittsburgh Pirates 1994" labels (WR)
	['var' => '011a', 'mfg' => 'Macau', 'liv' => "65th All Star Game-Pittsburgh Pirates 1994",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "red container, 65TH ALL STAR GAME-PITTSBURGH PIRATES 1994 labels",
	],
// 12. Purple cab with chrome chassis, black container, "Colorado Rockies" labels (WR)
	['var' => '012a', 'mfg' => 'Macau', 'liv' => "Colorado Rockies",
	    'cdt' => 'purple cab with chrome chassis',
	    'tdt' => "black container, COLORADO ROCKIES labels",
	],
// 13. Black cab with chrome chassis, black container, "Carolina Panthers-Inaugural Season 1995" labels (WR)
	['var' => '013a', 'mfg' => 'Macau', 'liv' => "Carolina Panthers-Inaugural Season 1995",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, CAROLINA PANTHERS-INAUGURAL SEASON 1995 labels",
	],
// 14. Blue-green cab with chrome chassis, blue-green container, "Jacksonville Jaguars Inaugural Season 1995" labels (WR)
	['var' => '014a', 'mfg' => 'Macau', 'liv' => "Jacksonville Jaguars Inaugural Season 1995",
	    'cdt' => 'blue-green cab with chrome chassis',
	    'tdt' => "blue-green container, JACKSONVILLE JAGUARS INAUGURAL SEASON 1995 labels",
	],
// 15. Yellow cab with chrome chassis, yellow container, "White House Apple Juice Racing" (red lettering) labels (WR)(OP)
	['var' => '015a', 'mfg' => 'Macau', 'liv' => "White House Apple Juice Racing",
	    'cdt' => 'yellow cab with chrome chassis',
	    'tdt' => "yellow container, WHITE HOUSE APPLE JUICE RACING (red lettering) labels",
	],
// 16. Black cab with chrome chassis, black container, "Good-wrench Racing" labels (WR)
	['var' => '016a', 'mfg' => 'Macau', 'liv' => "Good-wrench Racing",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, GOOD-WRENCH RACING labels",
	],
// 17. Powder blue cab with dark blue chassis, dark blue container, "Penn State 94" labels (WR)
	['var' => '017a', 'mfg' => 'Macau', 'liv' => "Penn State 94",
	    'cdt' => 'powder blue cab with dark blue chassis',
	    'tdt' => "dark blue container, PENN STATE 94 labels",
	],
// 18. White body with dark gray chassis, white container, "AC-Delco" labels (WR)
	['var' => '018a', 'mfg' => 'Macau', 'liv' => "AC-Delco",
	    'cdt' => 'white body with dark gray chassis',
	    'tdt' => "white container, AC-DELCO labels",
	],
// 19. Metallic blue cab with chrome chassis, dark blue container, "Dupont Racing" labels (WR)
	['var' => '019a', 'mfg' => 'Macau', 'liv' => "Dupont Racing",
	    'cdt' => 'metallic blue cab with chrome chassis',
	    'tdt' => "dark blue container, DUPONT RACING labels",
	],
// 20. Orange/yellow cab with black chassis, white container, "Kodak Funsaver Racing" labels (WR)
	['var' => '020a', 'mfg' => 'Macau', 'liv' => "Kodak Funsaver Racing",
	    'cdt' => 'orange/yellow cab with black chassis',
	    'tdt' => "white container, KODAK FUNSAVER RACING labels",
	],
// 21. White cab with chrome chassis, black container, "Western Auto 17" labels (WR)
	['var' => '021a', 'mfg' => 'Macau', 'liv' => "Western Auto 17",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "black container, WESTERN AUTO 17 labels",
	],
// 22. Silver-gray cab with chrome chassis, gray container, "Cowboys Super Bowl" labels (WR)
	['var' => '022a', 'mfg' => 'Macau', 'liv' => "Cowboys Super Bowl",
	    'cdt' => 'silver-gray cab with chrome chassis',
	    'tdt' => "gray container, COWBOYS SUPER BOWL labels",
	],
// 23. White cab with chrome chassis, white container, "Black Flag/French's" labels (WR)
	['var' => '023a', 'mfg' => 'Macau', 'liv' => "Black Flag/French's",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "white container, BLACK FLAG/FRENCH'S labels",
	],
// 24. Black cab with black chassis, black container, "Kendall Motor Oil Racing" labels (WR)
	['var' => '024a', 'mfg' => 'Macau', 'liv' => "Kendall Motor Oil Racing",
	    'cdt' => 'black cab with black chassis',
	    'tdt' => "black container, KENDALL MOTOR OIL RACING labels",
	],
// 25. Black cab with chrome chassis, black container, "Orioles 40 Years" labels (WR)
	['var' => '025a', 'mfg' => 'Macau', 'liv' => "Orioles 40 Years",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, ORIOLES 40 YEARS labels",
	],
// 26. White cab with white chassis, white container, "Polaroid" labels
	['var' => '026a', 'mfg' => 'Macau', 'liv' => "Polaroid",
	    'cdt' => 'white cab with white chassis',
	    'tdt' => "white container, POLAROID labels",
	],
// 27. Black cab with black chassis, black container, "Good-wrench Racing Team" with "Snap-On Tools" roof label
	['var' => '027a', 'mfg' => 'Macau', 'liv' => "Good-wrench Racing Team",
	    'cdt' => 'black cab with black chassis',
	    'tdt' => "black container, GOOD-WRENCH RACING TEAM with SNAP-ON TOOLS roof label",
	],
// 28. Green cab with chrome chassis, white container, "Merry Christmas 1994 from White Rose Collectibles" labels
	['var' => '028a', 'mfg' => 'Macau', 'liv' => "Merry Christmas 1994 from White Rose Collectibles",
	    'cdt' => 'green cab with chrome chassis',
	    'tdt' => "white container, MERRY CHRISTMAS 1994 FROM WHITE ROSE COLLECTIBLES labels",
	],
// 29. Powder blue cab with chrome chassis, dark blue container, "Penn State 94" labels (WR)
	['var' => '029a', 'mfg' => 'Macau', 'liv' => "Penn State 94",
	    'cdt' => 'powder blue cab with chrome chassis',
	    'tdt' => "dark blue container, PENN STATE 94 labels",
	],
// 30. Metallic blue cab with chrome chassis, blue container, "Dupont Automotive Refinishes" labels (WR)
	['var' => '030a', 'mfg' => 'Macau', 'liv' => "Dupont Automotive Refinishes",
	    'cdt' => 'metallic blue cab with chrome chassis',
	    'tdt' => "blue container, DUPONT AUTOMOTIVE REFINISHES labels",
	],
// 31. Blue and yellow cab with yellow chassis, blue container, "Straight Arrow Motorsports 12" labels (WR)
	['var' => '031a', 'mfg' => 'Macau', 'liv' => "Straight Arrow Motorsports 12",
	    'cdt' => 'blue and yellow cab with yellow chassis',
	    'tdt' => "blue container, STRAIGHT ARROW MOTORSPORTS 12 labels",
	],
// 32. Red cab with chrome chassis, red container, "Detroit Gasket Racing 72" labels
	['var' => '032a', 'mfg' => 'Macau', 'liv' => "Detroit Gasket Racing 72",
	    'cdt' => 'red cab with chrome chassis',
	    'tdt' => "red container, DETROIT GASKET RACING 72 labels",
	],
// 33. Red cab with black chassis, red container, "Bosal Exhaust Systems" labels (US)
	['var' => '033a', 'mfg' => 'Macau', 'liv' => "Bosal Exhaust Systems", 'cod' => '1',
	    'cdt' => 'red cab with black chassis',
	    'tdt' => "red container, BOSAL EXHAUST SYSTEMS labels",
	],
// 34. Black cab and chassis, black container, "Florida State University" labels (WR)
	['var' => '034a', 'mfg' => 'Macau', 'liv' => "Florida State University",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, FLORIDA STATE UNIVERSITY labels",
	],
// 35. White cab with chrome chassis, white container, "Luxaire 99" labels (WR)
	['var' => '035a', 'mfg' => 'Macau', 'liv' => "Luxaire 99",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "white container, LUXAIRE 99 labels",
	],
// 36. Red cab and chassis, red container, "Lipton Tea 74" labels
	['var' => '036a', 'mfg' => 'Macau', 'liv' => "Lipton Tea 74",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, LIPTON TEA 74 labels",
	],
// 37. White cab with chrome chassis, turquoise container, "Vermont Teddy Bear Co. 71" labels
	['var' => '037a', 'mfg' => 'Macau', 'liv' => "Vermont Teddy Bear Co. 71",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "turquoise container, VERMONT TEDDY BEAR CO. 71 labels",
	],
// 38. Dark blue cab, chrome chassis, white container, "Minnesota Twins 95" labels (WR)
	['var' => '038a', 'mfg' => 'Macau', 'liv' => "Minnesota Twins 95",
	    'cdt' => 'dark blue cab, chrome chassis',
	    'tdt' => "white container, MINNESOTA TWINS 95 labels",
	],
// 39. Dark blue cab, chrome chassis, white container, "New York Yankees 95" labels (WR)
	['var' => '039a', 'mfg' => 'Macau', 'liv' => "New York Yankees 95",
	    'cdt' => 'dark blue cab, chrome chassis',
	    'tdt' => "white container, NEW YORK YANKEES 95 labels",
	],
// 40. Dark blue cab, chrome chassis, white container, "Cleveland Indians 95" labels (WR)
	['var' => '040a', 'mfg' => 'Macau', 'liv' => "Cleveland Indians 95",
	    'cdt' => 'dark blue cab, chrome chassis',
	    'tdt' => "white container, CLEVELAND INDIANS 95 labels",
	],
// 41. Dark blue cab, chrome chassis, white container, "San Diego Padres 95" labels (WR)
	['var' => '041a', 'mfg' => 'Macau', 'liv' => "San Diego Padres 95",
	    'cdt' => 'dark blue cab, chrome chassis',
	    'tdt' => "white container, SAN DIEGO PADRES 95 labels",
	],
// 42. Blue cab, chrome chassis, white container, "Atlanta Braves 95" labels (WR)
	['var' => '042a', 'mfg' => 'Macau', 'liv' => "Atlanta Braves 95",
	    'cdt' => 'blue cab, chrome chassis',
	    'tdt' => "white container, ATLANTA BRAVES 95 labels",
	],
// 43. Blue cab, chrome chassis, white container, "Philadelphia Phillies 95" labels (WR)
	['var' => '043a', 'mfg' => 'Macau', 'liv' => "Philadelphia Phillies 95",
	    'cdt' => 'blue cab, chrome chassis',
	    'tdt' => "white container, PHILADELPHIA PHILLIES 95 labels",
	],
// 44. Blue cab, chrome chassis, white container, "Los Angeles Dodgers 95" labels (WR)
	['var' => '044a', 'mfg' => 'Macau', 'liv' => "Los Angeles Dodgers 95",
	    'cdt' => 'blue cab, chrome chassis',
	    'tdt' => "white container, LOS ANGELES DODGERS 95 labels",
	],
// 45. Light blue cab, chrome chassis, white container, "Toronto Blue Jays 95" labels (WR)
	['var' => '045a', 'mfg' => 'Macau', 'liv' => "Toronto Blue Jays 95",
	    'cdt' => 'light blue cab, chrome chassis',
	    'tdt' => "white container, TORONTO BLUE JAYS 95 labels",
	],
// 46. Purple cab, chrome chassis, white container, "Colorado Rockies 95" labels (WR)
	['var' => '046a', 'mfg' => 'Macau', 'liv' => "Colorado Rockies 95",
	    'cdt' => 'purple cab, chrome chassis',
	    'tdt' => "white container, COLORADO ROCKIES 95 labels",
	],
// 47. Blue-green cab, chrome chassis, white container, "Seattle Mariners 95" labels (WR)
	['var' => '047a', 'mfg' => 'Macau', 'liv' => "Seattle Mariners 95",
	    'cdt' => 'blue-green cab, chrome chassis',
	    'tdt' => "white container, SEATTLE MARINERS 95 labels",
	],
// 48. Green cab, chrome chassis, white container, "Milwaukee Brewers 95" labels (WR)
	['var' => '048a', 'mfg' => 'Macau', 'liv' => "Milwaukee Brewers 95",
	    'cdt' => 'green cab, chrome chassis',
	    'tdt' => "white container, MILWAUKEE BREWERS 95 labels",
	],
// 49. Black cab, chrome chassis, white container, "Chicago White Sox 95" labels (WR)
	['var' => '049a', 'mfg' => 'Macau', 'liv' => "Chicago White Sox 95",
	    'cdt' => 'black cab, chrome chassis',
	    'tdt' => "white container, CHICAGO WHITE SOX 95 labels",
	],
// 50. Black cab, chrome chassis, white container, "San Francisco Giants 95" labels (WR)
	['var' => '050a', 'mfg' => 'Macau', 'liv' => "San Francisco Giants 95",
	    'cdt' => 'black cab, chrome chassis',
	    'tdt' => "white container, SAN FRANCISCO GIANTS 95 labels",
	],
// 51. Black cab, chrome chassis, white container, "Florida Marlins 95" labels (WR)
	['var' => '051a', 'mfg' => 'Macau', 'liv' => "Florida Marlins 95",
	    'cdt' => 'black cab, chrome chassis',
	    'tdt' => "white container, FLORIDA MARLINS 95 labels",
	],
// 52. Silver-gray cab, chrome chassis, white container, "California Angels 95" labels (WR)
	['var' => '052a', 'mfg' => 'Macau', 'liv' => "California Angels 95",
	    'cdt' => 'silver-gray cab, chrome chassis',
	    'tdt' => "white container, CALIFORNIA ANGELS 95 labels",
	],
// 53. Gold cab, chrome chassis, white container, "Houston Astros 95" labels (WR)
	['var' => '053a', 'mfg' => 'Macau', 'liv' => "Houston Astros 95",
	    'cdt' => 'gold cab, chrome chassis',
	    'tdt' => "white container, HOUSTON ASTROS 95 labels",
	],
// 54. Gold cab, chrome chassis, white container, "Kansas City Royals 95" labels (WR)
	['var' => '054a', 'mfg' => 'Macau', 'liv' => "Kansas City Royals 95",
	    'cdt' => 'gold cab, chrome chassis',
	    'tdt' => "white container, KANSAS CITY ROYALS 95 labels",
	],
// 55. Yellow cab, chrome chassis, white container, "Pittsburgh Pirates 95" labels (WR)
	['var' => '055a', 'mfg' => 'Macau', 'liv' => "Pittsburgh Pirates 95",
	    'cdt' => 'yellow cab, chrome chassis',
	    'tdt' => "white container, PITTSBURGH PIRATES 95 labels",
	],
// 56. Yellow cab, chrome chassis, white container, "Oakland Athletics 95" labels (WR)
	['var' => '056a', 'mfg' => 'Macau', 'liv' => "Oakland Athletics 95",
	    'cdt' => 'yellow cab, chrome chassis',
	    'tdt' => "white container, OAKLAND ATHLETICS 95 labels",
	],
// 57. Orange cab, chrome chassis, white container, "Baltimore Orioles 95" labels (WR)
	['var' => '057a', 'mfg' => 'Macau', 'liv' => "Baltimore Orioles 95",
	    'cdt' => 'orange cab, chrome chassis',
	    'tdt' => "white container, BALTIMORE ORIOLES 95 labels",
	],
// 58. Orange cab, chrome chassis, white container, "Detroit Tigers 95" labels (WR)
	['var' => '058a', 'mfg' => 'Macau', 'liv' => "Detroit Tigers 95",
	    'cdt' => 'orange cab, chrome chassis',
	    'tdt' => "white container, DETROIT TIGERS 95 labels",
	],
// 59. Orange cab, chrome chassis, white container, "New York Mets 95" labels (WR)
	['var' => '059a', 'mfg' => 'Macau', 'liv' => "New York Mets 95",
	    'cdt' => 'orange cab, chrome chassis',
	    'tdt' => "white container, NEW YORK METS 95 labels",
	],
// 60. Red cab, chrome chassis, white container, "Chicago Cubs 95" labels (WR)
	['var' => '060a', 'mfg' => 'Macau', 'liv' => "Chicago Cubs 95",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "white container, CHICAGO CUBS 95 labels",
	],
// 61. Red cab, chrome chassis, white container, "Montreal Expos 95" labels (WR)
	['var' => '061a', 'mfg' => 'Macau', 'liv' => "Montreal Expos 95",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "white container, MONTREAL EXPOS 95 labels",
	],
// 62. Red cab, chrome chassis, white container, "St. Louis Cardinals 95" labels (WR)
	['var' => '062a', 'mfg' => 'Macau', 'liv' => "St. Louis Cardinals 95",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "white container, ST. LOUIS CARDINALS 95 labels",
	],
// 63. Red cab, chrome chassis, white container, "Boston Red Sox 95" labels (WR)
	['var' => '063a', 'mfg' => 'Macau', 'liv' => "Boston Red Sox 95",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "white container, BOSTON RED SOX 95 labels",
	],
// 64. Red cab, chrome chassis, white container, "Texas Rangers 95" labels (WR)
	['var' => '064a', 'mfg' => 'Macau', 'liv' => "Texas Rangers 95",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "white container, TEXAS RANGERS 95 labels",
	],
// 65. Pink-red cab, chrome chassis, white container, "Cincinnati Reds 95" labels (WR)
	['var' => '065a', 'mfg' => 'Macau', 'liv' => "Cincinnati Reds 95",
	    'cdt' => 'pink-red cab, chrome chassis',
	    'tdt' => "white container, CINCINNATI REDS 95 labels",
	],
// 66. Dark blue cab with chrome chassis, dark blue container, "66th All Star Game" labels (WR)
	['var' => '066a', 'mfg' => 'Macau', 'liv' => "66th All Star Game",
	    'cdt' => 'dark blue cab with chrome chassis',
	    'tdt' => "dark blue container, 66TH ALL STAR GAME labels",
	],
// 67. Black cab with chrome chassis, black container, "DeWalt Racing 1/Peebles" labels (WR)
	['var' => '067a', 'mfg' => 'Macau', 'liv' => "DeWalt Racing 1/Peebles",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, DEWALT RACING 1/PEEBLES labels",
	],
// 68. Orange-yellow cab with chrome chassis, orange-yellow container, "Kodak Film Racing 4" labels (WR)
	['var' => '068a', 'mfg' => 'Macau', 'liv' => "Kodak Film Racing 4",
	    'cdt' => 'orange-yellow cab with chrome chassis',
	    'tdt' => "orange-yellow container, KODAK FILM RACING 4 labels",
	],
// 69. White cab with chrome chassis, gold container, "49ers Super Bowl XXIX" labels (WR)
	['var' => '069a', 'mfg' => 'Macau', 'liv' => "49ers Super Bowl XXIX",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "gold container, 49ERS SUPER BOWL XXIX labels",
	],
// 70. Silver-gray cab with chrome chassis, gray container, "Coors Light-Silver Bullet" labels, sealed in plexi box (WR)
	['var' => '070a', 'mfg' => 'Macau', 'liv' => "Coors Light-Silver Bullet",
	    'cdt' => 'silver-gray cab with chrome chassis',
	    'tdt' => "gray container, COORS LIGHT-SILVER BULLET labels",
	    'nts' => 'Sealed in plexi box',
	],
// 71. White cab with chrome chassis, white container, "Hyde Tools Racing Team" labels (WR)
	['var' => '071a', 'mfg' => 'Macau', 'liv' => "Hyde Tools Racing Team",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "white container, HYDE TOOLS RACING TEAM labels",
	],
// 72. Black cab and chassis, black container, "Goodwrench Service" (Monte Carlo) labels (WR)
	['var' => '072a', 'mfg' => 'Macau', 'liv' => "Goodwrench Service",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, GOODWRENCH SERVICE (Monte Carlo) labels",
	],
// 73. Black cab and chassis, black container, "Goodwrench Service" (Super Truck) labels (WR)
	['var' => '073a', 'mfg' => 'Macau', 'liv' => "Goodwrench Service",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, GOODWRENCH SERVICE (Super Truck) labels",
	],
// 74. Red cab and chassis, red container, "Total Racing" (Super Truck) (WR)
	['var' => '074a', 'mfg' => 'Macau', 'liv' => "Total Racing",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, TOTAL RACING (Super Truck) labels",
	],
// 75. Purple cab with chrome chassis, purple container, "Burger King" labels (WR)
	['var' => '075a', 'mfg' => 'Macau', 'liv' => "Burger King",
	    'cdt' => 'purple cab with chrome chassis',
	    'tdt' => "purple container, BURGER KING labels",
	],
// 76. Red cab and chassis, white container, "The Budget Gourmet Racing" labels (WR)
	['var' => '076a', 'mfg' => 'Macau', 'liv' => "The Budget Gourmet Racing",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "white container, THE BUDGET GOURMET RACING labels",
	],
// 77. Navy blue cab with chrome chassis, navy blue container, "University of Michigan 95" labels (WR)
	['var' => '077a', 'mfg' => 'Macau', 'liv' => "University of Michigan 95",
	    'cdt' => 'navy blue cab with chrome chassis',
	    'tdt' => "navy blue container, UNIVERSITY OF MICHIGAN 95 labels",
	],
// 78. White cab with chrome chassis, light blue container, "University of North Carolina Tar Heels 95" labels (WR)
	['var' => '078a', 'mfg' => 'Macau', 'liv' => "University of North Carolina Tar Heels 95",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "light blue container, UNIVERSITY OF NORTH CAROLINA TAR HEELS 95 labels",
	],
// 79. White cab with orange chassis, orange container, "University of Tennessee Vols 95" labels (WR)
	['var' => '079a', 'mfg' => 'Macau', 'liv' => "University of Tennessee Vols 95",
	    'cdt' => 'white cab with orange chassis',
	    'tdt' => "orange container, UNIVERSITY OF TENNESSEE VOLS 95 labels",
	],
// 80. Red cab with chrome chassis, red container, "University of Georgia Bulldogs 95" labels (WR)
	['var' => '080a', 'mfg' => 'Macau', 'liv' => "University of Georgia Bulldogs 95",
	    'cdt' => 'red cab with chrome chassis',
	    'tdt' => "red container, UNIVERSITY OF GEORGIA BULLDOGS 95 labels",
	],
// 81. White cab with chrome chassis, dark blue container, "Penn State 95" labels (WR)
	['var' => '081a', 'mfg' => 'Macau', 'liv' => "Penn State 95",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "dark blue container, PENN STATE 95 labels",
	],
// 82. Black cab with chrome chassis, black container, "Sears Die Hard" (Super Truck) labels (WR)
	['var' => '082a', 'mfg' => 'Macau', 'liv' => "Sears Die Hard",
	    'cdt' => 'black cab with chrome chassis',
	    'tdt' => "black container, SEARS DIE HARD (Super Truck) labels",
	],
// 83. Dark blue and orange cab with orange chassis, dark blue container, "Purex Dial 40" labels (WR)
	['var' => '083a', 'mfg' => 'Macau', 'liv' => "Purex Dial 40",
	    'cdt' => 'dark blue and orange cab with orange chassis',
	    'tdt' => "dark blue container, PUREX DIAL 40 labels",
	],
// 84. Red and blue cab, chrome chassis, blue container, "New England Patriots 1995" labels (WR)
	['var' => '084a', 'mfg' => 'Macau', 'liv' => "New England Patriots 1995",
	    'cdt' => 'red and blue cab, chrome chassis',
	    'tdt' => "blue container, NEW ENGLAND PATRIOTS 1995 labels",
	],
// 85. Red and blue cab, chrome chassis, blue container, "New York Giants 1995" labels (WR)
	['var' => '085a', 'mfg' => 'Macau', 'liv' => "New York Giants 1995",
	    'cdt' => 'red and blue cab, chrome chassis',
	    'tdt' => "blue container, NEW YORK GIANTS 1995 labels",
	],
// 86. Red and blue cab, chrome chassis, blue container, "Buffalo Bills 1995" labels (WR)
	['var' => '086a', 'mfg' => 'Macau', 'liv' => "Buffalo Bills 1995",
	    'cdt' => 'red and blue cab, chrome chassis',
	    'tdt' => "blue container, BUFFALO BILLS 1995 labels",
	],
// 87. Red and blue cab, chrome chassis, black container, "Atlanta Falcons 1995" labels (WR)
	['var' => '087a', 'mfg' => 'Macau', 'liv' => "Atlanta Falcons 1995",
	    'cdt' => 'red and blue cab, chrome chassis',
	    'tdt' => "black container, ATLANTA FALCONS 1995 labels",
	],
// 88. Orange and turquoise cab, chrome chassis, blue-green container, "Miami Dolphins 1995" labels (WR)
	['var' => '088a', 'mfg' => 'Macau', 'liv' => "Miami Dolphins 1995",
	    'cdt' => 'orange and turquoise cab, chrome chassis',
	    'tdt' => "blue-green container, MIAMI DOLPHINS 1995 labels",
	],
// 89. Orange and blue cab, chrome chassis, blue container, "Denver Broncos 1995" labels (WR)
	['var' => '089a', 'mfg' => 'Macau', 'liv' => "Denver Broncos 1995",
	    'cdt' => 'orange and blue cab, chrome chassis',
	    'tdt' => "blue container, DENVER BRONCOS 1995 labels",
	],
// 90. Orange and navy blue cab, chrome chassis, blue container, "Chicago Bears 1995" labels (WR)
	['var' => '090a', 'mfg' => 'Macau', 'liv' => "Chicago Bears 1995",
	    'cdt' => 'orange and navy blue cab, chrome chassis',
	    'tdt' => "blue container, CHICAGO BEARS 1995 labels",
	],
// 91. Orange and black cab, chrome chassis, black container, "Cincinnati Bengals 1995" labels (WR)
	['var' => '091a', 'mfg' => 'Macau', 'liv' => "Cincinnati Bengals 1995",
	    'cdt' => 'orange and black cab, chrome chassis',
	    'tdt' => "black container, CINCINNATI BENGALS 1995 labels",
	],
// 92. Orange and brown cab, chrome chassis, brown container, "Cleveland Browns 1995" labels (WR)
	['var' => '092a', 'mfg' => 'Macau', 'liv' => "Cleveland Browns 1995",
	    'cdt' => 'orange and brown cab, chrome chassis',
	    'tdt' => "brown container, CLEVELAND BROWNS 1995 labels",
	],
// 93. Orange and red cab, chrome chassis, red container, "Tampa Bay Buccaneers 1995" labels (WR)
	['var' => '093a', 'mfg' => 'Macau', 'liv' => "Tampa Bay Buccaneers 1995",
	    'cdt' => 'orange and red cab, chrome chassis',
	    'tdt' => "red container, TAMPA BAY BUCCANEERS 1995 labels",
	],
// 94. Yellow and olive cab, chrome chassis, olive green container, "Green Bay Packers 1995" labels (WR)
	['var' => '094a', 'mfg' => 'Macau', 'liv' => "Green Bay Packers 1995",
	    'cdt' => 'yellow and olive cab, chrome chassis',
	    'tdt' => "olive green container, GREEN BAY PACKERS 1995 labels",
	],
// 95. Yellow and blue cab, chrome chassis, blue container, "St. Louis Rams 1995" labels (WR)
	['var' => '095a', 'mfg' => 'Macau', 'liv' => "St. Louis Rams 1995",
	    'cdt' => 'yellow and blue cab, chrome chassis',
	    'tdt' => "blue container, ST. LOUIS RAMS 1995 labels",
	],
// 96. Yellow and dark blue cab, chrome chassis, dark blue container, "San Diego Chargers 1995" labels (WR)
	['var' => '096a', 'mfg' => 'Macau', 'liv' => "San Diego Chargers 1995",
	    'cdt' => 'yellow and dark blue cab, chrome chassis',
	    'tdt' => "dark blue container, SAN DIEGO CHARGERS 1995 labels",
	],
// 97. Yellow and dark blue cab, chrome chassis, dark blue container, "Minnesota Vikings 1995" labels (WR)
	['var' => '097a', 'mfg' => 'Macau', 'liv' => "Minnesota Vikings 1995",
	    'cdt' => 'yellow and dark blue cab, chrome chassis',
	    'tdt' => "dark blue container, MINNESOTA VIKINGS 1995 labels",
	],
// 98. Yellow and black cab, chrome chassis, black container, "Pittsburgh Steelers 95" labels (WR)
	['var' => '098a', 'mfg' => 'Macau', 'liv' => "Pittsburgh Steelers 95",
	    'cdt' => 'yellow and black cab, chrome chassis',
	    'tdt' => "black container, PITTSBURGH STEELERS 95 labels",
	],
// 99. Yellow and maroon cab, chrome chassis, dark red container, "Washington Redskins 1995" labels (WR)
	['var' => '099a', 'mfg' => 'Macau', 'liv' => "Washington Redskins 1995",
	    'cdt' => 'yellow and maroon cab, chrome chassis',
	    'tdt' => "dark red container, WASHINGTON REDSKINS 1995 labels",
	],
// 100. Yellow and maroon cab, chrome chassis, dark red container, "Arizona Cardinals 1995" labels (WR)
	['var' => '100a', 'mfg' => 'Macau', 'liv' => "Arizona Cardinals 1995",
	    'cdt' => 'yellow and maroon cab, chrome chassis',
	    'tdt' => "dark red container, ARIZONA CARDINALS 1995 labels",
	],
// 101. Yellow and red cab, chrome chassis, red container, "Kansas City Chiefs 1995" labels (WR)
	['var' => '101a', 'mfg' => 'Macau', 'liv' => "Kansas City Chiefs 1995",
	    'cdt' => 'yellow and red cab, chrome chassis',
	    'tdt' => "red container, KANSAS CITY CHIEFS 1995 labels",
	],
// 102. Gold and red cab, chrome chassis, red container, "San Francisco 49ers 1995" labels (WR)
	['var' => '102a', 'mfg' => 'Macau', 'liv' => "San Francisco 49ers 1995",
	    'cdt' => 'gold and red cab, chrome chassis',
	    'tdt' => "red container, SAN FRANCISCO 49ERS 1995 labels",
	],
// 103. Gold and black cab, chrome chassis, black container, "New Orleans Saints 1995" labels (WR)
	['var' => '103a', 'mfg' => 'Macau', 'liv' => "New Orleans Saints 1995",
	    'cdt' => 'gold and black cab, chrome chassis',
	    'tdt' => "black container, NEW ORLEANS SAINTS 1995 labels",
	],
// 104. Silver and blue cab, chrome chassis, blue container, "Detroit Lions 1995" labels (WR)
	['var' => '104a', 'mfg' => 'Macau', 'liv' => "Detroit Lions 1995",
	    'cdt' => 'silver and blue cab, chrome chassis',
	    'tdt' => "blue container, DETROIT LIONS 1995 labels",
	],
// 105. Silver and dark blue cab, chrome chassis, dark blue container, "Dallas Cowboys 1995" labels (WR)
	['var' => '105a', 'mfg' => 'Macau', 'liv' => "Dallas Cowboys 1995",
	    'cdt' => 'silver and dark blue cab, chrome chassis',
	    'tdt' => "dark blue container, DALLAS COWBOYS 1995 labels",
	],
// 106. Silver and black cab, chrome chassis, black container, "Oakland Raiders 1995" labels (WR)
	['var' => '106a', 'mfg' => 'Macau', 'liv' => "Oakland Raiders 1995",
	    'cdt' => 'silver and black cab, chrome chassis',
	    'tdt' => "black container, OAKLAND RAIDERS 1995 labels",
	],
// 107. Silver and green cab, chrome chassis, green container, "Philadelphia Eagles 1995" labels (WR)
	['var' => '107a', 'mfg' => 'Macau', 'liv' => "Philadelphia Eagles 1995",
	    'cdt' => 'silver and green cab, chrome chassis',
	    'tdt' => "green container, PHILADELPHIA EAGLES 1995 labels",
	],
// 108. Blue and black cab, chrome chassis, black container, "Carolina Panthers 1995" labels (WR)
	['var' => '108a', 'mfg' => 'Macau', 'liv' => "Carolina Panthers 1995",
	    'cdt' => 'blue and black cab, chrome chassis',
	    'tdt' => "black container, CAROLINA PANTHERS 1995 labels",
	],
// 109. Light blue and red cab, chrome chassis, red container, "Houston Oilers 1995" labels (WR)
	['var' => '109a', 'mfg' => 'Macau', 'liv' => "Houston Oilers 1995",
	    'cdt' => 'light blue and red cab, chrome chassis',
	    'tdt' => "red container, HOUSTON OILERS 1995 labels",
	],
// 110. Dark green and black cab, chrome chassis, black container, "New York Jets 1995 labels (WR)
	['var' => '110a', 'mfg' => 'Macau', 'liv' => "New York Jets 1995",
	    'cdt' => 'dark green and black cab, chrome chassis',
	    'tdt' => "black container, NEW YORK JETS 1995 labels",
	],
// 111. Green and blue cab, chrome chassis, blue container, "Seattle Seahawks 1995" labels (WR)
	['var' => '111a', 'mfg' => 'Macau', 'liv' => "Seattle Seahawks 1995",
	    'cdt' => 'green and blue cab, chrome chassis',
	    'tdt' => "blue container, SEATTLE SEAHAWKS 1995 labels",
	],
// 112. White and blue cab, chrome chassis, blue container, "Indianapolis Colts 1995" labels (WR)
	['var' => '112a', 'mfg' => 'Macau', 'liv' => "Indianapolis Colts 1995",
	    'cdt' => 'white and blue cab, chrome chassis',
	    'tdt' => "blue container, INDIANAPOLIS COLTS 1995 labels",
	],
// 113. Mustard and turquoise cab, chrome chassis, turquoise container, "Jacksonville Jaguars 1995" labels (WR)
	['var' => '113a', 'mfg' => 'Macau', 'liv' => "Jacksonville Jaguars 1995",
	    'cdt' => 'mustard and turquoise cab, chrome chassis',
	    'tdt' => "turquoise container, JACKSONVILLE JAGUARS 1995 labels",
	],
// 114. Red cab and chassis, red container, "Budweiser King of Beers" labels, sealed in plexi box (WR)
	['var' => '114a', 'mfg' => 'Macau', 'liv' => "Budweiser King of Beers",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, BUDWEISER KING OF BEERS labels",
	    'nts' => 'Sealed in plexi box',
	],
// 115. Yellow cab and chassis, yellow container, "Caterpillar Racing" labels (WR)
	['var' => '115a', 'mfg' => 'Macau', 'liv' => "Caterpillar Racing",
	    'cdt' => 'yellow cab and chassis',
	    'tdt' => "yellow container, CATERPILLAR RACING labels",
	],
// 116. White cab with chrome chassis, white container, "Lance Snacks Racing" labels (WR)
	['var' => '116a', 'mfg' => 'Macau', 'liv' => "Lance Snacks Racing",
	    'cdt' => 'white cab with chrome chassis',
	    'tdt' => "white container, LANCE SNACKS RACING labels",
	],
// 117. Black and orange cab with chrome chassis, black container, "Baltimore Orioles 96" labels (WR)
	['var' => '117a', 'mfg' => 'Macau', 'liv' => "Baltimore Orioles 96",
	    'cdt' => 'black and orange cab with chrome chassis',
	    'tdt' => "black container, BALTIMORE ORIOLES 96 labels",
	],
// 118. Dark blue and red cab with chrome chassis, dark blue container, "Cleveland Indians 96" labels (WR)
	['var' => '118a', 'mfg' => 'Macau', 'liv' => "Cleveland Indians 96",
	    'cdt' => 'dark blue and red cab with chrome chassis',
	    'tdt' => "dark blue container, CLEVELAND INDIANS 96 labels",
	],
// 119. Red cab and chassis, red container, "Royal Oak Charcoal Briquets" labels (WR)
	['var' => '119a', 'mfg' => 'Macau', 'liv' => "Royal Oak Charcoal Briquets",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, ROYAL OAK CHARCOAL BRIQUETS labels",
	],
// 120. White cab and chassis, white container, "Channellock Racing" labels (WR)
	['var' => '120a', 'mfg' => 'Macau', 'liv' => "Channellock Racing",
	    'cdt' => 'white cab and chassis',
	    'tdt' => "white container, CHANNELLOCK RACING labels",
	],
// 121. Black cab and chassis, black container, "MBNA Racing" labels (WR)
	['var' => '121a', 'mfg' => 'Macau', 'liv' => "MBNA Racing",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, MBNA RACING labels",
	],
// 122. White cab and chassis, white container, "Q Quaker State Racing" labels (WR)
	['var' => '122a', 'mfg' => 'Macau', 'liv' => "Q Quaker State Racing",
	    'cdt' => 'white cab and chassis',
	    'tdt' => "white container, Q QUAKER STATE RACING labels",
	],
// 123. White cab and chassis, dark green container, "Kodiak Racing" labels (WR)
	['var' => '123a', 'mfg' => 'Macau', 'liv' => "Kodiak Racing",
	    'cdt' => 'white cab and chassis',
	    'tdt' => "dark green container, KODIAK RACING labels",
	],
// 124. Red cab, chrome chassis, green container, "Merry Christmas 96" labels (WR)
	['var' => '124a', 'mfg' => 'Macau', 'liv' => "Merry Christmas 96",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "green container, MERRY CHRISTMAS 96 labels",
	],
// 125. Black cab, black chassis, black container, "88 Hype Racing Team" labels (WR)
	['var' => '125a', 'mfg' => 'Macau', 'liv' => "88 Hype Racing Team",
	    'cdt' => 'black cab, black chassis',
	    'tdt' => "black container, 88 HYPE RACING TEAM labels",
	],
// 126. Red and white cab, blue chassis, blue container, "New York Yankees World Series Champions" labels (WR)
	['var' => '126a', 'mfg' => 'Macau', 'liv' => "New York Yankees World Series Champions",
	    'cdt' => 'red and white cab, blue chassis',
	    'tdt' => "blue container, NEW YORK YANKEES WORLD SERIES CHAMPIONS labels",
	],
// 127. Red and white cab, blue chassis, blue container, "Cleveland Welcomes the 1997 All-Star Game" labels (WR)
	['var' => '127a', 'mfg' => 'Macau', 'liv' => "Cleveland Welcomes the 1997 All-Star Game",
	    'cdt' => 'red and white cab, blue chassis',
	    'tdt' => "blue container, CLEVELAND WELCOMES THE 1997 ALL-STAR GAME labels",
	],
// 128. Blue cab, chrome chassis, blue container, "Fina" labels (WR)
	['var' => '128a', 'mfg' => 'Macau', 'liv' => "Fina",
	    'cdt' => 'blue cab, chrome chassis',
	    'tdt' => "blue container, FINA labels",
	],
// 129. Red cab and chassis, red container, "Team Remax Racing" labels (WR)
	['var' => '129a', 'mfg' => 'Macau', 'liv' => "Team Remax Racing",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, TEAM REMAX RACING labels",
	],
// 130. Red cab and chassis, red container, "Skittles Racing Team" labels (WR)
	['var' => '130a', 'mfg' => 'Macau', 'liv' => "Skittles Racing Team",
	    'cdt' => 'red cab and chassis',
	    'tdt' => "red container, SKITTLES RACING TEAM labels",
	],
// 131. Lemon cab, red chassis, red container, "Kellogg's 5 Racing Team" labels )(WR)
	['var' => '131a', 'mfg' => 'Macau', 'liv' => "Kellogg's 5 Racing Team",
	    'cdt' => 'lemon cab, red chassis',
	    'tdt' => "red container, KELLOGG'S 5 RACING TEAM labels",
	],
// 132. Orange and green cab, chrome chassis, orange container, "Baltimore Orioles 1997" labels (WR)
	['var' => '132a', 'mfg' => 'Macau', 'liv' => "Baltimore Orioles 1997",
	    'cdt' => 'orange and green cab, chrome chassis',
	    'tdt' => "orange container, BALTIMORE ORIOLES 1997 labels",
	],
// 133. Orange cab, chrome chassis, gray container, "Go Tennessee Vols" labels (WR)
	['var' => '133a', 'mfg' => 'Macau', 'liv' => "Go Tennessee Vols",
	    'cdt' => 'orange cab, chrome chassis',
	    'tdt' => "gray container, GO TENNESSEE VOLS labels",
	],
// 134. Blue cab, chrome chassis, gray container, "Jay Hawks" labels (WR)
	['var' => '134a', 'mfg' => 'Macau', 'liv' => "Jay Hawks",
	    'cdt' => 'blue cab, chrome chassis',
	    'tdt' => "gray container, JAY HAWKS labels",
	],
// 135. Red cab, chrome chassis, gray container, "Nebraska Huskers" labels (WR)
	['var' => '135a', 'mfg' => 'Macau', 'liv' => "Nebraska Huskers",
	    'cdt' => 'red cab, chrome chassis',
	    'tdt' => "gray container, NEBRASKA HUSKERS labels",
	],
// 136. Silver-gray cab, chrome chassis, gray container, "Penn State 1997" labels (WR)
	['var' => '136a', 'mfg' => 'Macau', 'liv' => "Penn State 1997",
	    'cdt' => 'silver-gray cab, chrome chassis',
	    'tdt' => "gray container, PENN STATE 1997 labels",
	],
// 137. Silver-gray cab, purple chassis, gray container, "Kansas State" labels (WR)
	['var' => '137a', 'mfg' => 'Macau', 'liv' => "Kansas State",
	    'cdt' => 'silver-gray cab, purple chassis',
	    'tdt' => "gray container, KANSAS STATE labels",
	],
// 138. Silver-gray cab, blue chassis, gray container, "Kentucky Wildcats" labels (WR)
	['var' => '138a', 'mfg' => 'Macau', 'liv' => "Kentucky Wildcats",
	    'cdt' => 'silver-gray cab, blue chassis',
	    'tdt' => "gray container, KENTUCKY WILDCATS labels",
	],
// 139. Silver-gray cab, red chassis, red container, "Go Big Red" labels (WR)
	['var' => '139a', 'mfg' => 'Macau', 'liv' => "Go Big Red",
	    'cdt' => 'silver-gray cab, red chassis',
	    'tdt' => "red container, GO BIG RED labels",
	],
// 140. Dark blue cab, chrome chassis, dark blue container, "Wolverines" labels (WR)
	['var' => '140a', 'mfg' => 'Macau', 'liv' => "Wolverines",
	    'cdt' => 'dark blue cab, chrome chassis',
	    'tdt' => "dark blue container, WOLVERINES labels",
	],
// 141. Dark blue cab, chrome chassis, gray container, "Seminoles" labels (WR)
	['var' => '141a', 'mfg' => 'Macau', 'liv' => "Seminoles",
	    'cdt' => 'dark blue cab, chrome chassis',
	    'tdt' => "gray container, SEMINOLES labels",
	],
// 142. Black cab and chassis, black container, "Timber Wolf Racing" labels (WR)
	['var' => '142a', 'mfg' => 'Macau', 'liv' => "Timber Wolf Racing",
	    'cdt' => 'black cab and chassis',
	    'tdt' => "black container, TIMBER WOLF RACING labels",
	],
// 143. Green and silver cab, chrome chassis, gray container, "Associated Truck Parts" and numerous logos labels (WR)
	['var' => '143a', 'mfg' => 'Macau', 'liv' => "Associated Truck Parts",
	    'cdt' => 'green and silver cab, chrome chassis',
	    'tdt' => "gray container, ASSOCIATED TRUCK PARTS and numerous logos labels",
	],
    ]);
}
?>
